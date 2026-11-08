# 智慧芽 MCP / API 架构索引（非官方社区维护 · 机读优先）

> 本仓库为社区维护的非官方智慧芽 MCP / API 架构索引。**主要面向 AI 客户端 / 智能体消费**：WorkBuddy 这类平台读到本仓库后，即可在用户提出一个检索需求时回答「智慧芽有多少 MCP / API、各自能取什么数据、MCP 与 API 怎么对应、这个场景该配哪些、先装哪几个起步、哪些属于高阶用途」，而不必让用户逐个试错，也避免 MCP 装得越多越占用大上下文（越费积分）。
>
> **给 AI 平台的入口**：根目录 [llms.txt](llms.txt)（轻量导航）与 [AGENTS.md](AGENTS.md)（决策流程与数据边界）。**给人看的入口**：[docs/getting-started.md](docs/getting-started.md)。三者都从 `index.json` 自动生成。
>
> 数据来源为 [open.zhihuiya.com](https://open.zhihuiya.com) 公开页面与 OpenAPI 规范（**免登录**）。如需获取 API Key 调用数据，请访问该站点。

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <img src="https://img.shields.io/badge/%E6%99%BA%E6%85%A7%E8%8A%BD%E5%8E%9F%E7%94%9F-MCP-50-blue.svg" alt="智慧芽原生 MCP: 50">
  <img src="https://img.shields.io/badge/%E8%83%BD%E5%8A%9B%E5%9F%9F%2F%E4%B8%BB%E5%B9%B2-5-green.svg" alt="能力域/主干: 5">
  <img src="https://img.shields.io/badge/Tools-411-orange.svg" alt="Tools: 411">
  <img src="https://img.shields.io/badge/API-376-blueviolet.svg" alt="API: 376">
  <img src="https://img.shields.io/badge/%E5%88%B7%E6%96%B0-%E5%85%8D%E7%99%BB%E5%BD%95%E5%85%A8%E8%87%AA%E5%8A%A8-brightgreen.svg" alt="免登录全自动">
</p>

## 本轮更新（v0.6.0 · 2026-11-08）

**补齐「起步配置 + 场景组合建议」这一层，让仓库真正能被 AI 平台用来回答配置问题**：

- **新增 5 个起步包**（按用户身份/领域，每个分最小档 / 标准档两档）：专利 IP、医药情报、企业尽调、材料研发、研发创新。最小档通常只占全量上下文的 **2–4%**。
- **⚠️ 纠正旧建议**：此前 README 写「默认只装 5 根主干」，实测 5 根主干合计约 **35,645 token**，其中 `pharma-intelligence` 单个就占 **26,955 token**——只做专利的用户装全部主干等于白扛一整套医药工具定义。**「主干」是架构概念，不是安装清单**，已全文修正。
- **场景路由表扩到 36 条**（20 起步级 / 16 高阶），覆盖 **50/50 个 MCP**（上一版 21 条漏了 14 个）。每条新增结构化 `api_codes`（从 204 条映射自动反查）、`level`、`est_context_tokens`、`api_only_gap`。
- **上下文成本可计算**：`mcps[].context_cost` 由 411 个 tool 的真实 schema 自动算出 tool 数 / 入参数 / 估算 token，替代原先人工拍的 high/medium/low（旧值保留作对照）。
- **新增 AI 入口**：`llms.txt` + `AGENTS.md`，写明读取顺序、四段式推荐流程与「不要编造」的数据边界；`docs/getting-started.md` 是人读版起步指南。
- **人工判断独立成文件**：[data/recommendations.json](data/recommendations.json)（起步包与场景的「该装什么」），与 `data/manual-overrides.json` 一样，月度自动刷新不覆盖。

> v0.5.0：新增 MCP ↔ API 对应关系推断，复核修正 15 条旧人工标注冲突（[复核清单](docs/api-mapping-review.md)）。v0.4.0：全量重抓 50 MCP / 411 tool / 376 API，自动化改为纯 HTTP 免登录。

## 范围说明（重要）

- **纳入索引**：仅智慧芽**原生** MCP / API，共 **50 个 MCP / 411 个 tool / 376 个 API 端点**。
- **单列排除**：13 个第三方数据源封装（pubmed / ncbi / chembl / uniprot / otp / aact / clinicaltrialsgov / nccn / fda / who / globocan / rdkit / mineru）非智慧芽原生，按维护者决策暂不纳入深度索引，仅列名于 `index.json → excluded_external`。
- **不在本仓库**：任何密钥、Cookie、登录态。抓取与刷新均不需要凭据。

## 这是什么 / 设计目标

智慧芽开放平台提供了数十个 MCP 服务，分散在官方市场页；不同场景的 MCP 里常封装了**相同能力**的工具，且页面并未呈现这种「架构关系」，导致用户 confusion、并因安装过多 MCP 而大量占用大上下文。本仓库把这套结构梳理为：

1. **架构树**：哪些 MCP 是「主干(trunk，每能力域一根)」，哪些是「分支(branch，按场景按需)」。
2. **工具明细**：不止工具名，包含中英文能力描述、完整入参 schema（参数名/类型/必填/说明）。
3. **API 目录**：376 个端点的编号、路径、方法、分组、请求字段与响应字段。
4. **MCP ↔ API 映射**：每个 tool 对应哪个 API 编号 / 路径、依据是什么、置信度多高、要不要人工复核；反向也能查某个 API 被哪些 MCP 封装。带证据分级，不可推断的明确留空。
5. **起步配置**：按用户身份分 5 个包，每包最小档 / 标准档，附工具数与估算上下文成本。
6. **场景路由表**：用户提一个需求 → 必备 / 可选 MCP + 对应 API 编号 + 上下文成本 + 起步/高阶分级，共 **36 条**，覆盖全部 50 个 MCP。
7. **专属知识（API-only / MCP-only）**：哪些数据「只能 API 取、MCP 包不住」、哪些「只有 MCP 才有」——大量实测得出的硬知识，由维护者逐个补充（**当前为空**）。

## 五根主干（能力域）

| 能力域 | 主干 MCP（架构概念） | MCP 数 | tool 数 | 典型场景 |
|--------|---------------------|--------|---------|----------|
| 🔵 专利检索与分析 | `core-patents` | 23 | 详见目录 | 专利检索/阅读、法律状态/年费/诉讼/SEP、全景分析、FTO、查新、价值评估、专利撰写、文档 OCR（仅专利）、通信标准 |
| 🟢 医药情报 | `pharma-intelligence` | 11 | 详见目录 | 药物管线、临床试验、靶点/疾病、生物序列、监管/指南、交易/财报、化学分子、SAR 提取 |
| 🟡 金融 | `company-profile` | 8 | 详见目录 | 工商 360 档案、科创力评估、科技标签、风险预警、投行/科创尽调 |
| 🟣 材料 | `materials-search-mcp` | 2 | 3 | 材料搜索（金属/高分子配方/合金成分/性能实体）、化妆品法规 |
| 🟠 研发 | `patsnap-search` | 6 | 详见目录 | 专利+文献融合检索、TRIZ 创新/降本、报告生成、产学研合作、科研文献 |

> ⚠️ **这不是安装清单**。完整逐域架构树与 36 条场景路由见 [docs/architecture-tree.md](docs/architecture-tree.md)；**该先装哪几个请直接看 [docs/getting-started.md](docs/getting-started.md)**。

## 机读真相源：`index.json`

本仓库以 `index.json` 为**唯一真相源**，所有结构 / 路由 / 成本字段都在其中；Markdown 文档由 `scripts/build_docs.py` 从其生成，**请勿手改自动生成的文档**。核心字段：

- `meta` — 版本、数据源清单、统计、分层模型、`recommendation_model`（起步包口径与估算方法）、`known_gaps`（数据边界）、`change_log`。
- `domains` — 5 个能力域，每域指定一根 `trunk` 主干及 MCP 数。
- `mcps[]` — 每个 MCP 的 `tier` / `domain` / 官方分类 / 中英文描述 / 连接地址 / 版本 / 使用量。
- `mcps[].context_cost` — **自动计算**：tool 数 / 入参数 / schema 字符数 / 估算 token / 自动分档；`weight_human` 是旧的人工 high/medium/low。
- `mcps[].replaces` — 与哪些 MCP 工具重复（解决重复 tool 问题）。
- `mcps[].tools[]` — 工具名、中英文能力、`input_fields` / `input_schema`、`api_ref`、`source`、`mcp_only`。
- `mcps[].tools[].api_link` — 映射的「小卡片」：`status`（依据）/ `confidence`（verified·high·medium·low）/ `evidence`（人话解释）/ `legacy_ref`（旧标注，供审计）/ `needs_review` / `ambiguous_code`。
- `mcps[].tools[].api_ref_paths` — 该编号对应的全部接口路径（20 个编号有新旧两版路径）。
- `mcps[].tools[].mapping_status` — `mapped` / `opaque_workflow`（工作流不可静态推断）/ `candidate_only`（仅弱候选）。
- `apis[]` — 376 个端点：编号 `code`、路径、方法、分组/分类、`request_fields`、`response_fields`、`mcp_wrappers`（反向：哪些 MCP 工具封装了它）。
- `api_mapping` — 映射方法、统计、置信度图例、人工覆盖文件位置。
- `starter_kits[]` — **起步包**：按身份分 5 个，每包 `minimal` / `standard`（MCP 列表、tool 数、估算 token、占全量比例），以及 `covers_scenarios` / `upgrade_to`。
- `scenario_bundles[]` — **场景路由**：`level`（starter/advanced）、`required_mcps` / `optional_mcps`、`api_codes`（结构化编号）、`api_coverage`、`est_context_tokens`、`api_only_gap`。
- `exclusive` — API-only / MCP-only 硬知识（**当前为空，待维护者填充**）。
- `excluded_external` — 13 个第三方封装名单。

> ⚠️ `index.json` 约 2.3 MB（含全部 schema）。AI 平台应**程序化按需解析**（先读 `meta` / `starter_kits` / `scenario_bundles`，再按 id 取所需 MCP 或 API），不要把整个文件塞进对话上下文——这恰恰违背本仓库"省上下文"的初衷。

## 数据边界（诚实说明）

以下是官方数据源本身不提供的，仓库**没有编造**，已在 `meta.known_gaps` 标注：

1. **MCP tool 的返回字段**：官方详情页只给入参 schema，不给输出 schema。`tools[].data_fields` 为空；字段级信息请看 `apis[].response_fields`。**这也意味着无法用响应参数反推映射**。
2. **MCP ↔ API 官方映射**：官方确实不给，本轮用「官方描述模板 + 入参指纹」推断出 204 条，但 **207 条仍为空**（135 条工作流聚合类静态不可还原、72 条仅弱信号）。全部置信度与待复核清单见 [docs/api-mapping-review.md](docs/api-mapping-review.md)。
3. **API 编号不唯一**：20 个编号对应新旧两版接口路径，涉及条目已标 `ambiguous_code` 并附全部 path，需维护者选具体版本。
4. **API-only / MCP-only**：`exclusive` 按维护者要求保持为空，需逐个口述补充；复核文档第八节给了一份「尚未发现 MCP 封装的 API」排查线索（**不等于** API-only 结论）。
5. **场景的 API 组合不完整**：`scenario_bundles[].api_codes` 只来自已建立的映射，显示为空**不代表该场景不需要 API**；「哪些数据只能走 API、需额外申请 API Key」要等 `exclusive` 补充后才能给全。
6. **上下文 token 是粗估**：按 tool schema 字符数 / 3.2 估算，用于相对择优，不是精确 tokenizer 结果，不可用于计费核算。

## 快速开始

### 1. 先确定该装哪几个（重要）

**不要全装，也不要默认装 5 根主干。** 打开 [docs/getting-started.md](docs/getting-started.md)，按你的身份选一个起步包的最小档，遇到具体任务再按场景叠加。全量 50 个 MCP 的工具定义约 8.7 万 token，而起步最小档通常只要 1,700–3,700 token。

### 2. 获取 MCP Key

登录 [智慧芽开放平台](https://open.zhihuiya.com) → API 密钥页面 → 创建 MCP Key（格式：`sk-xxxxxxxxxxxx`）

### 3. 连接 MCP 服务

在 [MCP 服务市场](https://open.zhihuiya.com/marketplace/mcp-servers) 选择上一步确定的服务，生成连接链接，按照 [快速接入指南](https://open.zhihuiya.com/devportal/guides/mcp-quickstart) 配置你的 AI 客户端。

### 4. 验证连通性

```bash
curl https://connect.zhihuiya.com/<service-id>/mcp \
  -H 'Authorization: Bearer YOUR_MCP_KEY' \
  -H 'accept: application/json, text/event-stream' \
  -H 'Content-Type: application/json' \
  -H 'mcp-protocol-version: 2025-11-25' \
  --data-raw '{"method": "tools/list", "params": {}, "jsonrpc": "2.0", "id": 1}'
```

## 文档目录

| 文件 | 内容 |
|------|------|
| [llms.txt](llms.txt) | **给 AI 平台的轻量导航**：读取顺序、文件索引、关键约束 |
| [AGENTS.md](AGENTS.md) | **给智能体的决策流程**：用户提需求 → 四段式推荐 → 数据边界 |
| [index.json](index.json) | **机读真相源**（唯一）：架构树 + 411 tool + 376 API + 204 条映射 + 5 起步包 + 36 场景 |
| [docs/getting-started.md](docs/getting-started.md) | 自动生成：**起步配置与典型场景推荐（人读入口）** |
| [docs/architecture-tree.md](docs/architecture-tree.md) | 自动生成：5 主干架构树、逐域分支、36 条场景路由表、上下文成本 |
| [docs/mcp-catalog.md](docs/mcp-catalog.md) | 自动生成：50 个 MCP 全量明细 + 411 个 tool 的入参一览 |
| [docs/api-catalog.md](docs/api-catalog.md) | 自动生成：376 个 API 端点索引（编号/路径/方法/请求与响应字段/MCP 封装） |
| [docs/api-mapping-review.md](docs/api-mapping-review.md) | 自动生成：**映射复核清单** —— 15 条冲突、置信度分级、207 条不可推断、补充确认操作说明 |
| [data/recommendations.json](data/recommendations.json) | **人工策展表**：起步包与场景的「该装什么」判断，自动刷新不覆盖 |
| [data/manual-overrides.json](data/manual-overrides.json) | **人工确认表**：你实测确认的映射，优先级最高，自动刷新不覆盖 |
| [data/legacy-api-refs.json](data/legacy-api-refs.json) | 上一版 59 条人工标注的只读存档，用于冲突比对 |
| [scripts/refresh_all.py](scripts/refresh_all.py) | **一键刷新入口**（推荐）：按正确顺序跑完整条链路 |
| [scripts/recommend.py](scripts/recommend.py) | **场景 → 配置建议的参考实现**：`python scripts/recommend.py "FTO"` 可直接看到四段式建议 |
| [scripts/fetch_catalog.py](scripts/fetch_catalog.py) | 纯 HTTP 全量抓取（免登录，约 42 秒） |
| [scripts/infer_api_mapping.py](scripts/infer_api_mapping.py) | 分层证据推断 MCP → API 映射，产出 `data/api-mapping.json` |
| [scripts/apply_catalog.py](scripts/apply_catalog.py) | 把官方事实 + 映射写入 `index.json`，保留人工策展字段 |
| [scripts/build_recommendations.py](scripts/build_recommendations.py) | 起步包 / 场景推荐 / 上下文成本 / 场景 API 反查，写回 `index.json` |
| [scripts/build_docs.py](scripts/build_docs.py) | 从 `index.json` 重出 5 份 Markdown + `llms.txt` + `AGENTS.md` |
| [scripts/parse_nuxt.py](scripts/parse_nuxt.py) | Nuxt `__NUXT_DATA__` (devalue) 解码器 |
| [scripts/build_catalog.py](scripts/build_catalog.py) | 备用：从浏览器 dump 合并详情（本轮首次解析使用；日常刷新不需要） |

> 远程原仓库 `docs/` 下另有早期人工整理的服务目录、工具矩阵、配置指南、已知约束、API 索引与映射表，属**旧口径**（含 13 个第三方、46/356/372 统计）。以 `index.json` 与上面 5 份自动生成的文档为准；旧文档保留供溯源，后续逐步归档。

## 更新机制（100% 无人值守）

**关键事实（2026-11-08 实测）**：MCP 市场页、每个 MCP 详情页、`/openapi.json` 均免登录；SSR 页面用普通 HTTP GET 即可取得 `__NUXT_DATA__`。因此不需要浏览器、Cookie、API Token 或任何 GitHub Secret。

**日常只需一条命令**：`python scripts/refresh_all.py`。它会按下面顺序跑完（顺序有讲究：推断映射要基于最新抓到的 tool 描述，推荐层又要基于合并后的映射反查 API 编号）：

| 步骤 | 命令 | 说明 |
|------|------|------|
| 1. 抓全量 | `fetch_catalog.py` | 纯 HTTP + 8 并发，约 42 秒；50 个详情页 + OpenAPI 3.5 MB |
| 2. 先写官方事实 | `apply_catalog.py` | 让推断基于最新 tool 描述，而不是上个月的 |
| 3. 推断映射 | `infer_api_mapping.py` | 零网络；人工确认优先 + 官方描述/入参指纹，产出 `data/api-mapping.json` |
| 4. 合并写入 | `apply_catalog.py` | 官方事实 + 映射一起落到 `index.json`；**幂等**（数据没变则输出不变） |
| 5. 算推荐层 | `build_recommendations.py` | 零网络；读 `data/recommendations.json`，算上下文成本、反查场景 API、生成起步包 |
| 6. 重出文档 | `build_docs.py` | 零网络、确定性生成 5 份 Markdown + `llms.txt` + `AGENTS.md` |

- **自动节奏**：[.github/workflows/refresh.yml](.github/workflows/refresh.yml) 每月 1 日 02:00 UTC 自动跑一键编排并开 PR；数据无变化时不产生噪声 PR。也可手动触发。
- **人工节奏（建议每季度）**：复核 `exclusive`、`context_weight`、`replaces`、`needs_review` 条目，以及 [data/recommendations.json](data/recommendations.json) 里的起步包与场景判断——这些是判断，不是抓取能得到的。
- **两份人工文件不会被刷新覆盖**：`data/recommendations.json`（起步/场景）、`data/manual-overrides.json`（映射实测）。
- **本地复现**：仓库根目录执行 `python scripts/refresh_all.py` 一条命令即可；抓取产物落在 `raw/`（已 gitignore，不入库）。

## 相关项目

| 仓库 | 定位 |
|------|------|
| [patsnap-patent-skill-suite](https://github.com/Philip0910732123/patsnap-patent-skill-suite) | 专利撰写全流程 Skill 套件（9 子技能） |
| [patent-oa-analysis-skills](https://github.com/Philip0910732123/patent-oa-analysis-skills) | 专利审查意见分析技能（单局深度 + 跨局汇总） |
| [patent-sequence-exporter](https://github.com/Philip0910732123/patent-sequence-exporter) | 专利序列自动提取工具 |

---

## 💬 交流与合作

如需技术交流、问题反馈或商业合作，欢迎扫描下方微信二维码联系作者。

<p align="center">
  <img src="wechat_qr.jpg" width="200" alt="作者微信二维码" />
</p>

> 添加时请注明来自 GitHub 仓库，我会优先通过。
