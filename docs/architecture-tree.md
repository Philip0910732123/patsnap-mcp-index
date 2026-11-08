# 架构树与场景路由

> 本文件由 `scripts/build_docs.py` 从 `index.json`（机读真相源）自动生成，请勿手改。结构与内容请在 `index.json` 中修改后重跑脚本。

> 数据版本 v0.6.0 · 生成时间 2026-11-08T08:46:13Z · 数据源：open.zhihuiya.com（免登录）

**核心用途**：用户提出一个需求 → AI 平台读取本表 → 反推应配置哪些 MCP / API。

## 一、五根主干（trunk）

> ⚠️ **「主干」是架构概念（每个能力域一根），不是安装建议。** 实测 5 根主干合计约 35,645 token，其中 `pharma-intelligence` 单个就占约 26,955 token。只做单一领域的用户装全部主干会白白占用大量上下文。**起步该装哪几个请看 [getting-started.md](getting-started.md)。**

- **专利检索与分析** (`patent`) — 主干 `core-patents`（20 tool，约 1,820 token，共 23 个 MCP）
  - 面向高频专利工作场景的核心专利数据工具。可查看检索结果、全文附图、法律状态、许可、转移、质押、复审无效等关键信息，帮助团队快速完成专利核查与事实查证。适合用于日常检索、案件研究、法务支持和运营分析。
- **医药情报** (`pharma`) — 主干 `pharma-intelligence`（36 tool，约 26,955 token，共 11 个 MCP）
  - 医药情报终端提供结构化搜索、语义向量搜索和实体检索，涵盖临床试验、药物、靶点、疾病、专利、论文、交易、FDA药品说明书、流行病学、医学指南、财务报告、新闻和转化医学等领域。
- **金融** (`finance`) — 主干 `company-profile`（24 tool，约 2,149 token，共 8 个 MCP）
  - 提供企业科技相关信息的 360 度档案。可综合查看工商、股东、资质证书、科技资质、专利价值、专利转移、标准、软著等多类信息，帮助团队从经营主体、技术实力和无形资产多个维度理解企业。适合用于客户研究、项目尽调和销售支持。
- **材料** (`materials`) — 主干 `materials-search-mcp`（2 tool，约 1,714 token，共 2 个 MCP）
  - 结合标准专利筛选条件、关键词及语义检索，查找包含目标材料名称、性能和合金成分的专利。然后，从专利文献中提取有原文证据支持的材料实体。
- **研发** (`rnd`) — 主干 `patsnap-search`（9 tool，约 3,007 token，共 6 个 MCP）
  - 搜索全球专利、期刊文献和专业信息，读取专利、文献基本信息及专利生命周期详情，并支持申请人标准化与集团层级确认。

## 二、逐域架构树

### 专利检索与分析（`patent`）

- 🌳 **core-patents** ·trunk· ctx=high · 20 tools
  - ├─ `drafting` ·branch· ctx=high · 18 tools
  - ├─ `fto-search` ·branch· ctx=medium · 12 tools
  - ├─ `s-telecom-mcp-sep` ·branch· ctx=low · 1 tools
  - ├─ `patent-analysis` ·branch· ctx=low · 2 tools
  - ├─ `patsnap-workspace` ·branch· ctx=low · 11 tools
  - ├─ `document-processing` ·branch· ctx=low · 4 tools
  - ├─ `patsnap-analytics` ·branch· ctx=low · 1 tools
  - ├─ `patsnap-ip-searching` ·branch· ctx=low · 5 tools
  - ├─ `patsnap-web-search` ·branch· ctx=low · 1 tools
  - ├─ `s-telecom-mcp-tools` ·branch· ctx=low · 4 tools
  - ├─ `novelty-search-lite` ·branch· ctx=medium · 11 tools
  - ├─ `intangible-assets` ·branch· ctx=low · 5 tools
  - ├─ `patent-dispute` ·branch· ctx=high · 21 tools · replaces: core-patents
  - ├─ `design-fto-search-mcp` ·branch· ctx=low · 4 tools
  - ├─ `ip-courses` ·branch· ctx=low · 3 tools
  - ├─ `landscape-projects` ·branch· ctx=low · 6 tools
  - ├─ `patent-visual` ·branch· ctx=high · 24 tools
  - ├─ `patent-value` ·branch· ctx=medium · 10 tools
  - ├─ `patent-mining` ·branch· ctx=medium · 7 tools
  - ├─ `patent-landscape` ·branch· ctx=high · 24 tools
  - ├─ `patent-briefing` ·branch· ctx=medium · 12 tools · replaces: core-patents
  - ├─ `patent-status` ·branch· ctx=medium · 12 tools

