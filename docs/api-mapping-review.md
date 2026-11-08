# MCP ↔ API 对应关系 · 复核清单

> 本文件由 `scripts/build_docs.py` 从 `index.json`（机读真相源）自动生成，请勿手改。结构与内容请在 `index.json` 中修改后重跑脚本。

> 数据版本 v0.6.0 · 生成时间 2026-11-08T08:46:13Z · 数据源：open.zhihuiya.com（免登录）

**这份文件回答两个问题**：映射关系是怎么来的、哪些还需要维护者实测确认。

## 一句话结论

官方开放平台**不提供** MCP 与 API 的对应关系。我们用两份公开数据做了推断：① 每个 tool 的官方中文能力描述，② 每个 tool 的入参名与每个 API 的请求字段名。结果：204 / 411 个 tool 有了对应 API，其中 157 条证据强、可直接采信；其余 207 条**明确留空**，不猜测。

## 一、数字

| 项目 | 数量 | 含义 |
|------|------|------|
| 已建立映射 | 204 | 有明确对应的 API 编号 |
| ↳ 高置信（官方描述） | 157 | tool 描述直接写出源 API 中文名 |
| ↳ 中置信（入参唯一） | 19 | 入参名集合在两侧双向唯一 |
| ↳ 低置信（沿用旧标注） | 28 | 无本轮证据，仅保留旧值待核 |
| 未建立映射 | 207 | 静态数据不足以判定 |
| ↳ 工作流/AI 聚合类 | 135 | 入参被重写、内部串多个 API |
| ↳ 仅有弱信号 | 72 | 有候选但不足以定论 |
| 与旧人工标注冲突 | 15 | 已按官方证据修正，旧值保留在 `api_link.legacy_ref` |
| 覆盖到的不同 API | 123 | 反向索引见 `apis[].mcp_wrappers` |

## 二、为什么不能只靠「入参/响应参数」推断

1. **响应参数这条路根本不存在**：官方 MCP 详情页只给 tool 的*输入*参数，完全不提供返回字段。字段级响应信息只在 `apis[].response_fields` 里，两侧没有可比对的输出。
2. **入参相同 ≠ 同一个 API**：61 个 tool 的入参都是 `patent_id + patent_number`，却分别对应著录项目、权利要求、法律状态、法律详情、同族、PDF 全文等不同 API。纯参数匹配会把它们全部混在一起（第一版实验曾把 215 条判为高置信，其中 153 条的入参签名被 5 个以上 tool 共用、存在明显歧义，该判定已废弃）。
3. **工作流类工具重写了入参**：查新、FTO、TRIZ 这类 tool 的入参是 `task_id / data / execution / user_input`，且一个 tool 内部串行调用多个 API，静态 schema 无法还原调用链 —— 这正好属于维护者实测才知道的硬知识。

**最终采用的分层依据**（优先级从高到低）：

| 优先级 | 依据 | 置信度 |
|--------|------|--------|
| 1 | 你在 `data/manual-overrides.json` 里实测确认 | 已实测 |
| 2 | 官方 tool 描述模板「用于获取X相关…」中 X 唯一命中某 API 中文名 | 高 |
| 3 | 入参名集合在 tool 与 API 两侧双向唯一且完全一致 | 中 |
| 4 | 上一版人工标注（编号有效但本轮无证据） | 低 |
| 5 | 仅参数相似 / 工作流类 | **留空，不写入** |

## 三、⚠️ 与旧人工标注冲突（15 条，请重点看）

旧标注多为凭语义手工填写，且当时没有官方结构化数据可对照。下表已按官方证据修正，**旧值没有删除**，仍存在 `api_link.legacy_ref` 里供你复核。若你认为旧值才对，按文末方式覆盖即可。

