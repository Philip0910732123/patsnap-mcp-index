#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fetch_catalog.py —— 从 open.zhihuiya.com 重新抓取全量 MCP / API 目录。

重要结论（2026-11-08 实测，替代了早期"必须浏览器登录"的假设）：
    全部数据源均**免登录**，且 SSR 页面用普通 HTTP GET 即可拿到 __NUXT_DATA__，
    因此不需要浏览器、不需要 Cookie、不需要 API Token、不需要人工介入。
    可 100% 无人值守运行（GitHub Actions 每月定时）。

抓取内容：
    1. MCP 服务市场页        -> 50 条 MCP 记录
    2. 50 个 MCP 详情页      -> 全量 tools（capabilityTools）+ API 文档导航树
    3. /openapi.json         -> 376 个 API 的 OpenAPI 3.1.0 规范（3.5 MB）

产物（raw/ 目录）：
    mcp_records.json, detail_objects.json, api_nav.json, api_endpoints.json,
    openapi.json, mcp_details.json, fetch-report.json

完整刷新链路（推荐用一键编排 scripts/refresh_all.py，内部按正确顺序调用）：
    fetch_catalog.py      # 抓数据（本脚本，纯 HTTP）
    apply_catalog.py      # 第 1 次：写入最新官方事实
    infer_api_mapping.py  # 基于最新 index.json 推断 MCP -> API 映射
    apply_catalog.py           # 第 2 次：合并映射
    build_recommendations.py   # 起步包 / 场景推荐 / 上下文成本（读人工策展表）
    build_docs.py              # 重出 5 份 Markdown + llms.txt + AGENTS.md

用法：
    python scripts/fetch_catalog.py
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parse_nuxt import unflatten, walk  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "raw")
BASE = "https://open.zhihuiya.com"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")
NUXT_RE = re.compile(r'<script[^>]*id="__NUXT_DATA__"[^>]*>(.*?)</script>', re.S)


def http_get(url: str, retries: int = 3, timeout: int = 40) -> bytes:
    """Plain HTTP GET with retry. No cookies, no token, no browser."""
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            last = exc
            if attempt < retries - 1:
                time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"GET failed after {retries} tries: {url} -> {last}")


def nuxt_from_html(html: str) -> dict:
    """Extract and hydrate Nuxt SSR payload from raw HTML."""
    m = NUXT_RE.search(html)
    if not m:
        raise RuntimeError("__NUXT_DATA__ not found in HTML (site structure changed?)")
    return unflatten(json.loads(m.group(1)))