### 医药情报（`pharma`）

- 🌳 **pharma-intelligence** ·trunk· ctx=high · 36 tools
  - ├─ `target-disease` ·branch· ctx=low · 3 tools
  - ├─ `scientific-translational-evidence` ·branch· ctx=low · 2 tools
  - ├─ `sar-extraction` ·branch· ctx=low · 2 tools
  - ├─ `regulatory-guidelines` ·branch· ctx=low · 2 tools
  - ├─ `drug-asset` ·branch· ctx=low · 4 tools
  - ├─ `current-awareness` ·branch· ctx=low · 2 tools
  - ├─ `company-deal-intelligence` ·branch· ctx=low · 5 tools
  - ├─ `clinical-trials` ·branch· ctx=low · 4 tools
  - ├─ `chemical-molecular` ·branch· ctx=low · 7 tools
  - ├─ `biology-modality` ·branch· ctx=medium · 11 tools

### 金融（`finance`）

- 🌳 **company-profile** ·trunk· ctx=high · 24 tools
  - ├─ `company-intelligence-mcp` ·branch· ctx=medium · 6 tools
  - ├─ `company-tags` ·branch· ctx=medium · 8 tools
  - ├─ `patent-risk` ·branch· ctx=low · 3 tools
  - ├─ `tech-diligence` ·branch· ctx=medium · 12 tools
  - ├─ `company-credit` ·branch· ctx=medium · 14 tools · replaces: company-profile
  - ├─ `global-tech-eval` ·branch· ctx=medium · 8 tools
  - ├─ `company-risk` ·branch· ctx=low · 5 tools

### 材料（`materials`）

- 🌳 **materials-search-mcp** ·trunk· ctx=low · 2 tools
  - ├─ `mat-cosmetics-regulatory` ·branch· ctx=low · 1 tools

### 研发（`rnd`）

- 🌳 **patsnap-search** ·trunk· ctx=low · 9 tools
  - ├─ `patsnap-triz-case-library` ·branch· ctx=low · 2 tools
  - ├─ `patsnap-solution-engine` ·branch· ctx=low · 6 tools
  - ├─ `report-gen` ·branch· ctx=low · 6 tools
  - ├─ `tech-collab` ·branch· ctx=low · 4 tools
  - ├─ `literature-search` ·branch· ctx=low · 5 tools

## 三、场景路由表（需求 → MCP + API 组合）

`api_codes` 由已建立的 MCP→API 映射自动反查，完整列表见 `index.json`；表中只显示前 6 个。**显示「—」不代表不需要 API**，只表示该场景涉及的 MCP 工具尚未建立映射（多为工作流/AI 聚合类）。`api_only_gap` 说明「只能走 API、需额外申请 API Key」的部分尚不完整。

### 起步级 / 典型场景（20 条）