| MCP / 工具 | 旧标注 | 新推断 | 新 API 名称 | 依据 |
|------------|--------|--------|-------------|------|
| `company-profile/patent_legal_status` | P013/P041 | **P013** | 法律状态 | 官方 tool 描述「用于获取法律状态相关…」唯一对应 API 中文名「法律状态」 |
| `company-profile/patent_simple_bibliography` | P012 | **P011** | 简单著录项 | 官方 tool 描述「用于获取简单著录项相关…」唯一对应 API 中文名「简单著录项」 |
| `core-patents/get_patent_legal_status` | P013/P041 | **P041** | 简单法律状态 | 官方 tool 描述「用于获取简单法律状态相关…」唯一对应 API 中文名「简单法律状态」 |
| `core-patents/legal_data` | P013 | **P026** | 法律详情 | 官方 tool 描述「用于获取法律详情相关…」唯一对应 API 中文名「法律详情」 |
| `patent-briefing/legal_status` | P013/P041 | **P041** | 简单法律状态 | 官方 tool 描述「用于获取简单法律状态相关…」唯一对应 API 中文名「简单法律状态」 |
| `patent-dispute/legal_data` | P013 | **P026** | 法律详情 | 官方 tool 描述「用于获取法律详情相关…」唯一对应 API 中文名「法律详情」 |
| `patent-dispute/legal_status` | P013/P041 | **P041** | 简单法律状态 | 官方 tool 描述「用于获取简单法律状态相关…」唯一对应 API 中文名「简单法律状态」 |
| `patent-landscape/search_patents_statistics` | P001 | **D010** | 专利统计 | 入参名集合在 tool 与 API 两侧双向唯一且完全一致 |
| `patent-landscape/search_patents_v3` | P002 | **D005** | 专利检索 | 入参名集合在 tool 与 API 两侧双向唯一且完全一致 |
| `patent-landscape/search_patents_with_detail` | P003 | **D009** | 专利检索及详情 | 入参名集合在 tool 与 API 两侧双向唯一且完全一致 |
| `patent-mining/classification_description` | P071 | **P066** | 专利分类号说明 | 官方 tool 描述「用于获取专利分类号说明相关…」唯一对应 API 中文名「专利分类号说明」 |
| `patent-mining/tech_problem_benefit_summary` | AI31 | **P025** | 专利技术三要素 | 官方 tool 描述「用于获取专利技术三要素相关…」唯一对应 API 中文名「专利技术三要素」 |
| `patent-status/get_sep_data` | T001 | **P033** | 标准必要专利(SEP) | 官方 tool 描述「用于获取标准必要专利(SEP)相关…」唯一对应 API 中文名「标准必要专利(SEP)」 |
| `patent-status/legal_data` | P013 | **P026** | 法律详情 | 官方 tool 描述「用于获取法律详情相关…」唯一对应 API 中文名「法律详情」 |
| `patent-visual/most_cited` | P015 | **A005** | 被引用最多的专利 | 官方 tool 描述「用于获取被引用最多的专利相关…」唯一对应 API 中文名「被引用最多的专利」 |

## 四、中置信：靠入参签名推断（建议抽查）（19 条）

这些 tool 的入参名集合在所有 tool 与所有 API 中都只出现一次，判别力较强，但仍建议抽查。

| MCP / 工具 | 对应 API | 名称 |
|------------|----------|------|
| `company-credit/search_company` | C037 | 企业搜索接口 |
| `design-fto-search-mcp/get_stage_result` | AI39-3 | 外观防侵权检索-获取阶段执行结果 |
| `intangible-assets/potential_buyer` | C046 | 潜在买家推荐接口 |
| `ip-courses/course_list` | AC01 | 获取课程列表 |
| `literature-search/search_literature` | L001 | 文献检索 |
| `patent-landscape/info` | D114 | 专利字段详情（仅包含大文本） |
| `patent-landscape/list` | D113 | 专利列表 |
| `patent-landscape/search_patents_facet` | D006 | 专利检索统计 |
| `patent-landscape/search_patents_statistics` | D010 | 专利统计 |
| `patent-landscape/search_patents_v3` | D005 | 专利检索 |
| `patent-landscape/search_patents_with_detail` | D009 | 专利检索及详情 |
| `patent-value/ability_indicators` | P051 | 专利申请前评估-可专利性 |
| `patent-value/market_prospect_indicators` | P052 | 专利申请前评估-市场前景 |
| `patent-value/operation_situation_indicators` | P053 | 专利申请前评估-运营情况 |
| `patent-value/tech_innovation_indicators` | P050 | 专利申请前评估-技术创新性 |
| `patent-visual/company_tech_effect_dist` | A201 | 技术效果分布 |
| `patent-visual/company_tech_field_word_cloud` | A202 | 技术领域词云 |
| `patent-visual/technology_effect_distribution` | A012 | 技术功效短语分布 |
| `report-gen/idea_validation_download` | AI29-3 | 下载技术想法查新报告 |