def save_json(obj, path):
    with open(os.path.join(ROOT, path), "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=2)


def find_records(graph) -> list[dict]:
    for node in walk(graph):
        if isinstance(node, dict) and isinstance(node.get("records"), list):
            return node["records"]
    raise RuntimeError("MCP records not found in marketplace payload")


def fetch_detail(slug: str) -> tuple[str, dict, dict | None]:
    """Return (slug, detail_object, api_nav) for one MCP."""
    html = http_get(f"{BASE}/marketplace/mcp-servers/{slug}").decode("utf-8", "replace")
    graph = nuxt_from_html(html)
    data = graph.get("data", {}) if isinstance(graph, dict) else {}
    detail = data.get(f"mcp-server-detail-{slug}") if isinstance(data, dict) else None
    if not isinstance(detail, dict):
        cands = [x for x in walk(graph)
                 if isinstance(x, dict) and "server" in x and "capabilityTools" in x]
        detail = cands[0] if cands else None
    if not isinstance(detail, dict):
        raise RuntimeError(f"detail object missing for {slug}")
    nav = data.get("api-doc-navigation-cn-anonymous") if isinstance(data, dict) else None
    return slug, detail, nav


def nav_to_endpoints(nav) -> list[dict]:
    eps = []
    if not isinstance(nav, dict):
        return eps
    for gname, gval in (nav.get("groups") or {}).items():
        for grp in (gval.get("groups") or []):
            gcn = grp.get("name_cn") or grp.get("name_en")
            for cat in (grp.get("categories") or []):
                for e in (cat.get("endpoints") or []):
                    eps.append({
                        "group": gname,
                        "group_cn": gcn,
                        "category": cat.get("name"),
                        "code": e.get("code"),
                        "name": e.get("name"),
                        "display_name": e.get("displayName"),
                        "path": e.get("document_path") or e.get("id"),
                        "document_id": e.get("document_id"),
                        "api_version": e.get("api_version"),
                        "has_permission": e.get("hasPermission"),
                    })
    return eps


def main():
    os.makedirs(RAW, exist_ok=True)
    started = datetime.now(timezone.utc)
    report: dict = {"started_at": started.strftime("%Y-%m-%dT%H:%M:%SZ"), "errors": []}

    # 1) marketplace -> full MCP record list
    print("[1/4] marketplace ...", flush=True)
    market_html = http_get(f"{BASE}/marketplace/mcp-servers").decode("utf-8", "replace")
    records = find_records(nuxt_from_html(market_html))
    save_json(records, "raw/mcp_records.json")
    slugs = [r["name"] for r in records]
    with open(os.path.join(RAW, "slugs.txt"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(slugs) + "\n")
    print(f"      {len(records)} MCP records", flush=True)

    # 2) detail pages, concurrent
    print(f"[2/4] {len(slugs)} detail pages (8 workers) ...", flush=True)
    details: dict[str, dict] = {}
    api_nav = None
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(fetch_detail, s): s for s in slugs}
        done = 0
        for fut in as_completed(futures):
            slug = futures[fut]
            done += 1
            try:
                s, detail, nav = fut.result()
                details[s] = detail
                if nav is not None and api_nav is None:
                    api_nav = nav
                print(f"      [{done:2d}/{len(slugs)}] {s}", flush=True)
            except Exception as exc:  # noqa: BLE001
                report["errors"].append(f"{slug}: {exc}")
                print(f"      [{done:2d}/{len(slugs)}] {slug} FAILED: {exc}", flush=True)
    save_json(details, "raw/detail_objects.json")
    save_json(api_nav, "raw/api_nav.json")
    endpoints = nav_to_endpoints(api_nav)
    save_json(endpoints, "raw/api_endpoints.json")
    print(f"      details ok={len(details)} failed={len(report['errors'])}"
          f" | api endpoints={len(endpoints)}", flush=True)

    # 3) OpenAPI spec
    print("[3/4] openapi.json ...", flush=True)
    spec_bytes = http_get(f"{BASE}/openapi.json", timeout=90)
    spec = json.loads(spec_bytes.decode("utf-8"))
    save_json(spec, "raw/openapi.json")
    print(f"      {len(spec_bytes):,} bytes, {len(spec.get('paths', {}))} paths", flush=True)

    # 4) normalize into the shape apply_catalog.py consumes
    print("[4/4] normalize ...", flush=True)
    normalized = []
    for rec in records:
        slug = rec["name"]
        det = details.get(slug)
        if not det:
            continue
        server = det.get("server") or {}
        tools = det.get("capabilityTools") or det.get("tools") or []
        normalized.append({
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
            "tools_total": det.get("toolsTotal"),
            "capability_tools": det.get("capabilityTools"),
            "requires_client_auth": det.get("requiresClientAuth"),
            "tools": [
                {"id": t.get("id"), "tool_name": t.get("tool_name"),
                 "description": t.get("description"),
                 "description_en": t.get("description_en"),
                 "input_schema": t.get("input_schema")}
                for t in tools if isinstance(t, dict)
            ],
        })
    save_json(normalized, "raw/mcp_details.json")

    report.update({
        "finished_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "mcp_count": len(records),
        "detail_count": len(normalized),
        "tool_count": sum(len(m["tools"]) for m in normalized),
        "api_nav_endpoints": len(endpoints),
        "openapi_paths": len(spec.get("paths", {})),
        "auth_required": False,
        "browser_required": False,
    })
    save_json(report, "raw/fetch-report.json")
    print("\nDONE:", json.dumps(report, ensure_ascii=False), flush=True)
    if report["errors"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