| 场景 | 必备 MCP | 可选 MCP | 涉及 API 编号 | 必备约 token |
|------|----------|----------|---------------|--------------|
| 专利检索与阅读 | `core-patents` | `patsnap-search`, `patent-briefing` | P002, P012, P014, P018, P019, P020 …(+12) | 1,820 |
| 查新检索 | `novelty-search-lite`, `core-patents` | `patsnap-ip-searching` | AI35-4, AI35-6, P002, P008, P012, P014 …(+15) | 3,073 |
| 法律状态/年费/诉讼监测 | `patent-status` | `patent-dispute`, `global-tech-eval`, `patent-risk` | P026, P027, P028, P029, P030, P031 …(+6) | 1,028 |
| 临床试验调研 | `clinical-trials` | `pharma-intelligence` | — | 1,952 |
| 靶点/疾病画像 | `target-disease` | `pharma-intelligence`, `scientific-translational-evidence` | — | 353 |
| 药物管线与资产 | `drug-asset` | `company-deal-intelligence`, `pharma-intelligence` | — | 1,721 |
| 企业画像/尽调 | `company-profile` | `company-credit`, `company-tags`, `tech-diligence`, `company-risk` | C001, C002, C003, C004, C007, C013 …(+16) | 2,149 |
| 文献检索 | `patsnap-search` | `literature-search`, `pharma-intelligence` | — | 3,007 |
| TRIZ 创新/降本 | `patsnap-solution-engine` | `patsnap-triz-case-library` | AI33-1 | 570 |
| 文档 OCR/翻译 | `document-processing` | — | AI61 | 654 |
| 企业科创力快评 | `company-intelligence-mcp` | `global-tech-eval` | — | 1,101 |
| 行业动态 / 竞情监测 | `current-awareness` | `patsnap-web-search`, `company-deal-intelligence` | — | 621 |
| 技术网页信息检索 | `patsnap-web-search` | — | — | 224 |
| 防侵权检索（简化流程） | `fto-search` | `patsnap-ip-searching`, `core-patents` | — | 2,462 |
| 平台分析任务状态 | `patsnap-analytics` | — | — | 110 |
| IP 知识学习 / 培训 | `ip-courses` | — | AC01, AC02, AC03 | 275 |
| 材料配方 / 性能检索 | `materials-search-mcp` | `chemical-molecular`, `patsnap-search` | — | 1,714 |
| 化妆品法规合规 | `mat-cosmetics-regulatory` | `materials-search-mcp` | — | 172 |
| 药品监管 / 临床指南 | `regulatory-guidelines` | `pharma-intelligence`, `clinical-trials` | — | 303 |
| 转化医学证据检索 | `scientific-translational-evidence` | `target-disease`, `pharma-intelligence` | — | 537 |

### 高阶 / 按需场景（16 条）

| 场景 | 必备 MCP | 可选 MCP | 涉及 API 编号 | 必备约 token |
|------|----------|----------|---------------|--------------|
| 发明 FTO 分析 | `patsnap-ip-searching`, `core-patents`, `patent-status` | `patent-dispute`, `fto-search` | AI35-2, AI39-1, AI66-4, P002, P010, P012 …(+22) | 3,648 |
| 外观 FTO 分析 | `design-fto-search-mcp`, `core-patents` | `patsnap-ip-searching` | AI39-1, AI39-3, P002, P010, P012, P014 …(+15) | 2,574 |
| 专利全景分析 | `patent-landscape`, `core-patents` | `patent-visual`, `landscape-projects` | D005, D006, D009, D010, D103, D105 …(+22) | 5,143 |
| 专利价值评估 | `patent-value`, `core-patents` | `company-profile` | P002, P012, P014, P018, P019, P020 …(+22) | 2,794 |
| 专利纠纷分析 | `patent-dispute`, `core-patents`, `patent-status` | — | P002, P012, P014, P018, P019, P020 …(+19) | 4,705 |
| 技术挖掘/三要素 | `patent-mining`, `core-patents` | `patent-analysis` | P002, P012, P014, P018, P019, P020 …(+17) | 2,531 |
| 医药综合情报 | `pharma-intelligence` | `clinical-trials`, `drug-asset`, `target-disease`, `company-deal-intelligence` | AI01, P002, P012 | 26,955 |
| 化学分子/ADMET/SAR | `chemical-molecular` | `sar-extraction` | — | 1,721 |
| 生物序列分析 | `biology-modality` | — | — | 5,741 |
| 科创评估/风险预警 | `global-tech-eval` | `company-risk`, `patent-risk`, `tech-diligence` | C022, C023, C024, C025, C026, C027 …(+1) | 721 |
| 报告生成 | `report-gen` | `patsnap-workspace` | AI29-1, AI29-3, AI30 | 554 |
| 通信标准/SEP | `s-telecom-mcp-tools` | `s-telecom-mcp-sep`, `patent-status` | — | 892 |
| 企业无形资产盘点 | `intangible-assets` | `company-profile`, `patent-value` | C033, C034, C046 | 635 |
| 专利撰写 / 交底书辅助 | `drafting` | `core-patents`, `patsnap-search` | — | 3,021 |
| 工作空间专利集合读取 | `patsnap-workspace` | `report-gen`, `patent-landscape` | — | 3,021 |
| 产学研合作 / 专家寻找 | `tech-collab` | `literature-search`, `patsnap-search` | C112, C114, C115 | 340 |

