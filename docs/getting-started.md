# 起步配置与典型场景推荐

> 本文件由 `scripts/build_docs.py` 从 `index.json`（机读真相源）自动生成，请勿手改。结构与内容请在 `index.json` 中修改后重跑脚本。

> 数据版本 v0.6.0 · 生成时间 2026-11-08T08:46:13Z · 数据源：open.zhihuiya.com（免登录）

**这份文件回答**：我该先装哪几个 MCP、每个典型场景需要哪些 MCP 与 API、哪些属于后续高阶用途。给 AI 平台看的机器版见根目录 `AGENTS.md` 与 `llms.txt`。

## 一句话结论

智慧芽现有 **50 个原生 MCP / 411 个 tool / 376 个 API**。全量安装光工具定义就要占约 **87,286 token**，所以**不要全装，也不要默认装 5 根主干**——按你的身份选一个起步包的最小档，通常只占全量的 2–4%，遇到具体任务再叠加。

> ⚠️ **纠正一个常见误区**：「5 根主干」是架构概念（每个能力域一根），不是安装清单。5 根主干合计约 35,645 token，其中 `pharma-intelligence` 单个约 26,955 token。只做专利的人装全部主干，等于白扛一整套医药工具定义。

## 一、五个起步包（按你的身份选一个）

| 起步包 | 适合谁 | 最小档 MCP | 最小档 | 标准档 MCP | 标准档 |
|--------|--------|------------|--------|------------|--------|
| **专利 / IP 从业者** | 企业 IP 部门、专利代理师、专利分析师、律所专利团队 | `core-patents` | 20 tool / ≈1,820 tok (2.1%) | `core-patents`, `patent-status`, `patsnap-ip-searching` | 37 tool / ≈3,648 tok (4.2%) |
| **医药 / 生命科学情报** | 药企 BD、研发立项、临床与注册、医药投资分析 | `drug-asset`, `clinical-trials` | 8 tool / ≈3,673 tok (4.2%) | `pharma-intelligence` | 36 tool / ≈26,955 tok (30.9%) |
| **企业 / 投资尽调** | 投资机构、券商研究、企业战略、供应链风控、科创板评估 | `company-profile` | 24 tool / ≈2,149 tok (2.5%) | `company-profile`, `tech-diligence`, `company-risk` | 41 tool / ≈3,477 tok (4.0%) |
| **材料 / 配方研发** | 材料研发工程师、日化配方、高分子与金属工艺、化妆品法规 | `materials-search-mcp` | 2 tool / ≈1,714 tok (2.0%) | `materials-search-mcp`, `chemical-molecular`, `mat-cosmetics-regulatory` | 10 tool / ≈3,607 tok (4.1%) |
| **研发 / 创新工程师** | 企业研发、技术预研、创新方法推进、科技情报 | `patsnap-search` | 9 tool / ≈3,007 tok (3.4%) | `patsnap-search`, `patsnap-solution-engine`, `report-gen` | 21 tool / ≈4,131 tok (4.7%) |

> 「≈tok」是把工具定义加载进 AI 客户端的粗略估算，仅用于相对比较；百分比是占全量 50 个 MCP 的比例。

### 专利 / IP 从业者（`patent-practitioner`）

- **适合**：企业 IP 部门、专利代理师、专利分析师、律所专利团队
- **最小档**：`core-patents` — 一个 MCP 覆盖全球专利检索、著录项目、权利要求、说明书、附图、同族与引用，是专利场景的最小可用闭环。
- **标准档**：`core-patents`, `patent-status`, `patsnap-ip-searching` — 在检索之上补法律状态/年费/诉讼监测，以及 FTO/查新检索入口，覆盖专利日常工作约 80% 的需求。
- **覆盖场景**：专利检索与阅读、法律状态/年费/诉讼监测、发明 FTO 分析、查新检索、专利纠纷分析
- **后续高阶再装**：`patent-landscape`, `patent-visual`, `novelty-search-lite`, `design-fto-search-mcp`, `patent-dispute`, `drafting`, `fto-search`
- **提醒**：不要一上来装专利域全部 23 个 MCP。全景分析、价值评估、撰写、SEP 对照等都属高阶，按具体任务再叠加。

### 医药 / 生命科学情报（`pharma-analyst`）

