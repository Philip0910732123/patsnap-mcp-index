# AGENTS.md — 给 AI 智能体的操作说明

> 本仓库是智慧芽（PatSnap）MCP / API 的**架构索引**，不是可调用的服务本身。当用户问「我要查 XX，该配哪些 MCP / API」时，按下面的流程用本仓库数据回答，不要凭印象推荐。

> 数据版本 v0.6.0 · 口径：50 个原生 MCP / 411 个 tool / 376 个 API / 5 个起步包 / 36 条场景路由。

## 0. 读取原则（先做这一步）

- **`index.json` 约 2.3 MB，禁止整文件塞进上下文。** 用脚本按 key 取子集。
- 先读 `meta`（counts / recommendation_model / known_gaps），再按需要读下面任一块。
- 人读版 `docs/getting-started.md` 只作解释参考，**判断以 `index.json` 为准**。
- 想验证数据是否够用，可跑 `python scripts/recommend.py "FTO"`；那是下面流程的参考实现，可直接复用其匹配与输出逻辑（`--json` 输出结构化结果）。

## 1. 用户提出一个检索 / 情报需求时的决策流程

1. **判断身份与领域**：从用户描述推断属于 `starter_kits[].who` 里的哪一类；无法判断时直接问，或按场景匹配。
2. **匹配场景**：在 `scenario_bundles[]` 里按 `scenario` 语义匹配，可读 `note` 辅助；同时看 `level`（`starter` = 起步典型 / `advanced` = 高阶按需）。
3. **给出四段式建议**：
   - ① **起步配置**：取对应 `starter_kits[].minimal.mcps`，附 `est_context_tokens` 与占全量比例；说明「先只装这些」。
   - ② **本次场景**：`required_mcps`（必备）+ `optional_mcps`（按需）+ `api_codes`（这些 MCP 对应的官方 API 编号），附 `required_est_context_tokens`。
   - ③ **是否需要额外 API Key**：读 `api_only_gap`。**当前 `exclusive` 为空，必须如实说明「哪些数据只能走 API 尚缺实测结论，无法给出完整 API 配置清单」，不要编造。**
   - ④ **后续高阶**：该包的 `upgrade_to`，以及同域 `level=advanced` 的场景。
4. **上下文优化优先级**：最小档 > 标准档 > 叠加分支；**不要建议「装全部主干」或「装全量 MCP」**；若用户已有多个 MCP，指出 `replaces` 里的重复可裁掉。

## 2. 回答「智慧芽有多少 MCP / API、能取什么数据」

- 数量：读 `meta.counts`（50 MCP / 411 tool / 376 API）。
- 架构：`domains`（5 个能力域）+ `mcps[].tier`（trunk=架构主干 / branch=场景分支）。**注意 trunk 是架构概念，不是默认安装清单。**
- 单个 MCP 能取什么：`mcps[id].tools[]` 的 `capability` / `input_fields` / `input_schema`。
- 单个 API 能取什么：`apis[code]` 的 `request_fields` / `response_fields`（374 个端点有响应字段）。
- MCP↔API 对应：`tools[].api_ref` + `api_link.confidence`（已实测/高/中/低），反向用 `apis[].mcp_wrappers`；方法与边界见 `docs/api-mapping-review.md`。

## 3. 字段速查

| 字段 | 含义 |
|------|------|
| `starter_kits[].minimal / standard` | 按身份的起步配置，`est_context_tokens` 是约占用上下文 |
| `scenario_bundles[].level` | `starter` 起步典型 / `advanced` 高阶按需 |
| `scenario_bundles[].api_codes` | 必备 MCP 对应的官方 API 编号（自动反查，非「需额外申请」）；为空 = 映射未确认，**不等于不需要 API** |
| `scenario_bundles[].api_only_gap` | API 组合建议的完整度说明（当前不完整） |
| `mcps[].context_cost` | tool 数 / 入参数 / 估算 token / 自动分档；`weight_human` 是旧的人工分档 |
| `mcps[].replaces` | 与其他 MCP 重复的工具，可用于裁剪已装服务 |
| `tools[].api_link` | 映射依据、置信度、是否需复核、旧标注审计值 |
| `tools[].mapping_status` | `opaque_workflow` = 工作流类，静态不可推断 |
| `exclusive.api_only / mcp_only` | 只能走 API / 只能走 MCP 的实测硬知识（**当前为空**） |

## 4. 数据边界（严格遵守，不要编造）

- 官方 MCP 详情页只提供 tool 的入参 schema，不提供返回字段；tools[].data_fields 暂为空，字段级信息见 apis[].response_fields。因此无法用「响应参数」反推 MCP↔API 对应关系。
- AI 工作流类 tool 重写入参（task_id/data/execution）并串行调用多个 API，静态 schema 无法还原调用链；这类工具的映射需维护者实测补充，见 tools[].mapping_status = opaque_workflow 与 docs/api-mapping-review.md。
- 20 个 API 编号对应新旧两版 path，编号本身不唯一；涉及条目以 tools[].api_link.ambiguous_code 标记并附全部 path。
- exclusive（API-only / MCP-only 实测结论）按维护者要求保持为空，逐个补充。
- 场景的 API 组合建议不完整：scenario_bundles[].api_codes 只来自已建立的 MCP→API 映射；exclusive 为空，因此「哪些数据只能 API 获取、需额外申请 API Key」尚缺实测结论。
- 映射只覆盖 204 / 411 个 tool；其余保持 `api_ref` 为空，**不要为其硬凑 API 编号**。
- `context_cost.est_tokens` 是粗估，用于相对比较，不能当计费或精确上下文数字引用。
- 本仓库只收录智慧芽原生能力；用户问及 pubmed/chembl/otp 等第三方封装时，说明它们不在本索引范围（见 `excluded_external`）。

## 5. 维护（当用户是维护者时）

- 改起步包 / 场景判断 → 编辑 `data/recommendations.json`。
- 补 MCP→API 实测结论 → 编辑 `data/manual-overrides.json`（优先级最高）。
- 补 API-only / MCP-only → 编辑 `index.json` 的 `exclusive`。
- 改完跑 `python scripts/refresh_all.py`（纯 HTTP、免登录、幂等）；每月 1 日 GitHub Actions 也会自动跑并开 PR。

---

*index.json v0.6.0 · 本文件由 scripts/build_docs.py 自动生成，请勿手改*