## 五、低置信：沿用旧标注、本轮无证据支持（建议实测）（28 条）

这些编号在官方清单里有效，但本轮没有找到描述或参数证据，属于「暂且保留」，最值得优先实测。

| MCP / 工具 | 对应 API | 名称 |
|------------|----------|------|
| `core-patents/family` | P014 | 专利家族 |
| `core-patents/search_patents` | P002 | 检索式检索专利 |
| `design-fto-search-mcp/create_image_upload_url` | P010 | 上传图片获取专利图像检索URL |
| `design-fto-search-mcp/submit_workflow` | AI39-1 | 外观防侵权检索-提交工作流任务 |
| `document-processing/translation_docx` | AI61 | AI翻译 |
| `document-processing/translation_text` | AI61 | AI翻译 |
| `novelty-search-lite/novelty_feature_extract` | AI35-4 | 查新检索-提取技术特征 |
| `novelty-search-lite/novelty_keywords_extract` | AI35-6 | 查新检索-提取检索要素 |
| `novelty-search-lite/novelty_lite_boolean_search` | P002 | 检索式检索专利 |
| `novelty-search-lite/novelty_lite_semantic_search` | P008 | 语义检索相似专利 |
| `patent-analysis/aggregate_patents` | P001 | 检索式统计专利量 |
| `patent-briefing/family` | P014 | 专利家族 |
| `patent-briefing/intelligent_image` | P042 | 全文附图 |
| `patent-briefing/search_patents` | P002 | 检索式检索专利 |
| `patent-dispute/family` | P014 | 专利家族 |
| `patent-dispute/search_patents` | P002 | 检索式检索专利 |
| `patent-landscape/detail` | P012 | 著录项目 |
| `patent-landscape/pdf` | P020 | PDF全文 |
| `patent-mining/intelligent_attached_image` | P042 | 全文附图 |
| `patsnap-ip-searching/design_fto` | AI39-1 | 外观防侵权检索-提交工作流任务 |
| `patsnap-ip-searching/fto_review` | AI66-4 | 防侵权检索-启动FTO检索 |
| `patsnap-ip-searching/novelty_search` | AI35-2 | 查新检索-总结技术要点 |
| `patsnap-ip-searching/upload_image` | P010 | 上传图片获取专利图像检索URL |
| `patsnap-solution-engine/run_triz_innovation_task` | AI33-1 | 技术方案探索-创建任务 |
| `pharma-intelligence/ls_ner_nor_normalize` | AI01 | 药物DDT抽取 |
| `pharma-intelligence/ls_patent_fetch` | P012 | 著录项目 |
| `pharma-intelligence/ls_patent_search` | P002 | 检索式检索专利 |
| `report-gen/idea_validation_similar` | AI30 | 相似专利检索与比对 |

## 六、编号歧义（7 条）

同一个 API 编号对应新旧两版接口路径，编号本身不唯一。`api_ref_paths` 已列出全部路径，需要你确认 tool 实际走的是哪一个。