- **适合**：药企 BD、研发立项、临床与注册、医药投资分析
- **最小档**：`drug-asset`, `clinical-trials` — 只查药物管线与临床试验时，两个小而专的 MCP 就够。★ 医药主干 pharma-intelligence 单个约 2.7 万 token，是本档的十几倍，轻量用户不要装。
- **标准档**：`pharma-intelligence` — 一个综合终端已聚合临床、药物、靶点、疾病、生物序列、交易、FDA、流行病学、指南、财报、新闻、转化医学等十余类数据，可替代几乎全部细分 MCP；代价是工具定义较重。
- **覆盖场景**：医药综合情报、临床试验调研、靶点/疾病画像、药物管线与资产、行业动态 / 竞情监测
- **后续高阶再装**：`biology-modality`, `chemical-molecular`, `company-deal-intelligence`, `regulatory-guidelines`, `scientific-translational-evidence`, `sar-extraction`
- **提醒**：★ 这是全库上下文成本最悬殊的一个域：若只做单一细分（如只查临床、只查靶点），优先按场景表装 1 个小 MCP，别装主干。需要跨十几类数据联动时才上 pharma-intelligence。

### 企业 / 投资尽调（`corporate-diligence`）

- **适合**：投资机构、券商研究、企业战略、供应链风控、科创板评估
- **最小档**：`company-profile` — 企业科技 360 档案一个 MCP 即覆盖工商、资质、团队、投融资、专利与科技画像，适合快速核验主体。
- **标准档**：`company-profile`, `tech-diligence`, `company-risk` — 补上科创投资尽调与风险预警，形成『核验 → 评估 → 预警』闭环。
- **覆盖场景**：企业画像/尽调、科创评估/风险预警、企业科创力快评、企业无形资产盘点
- **后续高阶再装**：`company-credit`, `company-tags`, `global-tech-eval`, `company-intelligence-mcp`, `patent-risk`, `intangible-assets`
- **提醒**：company-profile 与 company-credit 在企业工商维度有重叠，除非需要更细的信用档案，否则不要同时装。

### 材料 / 配方研发（`materials-rnd`）

- **适合**：材料研发工程师、日化配方、高分子与金属工艺、化妆品法规
- **最小档**：`materials-search-mcp` — 材料搜索（金属、高分子配方、化妆品等）是材料域的最小可用入口，只有 2 个工具。
- **标准档**：`materials-search-mcp`, `chemical-molecular`, `mat-cosmetics-regulatory` — 补化学分子结构/ADMET 与化妆品法规合规查询，覆盖配方研发到合规的主要链路。
- **覆盖场景**：材料配方 / 性能检索、化妆品法规合规、化学分子/ADMET/SAR
- **后续高阶再装**：`sar-extraction`, `patsnap-search`, `literature-search`
- **提醒**：材料域目前仅 2 个原生 MCP，是五个域里最轻的。化学分子相关 MCP 按官方分类归在医药情报，此处按用途跨域引用。

### 研发 / 创新工程师（`rnd-engineer`）

- **适合**：企业研发、技术预研、创新方法推进、科技情报
- **最小档**：`patsnap-search` — 专利 + 文献融合检索一个入口即可起步，避免同时装专利库和文献库两个 MCP。
- **标准档**：`patsnap-search`, `patsnap-solution-engine`, `report-gen` — 在融合检索之上补 TRIZ 创新方案生成与报告生成，形成『检索 → 解题 → 输出』链路。
- **覆盖场景**：文献检索、TRIZ 创新/降本、报告生成、产学研合作 / 专家寻找
- **后续高阶再装**：`literature-search`, `patsnap-triz-case-library`, `tech-collab`, `document-processing`
- **提醒**：若只查科研文献，可把 minimal 降级为 literature-search（约 480 token，比融合检索轻 6 倍）。

## 二、典型场景 → 需要哪些 MCP 与 API

### 起步级 / 高频场景（20 条）

这些场景用 1–2 个轻量 MCP 就能跑起来，建议优先按这里配。

