#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_docs.py —— 从 index.json（机读真相源）生成全部人类可读文档。

零网络、零登录、纯本地确定性渲染。改完 index.json 后运行本脚本即可重出：
  docs/architecture-tree.md   架构树 + 场景路由表
  docs/getting-started.md     起步配置与典型场景推荐（人读入口）
  docs/mcp-catalog.md         50 个 MCP / 411 个 tool 明细
  docs/api-catalog.md         376 个 API 索引（含请求/响应字段概览）
  docs/api-mapping-review.md  MCP↔API 映射的置信度与人工复核清单
  llms.txt                    给 AI 平台的轻量导航入口
  AGENTS.md                   给智能体的决策流程与数据边界

用法：
    python scripts/build_docs.py
"""
import json
import os
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "index.json")
DOCS = os.path.join(ROOT, "docs")


def header(title, meta, extra=""):
    return [
        f"# {title}\n",
        "> 本文件由 `scripts/build_docs.py` 从 `index.json`（机读真相源）自动生成，请勿手改。"
        "结构与内容请在 `index.json` 中修改后重跑脚本。\n",
        f"> 数据版本 v{meta.get('version', '?')} · 生成时间 {meta.get('generated_at', '')}"
        " · 数据源：open.zhihuiya.com（免登录）\n",
    ] + ([extra + "\n"] if extra else [])


def build_architecture(d, meta):
    domains, mcps = d["domains"], d["mcps"]
    by_id = {m["id"]: m for m in mcps}
    lines = header("架构树与场景路由", meta,
                   "**核心用途**：用户提出一个需求 → AI 平台读取本表 → 反推应配置哪些 MCP / API。")
    lines.append("## 一、五根主干（trunk）\n")
    lines.append("> ⚠️ **「主干」是架构概念（每个能力域一根），不是安装建议。** "
                 "实测 5 根主干合计约 "
                 f"{meta['counts'].get('est_context_tokens_5_trunks', 0):,} token，"
                 "其中 `pharma-intelligence` 单个就占约 "
                 f"{by_id['pharma-intelligence'].get('context_cost', {}).get('est_tokens', 0):,} token。"
                 "只做单一领域的用户装全部主干会白白占用大量上下文。"
                 "**起步该装哪几个请看 [getting-started.md](getting-started.md)。**\n")
    for dom in domains:
        t = by_id[dom["trunk"]]
        cc = t.get("context_cost") or {}
        lines.append(f"- **{dom['name']}** (`{dom['id']}`) — 主干 `{dom['trunk']}`"
                     f"（{t['tool_count']} tool，约 {cc.get('est_tokens', 0):,} token，共 {dom['mcp_count']} 个 MCP）")
        lines.append(f"  - {(t.get('summary') or '')[:160]}")
    lines.append("")

    lines.append("## 二、逐域架构树\n")
    for dom in domains:
        lines.append(f"### {dom['name']}（`{dom['id']}`）\n")
        trunk = by_id[dom["trunk"]]
        lines.append(f"- 🌳 **{trunk['id']}** ·trunk· ctx={trunk['context_weight']} · {trunk['tool_count']} tools")
        if trunk.get("replaces"):
            lines.append(f"  - replaces: {', '.join(trunk['replaces'])}")
        for b in [m for m in mcps if m["domain"] == dom["id"] and m["tier"] != "trunk"]:
            rep = f" · replaces: {', '.join(b['replaces'])}" if b.get("replaces") else ""
            lines.append(f"  - ├─ `{b['id']}` ·branch· ctx={b['context_weight']} · {b['tool_count']} tools{rep}")
        lines.append("")

    lines.append("## 三、场景路由表（需求 → MCP + API 组合）\n")
    lines.append("`api_codes` 由已建立的 MCP→API 映射自动反查，完整列表见 `index.json`；表中只显示前 6 个。"
                 "**显示「—」不代表不需要 API**，只表示该场景涉及的 MCP 工具尚未建立映射（多为工作流/AI 聚合类）。"
                 "`api_only_gap` 说明「只能走 API、需额外申请 API Key」的部分尚不完整。\n")
    for level, title in (("starter", "起步级 / 典型场景"), ("advanced", "高阶 / 按需场景")):
        group = [b for b in d.get("scenario_bundles", []) if b.get("level") == level]
        lines.append(f"### {title}（{len(group)} 条）\n")
        lines.append("| 场景 | 必备 MCP | 可选 MCP | 涉及 API 编号 | 必备约 token |")
        lines.append("|------|----------|----------|---------------|--------------|")
        for sb in group:
            req = ", ".join(f"`{x}`" for x in sb.get("required_mcps", [])) or "—"
            opt = ", ".join(f"`{x}`" for x in sb.get("optional_mcps", [])) or "—"
            codes = sb.get("api_codes", [])
            cstr = ", ".join(codes[:6]) + (f" …(+{len(codes)-6})" if len(codes) > 6 else "") if codes else "—"
            tok = f"{sb.get('required_est_context_tokens', 0):,}"
            lines.append(f"| {sb['scenario']} | {req} | {opt} | {cstr} | {tok} |")
        lines.append("")

    lines.append("## 四、上下文成本（装越多越费积分的量化）\n")
    counts = meta["counts"]
    cw = Counter(m.get("context_cost", {}).get("weight_auto") or m["context_weight"] for m in mcps)
    lines.append(f"- 自动分档（按真实 schema 体量）：高 {cw.get('high', 0)} 个 / "
                 f"中 {cw.get('medium', 0)} 个 / 低 {cw.get('low', 0)} 个 MCP")
    lines.append(f"- 全量 50 个 MCP 合计约 **{counts.get('est_context_tokens_all_mcps', 0):,} token**；"
                 f"5 根主干合计约 **{counts.get('est_context_tokens_5_trunks', 0):,} token**。")
    lines.append("- ★ **不要默认装 5 根主干**。起步应按用户身份选 1 个包的最小档"
                 "（通常只占全量 2–4%），按场景再叠加；详见 [getting-started.md](getting-started.md)。")
    lines.append("- 估算方式：工具名 + 能力描述 + `input_schema` JSON 的字符数 / 3.2，"
                 "仅用于相对比较，不是精确 tokenizer 结果，不可用于计费核算。\n")
    lines.append("最重的 8 个 MCP（单独装就要考虑的）：\n")
    lines.append("| MCP | tool 数 | 约 token |")
    lines.append("|-----|---------|----------|")
    for m in sorted(mcps, key=lambda x: -(x.get("context_cost") or {}).get("est_tokens", 0))[:8]:
        lines.append(f"| `{m['id']}` | {m['tool_count']} | {(m.get('context_cost') or {}).get('est_tokens', 0):,} |")
    lines.append("")

    lines.append("## 五、专属知识（API-only / MCP-only）\n")
    ex = d.get("exclusive", {})
    lines.append(f"- api_only：`{len(ex.get('api_only', []))}` 条（待维护者逐个补充）")
    lines.append(f"- mcp_only：`{len(ex.get('mcp_only', []))}` 条（待维护者逐个补充）")
    lines.append("")

    lines.append("## 六、已知数据边界\n")
    for g in meta.get("known_gaps", []):
        lines.append(f"- {g}")
    lines.append("")

    excl = d.get("excluded_external", {})
    lines.append("## 七、已排除的第三方封装（非智慧芽原生）\n")
    lines.append(excl.get("note", "") + "\n")
    lines += [f"- {x}" for x in excl.get("mcps", [])]
    lines.append("")
    lines.append("---\n")
    lines.append(f"*index.json v{meta.get('version', '?')} · {meta.get('generated_at', '')}*")
    return "\n".join(lines) + "\n"


def build_mcp_catalog(d, meta):
    domains, mcps = d["domains"], d["mcps"]
    lines = header("MCP 服务目录（全量 tool 明细）", meta,
                   f"共 **{len(mcps)}** 个原生 MCP / **{meta['counts']['tools_total']}** 个 tool。"
                   "每个 tool 的入参 schema 与 API 对应关系以 `index.json` 为准。")

    lines.append("## 概览\n")
    lines.append("| 能力域 | 主干 | MCP 数 | tool 数 |")
    lines.append("|--------|------|--------|---------|")
    for dom in domains:
        ms = [m for m in mcps if m["domain"] == dom["id"]]
        lines.append(f"| {dom['name']} | `{dom['trunk']}` | {len(ms)} | {sum(m['tool_count'] for m in ms)} |")
    lines.append("")

    for dom in domains:
        ms = [m for m in mcps if m["domain"] == dom["id"]]
        lines.append(f"## {dom['name']}（`{dom['id']}`，{len(ms)} 个 MCP）\n")
        for m in sorted(ms, key=lambda x: (x["tier"] != "trunk", x["id"])):
            badge = "🌳 主干" if m["tier"] == "trunk" else "分支"
            lines.append(f"### `{m['id']}` · {badge}\n")
            lines.append(f"- **名称**：{m.get('display_name') or m['id']}"
                         + (f" / {m['display_name_en']}" if m.get("display_name_en") else ""))
            lines.append(f"- **官方分类**：`{m.get('official_category')}` · **版本**：`{m.get('mcp_version')}`"
                         f" · **状态**：`{m.get('status')}` · **tool 数**：{m['tool_count']}"
                         f" · **上下文权重**：`{m['context_weight']}`")
            lines.append(f"- **MCP 地址**：`https://connect.zhihuiya.com{m.get('mcp_url') or ''}`")
            lines.append(f"- **能力**：{(m.get('summary') or '')[:300]}")
            if m.get("replaces"):
                lines.append(f"- **工具重复**：可替代 {', '.join(m['replaces'])}")
            lines.append("")
            lines.append("| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |")
            lines.append("|------|------|------------------|--------------------|")
            for t in m["tools"]:
                cap = (t.get("capability") or "").replace("|", "/").replace("\n", " ")[:110]
                fields = []
                for f in t.get("input_fields", []):
                    nm = f"**{f['name']}**" if f.get("required") else f["name"]
                    fields.append(nm)
                fstr = ", ".join(fields) if fields else "—"
                link = t.get("api_link") or {}
                zh = {"verified": "已实测", "high": "高", "medium": "中", "low": "低"}.get(link.get("confidence"))
                if t.get("api_ref") and zh:
                    api = f"{t['api_ref']} ·{zh}"
                elif t.get("mapping_status") == "opaque_workflow":
                    api = "— ·工作流不可推断"
                elif t.get("mapping_status") == "candidate_only":
                    api = "— ·待确认"
                else:
                    api = t.get("api_ref") or "—"
                lines.append(f"| `{t['name']}` | {cap} | {fstr} | {api} |")
            lines.append("")
    lines.append("---\n")
    lines.append(f"*index.json v{meta.get('version', '?')} · tool 入参 schema 见 index.json*")
    return "\n".join(lines) + "\n"


def build_api_catalog(d, meta):
    apis = d["apis"]
    lines = header("API 目录（全量端点与字段概览）", meta,
                   f"共 **{len(apis)}** 个端点（OpenAPI 3.1.0）。"
                   "完整请求/响应字段（含类型、必填、描述）以 `index.json` 的 `apis[]` 为准。")

    by_group = Counter(a.get("group") for a in apis)
    lines.append("## 统计\n")
    lines.append(f"- 分组：{dict(by_group)}")
    lines.append(f"- 含响应字段的端点：{sum(1 for a in apis if a.get('response_fields'))} / {len(apis)}")
    lines.append(f"- 含请求字段的端点：{sum(1 for a in apis if a.get('request_fields'))} / {len(apis)}")
    lines.append("")

    for group in ("DATA", "AI"):
        group_apis = [a for a in apis if a.get("group") == group]
        if not group_apis:
            continue
        lines.append(f"## {group} API（{len(group_apis)} 个）\n")
        cats = {}
        for a in group_apis:
            cats.setdefault(a.get("category") or "未分类", []).append(a)
        for cat, items in cats.items():
            lines.append(f"### {cat}（{len(items)} 个）\n")
            lines.append("| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |")
            lines.append("|------|------|------|------|----------|----------|----------|")
            for a in items:
                req = a.get("request_fields") or []
                resp = a.get("response_fields") or []
                req_s = ", ".join(f["name"] for f in req[:5]) + (f" …(+{len(req)-5})" if len(req) > 5 else "") if req else "—"
                resp_s = ", ".join(f["name"] for f in resp[:5]) + (f" …(+{len(resp)-5})" if len(resp) > 5 else "") if resp else "—"
                name = (a.get("name") or "").replace("|", "/")[:60]
                wr = a.get("mcp_wrappers") or []
                wr_s = ", ".join(f"`{w['mcp']}/{w['tool']}`" for w in wr[:2]) \
                    + (f" …(+{len(wr)-2})" if len(wr) > 2 else "") if wr else "—"
                lines.append(f"| {a.get('code') or '—'} | {name} | {a['method']} | `{a['path']}` | {req_s} | {resp_s} | {wr_s} |")
            lines.append("")
    lines.append("---\n")
    lines.append(f"*index.json v{meta.get('version', '?')} · 字段明细见 index.json 的 apis[]*")
    return "\n".join(lines) + "\n"


def build_mapping_review(d, meta):
    """Human-readable review queue for the inferred MCP<->API links.

    Written for a maintainer who does not want to read JSON: plain-language
    sections, explicit confidence levels, and a copy-paste recipe for
    confirming a mapping in data/manual-overrides.json.
    """
    am = d.get("api_mapping", {})
    st = am.get("stats", {})
    tools = [(mm["id"], t) for mm in d["mcps"] for t in mm["tools"]]
    lines = header(
        "MCP ↔ API 对应关系 · 复核清单", meta,
        "**这份文件回答两个问题**：映射关系是怎么来的、哪些还需要维护者实测确认。")

    lines.append("## 一句话结论\n")
    lines.append("官方开放平台**不提供** MCP 与 API 的对应关系。我们用两份公开数据做了推断："
                 "① 每个 tool 的官方中文能力描述，② 每个 tool 的入参名与每个 API 的请求字段名。"
                 f"结果：{st.get('mapped', 0)} / {st.get('tools_total', 0)} 个 tool 有了对应 API，"
                 f"其中 {st.get('by_status', {}).get('inferred_official_name', 0)} 条证据强、可直接采信；"
                 f"其余 {st.get('unresolved', 0)} 条**明确留空**，不猜测。\n")

    lines.append("## 一、数字\n")
    lines.append("| 项目 | 数量 | 含义 |")
    lines.append("|------|------|------|")
    lines.append(f"| 已建立映射 | {st.get('mapped', 0)} | 有明确对应的 API 编号 |")
    lines.append(f"| ↳ 高置信（官方描述） | {st.get('by_status', {}).get('inferred_official_name', 0)} | tool 描述直接写出源 API 中文名 |")
    lines.append(f"| ↳ 中置信（入参唯一） | {st.get('by_status', {}).get('inferred_param_exclusive', 0)} | 入参名集合在两侧双向唯一 |")
    lines.append(f"| ↳ 低置信（沿用旧标注） | {st.get('by_status', {}).get('legacy_unverified', 0)} | 无本轮证据，仅保留旧值待核 |")
    lines.append(f"| 未建立映射 | {st.get('unresolved', 0)} | 静态数据不足以判定 |")
    lines.append(f"| ↳ 工作流/AI 聚合类 | {st.get('unresolved_by_status', {}).get('opaque_workflow', 0)} | 入参被重写、内部串多个 API |")
    lines.append(f"| ↳ 仅有弱信号 | {st.get('unresolved_by_status', {}).get('candidate_only', 0)} | 有候选但不足以定论 |")
    lines.append(f"| 与旧人工标注冲突 | {st.get('conflicts_with_legacy', 0)} | 已按官方证据修正，旧值保留在 `api_link.legacy_ref` |")
    lines.append(f"| 覆盖到的不同 API | {st.get('distinct_apis_mapped', 0)} | 反向索引见 `apis[].mcp_wrappers` |")
    lines.append("")

    lines.append("## 二、为什么不能只靠「入参/响应参数」推断\n")
    lines.append("1. **响应参数这条路根本不存在**：官方 MCP 详情页只给 tool 的*输入*参数，"
                 "完全不提供返回字段。字段级响应信息只在 `apis[].response_fields` 里，"
                 "两侧没有可比对的输出。")
    lines.append("2. **入参相同 ≠ 同一个 API**：61 个 tool 的入参都是 `patent_id + patent_number`，"
                 "却分别对应著录项目、权利要求、法律状态、法律详情、同族、PDF 全文等不同 API。"
                 "纯参数匹配会把它们全部混在一起（第一版实验曾把 215 条判为高置信，"
                 "其中 153 条的入参签名被 5 个以上 tool 共用、存在明显歧义，该判定已废弃）。")
    lines.append("3. **工作流类工具重写了入参**：查新、FTO、TRIZ 这类 tool 的入参是 "
                 "`task_id / data / execution / user_input`，且一个 tool 内部串行调用多个 API，"
                 "静态 schema 无法还原调用链 —— 这正好属于维护者实测才知道的硬知识。\n")

    lines.append("**最终采用的分层依据**（优先级从高到低）：\n")
    lines.append("| 优先级 | 依据 | 置信度 |")
    lines.append("|--------|------|--------|")
    lines.append("| 1 | 你在 `data/manual-overrides.json` 里实测确认 | 已实测 |")
    lines.append("| 2 | 官方 tool 描述模板「用于获取X相关…」中 X 唯一命中某 API 中文名 | 高 |")
    lines.append("| 3 | 入参名集合在 tool 与 API 两侧双向唯一且完全一致 | 中 |")
    lines.append("| 4 | 上一版人工标注（编号有效但本轮无证据） | 低 |")
    lines.append("| 5 | 仅参数相似 / 工作流类 | **留空，不写入** |")
    lines.append("")

    # --- conflicts ---
    conflicts = [(m, t) for m, t in tools
                 if t.get("api_ref") and t["api_link"].get("legacy_ref")
                 and t["api_link"]["legacy_ref"] != t["api_ref"]]
    lines.append(f"## 三、⚠️ 与旧人工标注冲突（{len(conflicts)} 条，请重点看）\n")
    lines.append("旧标注多为凭语义手工填写，且当时没有官方结构化数据可对照。"
                 "下表已按官方证据修正，**旧值没有删除**，仍存在 `api_link.legacy_ref` 里供你复核。"
                 "若你认为旧值才对，按文末方式覆盖即可。\n")
    lines.append("| MCP / 工具 | 旧标注 | 新推断 | 新 API 名称 | 依据 |")
    lines.append("|------------|--------|--------|-------------|------|")
    for m, t in sorted(conflicts, key=lambda x: (x[0], x[1]["name"])):
        lk = t["api_link"]
        lines.append(f"| `{m}/{t['name']}` | {lk['legacy_ref']} | **{t['api_ref']}** | "
                     f"{t.get('api_ref_name') or ''} | {(lk.get('evidence') or '')[:70]} |")
    lines.append("")

    # --- medium / low ---
    for conf, title, note in (
        ("medium", "四、中置信：靠入参签名推断（建议抽查）",
         "这些 tool 的入参名集合在所有 tool 与所有 API 中都只出现一次，判别力较强，但仍建议抽查。"),
        ("low", "五、低置信：沿用旧标注、本轮无证据支持（建议实测）",
         "这些编号在官方清单里有效，但本轮没有找到描述或参数证据，属于「暂且保留」，最值得优先实测。"),
    ):
        group = [(m, t) for m, t in tools if t["api_link"].get("confidence") == conf]
        lines.append(f"## {title}（{len(group)} 条）\n")
        lines.append(note + "\n")
        lines.append("| MCP / 工具 | 对应 API | 名称 |")
        lines.append("|------------|----------|------|")
        for m, t in sorted(group, key=lambda x: (x[0], x[1]["name"])):
            lines.append(f"| `{m}/{t['name']}` | {t['api_ref']} | {t.get('api_ref_name') or ''} |")
        lines.append("")

    amb = [(m, t) for m, t in tools if t["api_link"].get("ambiguous_code")]
    lines.append(f"## 六、编号歧义（{len(amb)} 条）\n")
    lines.append("同一个 API 编号对应新旧两版接口路径，编号本身不唯一。"
                 "`api_ref_paths` 已列出全部路径，需要你确认 tool 实际走的是哪一个。\n")
    lines.append("| MCP / 工具 | 编号 | 可选路径 |")
    lines.append("|------------|------|----------|")
    for m, t in sorted(amb, key=lambda x: (x[0], x[1]["name"])):
        paths = "、".join(f"`{p['path']}`" for p in t.get("api_ref_paths", []))
        lines.append(f"| `{m}/{t['name']}` | {t['api_ref']} | {paths} |")
    lines.append("")

    opaque = [(m, t) for m, t in tools if t["mapping_status"] == "opaque_workflow"]
    cand = [(m, t) for m, t in tools if t["mapping_status"] == "candidate_only"]
    by_mcp = Counter(m for m, _ in opaque)
    lines.append(f"## 七、静态无法推断（{len(opaque) + len(cand)} 条）\n")
    lines.append(f"- 工作流 / AI 聚合类 **{len(opaque)}** 条：入参被 MCP 重写或异步任务化，"
                 "需实测才知道内部调了哪些 API。")
    lines.append(f"- 仅有弱信号 **{len(cand)}** 条：`api_candidates` 里给了前 3 个候选编号，供你快速判定。\n")
    lines.append("工作流类按 MCP 分布（前 15）：\n")
    lines.append("| MCP | 不可推断的 tool 数 |")
    lines.append("|-----|--------------------|")
    for k, v in by_mcp.most_common(15):
        lines.append(f"| `{k}` | {v} |")
    lines.append("")

    all_codes = {a["code"] for a in d["apis"] if a["code"]}
    wrapped = {a["code"] for a in d["apis"] if a["code"] and a.get("mcp_wrappers")}
    unwrapped = sorted(all_codes - wrapped)
    lines.append(f"## 八、尚未发现 MCP 封装的 API（{len(unwrapped)} 个编号）—— exclusive 排查线索\n")
    lines.append("> ⚠️ **这不是「只能 API 获取」的结论**。它只表示本轮推断没有找到对应 tool："
                 "可能是真的没有 MCP 封装（API-only），也可能是工作流类 tool 内部调用了它但静态看不出来。"
                 "请把它当作**优先实测清单**，确认后再写进 `index.json` 的 `exclusive.api_only`。\n")
    lines.append("前 40 个编号：" + "、".join(f"`{c}`" for c in unwrapped[:40]) + "\n")

    lines.append("## 九、怎么补充确认（不用改代码）\n")
    lines.append("只需编辑一个文件：`data/manual-overrides.json`。它的优先级最高，"
                 "**每月自动刷新不会覆盖你填的内容**。\n")
    lines.append("步骤：\n")
    lines.append("1. 打开 `data/manual-overrides.json`，找到 `\"mappings\": {}`。")
    lines.append("2. 按格式加一条，键是「MCP 的 id/工具名」，值是确认的 API 编号和一句备注。例如：\n")
    lines.append("```json")
    lines.append('{\n  "mappings": {')
    lines.append('    "core-patents/legal_data": {')
    lines.append('      "api_code": "P026",')
    lines.append('      "note": "实测返回法律详情字段，对应 /advanced-patent-data/legal-data"')
    lines.append("    }\n  }\n}")
    lines.append("```\n")
    lines.append("3. 依次运行 `python scripts/infer_api_mapping.py` → "
                 "`python scripts/apply_catalog.py` → `python scripts/build_docs.py`，"
                 "新结论会写进 `index.json` 并重出本文档。")
    lines.append("4. 若确认某工具**没有**对应 API，把 `api_code` 填 `null` 并在备注里说明。\n")
    lines.append("> `exclusive`（API-only / MCP-only）仍按你的要求保持为空，"
                 "可以边用边补，不阻塞发布。\n")
    lines.append("---\n")
    lines.append(f"*index.json v{meta.get('version', '?')} · "
                 "完整候选打分见 raw/mapping-inference.json（本地中间产物，不入库）*")
    return "\n".join(lines) + "\n"


def build_getting_started(d, meta):
    """Human-facing entry point: which MCPs to install first, and what each scenario needs."""
    c = meta["counts"]
    kits = d.get("starter_kits", [])
    bundles = d.get("scenario_bundles", [])
    by_id = {m["id"]: m for m in d["mcps"]}
    pharma_tok = (by_id.get("pharma-intelligence", {}).get("context_cost") or {}).get("est_tokens", 0)
    lines = header(
        "起步配置与典型场景推荐", meta,
        "**这份文件回答**：我该先装哪几个 MCP、每个典型场景需要哪些 MCP 与 API、"
        "哪些属于后续高阶用途。给 AI 平台看的机器版见根目录 `AGENTS.md` 与 `llms.txt`。")

    lines.append("## 一句话结论\n")
    lines.append(f"智慧芽现有 **{c['mcp_in_scope']} 个原生 MCP / {c['tools_total']} 个 tool / "
                 f"{c['api_total']} 个 API**。全量安装光工具定义就要占约 "
                 f"**{c.get('est_context_tokens_all_mcps', 0):,} token**，"
                 "所以**不要全装，也不要默认装 5 根主干**——按你的身份选一个起步包的最小档，"
                 "通常只占全量的 2–4%，遇到具体任务再叠加。\n")

    lines.append("> ⚠️ **纠正一个常见误区**：「5 根主干」是架构概念（每个能力域一根），"
                 "不是安装清单。5 根主干合计约 "
                 f"{c.get('est_context_tokens_5_trunks', 0):,} token，其中 "
                 f"`pharma-intelligence` 单个约 {pharma_tok:,} token。"
                 "只做专利的人装全部主干，等于白扛一整套医药工具定义。\n")

    lines.append("## 一、五个起步包（按你的身份选一个）\n")
    lines.append("| 起步包 | 适合谁 | 最小档 MCP | 最小档 | 标准档 MCP | 标准档 |")
    lines.append("|--------|--------|------------|--------|------------|--------|")
    for k in kits:
        mn = k["minimal"]
        st = k["standard"]
        lines.append(
            f"| **{k['name']}** | {k['who']} | {', '.join(f'`{x}`' for x in mn['mcps'])} | "
            f"{mn['tool_count']} tool / ≈{mn['est_context_tokens']:,} tok ({mn['share_of_full_catalog_pct']}%) | "
            f"{', '.join(f'`{x}`' for x in st['mcps'])} | "
            f"{st['tool_count']} tool / ≈{st['est_context_tokens']:,} tok ({st['share_of_full_catalog_pct']}%) |")
    lines.append("")
    lines.append("> 「≈tok」是把工具定义加载进 AI 客户端的粗略估算，仅用于相对比较；"
                 "百分比是占全量 50 个 MCP 的比例。\n")

    for k in kits:
        lines.append(f"### {k['name']}（`{k['id']}`）\n")
        lines.append(f"- **适合**：{k['who']}")
        lines.append(f"- **最小档**：{', '.join(f'`{x}`' for x in k['minimal']['mcps'])}"
                     f" — {k['minimal']['why']}")
        lines.append(f"- **标准档**：{', '.join(f'`{x}`' for x in k['standard']['mcps'])}"
                     f" — {k['standard']['why']}")
        lines.append(f"- **覆盖场景**：{'、'.join(k['covers_scenarios'])}")
        lines.append(f"- **后续高阶再装**：{', '.join(f'`{x}`' for x in k['upgrade_to']) or '—'}")
        lines.append(f"- **提醒**：{k['note']}")
        lines.append("")

    lines.append("## 二、典型场景 → 需要哪些 MCP 与 API\n")
    for level, title, note in (
        ("starter", "起步级 / 高频场景", "这些场景用 1–2 个轻量 MCP 就能跑起来，建议优先按这里配。"),
        ("advanced", "高阶 / 按需场景", "需要多个 MCP 或重型综合终端，确定真的要用再装。"),
    ):
        group = [b for b in bundles if b.get("level") == level]
        lines.append(f"### {title}（{len(group)} 条）\n")
        lines.append(note + "\n")
        lines.append("| 场景 | 必备 MCP | 涉及 API 编号 | 映射覆盖 | 必备约 token | 可选 MCP |")
        lines.append("|------|----------|---------------|----------|--------------|----------|")
        for b in group:
            req = ", ".join(f"`{x}`" for x in b["required_mcps"]) or "—"
            opt = ", ".join(f"`{x}`" for x in b["optional_mcps"]) or "—"
            codes = b.get("api_codes", [])
            cstr = ", ".join(codes[:6]) + (f" …(+{len(codes)-6})" if len(codes) > 6 else "") if codes else "—"
            cov = b.get("api_coverage") or {}
            covstr = f"{cov.get('mapped_tools', 0)}/{cov.get('tools_total', 0)}"
            lines.append(f"| {b['scenario']} | {req} | {cstr} | {covstr} | "
                         f"{b['required_est_context_tokens']:,} | {opt} |")
        lines.append("")
        lines.append("> **怎么读「涉及 API 编号」这一列**：`api_codes` 只列**已确认映射**的官方 API 编号，"
                     "完整清单在 `index.json`。显示「—」或映射覆盖很低（如 `3/36`）不代表该场景不需要 API，"
                     "而是这些 MCP 工具多为工作流 / AI 聚合类，官方未给出对应关系、本仓库也没有猜测填入。"
                     "排查线索见 [api-mapping-review.md](api-mapping-review.md) 第七、八节。\n")

    lines.append("## 三、只做一件事时怎么装\n")
    lines.append("| 你的需求 | 只装这个 | 约 token |")
    lines.append("|----------|----------|----------|")
    singles = [
        ("只查专利法律状态 / 年费", "patent-status"),
        ("只查临床试验", "clinical-trials"),
        ("只查靶点 / 疾病", "target-disease"),
        ("只做企业主体核验", "company-profile"),
        ("只查科研文献", "literature-search"),
        ("只做 TRIZ 解题", "patsnap-solution-engine"),
        ("只查化妆品法规", "mat-cosmetics-regulatory"),
        ("只查材料配方", "materials-search-mcp"),
    ]
    for label, mid in singles:
        tok = (by_id.get(mid, {}).get("context_cost") or {}).get("est_tokens", 0)
        lines.append(f"| {label} | `{mid}` | {tok:,} |")
    lines.append("")

    lines.append("## 四、数据边界（不要误读）\n")
    for g in meta.get("known_gaps", []):
        lines.append(f"- {g}")
    lines.append("")
    lines.append("> 场景表里的 `api_codes` 是**「这些 MCP 对应哪些 API」**，"
                 "不是「必须另外去申请这些 API Key」。哪些数据真的只能走 API、需要额外配置，"
                 "属于 `exclusive` 实测结论，当前为空，补充后会在这里自动出现。\n")
    lines.append("---\n")
    lines.append(f"*index.json v{meta.get('version', '?')} · "
                 "起步包与场景判断维护在 data/recommendations.json，自动刷新不覆盖*")
    return "\n".join(lines) + "\n"


def build_llms_txt(d, meta):
    """llms.txt — cross-platform, lightweight navigation entry for AI clients."""
    c = meta["counts"]
    base = "https://raw.githubusercontent.com/Philip0910732123/patsnap-mcp-index/main"
    lines = [
        "# patsnap-mcp-index",
        "",
        "> 智慧芽（PatSnap）开放平台 MCP / API 架构索引，社区维护、非官方。"
        "本仓库主要面向 AI 客户端 / 智能体程序化消费：回答「智慧芽有哪些 MCP 与 API、"
        "各自能取什么数据、MCP 与 API 如何对应、某个检索场景该配置哪些」。",
        "",
        f"> 数据版本 v{meta.get('version', '?')} · 更新于 {meta.get('generated_at', '')} · "
        "数据源 open.zhihuiya.com（免登录，每月自动刷新）· "
        f"当前口径：{c['mcp_in_scope']} 个原生 MCP / {c['tools_total']} 个 tool / "
        f"{c['api_total']} 个 API / {c.get('scenario_bundles', 0)} 条场景路由 / "
        f"{c.get('starter_kits', 0)} 个起步包。",
        "",
        "## 读取顺序（重要）",
        "",
        "- `index.json` 约 2.3 MB，**不要整文件塞进对话上下文**。请程序化按需解析：",
        "  1. `meta` — 范围、counts、recommendation_model、known_gaps",
        "  2. `starter_kits` — 起步配置建议（按用户身份，最小/标准两档）",
        "  3. `scenario_bundles` — 场景 → 必备/可选 MCP + `api_codes` + 上下文成本 + 起步/高阶分级",
        "  4. `domains` / `mcps[id]` — 单个 MCP 的 tool 清单、入参 schema、context_cost",
        "  5. `apis[code]` — 单个 API 的请求/响应字段",
        "  6. `api_mapping` — 映射方法与置信度分级",
        "  7. `exclusive` — API-only / MCP-only 硬知识（当前为空，待维护者补充）",
        "",
        "## 文件导航",
        "",
        f"- [AGENTS.md]({base}/AGENTS.md): 给智能体的决策流程与数据边界（回答用户检索需求时先读这个）",
        f"- [README.md]({base}/README.md): 仓库总览、范围说明、更新机制",
        f"- [docs/getting-started.md]({base}/docs/getting-started.md): 起步配置与典型场景推荐（人读）",
        f"- [index.json]({base}/index.json): 机读真相源，唯一权威数据",
        f"- [docs/architecture-tree.md]({base}/docs/architecture-tree.md): 5 域架构树与场景路由表",
        f"- [docs/mcp-catalog.md]({base}/docs/mcp-catalog.md): 50 个 MCP / 411 个 tool 全量明细",
        f"- [docs/api-catalog.md]({base}/docs/api-catalog.md): 376 个 API 端点与字段概览",
        f"- [docs/api-mapping-review.md]({base}/docs/api-mapping-review.md): MCP↔API 映射置信度与复核清单",
        f"- [data/recommendations.json]({base}/data/recommendations.json): 起步包与场景的人工策展判断",
        f"- [data/manual-overrides.json]({base}/data/manual-overrides.json): 映射的实测确认值（优先级最高）",
        "",
        "## 关键约束",
        "",
        "- 只收录智慧芽**原生** MCP / API；第三方数据源封装（pubmed/chembl/otp 等）不纳入。",
        "- `context_cost.est_tokens` 是按 tool schema 字符数 / 3.2 的粗估，仅用于相对择优，不是计费值。",
        "- 官方 MCP 详情页只给 tool 的**入参** schema，不给返回字段；字段级信息在 `apis[].response_fields`。",
        f"- MCP↔API 映射仅覆盖 {c.get('tools_with_api_ref', 0)} / {c['tools_total']} 个 tool；"
        "其余是工作流/AI 聚合类，静态不可推断，**留空而不猜测**。",
        "- `exclusive` 当前为空：不要据此断言「某数据只能 API 获取」或「只能 MCP 获取」。",
        "",
        "## Optional",
        "",
        f"- [scripts/refresh_all.py]({base}/scripts/refresh_all.py): 一键刷新链路（纯 HTTP，免登录）",
        f"- [scripts/recommend.py]({base}/scripts/recommend.py): 场景→MCP/API 建议的参考实现（`python scripts/recommend.py \"FTO\"`）",
        f"- [.github/workflows/refresh.yml]({base}/.github/workflows/refresh.yml): 每月 1 日自动刷新并开 PR",
        "",
    ]
    return "\n".join(lines)


def build_agents_md(d, meta):
    """AGENTS.md — decision procedure for an AI agent answering a user's request."""
    c = meta["counts"]
    lines = [
        "# AGENTS.md — 给 AI 智能体的操作说明",
        "",
        "> 本仓库是智慧芽（PatSnap）MCP / API 的**架构索引**，不是可调用的服务本身。"
        "当用户问「我要查 XX，该配哪些 MCP / API」时，按下面的流程用本仓库数据回答，不要凭印象推荐。",
        "",
        f"> 数据版本 v{meta.get('version', '?')} · 口径：{c['mcp_in_scope']} 个原生 MCP / "
        f"{c['tools_total']} 个 tool / {c['api_total']} 个 API / "
        f"{c.get('starter_kits', 0)} 个起步包 / {c.get('scenario_bundles', 0)} 条场景路由。",
        "",
        "## 0. 读取原则（先做这一步）",
        "",
        "- **`index.json` 约 2.3 MB，禁止整文件塞进上下文。** 用脚本按 key 取子集。",
        "- 先读 `meta`（counts / recommendation_model / known_gaps），再按需要读下面任一块。",
        "- 人读版 `docs/getting-started.md` 只作解释参考，**判断以 `index.json` 为准**。",
        "- 想验证数据是否够用，可跑 `python scripts/recommend.py \"FTO\"`；"
        "那是下面流程的参考实现，可直接复用其匹配与输出逻辑（`--json` 输出结构化结果）。",
        "",
        "## 1. 用户提出一个检索 / 情报需求时的决策流程",
        "",
        "1. **判断身份与领域**：从用户描述推断属于 `starter_kits[].who` 里的哪一类；无法判断时直接问，或按场景匹配。",
        "2. **匹配场景**：在 `scenario_bundles[]` 里按 `scenario` 语义匹配，可读 `note` 辅助；"
        "同时看 `level`（`starter` = 起步典型 / `advanced` = 高阶按需）。",
        "3. **给出四段式建议**：",
        "   - ① **起步配置**：取对应 `starter_kits[].minimal.mcps`，附 `est_context_tokens` 与占全量比例；"
        "说明「先只装这些」。",
        "   - ② **本次场景**：`required_mcps`（必备）+ `optional_mcps`（按需）+ `api_codes`（这些 MCP 对应的官方 API 编号），"
        "附 `required_est_context_tokens`。",
        "   - ③ **是否需要额外 API Key**：读 `api_only_gap`。**当前 `exclusive` 为空，"
        "必须如实说明「哪些数据只能走 API 尚缺实测结论，无法给出完整 API 配置清单」，不要编造。**",
        "   - ④ **后续高阶**：该包的 `upgrade_to`，以及同域 `level=advanced` 的场景。",
        "4. **上下文优化优先级**：最小档 > 标准档 > 叠加分支；"
        "**不要建议「装全部主干」或「装全量 MCP」**；若用户已有多个 MCP，指出 `replaces` 里的重复可裁掉。",
        "",
        "## 2. 回答「智慧芽有多少 MCP / API、能取什么数据」",
        "",
        f"- 数量：读 `meta.counts`（{c['mcp_in_scope']} MCP / {c['tools_total']} tool / {c['api_total']} API）。",
        "- 架构：`domains`（5 个能力域）+ `mcps[].tier`（trunk=架构主干 / branch=场景分支）。"
        "**注意 trunk 是架构概念，不是默认安装清单。**",
        "- 单个 MCP 能取什么：`mcps[id].tools[]` 的 `capability` / `input_fields` / `input_schema`。",
        "- 单个 API 能取什么：`apis[code]` 的 `request_fields` / `response_fields`（"
        f"{c['api_with_response_fields']} 个端点有响应字段）。",
        "- MCP↔API 对应：`tools[].api_ref` + `api_link.confidence`（已实测/高/中/低）"
        "，反向用 `apis[].mcp_wrappers`；方法与边界见 `docs/api-mapping-review.md`。",
        "",
        "## 3. 字段速查",
        "",
        "| 字段 | 含义 |",
        "|------|------|",
        "| `starter_kits[].minimal / standard` | 按身份的起步配置，`est_context_tokens` 是约占用上下文 |",
        "| `scenario_bundles[].level` | `starter` 起步典型 / `advanced` 高阶按需 |",
        "| `scenario_bundles[].api_codes` | 必备 MCP 对应的官方 API 编号（自动反查，非「需额外申请」）；"
        "为空 = 映射未确认，**不等于不需要 API** |",
        "| `scenario_bundles[].api_only_gap` | API 组合建议的完整度说明（当前不完整） |",
        "| `mcps[].context_cost` | tool 数 / 入参数 / 估算 token / 自动分档；`weight_human` 是旧的人工分档 |",
        "| `mcps[].replaces` | 与其他 MCP 重复的工具，可用于裁剪已装服务 |",
        "| `tools[].api_link` | 映射依据、置信度、是否需复核、旧标注审计值 |",
        "| `tools[].mapping_status` | `opaque_workflow` = 工作流类，静态不可推断 |",
        "| `exclusive.api_only / mcp_only` | 只能走 API / 只能走 MCP 的实测硬知识（**当前为空**） |",
        "",
        "## 4. 数据边界（严格遵守，不要编造）",
        "",
    ]
    for g in meta.get("known_gaps", []):
        lines.append(f"- {g}")
    lines += [
        f"- 映射只覆盖 {c.get('tools_with_api_ref', 0)} / {c['tools_total']} 个 tool；"
        "其余保持 `api_ref` 为空，**不要为其硬凑 API 编号**。",
        "- `context_cost.est_tokens` 是粗估，用于相对比较，不能当计费或精确上下文数字引用。",
        "- 本仓库只收录智慧芽原生能力；用户问及 pubmed/chembl/otp 等第三方封装时，"
        "说明它们不在本索引范围（见 `excluded_external`）。",
        "",
        "## 5. 维护（当用户是维护者时）",
        "",
        "- 改起步包 / 场景判断 → 编辑 `data/recommendations.json`。",
        "- 补 MCP→API 实测结论 → 编辑 `data/manual-overrides.json`（优先级最高）。",
        "- 补 API-only / MCP-only → 编辑 `index.json` 的 `exclusive`。",
        "- 改完跑 `python scripts/refresh_all.py`（纯 HTTP、免登录、幂等）；"
        "每月 1 日 GitHub Actions 也会自动跑并开 PR。",
        "",
        "---",
        "",
        f"*index.json v{meta.get('version', '?')} · 本文件由 scripts/build_docs.py 自动生成，请勿手改*",
        "",
    ]
    return "\n".join(lines)


def main():
    d = json.load(open(SRC, encoding="utf-8"))
    meta = d["meta"]
    os.makedirs(DOCS, exist_ok=True)
    outputs = {
        "docs/architecture-tree.md": build_architecture(d, meta),
        "docs/getting-started.md": build_getting_started(d, meta),
        "docs/mcp-catalog.md": build_mcp_catalog(d, meta),
        "docs/api-catalog.md": build_api_catalog(d, meta),
        "docs/api-mapping-review.md": build_mapping_review(d, meta),
        "llms.txt": build_llms_txt(d, meta),
        "AGENTS.md": build_agents_md(d, meta),
    }
    for rel, text in outputs.items():
        path = os.path.join(ROOT, rel)
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print(f"wrote {rel}: {len(text):,} chars, {text.count(chr(10)):,} lines")
    print("counts:", json.dumps(meta["counts"], ensure_ascii=False))


if __name__ == "__main__":
    main()