| MCP / 工具 | 编号 | 可选路径 |
|------------|------|----------|
| `core-patents/fulltext_image` | P042 | `/basic-patent-data/fulltext-image`、`/basic-patent-data/fulltext-inline-image` |
| `intangible-assets/new_plant_variety` | C034 | `/special-ip-data/new-plant-variety/application`、`/special-ip-data/new-plant-variety/issue` |
| `patent-briefing/intelligent_image` | P042 | `/basic-patent-data/fulltext-image`、`/basic-patent-data/fulltext-inline-image` |
| `patent-dispute/fulltext_image` | P042 | `/basic-patent-data/fulltext-image`、`/basic-patent-data/fulltext-inline-image` |
| `patent-mining/intelligent_attached_image` | P042 | `/basic-patent-data/fulltext-image`、`/basic-patent-data/fulltext-inline-image` |
| `patent-status/fee_info` | P047 | `/fee/apno_input`、`/fee/get_fee` |
| `patsnap-ip-searching/fto_review` | AI66-4 | `/ai/fto/search/agent`、`/fto_steps/keyword_expansion` |

## 七、静态无法推断（207 条）

- 工作流 / AI 聚合类 **135** 条：入参被 MCP 重写或异步任务化，需实测才知道内部调了哪些 API。
- 仅有弱信号 **72** 条：`api_candidates` 里给了前 3 个候选编号，供你快速判定。

工作流类按 MCP 分布（前 15）：

| MCP | 不可推断的 tool 数 |
|-----|--------------------|
| `pharma-intelligence` | 21 |
| `drafting` | 18 |
| `fto-search` | 12 |
| `patsnap-workspace` | 11 |
| `biology-modality` | 8 |
| `novelty-search-lite` | 7 |
| `company-intelligence-mcp` | 6 |
| `landscape-projects` | 6 |
| `patsnap-solution-engine` | 5 |
| `s-telecom-mcp-tools` | 4 |
| `chemical-molecular` | 4 |
| `target-disease` | 3 |
| `company-deal-intelligence` | 3 |
| `patsnap-search` | 3 |
| `materials-search-mcp` | 2 |

## 八、尚未发现 MCP 封装的 API（216 个编号）—— exclusive 排查线索

> ⚠️ **这不是「只能 API 获取」的结论**。它只表示本轮推断没有找到对应 tool：可能是真的没有 MCP 封装（API-only），也可能是工作流类 tool 内部调用了它但静态看不出来。请把它当作**优先实测清单**，确认后再写进 `index.json` 的 `exclusive.api_only`。

前 40 个编号：`A002`、`A004`、`A006`、`A007`、`A008`、`A010`、`A011`、`A101`、`A102`、`A103`、`A104`、`A108`、`A109`、`AI03`、`AI07`、`AI103-1`、`AI103-2`、`AI20`、`AI29-2`、`AI31`、`AI32-1`、`AI32-2`、`AI32-3`、`AI33-2`、`AI33-3`、`AI33-4`、`AI33-5`、`AI33-6`、`AI34-1`、`AI34-2`、`AI34-3`、`AI35-1`、`AI35-10`、`AI35-11`、`AI35-12`、`AI35-3`、`AI35-5`、`AI35-7`、`AI35-8`、`AI35-9`

## 九、怎么补充确认（不用改代码）

只需编辑一个文件：`data/manual-overrides.json`。它的优先级最高，**每月自动刷新不会覆盖你填的内容**。

步骤：

1. 打开 `data/manual-overrides.json`，找到 `"mappings": {}`。
2. 按格式加一条，键是「MCP 的 id/工具名」，值是确认的 API 编号和一句备注。例如：

```json
{
  "mappings": {
    "core-patents/legal_data": {
      "api_code": "P026",
      "note": "实测返回法律详情字段，对应 /advanced-patent-data/legal-data"
    }
  }
}
```

3. 依次运行 `python scripts/infer_api_mapping.py` → `python scripts/apply_catalog.py` → `python scripts/build_docs.py`，新结论会写进 `index.json` 并重出本文档。
4. 若确认某工具**没有**对应 API，把 `api_code` 填 `null` 并在备注里说明。

> `exclusive`（API-only / MCP-only）仍按你的要求保持为空，可以边用边补，不阻塞发布。

---

*index.json v0.6.0 · 完整候选打分见 raw/mapping-inference.json（本地中间产物，不入库）*