| 场景 | 必备 MCP | 涉及 API 编号 | 映射覆盖 | 必备约 token | 可选 MCP |
|------|----------|---------------|----------|--------------|----------|
| 专利检索与阅读 | `core-patents` | P002, P012, P014, P018, P019, P020 …(+12) | 30/41 | 1,820 | `patsnap-search`, `patent-briefing` |
| 查新检索 | `novelty-search-lite`, `core-patents` | AI35-4, AI35-6, P002, P008, P012, P014 …(+15) | 26/36 | 3,073 | `patsnap-ip-searching` |
| 法律状态/年费/诉讼监测 | `patent-status` | P026, P027, P028, P029, P030, P031 …(+6) | 41/44 | 1,028 | `patent-dispute`, `global-tech-eval`, `patent-risk` |
| 临床试验调研 | `clinical-trials` | — | 3/40 | 1,952 | `pharma-intelligence` |
| 靶点/疾病画像 | `target-disease` | — | 3/41 | 353 | `pharma-intelligence`, `scientific-translational-evidence` |
| 药物管线与资产 | `drug-asset` | — | 3/45 | 1,721 | `company-deal-intelligence`, `pharma-intelligence` |
| 企业画像/尽调 | `company-profile` | C001, C002, C003, C004, C007, C013 …(+16) | 60/63 | 2,149 | `company-credit`, `company-tags`, `tech-diligence`, `company-risk` |
| 文献检索 | `patsnap-search` | — | 8/50 | 3,007 | `literature-search`, `pharma-intelligence` |
| TRIZ 创新/降本 | `patsnap-solution-engine` | AI33-1 | 1/8 | 570 | `patsnap-triz-case-library` |
| 文档 OCR/翻译 | `document-processing` | AI61 | 2/4 | 654 | — |
| 企业科创力快评 | `company-intelligence-mcp` | — | 7/14 | 1,101 | `global-tech-eval` |
| 行业动态 / 竞情监测 | `current-awareness` | — | 0/8 | 621 | `patsnap-web-search`, `company-deal-intelligence` |
| 技术网页信息检索 | `patsnap-web-search` | — | 0/1 | 224 | — |
| 防侵权检索（简化流程） | `fto-search` | — | 22/37 | 2,462 | `patsnap-ip-searching`, `core-patents` |
| 平台分析任务状态 | `patsnap-analytics` | — | 0/1 | 110 | — |
| IP 知识学习 / 培训 | `ip-courses` | AC01, AC02, AC03 | 3/3 | 275 | — |
| 材料配方 / 性能检索 | `materials-search-mcp` | — | 0/18 | 1,714 | `chemical-molecular`, `patsnap-search` |
| 化妆品法规合规 | `mat-cosmetics-regulatory` | — | 0/3 | 172 | `materials-search-mcp` |
| 药品监管 / 临床指南 | `regulatory-guidelines` | — | 3/42 | 303 | `pharma-intelligence`, `clinical-trials` |
| 转化医学证据检索 | `scientific-translational-evidence` | — | 3/41 | 537 | `target-disease`, `pharma-intelligence` |

> **怎么读「涉及 API 编号」这一列**：`api_codes` 只列**已确认映射**的官方 API 编号，完整清单在 `index.json`。显示「—」或映射覆盖很低（如 `3/36`）不代表该场景不需要 API，而是这些 MCP 工具多为工作流 / AI 聚合类，官方未给出对应关系、本仓库也没有猜测填入。排查线索见 [api-mapping-review.md](api-mapping-review.md) 第七、八节。

### 高阶 / 按需场景（16 条）

需要多个 MCP 或重型综合终端，确定真的要用再装。

