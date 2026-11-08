#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_recommendations.py — 把「起步包 / 场景推荐」的判断变成机器可算的数据。

白话说明（给维护者）：
  人工只在 data/recommendations.json 里写「谁该装哪几个 MCP」这种判断；
  本脚本负责把所有能算的东西算出来，避免手写数字过时或写错：
    1. 每个 MCP 装进 AI 客户端后，大约会占多少上下文（由 411 个 tool 的真实 schema 算出）
    2. 每个场景涉及的 MCP，对应哪些官方 API 编号（由已建立的 204 条映射反查）
    3. 每个起步包 / 场景，需要加载多少个 tool、约多少 token、相对全量省多少
    4. 顺手校验：有没有写到不存在的 MCP id、有没有 MCP 完全没被场景覆盖

  本脚本零网络、确定性、幂等：数据没变时重复运行，index.json 字节不变。
  在刷新链路中的位置：fetch → infer_api_mapping → apply_catalog → 【本脚本】 → build_docs
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "index.json")
CURATED = os.path.join(ROOT, "data", "recommendations.json")

# 估算系数：工具定义的 JSON 以中英混合为主，按字符数 / 3.2 粗估 token。
# 这是「相对比较」用的近似值，不是精确 tokenizer 结果，不可用于计费核算。
CHARS_PER_TOKEN = 3.2