## 四、上下文成本（装越多越费积分的量化）

- 自动分档（按真实 schema 体量）：高 7 个 / 中 14 个 / 低 29 个 MCP
- 全量 50 个 MCP 合计约 **87,286 token**；5 根主干合计约 **35,645 token**。
- ★ **不要默认装 5 根主干**。起步应按用户身份选 1 个包的最小档（通常只占全量 2–4%），按场景再叠加；详见 [getting-started.md](getting-started.md)。
- 估算方式：工具名 + 能力描述 + `input_schema` JSON 的字符数 / 3.2，仅用于相对比较，不是精确 tokenizer 结果，不可用于计费核算。

最重的 8 个 MCP（单独装就要考虑的）：

| MCP | tool 数 | 约 token |
|-----|---------|----------|
| `pharma-intelligence` | 36 | 26,955 |
| `biology-modality` | 11 | 5,741 |
| `patent-visual` | 24 | 3,966 |
| `patent-landscape` | 24 | 3,323 |
| `drafting` | 18 | 3,021 |
| `patsnap-workspace` | 11 | 3,021 |
| `patsnap-search` | 9 | 3,007 |
| `fto-search` | 12 | 2,462 |

## 五、专属知识（API-only / MCP-only）

- api_only：`0` 条（待维护者逐个补充）
- mcp_only：`0` 条（待维护者逐个补充）

## 六、已知数据边界

- 官方 MCP 详情页只提供 tool 的入参 schema，不提供返回字段；tools[].data_fields 暂为空，字段级信息见 apis[].response_fields。因此无法用「响应参数」反推 MCP↔API 对应关系。
- AI 工作流类 tool 重写入参（task_id/data/execution）并串行调用多个 API，静态 schema 无法还原调用链；这类工具的映射需维护者实测补充，见 tools[].mapping_status = opaque_workflow 与 docs/api-mapping-review.md。
- 20 个 API 编号对应新旧两版 path，编号本身不唯一；涉及条目以 tools[].api_link.ambiguous_code 标记并附全部 path。
- exclusive（API-only / MCP-only 实测结论）按维护者要求保持为空，逐个补充。
- 场景的 API 组合建议不完整：scenario_bundles[].api_codes 只来自已建立的 MCP→API 映射；exclusive 为空，因此「哪些数据只能 API 获取、需额外申请 API Key」尚缺实测结论。

## 七、已排除的第三方封装（非智慧芽原生）

以下为第三方数据源封装 MCP，非智慧芽原生，按你的要求本仓库暂不纳入；后续如需再补。

- pubmed
- ncbi-mcp
- chembl
- uniprot-mcp
- otp-mcp
- aact-db
- clinicaltrialsgov
- nccn-guidelines
- fda-mcp-server
- who-mcp-server
- globocan-mcp
- rdkit
- mineru

---

*index.json v0.6.0 · 2026-11-08T08:46:13Z*