| 场景 | 必备 MCP | 涉及 API 编号 | 映射覆盖 | 必备约 token | 可选 MCP |
|------|----------|---------------|----------|--------------|----------|
| 发明 FTO 分析 | `patsnap-ip-searching`, `core-patents`, `patent-status` | AI35-2, AI39-1, AI66-4, P002, P010, P012 …(+22) | 54/70 | 3,648 | `patent-dispute`, `fto-search` |
| 外观 FTO 分析 | `design-fto-search-mcp`, `core-patents` | AI39-1, AI39-3, P002, P010, P012, P014 …(+15) | 25/29 | 2,574 | `patsnap-ip-searching` |
| 专利全景分析 | `patent-landscape`, `core-patents` | D005, D006, D009, D010, D103, D105 …(+22) | 40/74 | 5,143 | `patent-visual`, `landscape-projects` |
| 专利价值评估 | `patent-value`, `core-patents` | P002, P012, P014, P018, P019, P020 …(+22) | 50/54 | 2,794 | `company-profile` |
| 专利纠纷分析 | `patent-dispute`, `core-patents`, `patent-status` | P002, P012, P014, P018, P019, P020 …(+19) | 50/53 | 4,705 | — |
| 技术挖掘/三要素 | `patent-mining`, `core-patents` | P002, P012, P014, P018, P019, P020 …(+17) | 25/29 | 2,531 | `patent-analysis` |
| 医药综合情报 | `pharma-intelligence` | AI01, P002, P012 | 3/52 | 26,955 | `clinical-trials`, `drug-asset`, `target-disease`, `company-deal-intelligence` |
| 化学分子/ADMET/SAR | `chemical-molecular` | — | 0/9 | 1,721 | `sar-extraction` |
| 生物序列分析 | `biology-modality` | — | 0/11 | 5,741 | — |
| 科创评估/风险预警 | `global-tech-eval` | C022, C023, C024, C025, C026, C027 …(+1) | 26/28 | 721 | `company-risk`, `patent-risk`, `tech-diligence` |
| 报告生成 | `report-gen` | AI29-1, AI29-3, AI30 | 3/17 | 554 | `patsnap-workspace` |
| 通信标准/SEP | `s-telecom-mcp-tools` | — | 12/17 | 892 | `s-telecom-mcp-sep`, `patent-status` |
| 企业无形资产盘点 | `intangible-assets` | C033, C034, C046 | 35/39 | 635 | `company-profile`, `patent-value` |
| 专利撰写 / 交底书辅助 | `drafting` | — | 18/47 | 3,021 | `core-patents`, `patsnap-search` |
| 工作空间专利集合读取 | `patsnap-workspace` | — | 15/41 | 3,021 | `report-gen`, `patent-landscape` |
| 产学研合作 / 专家寻找 | `tech-collab` | C112, C114, C115 | 8/18 | 340 | `literature-search`, `patsnap-search` |

> **怎么读「涉及 API 编号」这一列**：`api_codes` 只列**已确认映射**的官方 API 编号，完整清单在 `index.json`。显示「—」或映射覆盖很低（如 `3/36`）不代表该场景不需要 API，而是这些 MCP 工具多为工作流 / AI 聚合类，官方未给出对应关系、本仓库也没有猜测填入。排查线索见 [api-mapping-review.md](api-mapping-review.md) 第七、八节。

## 三、只做一件事时怎么装

| 你的需求 | 只装这个 | 约 token |
|----------|----------|----------|
| 只查专利法律状态 / 年费 | `patent-status` | 1,028 |
| 只查临床试验 | `clinical-trials` | 1,952 |
| 只查靶点 / 疾病 | `target-disease` | 353 |
| 只做企业主体核验 | `company-profile` | 2,149 |
| 只查科研文献 | `literature-search` | 482 |
| 只做 TRIZ 解题 | `patsnap-solution-engine` | 570 |
| 只查化妆品法规 | `mat-cosmetics-regulatory` | 172 |
| 只查材料配方 | `materials-search-mcp` | 1,714 |

## 四、数据边界（不要误读）

- 官方 MCP 详情页只提供 tool 的入参 schema，不提供返回字段；tools[].data_fields 暂为空，字段级信息见 apis[].response_fields。因此无法用「响应参数」反推 MCP↔API 对应关系。
- AI 工作流类 tool 重写入参（task_id/data/execution）并串行调用多个 API，静态 schema 无法还原调用链；这类工具的映射需维护者实测补充，见 tools[].mapping_status = opaque_workflow 与 docs/api-mapping-review.md。
- 20 个 API 编号对应新旧两版 path，编号本身不唯一；涉及条目以 tools[].api_link.ambiguous_code 标记并附全部 path。
- exclusive（API-only / MCP-only 实测结论）按维护者要求保持为空，逐个补充。
- 场景的 API 组合建议不完整：scenario_bundles[].api_codes 只来自已建立的 MCP→API 映射；exclusive 为空，因此「哪些数据只能 API 获取、需额外申请 API Key」尚缺实测结论。

> 场景表里的 `api_codes` 是**「这些 MCP 对应哪些 API」**，不是「必须另外去申请这些 API Key」。哪些数据真的只能走 API、需要额外配置，属于 `exclusive` 实测结论，当前为空，补充后会在这里自动出现。

---

*index.json v0.6.0 · 起步包与场景判断维护在 data/recommendations.json，自动刷新不覆盖*
