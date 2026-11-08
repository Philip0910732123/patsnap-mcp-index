"""Apply the freshly fetched official catalog onto index.json (the single source of truth).

Reads:
  index.json                 - previous version, keeps human-curated fields
  raw/mcp_details.json       - 50 MCPs + 411 tools with input_schema
  raw/api_endpoints.json     - 376 API endpoints from the doc navigation tree
  raw/openapi.json           - full OpenAPI 3.1 spec (3.5 MB)
  data/api-mapping.json      - inferred MCP tool -> API links (from infer_api_mapping.py)
  data/manual-overrides.json - maintainer-confirmed links, highest priority

Writes:
  index.json                 - new version, machine-readable truth source

Design rules
------------
* Official data wins for facts (names, descriptions, tool lists, schemas, API paths).
* Human-curated fields win for decisions (tier / domain / context_weight / replaces /
  scenario_bundles / exclusive). They are preserved by id or tool name.
* Nothing is invented: fields the official source does not provide stay empty arrays
  and are called out in meta.known_gaps.
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "raw")
DATA_DIR = os.path.join(ROOT, "data")

# Official marketplace category -> our 5 capability domains.
# This mapping matches the maintainer's decisions (chem -> pharma, OCR -> patent, ...).
CATEGORY_DOMAIN = {
    "Ip-Intelligence": "patent",
    "Life-Sciences": "pharma",
    "Finance": "finance",
    "Material-Science": "materials",
    "R&D-Innovation": "rnd",
}
DOMAIN_CN = {
    "patent": "专利检索与分析",
    "pharma": "医药情报",
    "finance": "金融",
    "materials": "材料",
    "rnd": "研发",
}
TRUNKS = {
    "patent": "core-patents",
    "pharma": "pharma-intelligence",
    "finance": "company-profile",
    "materials": "materials-search-mcp",
    "rnd": "patsnap-search",
}


def jload(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as fh:
        return json.load(fh)


def load_mapping():
    """Read the inferred MCP<->API mapping table (produced by infer_api_mapping.py).

    Returns two lookups keyed by (mcp_id, tool_name), plus the metadata block.
    Missing file -> empty lookups, so the build never breaks.
    """
    path = os.path.join(DATA_DIR, "api-mapping.json")
    if not os.path.exists(path):
        return {}, {}, {}
    with open(path, encoding="utf-8") as fh:
        m = json.load(fh)
    entries = {(e["mcp"], e["tool"]): e for e in m.get("entries", [])}
    unresolved = {(u["mcp"], u["tool"]): u for u in m.get("unresolved", [])}
    meta = {k: m[k] for k in ("method", "important_limit", "stats") if k in m}
    return entries, unresolved, meta


def jdump(obj, path):
    with open(os.path.join(ROOT, path), "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=2)


def resolve_ref(spec, node, depth=0):
    """Follow local $ref pointers, with a depth guard."""
    if depth > 6 or not isinstance(node, dict):
        return node
    ref = node.get("$ref")
    if not ref or not ref.startswith("#/"):
        return node
    cur = spec
    for part in ref[2:].split("/"):
        part = part.replace("~1", "/").replace("~0", "~")
        if not isinstance(cur, dict) or part not in cur:
            return node
        cur = cur[part]
    return resolve_ref(spec, cur, depth + 1)


def schema_fields(spec, node, depth=0):
    """Return top-level field descriptors of a JSON schema object."""
    if depth > 6 or not isinstance(node, dict):
        return []
    node = resolve_ref(spec, node, depth)
    if not isinstance(node, dict):
        return []
    # allOf / oneOf / anyOf: merge their first-level properties
    out = []
    for key in ("allOf", "oneOf", "anyOf"):
        for sub in node.get(key) or []:
            out.extend(schema_fields(spec, sub, depth + 1))
    props = node.get("properties") or {}
    required = set(node.get("required") or [])
    for name, prop in props.items():
        p = resolve_ref(spec, prop, depth + 1) if isinstance(prop, dict) else {}
        if not isinstance(p, dict):
            p = {}
        out.append({
            "name": name,
            "type": p.get("type") or ("$ref" if prop.get("$ref") else None),
            "required": name in required,
            "description": (p.get("description") or "").strip() or None,
        })
    # de-duplicate by name, keep first
    seen, uniq = set(), []
    for f in out:
        if f["name"] not in seen:
            seen.add(f["name"])
            uniq.append(f)
    return uniq


def build_apis(spec, nav_endpoints):
    paths = spec.get("paths") or {}
    by_path = {}
    for e in nav_endpoints:
        p = e.get("path")
        if p and p not in by_path:
            by_path[p] = e

    apis = []
    matched_nav = 0
    for path, item in paths.items():
        for method, op in item.items():
            if method.lower() not in ("get", "post", "put", "delete", "patch"):
                continue
            if not isinstance(op, dict):
                continue
            nav = by_path.get(path) or by_path.get("/" + path.lstrip("/"))
            if nav:
                matched_nav += 1

            # request fields: parameters + JSON request body
            req = []
            for prm in op.get("parameters") or []:
                prm = resolve_ref(spec, prm) if isinstance(prm, dict) else {}
                sch = resolve_ref(spec, prm.get("schema") or {})
                req.append({
                    "name": prm.get("name"),
                    "in": prm.get("in"),
                    "type": sch.get("type") if isinstance(sch, dict) else None,
                    "required": bool(prm.get("required")),
                    "description": (prm.get("description") or "").strip() or None,
                })
            body = op.get("requestBody")
            if isinstance(body, dict):
                body = resolve_ref(spec, body)
                content = (body.get("content") or {}).get("application/json") or {}
                bsch = content.get("schema")
                if bsch:
                    for f in schema_fields(spec, bsch):
                        f["in"] = "body"
                        req.append(f)

            # response fields from the success (2xx) schema
            resp_fields = []
            responses = op.get("responses") or {}
            for code in ("200", "201", "202"):
                r = responses.get(code)
                if not isinstance(r, dict):
                    continue
                r = resolve_ref(spec, r)
                content = (r.get("content") or {}).get("application/json") or {}
                sch = content.get("schema")
                if sch:
                    resp_fields = schema_fields(spec, sch)
                    break

            apis.append({
                "code": (nav or {}).get("code"),
                "name": (nav or {}).get("display_name") or op.get("summary"),
                "nav_name": (nav or {}).get("name"),
                "path": path,
                "method": method.upper(),
                "group": (nav or {}).get("group") or ("AI" if "AI" in (op.get("tags") or [""]) [0] else "DATA"),
                "group_cn": (nav or {}).get("group_cn"),
                "category": (nav or {}).get("category") or (op.get("tags") or [None])[0],
                "summary": op.get("summary"),
                "description": (op.get("description") or "").strip() or None,
                "operation_id": op.get("operationId"),
                "tags": op.get("tags") or [],
                "request_fields": req,
                "response_fields": resp_fields,
                "mcp_wrappers": [],   # filled in main() from the inferred mapping table
            })
    return apis, matched_nav


def main():
    old = jload("index.json")
    details = jload("raw/mcp_details.json")
    nav_endpoints = jload("raw/api_endpoints.json")
    spec = jload("raw/openapi.json")
    map_entries, map_unresolved, map_meta = load_mapping()

    old_mcps = {m["id"]: m for m in old.get("mcps", [])}
    old_tools = {}
    for m in old.get("mcps", []):
        for t in m.get("tools", []):
            old_tools[(m["id"], t.get("name"))] = t

    apis, matched_nav = build_apis(spec, nav_endpoints)

    # Reverse index: for each API code, which MCP tools expose it.
    wrappers = {}
    for e in map_entries.values():
        code = e.get("api_code")
        if not code:
            continue
        wrappers.setdefault(code, []).append({
            "mcp": e["mcp"], "tool": e["tool"],
            "status": e["status"], "confidence": e["confidence"],
        })
    for a in apis:
        a["mcp_wrappers"] = sorted(wrappers.get(a.get("code"), []),
                                   key=lambda x: (x["mcp"], x["tool"]))

    mcps = []
    for d in details:
        slug = d["slug"]
        prev = old_mcps.get(slug, {})
        domain = CATEGORY_DOMAIN.get(d["category"], "patent")
        is_trunk = TRUNKS.get(domain) == slug
        n_tools = len(d["tools"])

        # context weight: keep curated value when present, else derive from tool count
        cw = prev.get("context_weight")
        if not cw or cw == "TBD":
            cw = "high" if n_tools >= 15 else ("medium" if n_tools >= 6 else "low")

        tools = []
        for t in d["tools"]:
            name = t.get("tool_name")
            old_t = old_tools.get((slug, name), {})
            schema = t.get("input_schema") or {}
            props = schema.get("properties") or {}
            required = set(schema.get("required") or [])
            input_fields = []
            for pname, pval in props.items():
                pv = pval if isinstance(pval, dict) else {}
                input_fields.append({
                    "name": pname,
                    "type": pv.get("type") or ("any_of" if pv.get("any_of") else None),
                    "required": pname in required,
                    "description": (pv.get("description") or "").strip() or None,
                })
            key = (slug, name)
            me = map_entries.get(key)
            un = map_unresolved.get(key)
            if me:
                api_ref = me["api_code"]
                api_ref_name = me.get("api_name")
                api_ref_paths = me.get("api_paths", [])
                api_candidates = []
                mapping_status = "mapped"
                api_link = {
                    "status": me["status"],
                    "confidence": me["confidence"],
                    "evidence": me.get("evidence"),
                    "legacy_ref": me.get("legacy_ref"),
                    "needs_review": me.get("needs_review", False),
                    "ambiguous_code": me.get("ambiguous_code", False),
                }
            else:
                api_ref, api_ref_name, api_ref_paths = None, None, []
                api_candidates = (un or {}).get("top_candidates", [])
                mapping_status = (un or {}).get("status", "unmapped")
                api_link = {
                    "status": mapping_status,
                    "confidence": None,
                    "evidence": (un or {}).get("reason"),
                    "legacy_ref": (un or {}).get("legacy_ref"),
                    "needs_review": mapping_status == "candidate_only",
                    "ambiguous_code": False,
                }

            tools.append({
                "name": name,
                "capability": t.get("description"),
                "description_en": t.get("description_en"),
                "input_fields": input_fields,
                "input_schema": schema,
                # Official MCP pages expose no output schema. Keep empty, see meta.known_gaps.
                "data_fields": old_t.get("data_fields") or [],
                "scenario": old_t.get("scenario") or [],
                "api_ref": api_ref,
                "api_ref_name": api_ref_name,
                "api_ref_paths": api_ref_paths,
                "api_link": api_link,
                "api_candidates": api_candidates,
                "mapping_status": mapping_status,
                "source": old_t.get("source"),
                "mcp_only": old_t.get("mcp_only", False),
            })

        rec = {
            "id": slug,
            "display_name": d.get("display_name"),
            "display_name_en": d.get("display_name_en"),
            "tier": "trunk" if is_trunk else "branch",
            "domain": domain,
            "category": DOMAIN_CN[domain],
            "official_category": d.get("category"),
            "status": d.get("status"),
            "summary": d.get("description"),
            "summary_en": d.get("description_en"),
            "tool_count": n_tools,
            "context_weight": cw,
            "replaces": prev.get("replaces", []),
            "mcp_url": d.get("mcp_url"),
            "mcp_version": d.get("mcp_version"),
            "connections": d.get("connections"),
            "tags": d.get("tags"),
            "created_at": d.get("created_at"),
            "stats_updated_at": d.get("stats_updated_at"),
            "usage": {
                "user_count": d.get("permission_user_count"),
                "company_count": d.get("permission_company_count"),
                "favorite_count": d.get("favorite_count"),
            },
            "tools": tools,
        }
        # context_cost is a derived value written by build_recommendations.py.
        # Carry it over so core_signature() stays stable across monthly refreshes.
        if prev.get("context_cost") is not None:
            rec["context_cost"] = prev["context_cost"]
        mcps.append(rec)

    # --- preserve curated sections, repair stale ids in scenario_bundles ---
    bundles = old.get("scenario_bundles", [])
    valid_ids = {m["id"] for m in mcps}
    alias = {
        "material-search": "materials-search-mcp",
        "s-telecom-mcp-tools-sep": "s-telecom-mcp-sep",
    }
    for b in bundles:
        for key in ("required_mcps", "optional_mcps", "mcps"):
            if key in b and isinstance(b[key], list):
                b[key] = [alias.get(x, x) for x in b[key]]
                b[key] = [x for x in b[key] if x in valid_ids]

    old_ids = set(old_mcps)
    new_ids = valid_ids
    removed = sorted(old_ids - new_ids)
    added = sorted(new_ids - old_ids)

    domains = [
        {"id": k, "name": DOMAIN_CN[k], "trunk": TRUNKS[k],
         "mcp_count": sum(1 for m in mcps if m["domain"] == k)}
        for k in ("patent", "pharma", "finance", "materials", "rnd")
    ]

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    old_meta = old.get("meta", {})
    out = {
        "meta": {
            "version": "0.6.0",
            "generated_at": now,
            "scope": "仅智慧芽原生 MCP/API；第三方数据源封装不纳入。",
            "tier_model": "每能力域一根主干(trunk)，其余为该域分支(branch)。5 主干：" +
                          " / ".join(TRUNKS.values()),
            "data_sources": [
                {"name": "MCP 服务市场", "url": "https://open.zhihuiya.com/marketplace/mcp-servers",
                 "access": "HTTP GET，解析 HTML 内 __NUXT_DATA__", "auth": "无需登录"},
                {"name": "MCP 详情页", "url": "https://open.zhihuiya.com/marketplace/mcp-servers/{slug}",
                 "access": "HTTP GET，解析 __NUXT_DATA__.capabilityTools", "auth": "无需登录"},
                {"name": "Data/AI API 导航树", "url": "内置于详情页 __NUXT_DATA__",
                 "access": "api-doc-navigation-cn-anonymous", "auth": "无需登录"},
                {"name": "OpenAPI 规范", "url": "https://open.zhihuiya.com/openapi.json",
                 "access": "HTTP GET，OpenAPI 3.1.0", "auth": "无需登录"},
            ],
            "counts": {
                "mcp_in_scope": len(mcps),
                "tools_total": sum(len(m["tools"]) for m in mcps),
                "tools_with_input_schema": sum(1 for m in mcps for t in m["tools"] if t["input_schema"]),
                "api_total": len(apis),
                "api_with_response_fields": sum(1 for a in apis if a["response_fields"]),
                "tools_with_api_ref": sum(1 for m in mcps for t in m["tools"] if t["api_ref"]),
                "apis_with_mcp_wrapper": sum(1 for a in apis if a["mcp_wrappers"]),
                "domains": len(domains),
                "trunks": sum(1 for m in mcps if m["tier"] == "trunk"),
                "scenario_bundles": len(bundles),
            },
            "known_gaps": [
                "官方 MCP 详情页只提供 tool 的入参 schema，不提供返回字段；"
                "tools[].data_fields 暂为空，字段级信息见 apis[].response_fields。"
                "因此无法用「响应参数」反推 MCP↔API 对应关系。",
                "AI 工作流类 tool 重写入参（task_id/data/execution）并串行调用多个 API，"
                "静态 schema 无法还原调用链；这类工具的映射需维护者实测补充，"
                "见 tools[].mapping_status = opaque_workflow 与 docs/api-mapping-review.md。",
                "20 个 API 编号对应新旧两版 path，编号本身不唯一；"
                "涉及条目以 tools[].api_link.ambiguous_code 标记并附全部 path。",
                "exclusive（API-only / MCP-only 实测结论）按维护者要求保持为空，逐个补充。",
                "场景的 API 组合建议不完整：scenario_bundles[].api_codes 只来自已建立的 MCP→API 映射；"
                "exclusive 为空，因此「哪些数据只能 API 获取、需额外申请 API Key」尚缺实测结论。",
            ],
            "change_log": [{
                "version": "0.6.0",
                "date": now,
                "source": "open.zhihuiya.com 全量重抓（免登录）",
                "removed_ids": removed,
                "added_ids": added,
                "api_nav_matched": matched_nav,
                "note": "新增起步包与场景推荐层：按用户身份分 5 个包（最小/标准两档）、"
                        "36 条场景覆盖全部 50 个 MCP、上下文成本由 tool schema 自动估算、"
                        "场景 API 编号由 204 条映射反查；新增 getting-started.md 与 AI 入口 llms.txt / AGENTS.md。",
            }],
        },
        "domains": domains,
        "mcps": mcps,
        "apis": apis,
        "api_mapping": {
            "method": map_meta.get("method", "映射表未生成"),
            "important_limit": map_meta.get("important_limit", ""),
            "stats": map_meta.get("stats", {}),
            "priority": "manual_verified > inferred_official_name > "
                        "inferred_param_exclusive > legacy_unverified",
            "confidence_legend": {
                "verified": "维护者实测确认（data/manual-overrides.json）",
                "high": "官方 tool 描述模板唯一对应某个 API 中文名",
                "medium": "入参名集合在 tool 与 API 两侧双向唯一且一致",
                "low": "沿用上一版人工标注，本轮未获证据支持",
            },
            "review_doc": "docs/api-mapping-review.md",
            "manual_override_file": "data/manual-overrides.json",
        },
        "scenario_bundles": bundles,
        "exclusive": old.get("exclusive", {"api_only": [], "mcp_only": []}),
        "excluded_external": old.get("excluded_external", {"mcps": []}),
    }

    # Idempotency: if the freshly fetched facts are byte-identical to the
    # previous version, keep its timestamp/version/changelog so that a no-op
    # refresh does not create a meaningless diff (and therefore no PR).
    def core_signature(obj):
        return json.dumps(
            {"mcps": obj.get("mcps"), "apis": obj.get("apis"), "domains": obj.get("domains")},
            ensure_ascii=False, sort_keys=True,
        )

    if old_meta.get("version") == out["meta"]["version"] and core_signature(old) == core_signature(out):
        out["meta"]["generated_at"] = old_meta.get("generated_at")
        out["meta"]["change_log"] = old_meta.get("change_log", [])
        print("no factual change -> kept previous timestamp/changelog (idempotent)")

    jdump(out, "index.json")

    print("index.json ->", out["meta"]["version"])
    print("counts     :", json.dumps(out["meta"]["counts"], ensure_ascii=False))
    print("removed    :", removed)
    print("added      :", added)
    print("nav matched:", matched_nav, "/", len(nav_endpoints))
    print("domain mcp :", {d["name"]: d["mcp_count"] for d in domains})
    print("trunks     :", [m["id"] for m in mcps if m["tier"] == "trunk"])
    print("apis with response fields:", sum(1 for a in apis if a["response_fields"]))
    print("tools with api_ref        :", sum(1 for m in mcps for t in m["tools"] if t["api_ref"]),
          "/", sum(len(m["tools"]) for m in mcps))
    print("apis with mcp wrapper     :", sum(1 for a in apis if a["mcp_wrappers"]))


if __name__ == "__main__":
    main()
