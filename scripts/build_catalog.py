"""Build the raw structured catalog from playwright-cli captured __NUXT_DATA__ dumps.

Inputs (produced by scripts/fetch_via_cli.sh):
  raw/mcp_records.json        - 50 MCP records from the marketplace page
  raw/details/<slug>.raw.txt  - playwright-cli `eval` output for each detail page

Outputs:
  raw/mcp_details.json  - each MCP with its full tools[] + input_schema
  raw/api_nav.json      - full API documentation navigation tree
  raw/catalog_raw.json  - combined raw catalog with build stats
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parse_nuxt import load as _load_unused, unflatten, walk  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "raw")
DETAILS = os.path.join(RAW, "details")


def decode_cli_output(path: str) -> str | None:
    """Recover the raw __NUXT_DATA__ text from a playwright-cli eval dump."""
    with open(path, encoding="utf-8", errors="replace") as fh:
        lines = fh.read().split("\n")
    for i, line in enumerate(lines):
        if line.strip() == "### Result" and i + 1 < len(lines):
            chunk = lines[i + 1].strip()
            # The result is a JSON string literal; it may be split over lines.
            for j in range(i + 2, min(i + 10, len(lines))):
                try:
                    return json.loads(chunk)
                except json.JSONDecodeError:
                    chunk += lines[j].strip()
            try:
                return json.loads(chunk)
            except json.JSONDecodeError:
                return None
    return None


def main() -> None:
    records = json.load(open(os.path.join(RAW, "mcp_records.json"), encoding="utf-8"))

    details: list[dict] = []
    api_nav = None
    problems: list[str] = []

    for rec in records:
        slug = rec["name"]
        path = os.path.join(DETAILS, f"{slug}.raw.txt")
        if not os.path.exists(path):
            problems.append(f"{slug}: missing dump")
            continue
        text = decode_cli_output(path)
        if not text:
            problems.append(f"{slug}: decode failed")
            continue
        try:
            graph = unflatten(json.loads(text))
        except Exception as exc:  # noqa: BLE001
            problems.append(f"{slug}: unflatten failed: {exc}")
            continue

        data = graph.get("data", {}) if isinstance(graph, dict) else {}
        if api_nav is None and isinstance(data, dict):
            api_nav = data.get("api-doc-navigation-cn-anonymous")

        detail = None
        if isinstance(data, dict):
            detail = data.get(f"mcp-server-detail-{slug}")
        if not isinstance(detail, dict):
            # fallback: find any dict that has server+tools
            candidates = [x for x in walk(graph)
                          if isinstance(x, dict) and "server" in x and "tools" in x]
            detail = candidates[0] if candidates else None
        if not isinstance(detail, dict):
            problems.append(f"{slug}: detail object not found")
            continue

        server = detail.get("server") or {}
        # `tools` is capped at 10 by the detail page; `capabilityTools` holds
        # the full set (length == toolsTotal) with identical schema fields.
        tools = detail.get("capabilityTools") or detail.get("tools") or []
        details.append({
            "slug": slug,
            "display_name": rec.get("display_name"),
            "display_name_en": rec.get("display_name_en"),
            "description": rec.get("description"),
            "description_en": rec.get("description_en"),
            "category": rec.get("category"),
            "mcp_url": rec.get("mcp_url"),
            "mcp_version": rec.get("mcp_version"),
            "status": rec.get("status"),
            "connections": rec.get("connections"),
            "created_at": rec.get("created_at"),
            "stats_updated_at": rec.get("stats_updated_at"),
            "permission_user_count": rec.get("permission_user_count"),
            "permission_company_count": rec.get("permission_company_count"),
            "favorite_count": rec.get("favorite_count"),
            "tags": server.get("tags"),
            "tools_total": detail.get("toolsTotal"),
            "capability_tools": detail.get("capabilityTools"),
            "requires_client_auth": detail.get("requiresClientAuth"),
            "tools": [
                {
                    "id": t.get("id"),
                    "tool_name": t.get("tool_name"),
                    "description": t.get("description"),
                    "description_en": t.get("description_en"),
                    "input_schema": t.get("input_schema"),
                }
                for t in tools if isinstance(t, dict)
            ],
        })

    json.dump(details, open(os.path.join(RAW, "mcp_details.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    json.dump(api_nav, open(os.path.join(RAW, "api_nav.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

    # API nav stats
    api_stats = {"groups": {}, "total_endpoints": 0}
    if isinstance(api_nav, dict):
        groups = api_nav.get("groups", {})
        for gname, gval in groups.items():
            count = 0
            cats = []
            for grp in (gval.get("groups") or []):
                for cat in (grp.get("categories") or []):
                    eps = cat.get("endpoints") or []
                    count += len(eps)
                    cats.append((cat.get("name"), len(eps)))
            api_stats["groups"][gname] = {"categories": len(cats), "endpoints": count}
            api_stats["total_endpoints"] += count

    total_tools = sum(len(d["tools"]) for d in details)
    stats = {
        "mcp_records": len(records),
        "mcp_details_parsed": len(details),
        "tools_total": total_tools,
        "api_nav_found": api_nav is not None,
        "api_stats": api_stats,
        "problems": problems,
    }
    json.dump({"stats": stats, "mcps": details},
              open(os.path.join(RAW, "catalog_raw.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

    print("MCP details parsed :", len(details), "/", len(records))
    print("Tools total        :", total_tools)
    print("API nav found      :", api_nav is not None)
    print("API groups         :", json.dumps(api_stats["groups"], ensure_ascii=False))
    print("API endpoints total:", api_stats["total_endpoints"])
    print("Problems           :", problems or "none")
    print("\nPer-MCP tool counts:")
    for d in details:
        print(f"  {d['slug']:<38} {len(d['tools']):>3} tools  | {d['category']}")


if __name__ == "__main__":
    main()