def jload(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def jdump(path, obj):
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def est_tokens(chars):
    return int(round(chars / CHARS_PER_TOKEN))


def weight_of(tokens):
    """由真实体量自动分档，替代原先人工拍的 high/medium/low（人工值仍保留作对照）。"""
    if tokens >= 3000:
        return "high"
    if tokens >= 1000:
        return "medium"
    return "low"


def main():
    d = jload(SRC)
    curated = jload(CURATED)

    by_id = {m["id"]: m for m in d["mcps"]}
    valid_codes = {a["code"] for a in d["apis"] if a.get("code")}

    # ---------- 1. 计算每个 MCP 的上下文成本 ----------
    cost = {}
    for mid, m in by_id.items():
        schema_chars = 0
        field_count = 0
        for t in m["tools"]:
            schema_chars += len(json.dumps(t.get("input_schema") or {}, ensure_ascii=False))
            schema_chars += len(t["name"]) + len(t.get("capability") or "")
            field_count += len(t.get("input_fields") or [])
        tok = est_tokens(schema_chars)
        cost[mid] = {
            "tool_count": len(m["tools"]),
            "input_field_count": field_count,
            "schema_chars": schema_chars,
            "est_tokens": tok,
            "weight_auto": weight_of(tok),
            "weight_human": m.get("context_weight"),
        }
        m["context_cost"] = cost[mid]

    all_tokens = sum(c["est_tokens"] for c in cost.values())
    trunk_ids = {x["trunk"] for x in d["domains"]}
    trunk_tokens = sum(cost[x]["est_tokens"] for x in trunk_ids if x in cost)

    # ---------- 2. MCP → API 编号索引（从已建立的映射反查） ----------
    api_by_mcp = {}
    for mid, m in by_id.items():
        codes = set()
        for t in m["tools"]:
            ref = t.get("api_ref")
            if ref and ref in valid_codes:
                codes.add(ref)
        api_by_mcp[mid] = codes

    mapped_tools = sum(1 for m in d["mcps"] for t in m["tools"]
                       if t.get("api_ref") in valid_codes)

    # exclusive 为空 => 场景的「额外需要哪些 API Key」暂时给不全，如实标注
    exclusive = d.get("exclusive") or {}
    exclusive_filled = bool(exclusive.get("api_only") or exclusive.get("mcp_only"))
    gap_note = (
        "已补齐：可给出本场景涉及的 API 编号。"
        if exclusive_filled else
        "待维护者补充：本场景的 api_codes 仅来自已建立的 MCP→API 映射；"
        "「哪些数据只能走 API、需额外申请 API Key」尚缺实测结论（exclusive 为空），因此 API 组合建议不完整。"
    )

    # ---------- 3. 起步包 ----------
    kits = []
    for k in curated["starter_kits"]:
        out = {
            "id": k["id"],
            "name": k["name"],
            "who": k["who"],
            "domain": k["domain"],
            "covers_scenarios": k["covers_scenarios"],
            "upgrade_to": k["upgrade_to"],
            "note": k["note"],
        }
        for tier in ("minimal", "standard"):
            ids = k[tier]["mcps"]
            tok = sum(cost[x]["est_tokens"] for x in ids if x in cost)
            ntool = sum(cost[x]["tool_count"] for x in ids if x in cost)
            out[tier] = {
                "mcps": ids,
                "why": k[tier]["why"],
                "tool_count": ntool,
                "est_context_tokens": tok,
                "share_of_full_catalog_pct": round(tok * 100.0 / all_tokens, 1) if all_tokens else 0,
            }
        # 两档之间的差额，供 AI 直接判断"多装这一档值不值"
        out["standard_vs_minimal_extra_tokens"] = (
            out["standard"]["est_context_tokens"] - out["minimal"]["est_context_tokens"]
        )
        kits.append(out)

    # ---------- 4. 场景路由表 ----------
    bundles = []
    for b in curated["scenario_bundles"]:
        req = b["required_mcps"]
        opt = b["optional_mcps"]
        req_codes = set()
        opt_codes = set()
        for x in req:
            req_codes |= api_by_mcp.get(x, set())
        for x in opt:
            opt_codes |= api_by_mcp.get(x, set())
        opt_codes -= req_codes

        req_tok = sum(cost[x]["est_tokens"] for x in req if x in cost)
        opt_tok = sum(cost[x]["est_tokens"] for x in opt if x in cost)
        req_tools = sum(cost[x]["tool_count"] for x in req if x in cost)
        all_ids = set(req) | set(opt)
        n_mapped = sum(1 for x in all_ids for t in by_id[x]["tools"]
                       if t.get("api_ref") in valid_codes) if all(x in by_id for x in all_ids) else 0
        n_total = sum(len(by_id[x]["tools"]) for x in all_ids if x in by_id)

        bundles.append({
            "scenario": b["scenario"],
            "level": b["level"],                       # starter=起步典型 / advanced=高阶按需
            "required_mcps": req,
            "optional_mcps": opt,
            "api_codes": sorted(req_codes),            # 结构化，可被 AI 直接消费
            "api_codes_optional": sorted(opt_codes),
            "api_coverage": {
                "mapped_tools": n_mapped,
                "tools_total": n_total,
                "note": "其余工具为工作流/AI 聚合类，官方未提供 MCP→API 映射，见 docs/api-mapping-review.md",
            },
            "api_only_gap": gap_note,
            "required_tool_count": req_tools,
            "required_est_context_tokens": req_tok,
            "optional_est_context_tokens": opt_tok,
            "total_est_context_tokens": req_tok + opt_tok,
            "note": b["note"],                        # 保留人话说明
        })

    # ---------- 5. 一致性校验（宁可报错，也不要把错的推荐写进真相源） ----------
    problems = []
    for k in kits:
        for tier in ("minimal", "standard"):
            for x in k[tier]["mcps"]:
                if x not in by_id:
                    problems.append(f"starter_kits/{k['id']}/{tier} 引用不存在的 MCP: {x}")
        for x in k["upgrade_to"]:
            if x not in by_id:
                problems.append(f"starter_kits/{k['id']}/upgrade_to 引用不存在的 MCP: {x}")
    names = {b["scenario"] for b in bundles}
    for k in kits:
        for s in k["covers_scenarios"]:
            if s not in names:
                problems.append(f"starter_kits/{k['id']}/covers_scenarios 引用不存在的场景: {s}")
    covered = set()
    for b in bundles:
        for key in ("required_mcps", "optional_mcps"):
            for x in b[key]:
                if x not in by_id:
                    problems.append(f"scenario/{b['scenario']}/{key} 引用不存在的 MCP: {x}")
                covered.add(x)
    for k in kits:
        for tier in ("minimal", "standard"):
            covered |= set(k[tier]["mcps"])
        covered |= set(k["upgrade_to"])
    uncovered = sorted(set(by_id) - covered)
    if uncovered:
        problems.append(f"以下 MCP 未被任何起步包或场景覆盖: {uncovered}")
    if problems:
        print("校验失败，index.json 未被修改：", file=sys.stderr)
        for p in problems:
            print("  - " + p, file=sys.stderr)
        sys.exit(1)

    # ---------- 6. 写回 index.json（顺序固定，保证幂等） ----------
    d["starter_kits"] = kits
    d["scenario_bundles"] = bundles

    d["meta"]["counts"].update({
        "starter_kits": len(kits),
        "scenario_bundles": len(bundles),
        "scenario_level_starter": sum(1 for b in bundles if b["level"] == "starter"),
        "scenario_level_advanced": sum(1 for b in bundles if b["level"] == "advanced"),
        "mcp_recommendation_coverage": len(covered),
        "tools_with_api_ref": mapped_tools,
        "est_context_tokens_all_mcps": all_tokens,
        "est_context_tokens_5_trunks": trunk_tokens,
    })
    d["meta"]["recommendation_model"] = {
        "starter_kit_dimension": "按用户身份/领域划分，不按能力域主干；每个包分 minimal / standard 两档",
        "why_not_trunks": (
            "5 根主干合计约 %s token，其中 pharma-intelligence 单个约 %s token；"
            "只做单一领域的用户装全部主干会白白占用大量上下文。"
            % (f"{trunk_tokens:,}", f"{cost.get('pharma-intelligence', {}).get('est_tokens', 0):,}")
        ),
        "context_estimate": (
            "mcps[].context_cost.est_tokens = 工具名+能力描述+input_schema JSON 的字符数 / %.1f 粗估，"
            "仅用于相对比较与最小上下文择优，不是精确 tokenizer 结果，不可用于计费核算。" % CHARS_PER_TOKEN
        ),
        "api_codes_source": "由 tools[].api_ref 反查并校验官方有效编号，不再手写；见 data/api-mapping.json",
        "api_only_gap": gap_note,
        "curated_input": "data/recommendations.json（人工判断，自动刷新不覆盖）",
        "generated_by": "scripts/build_recommendations.py（零网络、确定性、幂等）",
    }

    # known_gaps 由 apply_catalog.py 统一维护（单一真相源）；
    # 本脚本只在 recommendation_model 里给出随 exclusive 状态变化的动态说明。
    jdump(SRC, d)

    # ---------- 7. 摘要 ----------
    print("starter_kits:", len(kits), "| scenario_bundles:", len(bundles),
          "(starter %d / advanced %d)" % (
              sum(1 for b in bundles if b["level"] == "starter"),
              sum(1 for b in bundles if b["level"] == "advanced")))
    print("MCP 推荐覆盖: %d/%d | 有映射的 tool: %d" % (len(covered), len(by_id), mapped_tools))
    print("上下文估算: 全量 50 个 ≈ %s tok | 5 根主干 ≈ %s tok" %
          (f"{all_tokens:,}", f"{trunk_tokens:,}"))
    print("起步包（minimal → standard）:")
    for k in kits:
        print("  %-22s %2d→%2d tool  %6s→%6s tok  (占全量 %.1f%%→%.1f%%)" % (
            k["id"],
            k["minimal"]["tool_count"], k["standard"]["tool_count"],
            f"{k['minimal']['est_context_tokens']:,}",
            f"{k['standard']['est_context_tokens']:,}",
            k["minimal"]["share_of_full_catalog_pct"],
            k["standard"]["share_of_full_catalog_pct"]))
    print("index.json 已更新（v%s）" % d["meta"]["version"])


if __name__ == "__main__":
    main()
