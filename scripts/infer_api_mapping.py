#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
infer_api_mapping.py — 推断 MCP tool -> API 对应关系，产出可人工复核的映射表。

为什么不能只用「入参/响应参数」推断
------------------------------------
1. 官方 MCP 详情页只给 tool 的 *输入* schema，**完全不给输出字段**。
   所以「用响应参数推断」这条路在数据源层面就不存在。
2. 数据字典类 tool 大量共用同一组入参（61 个 tool 都是
   patent_id + patent_number），参数相同但对应不同 API。
   例：legal_data / legal_status / bibliography / claims / pdf 的入参完全一样，
   只有中文描述能区分 —— 纯参数匹配必然产生大量假阳性。
3. AI 工作流类 tool 重写了入参（task_id / data / execution / user_input），
   且一个 tool 内部串起多个 API，静态 schema 无法还原调用链。

因此按证据强弱分层，宁可留空也不臆断：
  P0 manual      : data/manual-overrides.json 人工确认（最高优先级，不被刷新覆盖）
  P1 description : capability 模板「用于获取X相关」中 X 唯一命中 API 中文名（强）
  P2 exclusive   : 入参签名在 tool 侧与 API 侧双向唯一（中）
  P3 candidate   : 仅参数/名称相似 -> 只记为候选，不写入 api_ref
  P4 opaque      : 工作流/AI 聚合类，静态不可推断，留给维护者实测

用法：python scripts/infer_api_mapping.py
产物：data/api-mapping.json（供 apply_catalog.py 合并进 index.json）
      raw/mapping-inference.json（全量候选与打分明细，供排查）
      raw/duplicate-tools.json（入参签名相同的冗余工具组）
