#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
recommend.py — 把「用户提一个检索场景 → 给出 MCP / API 组合建议」跑一遍给你看。

这不是 AI 平台必须依赖的组件：AGENTS.md 已经把决策流程写清楚了，任何智能体
都可以自己读 index.json 实现。本脚本是那份流程的**参考实现 + 可验证 demo**，
用来确认仓库里的数据真的够用、字段之间没有断点。

用法：
    python scripts/recommend.py "FTO"
    python scripts/recommend.py "临床试验"
    python scripts/recommend.py --list           # 列出全部 36 个场景
    python scripts/recommend.py "查新" --json   # 输出机器可读结果
"""
import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "index.json")


def norm(s):
    return re.sub(r"[\s/（）()·、，,。._-]", "", (s or "")).lower()


def bigrams(s):
    s = norm(s)
    return {s[i:i + 2] for i in range(len(s) - 1)} if len(s) > 1 else {s}


def match(bundles, query):
    """轻量中文语义匹配：完全包含 > 字符 2-gram 重合 > 备注命中。"""
    q = norm(query)
    scored = []
    for b in bundles:
        name = norm(b["scenario"])
        note = norm(b.get("note", ""))
        score = 0
        if q == name:
            score = 100
        elif q and (q in name or name in q):
            score = 60
        else:
            overlap = bigrams(q) & bigrams(b["scenario"])
            score = int(40 * len(overlap) / max(1, len(bigrams(q))))
            if q and q in note:
                score += 8
        if score:
            scored.append((score, b))
    scored.sort(key=lambda x: (-x[0], x[1]["scenario"]))
    return scored


def find_kit(kits, bundle, by_id):
    for k in kits:
        if bundle["scenario"] in k.get("covers_scenarios", []):
            return k
    # 退路：按场景必备 MCP 所属能力域找对应起步包
    doms = {by_id[x]["domain"] for x in bundle["required_mcps"] if x in by_id}
    for k in kits:
        if k.get("domain") in doms:
            return k
    return None


def recommend(d, query):
    bundles = d.get("scenario_bundles", [])
    kits = d.get("starter_kits", [])
    by_id = {m["id"]: m for m in d["mcps"]}
    hits = match(bundles, query)
    if not hits:
        return {"query": query, "matched": False,
                "message": "没有匹配到场景。可先用 --list 查看 36 个场景，或直接按身份选一个起步包。",
                "starter_kits": [{"id": k["id"], "name": k["name"]} for k in kits]}
    _, b = hits[0]
    kit = find_kit(kits, b, by_id)
    minimal = kit["minimal"] if kit else None
    advanced = [x["scenario"] for x in bundles
                if x.get("level") == "advanced" and x is not b
                and set(x["required_mcps"]) & (set(b["required_mcps"]) | set(b["optional_mcps"]))]
    return {
        "query": query,
        "matched": True,
        "other_candidates": [x["scenario"] for _, x in hits[1:4]],
        "scenario": b["scenario"],
        "level": b["level"],
        "starter_kit": {
            "id": kit["id"], "name": kit["name"],
            "minimal_mcps": minimal["mcps"],
            "minimal_tool_count": minimal["tool_count"],
            "minimal_est_context_tokens": minimal["est_context_tokens"],
            "share_of_full_catalog_pct": minimal["share_of_full_catalog_pct"],
            "standard_mcps": kit["standard"]["mcps"],
            "upgrade_to": kit["upgrade_to"],
        } if kit else None,
        "required_mcps": b["required_mcps"],
        "optional_mcps": b["optional_mcps"],
        "api_codes": b["api_codes"],
        "api_codes_optional": b["api_codes_optional"],
        "api_coverage": b["api_coverage"],
        "required_est_context_tokens": b["required_est_context_tokens"],
        "api_only_gap": b["api_only_gap"],
        "note": b["note"],
        "advanced_scenarios_in_same_domain": advanced[:6],
    }


def render(r, d):
    if not r["matched"]:
        return r["message"] + "\n\n可用起步包：" + "、".join(
            f"{k['name']}（`{k['id']}`）" for k in r["starter_kits"])
    c = d["meta"]["counts"]
    out = [f"=== 场景匹配：{r['scenario']}（{'起步级 / 典型' if r['level'] == 'starter' else '高阶 / 按需'}）===", ""]
    out.append(f"智慧芽现有 {c['mcp_in_scope']} 个原生 MCP / {c['tools_total']} 个 tool / "
               f"{c['api_total']} 个 API；全量安装约 {c['est_context_tokens_all_mcps']:,} token。")
    if r["other_candidates"]:
        out.append("其他可能相关：" + "、".join(r["other_candidates"]))
    out.append("")
    k = r["starter_kit"]
    if k:
        out.append("① 起步配置（先只装这些）")
        out.append(f"   {k['name']} · 最小档：{', '.join(k['minimal_mcps'])}")
        out.append(f"   {k['minimal_tool_count']} tool / ≈{k['minimal_est_context_tokens']:,} token"
                   f"（占全量 {k['share_of_full_catalog_pct']}%）")
        out.append(f"   标准档（用得更深再上）：{', '.join(k['standard_mcps'])}")
        out.append("   ⚠️ 不要装全部 5 根主干（约 35,645 token），也不要全装 50 个 MCP。")
        out.append("")
    out.append("② 本次场景需要的 MCP / API")
    out.append(f"   必备 MCP：{', '.join(r['required_mcps']) or '—'}")
    out.append(f"   可选 MCP：{', '.join(r['optional_mcps']) or '—'}")
    api = r["api_codes"]
    if api:
        shown = ", ".join(api[:12]) + (f" …(+{len(api)-12})" if len(api) > 12 else "")
        out.append(f"   对应 API 编号（已确认映射，共 {len(api)} 个）：{shown}")
    else:
        out.append("   对应 API 编号：— （该场景 MCP 工具的映射尚未确认，不等于不需要 API）")
    cov = r["api_coverage"]
    out.append(f"   映射覆盖：{cov['mapped_tools']}/{cov['tools_total']} 个 tool"
               f" · 必备约 {r['required_est_context_tokens']:,} token")
    out.append(f"   说明：{r['note']}")
    out.append("")
    out.append("③ 是否还需要额外申请 API Key")
    out.append(f"   ⚠️ {r['api_only_gap']}")
    out.append("")
    out.append("④ 后续高阶用途")
    if k:
        out.append(f"   起步包可再加：{', '.join(k['upgrade_to']) or '—'}")
    out.append(f"   同域高阶场景：{'、'.join(r['advanced_scenarios_in_same_domain']) or '—'}")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="按用户检索场景给出 MCP / API 配置建议")
    ap.add_argument("query", nargs="?", help="场景关键词，如 FTO / 临床试验 / 查新 / 企业尽调")
    ap.add_argument("--list", action="store_true", help="列出全部场景")
    ap.add_argument("--json", action="store_true", help="输出 JSON（给程序消费）")
    args = ap.parse_args()

    with open(SRC, encoding="utf-8") as fh:
        d = json.load(fh)

    if args.list:
        for b in d["scenario_bundles"]:
            print(f"  [{b['level']:<8}] {b['scenario']}")
        return 0
    if not args.query:
        ap.print_help()
        return 1
    r = recommend(d, args.query)
    if args.json:
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else:
        print(render(r, d))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