"""
import json
import math
import os
import re
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "raw")
DATA = os.path.join(ROOT, "data")

STOP_TOKENS = {
    "get", "post", "v1", "v2", "v3", "api", "search", "data", "list",
    "ls", "by", "the", "and", "of", "to", "for", "info", "detail",
    "details", "query", "result", "results", "fetch", "retrieve",
}
W = {"param_idf": 0.55, "param_cover": 0.15, "name_token": 0.28, "zh_bigram": 0.02}


def jload(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def jdump(obj, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)


def tokenize(text):
    if not text:
        return set()
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", str(text))
    parts = re.split(r"[^A-Za-z0-9]+", s.lower())
    return {p for p in parts if p and p not in STOP_TOKENS and len(p) > 1}


def zh_bigrams(text):
    if not text:
        return set()
    s = re.sub(r"[^一-鿿a-zA-Z0-9]+", "", str(text))
    return {s[i:i + 2] for i in range(len(s) - 1)} if len(s) >= 2 else {s}


def weighted_jaccard(s1, s2, idf):
    if not s1 or not s2:
        return 0.0
    num = sum(idf.get(w, 1.0) for w in (s1 & s2))
    den = sum(idf.get(w, 1.0) for w in (s1 | s2))
    return num / den if den else 0.0


def template_name(capability):
    """从官方模板句「用于获取X相关的详细内容…」提取 X。"""
    m = re.match(r"用于获取(.{2,14}?)相关", capability or "")
    return m.group(1) if m else None


def main():
    d = jload(os.path.join(ROOT, "index.json"))
    overrides_path = os.path.join(DATA, "manual-overrides.json")
    overrides = jload(overrides_path).get("mappings", {}) if os.path.exists(overrides_path) else {}
    # 原始人工标注单独存档：刷新后 index.json 里的 api_ref 已是推断结果，
    # 若从那里读会把修正值误当成"旧标注"，冲突检测随之失效。
    legacy_path = os.path.join(DATA, "legacy-api-refs.json")
    legacy_map = jload(legacy_path).get("refs", {}) if os.path.exists(legacy_path) else {}

    tools, apis = [], []
    for m in d["mcps"]:
        for t in m["tools"]:
            tools.append({
                "mcp": m["id"], "name": t["name"],
                "capability": t.get("capability") or "",
                "legacy_ref": legacy_map.get(f"{m['id']}/{t['name']}"),
                "params": frozenset(f["name"].lower() for f in t.get("input_fields", [])),
            })
    for a in d["apis"]:
        apis.append({
            "code": a.get("code"), "name": a.get("name") or "",
            "path": a.get("path") or "", "method": a.get("method"),
            "operation_id": a.get("operation_id") or "",
            "params": frozenset(f["name"].lower() for f in a.get("request_fields", [])),
        })

    by_name = defaultdict(list)
    for i, a in enumerate(apis):
        if a["name"]:
            by_name[a["name"]].append(i)
    valid_codes = {a["code"] for a in apis if a["code"]}
    # 同一编号可能对应新旧两版 path（如 /ai/fto/** 与 /fto_steps/**），
    # 编号本身不唯一，映射需附带全部 path 并标记歧义。
    code_paths = defaultdict(list)
    for a in apis:
        if a["code"]:
            code_paths[a["code"]].append({"path": a["path"], "method": a["method"]})
    ambiguous_codes = {k for k, v in code_paths.items() if len(v) > 1}

    # IDF over all tool + api parameter vocabularies
    df = Counter()
    for t in tools:
        df.update(t["params"])
    for a in apis:
        df.update(a["params"])
    n = len(tools) + len(apis)
    idf = {k: math.log((n + 1) / (v + 1)) + 1.0 for k, v in df.items()}

    # 参数签名的双向唯一性：只有两侧都仅出现 1 次，签名才有判别力
    sig_tools = Counter(t["params"] for t in tools)
    sig_apis = Counter(a["params"] for a in apis)

    api_tokens = [tokenize(a["path"]) | tokenize(a["operation_id"]) for a in apis]
    api_zh = [zh_bigrams(a["name"]) for a in apis]

    entries, unresolved, conflicts = [], [], []
    score_matrix = []

    for ti, t in enumerate(tools):
        key = f"{t['mcp']}/{t['name']}"
        ttok, tzh = tokenize(t["name"]), zh_bigrams(t["capability"])
        ranked = []
        for ai, a in enumerate(apis):
            tp, ap = t["params"], a["params"]
            inter = tp & ap
            sp = weighted_jaccard(tp, ap, idf)
            sc = len(inter) / len(ap) if ap else 0.0
            ntok = ttok & api_tokens[ai]
            sn = len(ntok) / len(ttok | api_tokens[ai]) if (ttok | api_tokens[ai]) else 0.0
            z = tzh & api_zh[ai]
            sz = len(z) / len(tzh | api_zh[ai]) if (tzh | api_zh[ai]) else 0.0
            score = (W["param_idf"] * sp + W["param_cover"] * sc
                     + W["name_token"] * sn + W["zh_bigram"] * sz)
            ranked.append((score, ai, sp, sc, sn, sz, sorted(ntok)))
        ranked.sort(key=lambda x: (-x[0], x[1]))
        top = [{
            "rank": i + 1, "api_code": apis[ai]["code"], "api_name": apis[ai]["name"],
            "api_path": apis[ai]["path"], "score": round(s, 4),
            "signals": {
                "param_idf": round(sp, 4), "param_cover": round(sc, 4),
                "name_token": round(sn, 4), "zh_bigram": round(sz, 4),
                "name_tokens_matched": ntok,
                "exact_param_match": bool(t["params"]) and t["params"] == apis[ai]["params"],
                "shared_params": sorted(t["params"] & apis[ai]["params"])[:12],
            },
        } for i, (s, ai, sp, sc, sn, sz, ntok) in enumerate(ranked[:5])]
        score_matrix.append({"mcp": t["mcp"], "tool": t["name"],
                             "legacy_ref": t["legacy_ref"], "candidates": top})

        chosen = None
        status = None
        evidence = None
        legacy = t["legacy_ref"]

        # P0 manual override
        if key in overrides:
            ov = overrides[key]
            chosen, status = ov.get("api_code"), "manual_verified"
            evidence = ov.get("note") or "维护者人工确认"

        # P1 official description template -> unique API Chinese name
        if chosen is None:
            x = template_name(t["capability"])
            if x and len(by_name.get(x, [])) == 1:
                ai = by_name[x][0]
                chosen = apis[ai]["code"]
                status = "inferred_official_name"
                evidence = f"官方 tool 描述「用于获取{x}相关…」唯一对应 API 中文名「{x}」"

        # P2双向唯一的入参签名 + 高分
        if chosen is None and t["params"]:
            if sig_tools[t["params"]] == 1 and sig_apis[t["params"]] == 1:
                for s, ai, sp, *_ in ranked[:1]:
                    if apis[ai]["params"] == t["params"] and sp >= 0.75:
                        chosen = apis[ai]["code"]
                        status = "inferred_param_exclusive"
                        evidence = "入参名集合在 tool 与 API 两侧双向唯一且完全一致"
                        break

        # legacy 兜底：有效且不冲突时保留（不凭空丢弃人工标注）
        if chosen is None and legacy in valid_codes:
            chosen, status = legacy, "legacy_unverified"
            evidence = "沿用上一版人工标注，未获本轮证据支持，待实测复核"

        if legacy and chosen and legacy != chosen:
            conflicts.append({
                "mcp": t["mcp"], "tool": t["name"], "legacy_ref": legacy,
                "new_ref": chosen, "new_api_name": next((a["name"] for a in apis if a["code"] == chosen), ""),
                "status": status, "evidence": evidence,
            })

        if chosen:
            entries.append({
                "mcp": t["mcp"], "tool": t["name"], "api_code": chosen,
                "api_name": next((a["name"] for a in apis if a["code"] == chosen), ""),
                "api_paths": code_paths.get(chosen, []),
                "ambiguous_code": chosen in ambiguous_codes,
                "status": status, "confidence": {
                    "manual_verified": "verified",
                    "inferred_official_name": "high",
                    "inferred_param_exclusive": "medium",
                    "legacy_unverified": "low",
                }[status],
                "evidence": evidence,
                "legacy_ref": legacy if legacy != chosen else None,
                "needs_review": (status in ("inferred_param_exclusive", "legacy_unverified")
                                or (legacy is not None and legacy != chosen)),
            })
        else:
            # P4: 判定是否为工作流/AI 聚合类
            p = t["params"]
            workflow_markers = {"task_id", "data", "execution", "user_input", "job_id", "input", "output"}
            opaque = bool(p & workflow_markers) or not p or ranked[0][0] < 0.25
            reason = ("工作流/AI 聚合类：入参被 MCP 重写或异步任务化，"
                      "静态 schema 无法还原调用链，需实测补充" if opaque
                      else "仅有弱参数/名称相似信号，不足以判定，需人工确认")
            unresolved.append({
                "mcp": t["mcp"], "tool": t["name"],
                "status": "opaque_workflow" if opaque else "candidate_only",
                "reason": reason, "legacy_ref": legacy,
                "top_candidates": [c["api_code"] for c in top[:3] if c["api_code"]],
            })

    stats = {
        "tools_total": len(tools),
        "mapped": len(entries),
        "unresolved": len(unresolved),
        "by_status": dict(Counter(e["status"] for e in entries)),
        "unresolved_by_status": dict(Counter(u["status"] for u in unresolved)),
        "conflicts_with_legacy": len(conflicts),
        "distinct_apis_mapped": len({e["api_code"] for e in entries if e["api_code"]}),
        "apis_without_request_fields": sum(1 for a in apis if not a["params"]),
    }

    jdump({
        "method": "分层证据判定：人工确认 > 官方描述模板 > 双向唯一入参签名 > 仅候选 > 工作流不可推断",
        "important_limit": "官方 MCP 页面不提供 tool 输出字段，因此无法用响应参数做映射；"
                           "且数据字典类 tool 共用同一组入参，纯参数匹配会产生大量假阳性。",
        "stats": stats,
        "entries": entries,
        "unresolved": unresolved,
        "conflicts": conflicts,
    }, os.path.join(DATA, "api-mapping.json"))
    jdump({"note": "全量候选与打分明细，供排查算法用；不入库为真相源。",
           "weights": W, "results": score_matrix}, os.path.join(RAW, "mapping-inference.json"))

    sig = defaultdict(list)
    for t in tools:
        if t["params"]:
            sig[tuple(sorted(t["params"]))].append(f"{t['mcp']}/{t['name']}")
    dups = [{"param_signature": list(k), "count": len(v), "tools": v}
            for k, v in sig.items() if len(v) >= 2]
    dups.sort(key=lambda x: -x["count"])
    jdump({"note": "入参签名完全一致的 tool 组，用于识别跨 MCP 冗余封装",
           "group_count": len(dups),
           "groups": dups}, os.path.join(RAW, "duplicate-tools.json"))

    print("=== 映射推断结果 ===")
    for k, v in stats.items():
        print(f"  {k}: {v}")
    print("\n=== 与旧人工标注冲突（前 12 条）===")
    for c in conflicts[:12]:
        print(f"  {c['mcp']}/{c['tool']}: {c['legacy_ref']} -> {c['new_ref']} ({c['new_api_name']})")
    print(f"\n写入 data/api-mapping.json（{len(entries)} 条映射）+ "
          f"raw/ 下 2 份诊断文件")


if __name__ == "__main__":
    main()
