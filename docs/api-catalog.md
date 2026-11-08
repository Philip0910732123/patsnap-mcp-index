# API 目录（全量端点与字段概览）

> 本文件由 `scripts/build_docs.py` 从 `index.json`（机读真相源）自动生成，请勿手改。结构与内容请在 `index.json` 中修改后重跑脚本。

> 数据版本 v0.6.0 · 生成时间 2026-11-08T08:46:13Z · 数据源：open.zhihuiya.com（免登录）

共 **376** 个端点（OpenAPI 3.1.0）。完整请求/响应字段（含类型、必填、描述）以 `index.json` 的 `apis[]` 为准。

## 统计

- 分组：{'AI': 107, 'DATA': 269}
- 含响应字段的端点：374 / 376
- 含请求字段的端点：343 / 376

## DATA API（269 个）

### 专利数据检索（20 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| P001 | 检索式统计专利量 | POST | `/search/patent/query-search-count/v2` | collapse_order, query_text, collapse_type, collapse_by, collapse_order_authority …(+1) | data, status, error_msg, error_code | `patent-analysis/aggregate_patents` |
| P002 | 检索式检索专利 | POST | `/search/patent/query-search-patent/v2` | query_text, collapse_type, collapse_by, collapse_order, collapse_order_authority …(+4) | data, status, error_msg, error_code | `core-patents/search_patents`, `novelty-search-lite/novelty_lite_boolean_search` …(+3) |
| P003 | 检索式检索专利并筛选 | POST | `/search/patent/query/v2` | query, field, lang, collapse_type, collapse_by …(+5) | data, status, error_msg, error_code | — |
| P004 | 公司申请人检索专利 | POST | `/search/patent/company-search-patent/v2` | offset, sort, collapse_order, collapse_by, collapse_order_authority …(+3) | data, status, error_msg, error_code | — |
| P005 | 公司专利权人检索专利 | POST | `/search/patent/current-search-patent/v2` | offset, sort, collapse_order, collapse_by, collapse_order_authority …(+3) | data, status, error_msg, error_code | — |
| P006 | 国防专利检索 | POST | `/search/patent/company-search-defense-patent/v2` | offset, sort, collapse_order, collapse_by, collapse_order_authority …(+3) | data, status, error_msg, error_code | — |
| P007 | 专利号检索相似专利 | POST | `/search/patent/similar-search-patent/v2` | patent_id, country, pbd_from, offset, apd_from …(+5) | data, status, error_msg, error_code | — |
| P008 | 语义检索相似专利 | POST | `/search/patent/semantic-search-patent/v2` | field, order, simple_legal_status, text, country …(+7) | data, status, error_msg, error_code | `novelty-search-lite/novelty_lite_semantic_search` |
| P010 | 上传图片获取专利图像检索URL | POST | `/image-search/image-upload` | — | data, status, error_msg, error_code | `design-fto-search-mcp/create_image_upload_url`, `patsnap-ip-searching/upload_image` |
| P060 | 专利图像检索-单图 | POST | `/search/patent/image-single` | apply_end_time, apply_start_time, assignees, country, field …(+20) | data, status, error_msg, error_code | — |
| P060 | 专利图像检索-单图形搜升级版 | POST | `/search/patent/image-single/beta` | apply_end_time, apply_start_time, assignees, country, field …(+20) | data, status, error_msg, error_code | — |
| P061 | 专利图像检索-多图 | POST | `/search/patent/image-multiple` | apply_end_time, apply_start_time, assignees, country, field …(+20) | data, status, error_msg, error_code | — |
| P062 | 生成图像批量检索任务 | POST | `/search/patent/image-search/single-batch-create` | apply_end_time, apply_start_time, assignees, country, field …(+20) | data, status, error_msg, error_code | — |
| P062 | 获取图像批量检索结果 | POST | `/search/patent/image-search/single-batch-result` | task_id | data, status, error_msg, error_code | — |
| P069 | 智慧芽标准专利号查询 | POST | `/search/patent/patent-search-pn` | pn, apno, authority, offset, limit | data, status, error_msg, error_code | — |
| P070 | 关键词助手 | POST | `/search/patent/keyword-suggest` | keyword, lang, type | data, status, error_msg, error_code | — |
| P071 | 分类号助手查询 | GET | `/search/patent/classification/helper-section-subclass` | code, type | data, status, error_msg, error_code | — |
| P072 | 分类号检索助手 | GET | `/search/patent/classification/helper-search` | keyword, type | data, status, error_msg, error_code | — |
| P075 | 检索式检索专利嵌套版 | POST | `/search/patent/nested-search-patent` | facet, limit, offset, query_text, sort …(+1) | data, status, error_msg, error_code | — |
| P081 | 专利/论文智能检索 | POST | `/search-agent/rag/v4/search` | search_strategy, semantic_query, keywords, filters, source …(+2) | data, status, error_message | — |

### 专利基础数据（15 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| P011 | 简单著录项 | GET | `/basic-patent-data/simple-bibliography` | patent_id, patent_number | data, status, error_msg, error_code | `company-profile/patent_simple_bibliography` |
| P012 | 著录项目 | GET | `/basic-patent-data/bibliography` | patent_id, patent_number | data, status, error_msg, error_code | `core-patents/bibliography`, `patent-briefing/bibliography` …(+3) |
| P013 | 法律状态 | GET | `/basic-patent-data/legal-status` | patent_id, patent_number | data, status, error_msg, error_code | `company-profile/patent_legal_status` |
| P014 | 专利家族 | GET | `/basic-patent-data/patent-family` | patent_id, patent_number | data, status, error_msg, error_code | `core-patents/family`, `patent-briefing/family` …(+1) |
| P018 | 权利要求 | GET | `/basic-patent-data/claim-data` | patent_id, patent_number, replace_by_related | data, status, error_msg, error_code | `core-patents/claims`, `patent-briefing/claims` …(+1) |
| P019 | 说明书 | GET | `/basic-patent-data/description-data` | patent_id, patent_number, replace_by_related | data, status, error_msg, error_code | `core-patents/description`, `patent-briefing/description` …(+1) |
| P020 | PDF全文 | GET | `/basic-patent-data/pdf-data` | patent_id, patent_number, replace_by_related | data, status, error_msg, error_code | `core-patents/pdf`, `patent-dispute/pdf` …(+1) |
| P021 | 摘要附图 | GET | `/basic-patent-data/abstract-image` | patent_id, patent_number | data, status, error_msg, error_code | `core-patents/abstract_image`, `patent-briefing/abstract_image` …(+1) |
| P041 | 简单法律状态 | GET | `/basic-patent-data/simple-legal-status` | patent_id, patent_number | data, status, error_msg, error_code | `core-patents/get_patent_legal_status`, `patent-briefing/legal_status` …(+1) |
| P042 | 全文附图 | POST | `/basic-patent-data/fulltext-image` | limit, offset, patent_id, patent_number | data, status, error_msg, error_code | `core-patents/fulltext_image`, `patent-briefing/intelligent_image` …(+2) |
| P042 | 全文内嵌附图 | GET | `/basic-patent-data/fulltext-inline-image` | patent_id, patent_number | data, status, error_msg, error_code | `core-patents/fulltext_image`, `patent-briefing/intelligent_image` …(+2) |
| P043 | 摘要翻译 | GET | `/basic-patent-data/abstract-data-translated` | lang, patent_id, patent_number, replace_by_related | data, status, error_msg, error_code | `core-patents/abstract_translated`, `patent-briefing/abstract_translated` …(+1) |
| P044 | 权利要求翻译 | GET | `/basic-patent-data/claim-data-translated` | lang, patent_id, patent_number, replace_by_related | data, status, error_msg, error_code | `core-patents/claim_translated`, `patent-briefing/claim_translated` …(+1) |
| P045 | 说明书翻译 | GET | `/basic-patent-data/description-data-translated` | lang, patent_id, patent_number, replace_by_related | data, status, error_msg, error_code | `core-patents/description_translated`, `patent-briefing/description_translated` …(+1) |
| P073 | 全文导航位置信息 | GET | `/basic-patent-data/description-offset` | lang, patent_id, patent_number | data, status, error_msg, error_code | — |

### Patent Basic Data（2 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| — | P015 Cited By Patents（Beta） | GET | `/basic-patent-data/forward-citation/v3` | patent_id, patent_number | data, status, error_msg, error_code | — |
| — | P016 Patent Citation NPL | GET | `/advanced-patent-data/forward-citation/npl` | patent_id, patent_number | data, status, error_msg, error_code | — |

### 专利挖掘数据（12 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| P022 | 战略新兴产业分类 | GET | `/high-value-data/seic-classification` | lang, patent_id, patent_number | data, status, error_msg, error_code | `patent-mining/seic_classification` |
| P023 | 应用领域分类V2 | GET | `/high-value-data/application-domain-v2` | lang, patent_id, patent_number | data, status, error_msg, error_code | — |
| P024 | 技术主题分类 | GET | `/high-value-data/technology-topic` | lang, patent_id, patent_number | data, status, error_msg, error_code | `patent-mining/technology_topic` |
| P025 | 专利技术三要素 | GET | `/high-value-data/tech-problem-and-benefit-summary` | lang, patent_id, patent_number | data, status, error_msg, error_code | `patent-briefing/tech_summary`, `patent-mining/tech_problem_benefit_summary` |
| P063 | 专利智能附图 | POST | `/search/patent/intelligent-attached-image` | lang, patent_id, pn | data, status, error_msg, error_code | — |
| P064 | 专利增值数据 | GET | `/basic-patent-data/patent_enhanced_data` | fields, patent_id, patent_number | data, status, error_msg, error_code | `patent-mining/enhanced_data` |
| P066 | 专利分类号说明 | POST | `/high-value-data/patent-classification-description` | code, replace_by_merge, type | data, status, error_msg, error_code | `patent-mining/classification_description` |
| P100 | 专利PUM | POST | `/material/patent-pum` | patent_id, patent_number | data, status, error_msg, error_code | — |
| P101 | 材料工作流 | POST | `/material/material-ontology` | patent_id, patent_number | data, status, error_msg, error_code | — |
| P102 | 材料物质 | POST | `/material/material-substance` | patent_id, patent_number | data, status, error_msg, error_code | — |
| P103 | 专利SPUM | POST | `/material/material-spum` | patent_id, patent_number | data, status, error_msg, error_code | — |
| P067 | 专利/论文Markdown获取工具 | POST | `/data-pd/convert/markdown/fetch` | keys, key_type, compress, include_images, module …(+1) | total, results, time_cost, failed_count, success_count | — |

### 专利法律详情（13 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| P026 | 法律详情 | GET | `/advanced-patent-data/legal-data` | patent_id, patent_number | data, status, error_msg, error_code | `core-patents/legal_data`, `patent-dispute/legal_data` …(+1) |
| P027 | 复审无效 | GET | `/advanced-patent-data/re-examination-and-invalidation` | patent_id, patent_number | data, status, error_msg, error_code | `company-profile/patent_reexamination`, `core-patents/reexamination_invalidation` …(+2) |
| P028 | 专利许可 | GET | `/advanced-patent-data/license-data` | patent_id, patent_number | data, status, error_msg, error_code | `company-profile/patent_license_data`, `core-patents/license_data` …(+2) |
| P029 | 专利转移 | GET | `/advanced-patent-data/transfer-data` | patent_id, patent_number | data, status, error_msg, error_code | `company-profile/patent_transfer_data`, `core-patents/transfer_data` …(+2) |
| P030 | 专利质押 | GET | `/advanced-patent-data/pledge-data` | patent_id, patent_number | data, status, error_msg, error_code | `company-profile/patent_pledge_data`, `patent-dispute/pledge_data` …(+1) |
| P031 | 海关备案 | GET | `/advanced-patent-data/customs-data` | patent_id, patent_number | data, status, error_msg, error_code | `core-patents/customs_data`, `patent-dispute/customs_data` …(+1) |
| P032 | 专利奖 | GET | `/advanced-patent-data/award-data` | patent_id, patent_number | data, status, error_msg, error_code | `core-patents/award_data`, `patent-dispute/award_data` …(+1) |
| P033 | 标准必要专利(SEP) | GET | `/advanced-patent-data/sep-data` | patent_id, patent_number | data, status, error_msg, error_code | `patent-status/get_sep_data` |
| P034 | 诉讼数据 | GET | `/high-value-data/litigation` | patent_id, patent_number | data, status, error_msg, error_code | `patent-status/litigation_data` |
| P046 | 欧洲统一法院状态 | GET | `/advanced-patent-data/status-of-unified-patent-court` | patent_id, patent_number | data, status, error_msg, error_code | `patent-status/unified_patent_court_status` |
| P047 | 专利缴费信息请求 | POST | `/fee/apno_input` | apnos | data, status, error_msg, error_code | `patent-status/fee_info` |
| P047 | 专利缴费结果获取 | POST | `/fee/get_fee` | ticket | data, status, error_msg, error_code | `patent-status/fee_info` |
| P048 | 海外专利审查文件 | POST | `/advanced-patent-data/overseas-patent-documents` | apno, date_from, date_to, doc_code, limit …(+3) | data, status, error_msg, error_code | `patent-status/overseas_patent_documents` |

### 专利价值评估（10 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| P035 | 专利价值 | GET | `/patent-valuation-data/patent_valuation` | patent_id, patent_number | data, status, error_msg, error_code | `company-profile/patent_valuation`, `patent-dispute/patent_valuation` …(+2) |
| P036 | 技术指标 | GET | `/patent-valuation-data/technology_indicators` | patent_id, patent_number | data, status, error_msg, error_code | `patent-value/technology_indicators`, `tech-diligence/tech_indicators` |
| P037 | 法律指标 | GET | `/patent-valuation-data/legal_indicators` | patent_id, patent_number | data, status, error_msg, error_code | `patent-value/legal_indicators`, `tech-diligence/legal_indicators` |
| P038 | 市场指标 | GET | `/patent-valuation-data/market_indicators` | patent_id, patent_number | data, status, error_msg, error_code | `patent-value/market_indicators`, `tech-diligence/market_indicators` |
| P039 | 战略指标 | GET | `/patent-valuation-data/strategic_indicators` | patent_id, patent_number | data, status, error_msg, error_code | `patent-value/strategic_indicators`, `tech-diligence/strategic_indicators` |
| P040 | 经济指标 | GET | `/patent-valuation-data/economic_indicators` | patent_id, patent_number | data, status, error_msg, error_code | `patent-value/economic_indicators`, `tech-diligence/economic_indicators` |
| P050 | 专利申请前评估-技术创新性 | POST | `/patent-valuation-data/tech_innovation` | patent_info, relevancy_threshold, cited_by_threshold | data, status, error_msg, error_code | `patent-value/tech_innovation_indicators` |
| P051 | 专利申请前评估-可专利性 | POST | `/patent-valuation-data/patent_ability` | patent_info, claim_cnt_threshold | data, status, error_msg, error_code | `patent-value/ability_indicators` |
| P052 | 专利申请前评估-市场前景 | POST | `/patent-valuation-data/market_prospect` | ipc_cnt_threshold, year_threshold, patent_info | data, status, error_msg, error_code | `patent-value/market_prospect_indicators` |
| P053 | 专利申请前评估-运营情况 | POST | `/patent-valuation-data/operation_situation` | family_threshold, patent_info | data, status, error_msg, error_code | `patent-value/operation_situation_indicators` |

### 专利监控导出（5 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| P055 | 检索式创建专利导出任务 | POST | `/patent-search/export/V2` | collapse_by, collapse_order, collapse_order_authority, collapse_type, query_text …(+11) | data, status, error_msg, error_code | — |
| P055 | 获取专利导出详情 | GET | `/patent-search/task` | task_id | data, status, error_msg, error_code | — |
| P056 | 创建专利监控预警项目v2 | POST | `/patent-alert/creation` | alert_name, content, query | data, status, error_msg, error_code | — |
| P057 | 查询监控项更新状态 | GET | `/patent-alert/check` | alert_id | data, status, error_msg, error_code | — |
| P059 | 删除专利监控项目 | DELETE | `/patent-alert/delete` | alert_id | data, status, error_msg, error_code | — |

### Patent Monitor and Export（1 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| — | P058 Edit Patent Monitor Project v2 | POST | `/patent-alert/update/v2` | alert_id, alert_name, content, query | data, status, error_msg, error_code | — |

### Technology Key Report（1 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| — | A001 Application and Issued Trend (Query Search) | POST | `/insights-openapi/patent-trends-query` | collapse_order, query_text, collapse_type, collapse_by, collapse_order_authority | data, status, error_msg, error_code | — |

### 专利技术全景分析（23 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| A002 | 创新词云（检索式搜索） | POST | `/insights/word-cloud-query` | collapse_order, collapse_by, lang, collapse_type, query_text | data, status, error_msg, error_code | — |
| A003 | 旭日图 | GET | `/insights/wheel-of-innovation` | apply_end_time, apply_start_time, authority, ipc, keywords …(+4) | data, status, error_msg, error_code | `patent-visual/wheel_of_innovation` |
| A004 | 技术来源国/地区排名 | GET | `/insights/priority-country` | apply_end_time, apply_start_time, authority, ipc, keywords …(+3) | data, status, error_msg, error_code | — |
| A005 | 被引用最多的专利 | GET | `/insights/most-cited` | apply_end_time, apply_start_time, authority, ipc, keywords …(+3) | data, status, error_msg, error_code | `patent-visual/most_cited` |
| A006 | 发明人排名分析 | GET | `/insights/inventor-ranking` | apply_end_time, apply_start_time, authority, ipc, keywords …(+3) | data, status, error_msg, error_code | — |
| A007 | 申请人排名分析 | GET | `/insights/applicant-ranking` | apply_end_time, apply_start_time, authority, ipc, keywords …(+4) | data, status, error_msg, error_code | — |
| A008 | 简单法律状态统计 | GET | `/insights/simple-legal-status` | apply_end_time, apply_start_time, authority, ipc, keywords …(+3) | data, status, error_msg, error_code | — |
| A009 | 最多诉讼专利 | GET | `/insights/most-asserted` | apply_end_time, apply_start_time, authority, ipc, keywords …(+3) | data, status, error_msg, error_code | `patent-visual/most_asserted` |
| A010 | 专利价值分布 | GET | `/insights/portfolio-value` | apply_end_time, apply_start_time, authority, ipc, keywords …(+3) | data, status, error_msg, error_code | — |
| A011 | 专利类型趋势分析 | POST | `/insights/patent-type-trend` | query, time_range | data, status, error_msg, error_code | — |
| A012 | 技术功效短语分布 | POST | `/insights/technology-effect-Distribution` | collapse_by, collapse_order, collapse_order_authority, collapse_type, lang …(+2) | data, status, error_msg, error_code | `patent-visual/technology_effect_distribution` |
| A101 | 企业创新词云 | GET | `/insights-company/word-cloud` | company_name, org_number, credit_code, apply_start_time, apply_end_time …(+6) | data, status, error_msg, error_code | — |
| A102 | 企业创新战略雷达图 | GET | `/insights-company/strategy-map` | company_name, org_number, credit_code, apply_start_time, apply_end_time …(+6) | data, status, error_msg, error_code | — |
| A103 | 企业技术构成分析 | GET | `/insights-company/key-technology-overview` | company_name, org_number, credit_code, apply_start_time, apply_end_time …(+6) | data, status, error_msg, error_code | — |
| A104 | 企业专利申请趋势 | GET | `/insights-company/patent-trends` | company_name, org_number, credit_code, apply_start_time, apply_end_time …(+5) | data, status, error_msg, error_code | — |
| A105 | 企业专利总申请布局 | GET | `/insights-company/patent-portfolio-overview` | company_name, org_number, credit_code, apply_start_time, apply_end_time …(+5) | data, status, error_msg, error_code | `patent-visual/company_portfolio_overview` |
| A106 | 企业被引用最多的专利 | GET | `/insights-company/most-cited-latest` | company_name, org_number, credit_code, apply_start_time, apply_end_time …(+6) | data, status, error_msg, error_code | `patent-visual/company_most_cited_latest` |
| A107 | 最多引用该企业专利的公司 | GET | `/insights-company/most-cited` | company_name, org_number, credit_code, apply_start_time, apply_end_time …(+6) | data, status, error_msg, error_code | `patent-visual/company_most_cited` |
| A108 | 企业规模最大的专利家族 | GET | `/insights-company/largest-patent-family` | company_name, org_number, credit_code, apply_start_time, apply_end_time …(+6) | data, status, error_msg, error_code | — |
| A109 | 企业简单法律状态统计 | GET | `/insights-company/simple-legal-status` | company_name, org_number, credit_code, apply_start_time, apply_end_time …(+5) | data, status, error_msg, error_code | — |
| A110 | 企业专利转入转出 | GET | `/insights-company/acquisition-divestiture` | company_name, org_number, credit_code, apply_start_time, apply_end_time …(+6) | data, status, error_msg, error_code | `patent-visual/company_acquisition_divestiture` |
| A201 | 技术效果分布 | POST | `/search/company/technology-effect-Distribution` | apply_end_time, apply_start_time, company_name, lang | data, status, error_msg, error_code | `patent-visual/company_tech_effect_dist` |
| A202 | 技术领域词云 | POST | `/search/company/technology-field-word-cloud` | company_name, lang | data, status, error_msg, error_code | `patent-visual/company_tech_field_word_cloud` |

### 文献数据（5 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| L001 | 文献检索 | POST | `/search/literature/query-search` | date_time, limit, offset, query_text, text …(+1) | data, status, error_msg, error_code | `literature-search/search_literature` |
| L010 | 文献著录信息 | POST | `/literature/bibliography` | doi, paper_id | data, status, error_msg, error_code | `literature-search/literature_bibliography` |
| L011 | 文献作者和机构 | POST | `/literature/author-affiliation` | doi, paper_id | data, status, error_msg, error_code | `literature-search/literature_author_affiliation` |
| L012 | 文献引用 | POST | `/literature/citation` | doi, page_number, paper_id | data, status, error_msg, error_code | `literature-search/literature_citation` |
| L014 | 文献期刊 | POST | `/literature/journal` | doi, paper_id | data, status, error_msg, error_code | `literature-search/literature_journal` |

### 定制聚合数据（25 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| D005 | 专利检索 | POST | `/search/patent/query-search-patent/v3` | offset, sort, collapse_by, stemming, query_text …(+1) | data, status, error_msg, error_code | `patent-landscape/search_patents_v3` |
| D006 | 专利检索统计 | POST | `/search/patent/query-search-patent-facet` | offset, sort, collapse_by, field, limit …(+4) | data, status, error_msg, error_code | `patent-landscape/search_patents_facet` |
| D007 | 专利详情接口 | GET | `/basic-patent-data/patent-detail` | lang, patent_id, patent_number, replace_by_related | data, status, error_msg, error_code | — |
| D008 | 专利 PDF | GET | `/basic-patent-data/patent-pdf` | patent_id, patent_number, replace_by_related | data, status, error_msg, error_code | — |
| D009 | 专利检索及详情 | POST | `/search/patent/query-search-patent-detail` | collapse_by, query_text, collapse_type, sort, offset …(+6) | data, status, error_msg, error_code | `patent-landscape/search_patents_with_detail` |
| D010 | 专利统计 | POST | `/search/patent/query-search-facet` | collapse_by, field, limit, stemming, lang …(+2) | data, status, error_msg, error_code | `patent-landscape/search_patents_statistics` |
| D101 | 技术生命周期 | POST | `/shhgy/reportdata/life-cycle` | collapse_order, query_text, sort, collapse_type, collapse_by …(+1) | data, status, error_msg, error_code | — |
| D102 | 申请人排名 | POST | `/shhgy/reportdata/applicant-rank` | query_text, collapse_type, collapse_by, collapse_order, collapse_order_authority …(+1) | data, status, error_msg, error_code | — |
| D103 | 主要申请人技术分析 | POST | `/shhgy/reportdata/applicant-technology-analysis` | query_text, collapse_type, collapse_by, collapse_order, collapse_order_authority …(+1) | data, status, error_msg, error_code | `patent-landscape/applicant_technology_analysis` |
| D104 | 主要申请人申请趋势 | POST | `/shhgy/reportdata/applicant-trend` | query_text, collapse_type, collapse_by, collapse_order, collapse_order_authority …(+1) | data, status, error_msg, error_code | — |
| D105 | 合作申请分析 | POST | `/shhgy/reportdata/cooperation-applicant-analysis` | query_text, collapse_type, collapse_by, collapse_order, collapse_order_authority …(+1) | data, status, error_msg, error_code | `patent-landscape/cooperation_applicant_analysis` |
| D106 | 专利趋势 | POST | `/shhgy/reportdata/patent-trend` | query_text, collapse_type, collapse_by, collapse_order, collapse_order_authority …(+1) | data, status, error_msg, error_code | — |
| D107 | 重要技术分支主要申请人分布 | POST | `/shhgy/reportdata/technology-applicant-distribution` | query_text, collapse_type, collapse_by, collapse_order, collapse_order_authority …(+1) | data, status, error_msg, error_code | — |
| D108 | 技术构成 | POST | `/shhgy/reportdata/technology-constitute` | query_text, collapse_type, collapse_by, collapse_order, collapse_order_authority …(+1) | data, status, error_msg, error_code | — |
| D109 | 受理局统计 | POST | `/shhgy/reportdata/rec-office` | query_text, collapse_type, collapse_by, collapse_order, collapse_order_authority …(+1) | data, status, error_msg, error_code | — |
| D110 | 受理局统计（按照年） | POST | `/shhgy/reportdata/rec-office-year` | query_text, collapse_type, collapse_by, collapse_order, collapse_order_authority …(+1) | data, status, error_msg, error_code | — |
| D111 | 被引用数排名 | POST | `/shhgy/reportdata/refered-rank` | query_text, collapse_type, collapse_by, collapse_order, collapse_order_authority …(+1) | data, status, error_msg, error_code | — |
| D112 | 同族排名 | POST | `/shhgy/reportdata/famn-rank` | query_text, collapse_type, collapse_by, collapse_order, collapse_order_authority …(+1) | data, status, error_msg, error_code | — |
| D113 | 专利列表 | POST | `/shhgy/reportdata/patent-list` | query_text, collapse_type, collapse_by, collapse_order, collapse_order_authority …(+3) | data, status, error_msg, error_code | `patent-landscape/list` |
| D114 | 专利字段详情（仅包含大文本） | POST | `/shhgy/reportdata/patent-info` | patent_number | data, status, error_msg, error_code | `patent-landscape/info` |
| D115 | 领域地图 | POST | `/shhgy/reportdata/domain-map` | query_text, collapse_type, collapse_by, collapse_order, collapse_order_authority …(+1) | data, status, error_msg, error_code | — |
| D116 | 3D地图分析 | POST | `/shhgy/reportdata/3d-map` | group1, group2, group3, group4, group5 …(+9) | data, status, error_msg, error_code | — |
| D201 | 专利详情文本 | POST | `/jdf/patent_detail_text` | patent_id, patent_number | data, status, error_msg, error_code | `patent-landscape/detail_text` |
| D301 | 专利详情聚合 | GET | `/basic-patent-data/patent-detail-aggregation` | patent_id, patent_number | data, status, error_msg, error_code | `patent-landscape/detail_aggregation` |
| — | 对账单V2 | POST | `/open-user/statement/v2` | apikey, client_secret, time_start, time_end | data, status, error_msg, error_code | — |

### 科创企业评估（8 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| C022 | 科创企业评估（全球） | POST | `/company/technology-evaluation-global` | company_name, credit_code, org_number | data, status, error_msg, error_code | `global-tech-eval/technology_evaluation_global` |
| C023 | 科创企业指标（全球） | POST | `/company/technology-indicators-global` | company_name, credit_code, org_number | data, status, error_msg, error_code | `global-tech-eval/technology_indicators_global` |
| C024 | 科创企业评估指标（全球） | POST | `/company/technology-evaluation-indicators-global` | company_name, credit_code, org_number | data, status, error_msg, error_code | `company-profile/get_company_tech_eval_indicators_global`, `global-tech-eval/tech_eval_indicators_global` …(+1) |
| C025 | 科创企业集团穿透（全球） | POST | `/company/global-company-group-technology-evaluation-indicators` | company_name, credit_code, org_number | data, status, error_msg, error_code | `global-tech-eval/global_company_group_eval`, `tech-diligence/acquisition_get_group_tech_eval` |
| C026 | 科创企业回溯（全球） | POST | `/company/technology-evaluation-indicators-backtracking-global` | company_name, credit_code, date, org_number | data, status, error_msg, error_code | `company-profile/get_company_tech_eval_backtrack_global`, `global-tech-eval/tech_eval_backtrack_global` …(+1) |
| C027 | 企业专利风险预警 | POST | `/company/enterprise-patent-risk-warning` | company_name, credit_code, org_number | data, status, error_msg, error_code | `global-tech-eval/patent_risk_warning`, `tech-diligence/patent_risk_warning` |
| C028 | 企业专利风险预警回溯 | POST | `/company/enterprise-patent-risk-warning-backtracking` | company_name, credit_code, date, org_number | data, status, error_msg, error_code | `global-tech-eval/patent_risk_warning_backtrack`, `patent-risk/patent_risk_backtracking` |
| C029 | 企业专利风险预警趋势 | POST | `/company/enterprise-patent-risk-warning-trend` | company_name, credit_code, org_number | data, status, error_msg, error_code | — |

### 企业基础数据（14 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| C001 | 工商信息 | POST | `/company/registration-information` | company_name, credit_code, org_number | data, status, error_msg, error_code | `company-credit/registration_information`, `company-profile/registration_information` |
| C002 | 对外投资 | POST | `/company/outbound-investment` | company_name, credit_code, org_number | data, status, error_msg, error_code | `company-credit/outbound_investment`, `company-profile/outbound_investment` |
| C003 | 股东信息 | POST | `/company/shareholder-information` | company_name, credit_code, org_number | data, status, error_msg, error_code | `company-credit/shareholder_information`, `company-profile/shareholder_information` |
| C013 | 融资信息 | POST | `/company/financing-information` | company_name, credit_code, org_number | data, status, error_msg, error_code | `company-credit/financing_information`, `company-profile/financing_information` …(+1) |
| C014 | 科技资质 | POST | `/company/technology-qualification` | company_name, credit_code, org_number | data, status, error_msg, error_code | `company-credit/technology_qualification`, `company-profile/technology_qualification` |
| C015 | 获奖信息 | POST | `/company/awards-information` | company_name, credit_code, org_number | data, status, error_msg, error_code | `company-credit/awards_information`, `company-profile/awards_information` |
| C016 | 主要人员 | POST | `/company/main-member` | company_name, credit_code, org_number | data, status, error_msg, error_code | `company-credit/main_member` |
| C017 | 核心团队 | POST | `/company/core-member` | company_name, credit_code, org_number | data, status, error_msg, error_code | `company-credit/core_member`, `company-profile/core_member` |
| C018 | 上市信息 | POST | `/company/listing-Information` | company_name, credit_code, org_number | data, status, error_msg, error_code | `company-credit/listing_information`, `company-profile/listing_information` |
| C019 | IPO进程 | POST | `/company/ipo-process` | company_name, credit_code, org_number | data, status, error_msg, error_code | `company-credit/ipo_process`, `company-profile/ipo_process` |
| C020 | 标准信息 | POST | `/company/standard-information` | standard_type, page_number, company_name, credit_code, org_number | data, status, error_msg, error_code | `company-credit/standard_information`, `company-profile/standard_information` |
| C021 | 资质证书 | POST | `/company/qualification-certificate` | company_name, credit_code, org_number, page_number | data, status, error_msg, error_code | `company-credit/qualification_certificate`, `company-profile/qualification_certificate` |
| C037 | 企业搜索接口 | POST | `/company/search` | city, country, district, entity_status, fin_process …(+21) | data, status, error_msg, error_code | `company-credit/search_company` |
| C038 | 投资信息 | POST | `/company/investment-information` | company_name, credit_code, org_number | data, status, error_msg, error_code | `company-credit/investment_information` |

### 科创企业画像标签（8 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| C004 | 企业属性 | POST | `/company/attribute` | company_name, credit_code, org_number | data, status, error_msg, error_code | `company-profile/get_company_attribute`, `company-tags/get_company_attribute` |
| C005 | 科技认定 | POST | `/company/technology-label` | company_name, credit_code, org_number | data, status, error_msg, error_code | `company-tags/technology_label`, `tech-diligence/company_tech_label` |
| C006 | 获奖情况 | POST | `/company/awards` | company_name, credit_code, org_number | data, status, error_msg, error_code | `company-tags/company_awards` |
| C007 | 行业分类 | POST | `/company/industry-classification` | company_name, credit_code, org_number | data, status, error_msg, error_code | `company-profile/industry_classification`, `company-tags/industry_classification` …(+1) |
| C008 | 产品技术分类 | POST | `/company/product-technical-classification` | company_name, credit_code, org_number | data, status, error_msg, error_code | `company-tags/product_technical_classification` |
| C009 | 产业技术链节点 | POST | `/company/industrial-technology-chain` | company_name, credit_code, org_number | data, status, error_msg, error_code | — |
| C010 | 标准制定 | POST | `/company/standard-development` | company_name, credit_code, org_number | data, status, error_msg, error_code | `company-tags/standard_development` |
| C011 | 知识产权 | POST | `/company/intellectual-property` | company_name, credit_code, org_number | data, status, error_msg, error_code | `company-tags/intellectual_property` |

### 科创企业知识产权（6 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| C031 | 科创企业商标数据 | POST | `/special-ip-data/enterprise-trademark` | app_year, company_name, credit_code, org_number, page_number …(+3) | data, status, error_msg, error_code | — |
| C032 | 科创企业软件著作权 | POST | `/special-ip-data/software-copyright` | company_name, credit_code, org_number, page_number, page_size | data, status, error_msg, error_code | — |
| C033 | 科创企业集成电路布图设计 | POST | `/special-ip-data/ic-design` | company_name, credit_code, org_number, page_number, page_size | data, status, error_msg, error_code | `intangible-assets/ic_design` |
| C034 | 企业植物新品种保护申请信息 | POST | `/special-ip-data/new-plant-variety/application` | page_number, company_name, page_size | total, plant_variety_protection_application_data | `intangible-assets/new_plant_variety` |
| C034 | 企业植物新品种保护授权信息 | POST | `/special-ip-data/new-plant-variety/issue` | page_number, company_name, page_size | total, plant_variety_protection_application_data | `intangible-assets/new_plant_variety` |
| C046 | 潜在买家推荐接口 | POST | `/search/patent/potential-buyer` | patent_id, pn | data, status, error_msg, error_code | `intangible-assets/potential_buyer` |

### 企业科创力分析（4 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| C112 | 企业核心专利 | POST | `/innovation/company/core_patent` | company_name, credit_code, org_number | data, status, error_msg, error_code | `tech-collab/company_core_patent` |
| C114 | 企业产学研分析 | POST | `/company/industry-university-research` | company_name, credit_code, org_number | data, status, error_msg, error_code | `tech-collab/industry_university_research` |
| C115 | 企业产学研研发技术分析 | POST | `/company/industry-university-research-ipc` | company_name, credit_code, org_number | data, status, error_msg, error_code | `tech-collab/industry_university_research_ipc` |
| C116 | 企业产学研共同申请地域分布 | POST | `/company/industry-university-research-region-distribution` | company_name, credit_code, org_number | data, status, error_msg, error_code | — |

### 生物医药检索（9 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| B007 | 药物搜索 | POST | `/synapse/drug/search` | offset, limit, drug, target, disease …(+11) | data, status, error_msg, error_code | — |
| B009 | 药物核心专利检索 | POST | `/synapse/patent/core/search` | offset, limit, drug, filter_dto, legal_status …(+17) | data, status, error_msg, error_code | — |
| B009-1 | 药物核心专利聚合 | POST | `/synapse/patent/core/aggregation` | drug, drug_patent_type, drug_type, patent_tech_type, target …(+13) | data, status, error_msg, error_code | — |
| B011 | 医药文献检索 | POST | `/synapse/paper/search` | offset, limit, keyword, drug, target …(+6) | data, status, error_msg, error_code | — |
| B012 | 临床试验检索 | POST | `/synapse/clinical-trial/search` | offset, limit, keyword, main_experimentation_drug, control_drug …(+18) | data, status, error_msg, error_code | — |
| B043 | 医药新闻检索 | POST | `/synapse/news/search` | offset, limit, drug, target, disease …(+4) | data, status, error_msg, error_code | — |
| B044 | 临床结果检索 | POST | `/synapse/ct-result/search` | offset, limit, main_experimentation_drug, overall_enrollment, sort …(+15) | data, status, error_msg, error_code | — |
| B045 | 医药交易检索 | POST | `/synapse/drug-deal/search` | offset, limit, drug, drug_type, principle …(+15) | data, status, error_msg, error_code | — |
| B069 | 转化医学检索 | POST | `/synapse/translational/medicine/search` | conference, disease, drug, drug_type, journal …(+10) | data, status, error_msg, error_code | — |

### 化合物和生物序列（24 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| B001 | 化学结构式检索 | POST | `/chemical-openapi/compound` | — | data, status, error_msg, error_code | — |
| B002 | 单个化学结构专利检索 | GET | `/chemical-openapi/compound/patents` | inchi_key, page, rows | data, status, error_msg, error_code | — |
| B003 | 生物序列Motif检索 | POST | `/bio-openapi/sequence/motif/job` | — | data, status, error_msg, error_code | — |
| — | [B003/4-0]后台检索任务状态 | GET | `/bio-openapi/sequence/job/status` | job_id | data, status, error_msg, error_code | — |
| — | [B003/4-1]获取序列检索结果 | POST | `/bio-openapi/sequence/job/result` | — | data, status, error_msg, error_code | — |
| B004 | 生物序列普通检索 | POST | `/bio-openapi/sequence/job` | — | data, status, error_msg, error_code | — |
| B005 | 单个序列全部专利 | POST | `/bio-openapi/sequence/patent` | — | data, status, error_msg, error_code | — |
| B014 | 化合物基本信息 | GET | `/chemical-openapi/compound/detail` | inchi_key | data, status, error_msg, error_code | — |
| B015 | 化合物理化性质 | GET | `/synapse/drug/compound-physicochemical-props` | inchi_key | data, status, error_msg, error_code | — |
| B016 | 序列信息 | POST | `/bio/sequence/info` | sequence_id | data, status, error_msg, error_code | — |
| B042 | 单个化学结构文献检索 | POST | `/synapse/chemical/paper/search` | inchi_key, lang, page, rows, sort_order | data, status, error_msg, error_code | — |
| B062 | 提取单篇专利生物序列 | POST | `/bio-openapi/patent/extract/single` | — | data, status, error_msg, error_code | — |
| B063 | 提取多篇专利生物序列 | POST | `/bio-openapi/patent/extract/multi` | — | data, status, error_msg, error_code | — |
| B067-1 | 创建OCSR识别任务 | POST | `/eurekals/open/ocsr/v2/task/submit` | — | data, status, error_msg, error_code | — |
| B067-2 | 查询OCSR任务结果 | GET | `/eurekals/open/ocsr/v2/task` | task_id | data, status, error_msg, error_code | — |
| B068-1 | 创建三元组识别任务 | POST | `/eureka/material/docAnalyzer/submitPDF` | — | data, status, error_msg, error_code | — |
| B068-1 | PCC分子结构预测-发起任务 | POST | `/chat/pcc-molecule-task` | — | data, status, error_msg, error_code | — |
| B068-2 | PCC分子结构预测-获取结果 | POST | `/chat/pcc-molecule-result` | — | data, status, error_msg, error_code | — |
| B068-2 | 查询三元组任务结果 | POST | `/eureka/material/docAnalyzer/getExtractMaterial` | job_id | data, status, error_msg, error_code | — |
| B071 | 提取单篇专利化学结构 | POST | `/synapse/patent/chemical/getSingleData` | exclude_reagents, limit, only_first, page, patent_id …(+4) | data, status, error_msg, error_code | — |
| B072-1 | 提取多篇专利化学结构-创建 | POST | `/synapse/patent/chemical/submitTask` | limit, page, patent_ids, patent_numbers, range_max …(+2) | data, status, error_msg, error_code | — |
| B072-2 | 提取多篇专利化学结构-查询 | GET | `/synapse/patent/chemical/getTaskResult` | task_id | data, status, error_msg, error_code | — |
| B073 | 化合物关键词检索 | POST | `/chemical-business/keyword/search` | keyword | data, status, error_msg, error_code | — |
| B075 | 化合物合成路线 | POST | `/synapse/chemical/reaction/route` | inchi_key, limit, offset, pn, type | data, status, error_msg, error_code | — |

### 药物基础数据（8 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| B018 | 药物基本信息 | GET | `/synapse/drug/detail` | drug_id | data, status, error_msg, error_code | — |
| B019 | 药物批准信息 | GET | `/synapse/drug/approval` | drug_id | data, status, error_msg, error_code | — |
| B020 | 药物研发状态-V2 | GET | `/synapse/drug/highest-dev-status` | drug_id, disease_id, country_id, highest_dev_status_id, offset …(+1) | data, status, error_msg, error_code | — |
| B021 | 药物特殊审评 | GET | `/synapse/drug/special-approval` | drug_id | data, status, error_msg, error_code | — |
| B040 | 靶点基本信息 | GET | `/synapse/target/detail` | target_id | data, status, error_msg, error_code | — |
| B041 | 靶点竞争格局 | GET | `/synapse/target/analysis` | target_id, type, roll_up | data, status, error_msg, error_code | — |
| B047 | 药物相关技术 | GET | `/synapse/drug/xdc` | drug_id | data, status, error_msg, error_code | — |
| B059 | 药物批准文件 | POST | `/synapse/drug/approval/file` | drug_id, approval_id, approval_source | data, status, error_msg, error_code | — |

### 药物临床数据（8 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| B022 | 临床基本信息 | GET | `/synapse/clinical-trial/detail` | clinical_trial_id, register_number | data, status, error_msg, error_code | — |
| B023 | 临床相关实体 | GET | `/synapse/clinical-trial/related-entity` | clinical_trial_id, register_number | data, status, error_msg, error_code | — |
| B024 | 临床研究描述 | GET | `/synapse/clinical-trial/description` | clinical_trial_id, register_number | data, status, error_msg, error_code | — |
| B025 | 临床受试者信息与入排标准 | GET | `/synapse/clinical-trial/eligibility` | clinical_trial_id, register_number | data, status, error_msg, error_code | — |
| B026 | 临床研究方案与设计 | GET | `/synapse/clinical-trial/design` | clinical_trial_id, register_number | data, status, error_msg, error_code | — |
| B027 | 临床联系人 | GET | `/synapse/clinical-trial/contact` | clinical_trial_id, register_number | data, status, error_msg, error_code | — |
| B032 | 药物临床结果基本信息 | GET | `/synapse/ct-result/detail` | ct_result_id | data, status, error_msg, error_code | — |
| B048 | 药物临床结果分组信息 | GET | `/synapse/ct-result/group` | ct_result_id | data, status, error_msg, error_code | — |

### 药物挖掘数据（7 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| B028 | 专利保护药物与专利分类 | GET | `/synapse/patent/detail` | patent_id | data, status, error_msg, error_code | — |
| B030 | 医药文献 | GET | `/synapse/paper/detail` | paper_id | data, status, error_msg, error_code | — |
| B031 | 医药新闻 | GET | `/synapse/news` | news_id | data, status, error_msg, error_code | — |
| B039 | 药物交易信息 | GET | `/synapse/drug-deal` | deal_id | data, status, error_msg, error_code | — |
| B065 | 抗原-抗体配对检索 | GET | `/synapse/bio/antibody/search` | antigen_name, page, rows | data, status, error_msg, error_code | — |
| B066 | 亲和力检索 | GET | `/synapse/bio/affinity/search` | affinity_id, page, rows | data, status, error_msg, error_code | — |
| B070 | 转化医学详情 | GET | `/synapse/translational/medicine/detail` | translational_medicine_id | data, status, error_msg, error_code | — |

### 药物研发机构（6 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| B033 | 机构管线信息 | POST | `/synapse/organization/pipeline` | offset, limit, organization_id | data, status, error_msg, error_code | — |
| B034 | 机构基本信息 | GET | `/synapse/organization/basic-info` | organization_id | data, status, error_msg, error_code | — |
| B035 | 机构营收 | POST | `/synapse/organization/profit` | organization_id, duration_type, duration | data, status, error_msg, error_code | — |
| B036 | 科研基金 | POST | `/synapse/organization/grant-funding` | offset, limit, organization_id | data, status, error_msg, error_code | — |
| B037 | 投资 | POST | `/synapse/organization/investment` | offset, limit, organization_id | data, status, error_msg, error_code | — |
| B038 | 融资 | POST | `/synapse/organization/financing` | offset, limit, organization_id | data, status, error_msg, error_code | — |

### 药物可视化分析（5 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| B057 | 牛眼图分析 | POST | `/synapse/bull-eyes-plot` | limit, dimension, roll_up, drug, drug_type …(+11) | data, status, error_msg, error_code | — |
| B064-1 | 创建药物监控 | POST | `/synapse/alert/drug_search/create` | events, frequency, lang, query, title | data, status, error_msg, error_code | — |
| B064-2 | 编辑药物监控 | POST | `/synapse/alert/drug_search/edit` | alert_id, events, frequency, lang, query …(+1) | data, status, error_msg, error_code | — |
| B064-3 | 查询药物监控 | POST | `/synapse/alert/drug_search/query` | alert_id | data, status, error_msg, error_code | — |
| B074 | 药物里程碑 | POST | `/synapse/drug/milestone` | offset, limit, drug_id, sort_order, milestone …(+6) | data, status, error_msg, error_code | — |

### 智慧芽分析报告（8 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| R001 | 创建企业科创力报告（无Logo版） | POST | `/innovation/company-report/task/create-no-logo` | company_name, credit_code, org_number, report_type | data, status, error_msg, error_code | — |
| R001 | 创建企业科创力报告（智慧芽Logo） | POST | `/innovation/company-report/task/create` | company_name, credit_code, org_number, report_type | data, status, error_msg, error_code | — |
| R001 | 下载企业科创力报告 | GET | `/innovation/company-report/job_id/status` | job_id | data, status, error_msg, error_code | — |
| R002 | 创建专利价值报告（无logo） | POST | `/patent-valuation-data/patent-report/task/create-no-logo` | patent_id, patent_number, report_type | data, status, error_msg, error_code | — |
| R002 | 创建专利价值报告（智慧芽Logo） | POST | `/patent-valuation-data/patent-report/task/create` | patent_id, patent_number, report_type | data, status, error_msg, error_code | — |
| R002 | 下载专利价值报告 | GET | `/patent-valuation-data/patent-report/job_id/status` | job_id | data, status, error_msg, error_code | — |
| R003 | 创建专利申请前评估报告 | POST | `/patent-valuation-data/pre_patent-evaluation-create` | text, limit, tech_maturity_index, report_name, report_info | data, status, error_msg, error_code | — |
| R003 | 下载专利申请前评估报告 | GET | `/patent-valuation-data/pre_patent-evaluation-export` | job_id | data, status, error_msg, error_code | — |

### Insights公司报告（6 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| — | 获取特定分面类型的所有列表 | GET | `/landscape-api/jobs/{job_id}/facets/{facet_type}` | length, start | data, status | — |
| — | 获取特定Landscape分面的所有专利列表 | GET | `/landscape-api/jobs/{job_id}/facets/{facet_type}/detail` | filter_expired, length, start | data, status | — |
| — | 获取作业的所有专利列表 | GET | `/landscape-api/jobs/{job_id}/patents` | all_legal, length, patent_value, start | data, status | — |
| — | 获取Landscape作业结果 | GET | `/landscape-api/jobs/{job_id}/result` | job_seq, label_num, lang | data, status | — |
| — | 获取作业状态 | GET | `/landscape-api/jobs/{job_id}/status` | job_seq | status, error_code, job_status, error_message | — |
| — | 提交新的Landscape作业 | POST | `/landscape-api/jobs` | — | data, status | — |

### 企业科创评估(5级)（5 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| DP001 | 科创企业评估 | POST | `/innovation/company_valuation` | company_name, credit_code, org_number | data, status, error_msg, error_code | `company-risk/enterprise_valuation` |
| DP002 | 科创企业指标 | POST | `/innovation/company_valuation_indicators` | company_name, credit_code, org_number | data, status, error_msg, error_code | `company-risk/enterprise_indicators` |
| DP003 | 科创企业风险预警 | POST | `/innovation/company_warning` | company_name, credit_code, org_number | data, status, error_msg, error_code | `company-risk/enterprise_risk_warning` |
| DP004 | 科创企业评估指标&风险预警 | POST | `/innovation/estimate/company-index-warning` | company_name, credit_code, org_number | data, status, error_msg, error_code | `company-risk/enterprise_valuation_full` |
| DP005 | 科创企业评估指标 | POST | `/innovation/estimate/company-index` | company_name, credit_code, org_number | data, status, error_msg, error_code | `company-risk/enterprise_valuation_with_indicators` |

### 生物医药字典数据（10 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| B049 | 药物类型ID查询 | POST | `/synapse/drug-type/autocomplete` | limit, prefix | data, status, error_msg, error_code | — |
| B050 | 适应症ID查询 | POST | `/synapse/disease/autocomplete` | limit, prefix | data, status, error_msg, error_code | — |
| B051 | 靶点ID查询 | POST | `/synapse/target/autocomplete` | limit, prefix | data, status, error_msg, error_code | — |
| B052 | 机构ID查询 | POST | `/synapse/organization/autocomplete` | limit, prefix | data, status, error_msg, error_code | — |
| B053 | 药物ID查询 | POST | `/synapse/drug/autocomplete` | prefix, limit | data, status, error_msg, error_code | — |
| B054 | 作用机制ID查询 | POST | `/synapse/mechanism-action/autocomplete` | limit, prefix | data, status, error_msg, error_code | — |
| B055 | 指标ID查询 | POST | `/synapse/outcome/autocomplete` | limit, prefix | data, status, error_msg, error_code | — |
| B056 | 字典查询 | POST | `/synapse/dictionary/search` | dict_type, id, keyword, limit, offset …(+3) | data, status, error_msg, error_code | — |
| B056-1 | 专利技术分类ID查询 | POST | `/synapse/patent/technology/autocomplete` | limit, prefix | data, status, error_msg, error_code | — |
| B058 | 治疗领域 | POST | `/synapse/disease/therapeutic-area` | disease_id | data, status, error_msg, error_code | — |

### LOC预测（1 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| — | LOC预测(Beta) | POST | `/ai/image/loc_predict` | description, url | — | — |

## AI API（107 个）

### 智慧芽大模型（3 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| AI07 | 大模型(CC GPT) | POST | `/chat/cc-gpt-stream` | — | data, status, error_msg, error_code | — |
| AI20 | 生物医药大模型 | POST | `/chat/pharm-gpt-stream` | — | data, status, error_msg, error_code | — |
| AI50 | 专利大模型(Pat GPT) | POST | `/chat/pat-gpt-stream` | — | data, status, error_msg, error_code | — |

### 生物制药百科问答（2 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| AI68-1 | 生物医药百科问答-创建 | POST | `/chat/ai-ls-chat` | — | data, status, error_msg, error_code | — |
| AI68-2 | 生物医药百科问答-获取结果 | POST | `/chat/ai-ls-stream` | — | data, status, error_msg, error_code | — |

### 技术交底书（3 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| AI32-1 | 重点内容提取 | POST | `/search/patent/patent-disclosure/tech-means` | tech_solution | data, status, error_msg, error_code | — |
| AI32-2 | 生成技术交底书 | POST | `/search/patent/patent-disclosure/generate` | application, background, embodiment, language, mechanism …(+5) | data, status, error_msg, error_code | — |
| AI32-3 | 下载技术交底书 | POST | `/search/patent/patent-disclosure/download` | job_id | data, status, error_msg, error_code | — |

### 技术方案探索（6 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| AI33-1 | 技术方案探索-创建任务 | POST | `/ai/find-solution/step1/v3` | lang, solution_issues | data, status, error_msg, error_code | `patsnap-solution-engine/run_triz_innovation_task` |
| AI33-2 | 技术方案探索-获取推荐 | POST | `/ai/find-solution/step2/v3` | task_id | data, status, error_msg, error_code | — |
| AI33-3 | 技术方案探索-选择推荐 | POST | `/ai/find-solution/step3-submit/v3` | lang, recommend, task_id | data, status, error_msg, error_code | — |
| AI33-4 | 技术方案探索-获取方向 | POST | `/ai/find-solution/step3-query/v3` | task_id | data, status, error_msg, error_code | — |
| AI33-5 | 技术方案探索-选择方向 | POST | `/ai/find-solution/step4/v3` | directions, lang, task_id | data, status, error_msg, error_code | — |
| AI33-6 | 技术方案探索-获取方案和细节 | POST | `/ai/find-solution/step5/v3` | task_id | data, status, error_msg, error_code | — |

### 材料技术方案探索（9 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| AI73-1 | 材料技术方案探索-提交任务 | POST | `/ai/material/find-solution/submit` | input, lang | data, status, error_msg, error_code | — |
| AI73-2 | 材料技术方案探索-获取推荐方案 | POST | `/ai/material/find-solution/recommend` | task_id | data, status, error_msg, error_code | — |
| AI73-3 | 材料技术方案探索-确认推荐方案 | POST | `/ai/material/find-solution/confirm-recommend` | recommend, task_id | data, status, error_msg, error_code | — |
| AI73-4 | 材料技术方案探索-获取思考过程 | POST | `/ai/material/find-solution/thinking` | task_id | data, status, error_msg, error_code | — |
| AI73-5 | 材料技术方案探索-获取脑图 | POST | `/ai/material/find-solution/mind` | task_id | data, status, error_msg, error_code | — |
| AI73-6 | 材料技术方案探索-获取节点引用文献列表 | POST | `/ai/material/find-solution/citation-reference-list` | board_id, limit, node_id, page, task_id | data, status, error_msg, error_code | — |
| AI73-7 | 材料技术方案探索-获取节点参考信息 | POST | `/ai/material/find-solution/node-reference` | board_id, node_id, task_id | data, status, error_msg, error_code | — |
| AI73-8 | 材料技术方案探索-生成方案 | POST | `/ai/material/find-solution/implementation` | board_id, node_id, task_id | data, status, error_msg, error_code | — |
| AI73-9 | 材料技术方案探索-获取结果 | POST | `/ai/material/find-solution/implementation-response` | board_id, node_id, task_id | data, status, error_msg, error_code | — |

### 技术预研报告（3 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| AI34-1 | 预研报告创建（Beta） | POST | `/ai/quick-search-report/creation` | auto_directory, technical_issues | data, status, error_msg, error_code | — |
| AI34-2 | 预研报告创建-自定义目录（Beta） | POST | `/ai/quick-search-report/creation/custom-dir` | analysis_directory, report_id, technical_issues | data, status, error_msg, error_code | — |
| AI34-3 | 预研报告查询（Beta） | GET | `/ai/quick-search-report/query` | report_id | data, status, error_msg, error_code | — |

### 查新检索（12 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| AI35-1 | 查新检索-创建任务 | POST | `/ai/novelty-search/submit` | input, lang, pbd_end, pbd_start | data, status, error_msg, error_code | — |
| AI35-2 | 查新检索-总结技术要点 | POST | `/ai/novelty-search/tech-solution/get` | task_id | data, status, error_msg, error_code | `patsnap-ip-searching/novelty_search` |
| AI35-3 | 查新检索-确认技术要点 | POST | `/ai/novelty-search/tech-solution/update` | task_id, tech_solution | data, status, error_msg, error_code | — |
| AI35-4 | 查新检索-提取技术特征 | POST | `/ai/novelty-search/feature/extract` | task_id | data, status, error_msg, error_code | `novelty-search-lite/novelty_feature_extract` |
| AI35-5 | 查新检索-确认技术特征 | POST | `/ai/novelty-search/feature/confirm` | task_id, tech_features | data, status, error_msg, error_code | — |
| AI35-6 | 查新检索-提取检索要素 | POST | `/ai/novelty-search/retrieval/elements` | task_id | data, status, error_msg, error_code | `novelty-search-lite/novelty_keywords_extract` |
| AI35-7 | 查新检索-确认检索要素 | POST | `/ai/novelty-search/agent-search` | elements, task_id | data, status, error_msg, error_code | — |
| AI35-8 | 查新检索-获取检索策略与筛选列表与特征对比 | POST | `/ai/novelty-search/agent-result` | task_id | data, status, error_msg, error_code | — |
| AI35-9 | 查新检索-确认筛选列表与特征对比 | POST | `/ai/novelty-search/feature/comparison/confirm` | final_result, task_id | data, status, error_msg, error_code | — |
| AI35-10 | 查新检索-创建报告 | POST | `/ai/novelty-search/export` | task_id, title | data, status, error_msg, error_code | — |
| AI35-11 | 查新检索-下载报告 | POST | `/ai/novelty-search/report/get` | task_id | data, status, error_msg, error_code | — |
| AI35-12 | 查新检索-添加对比文献或专利 | POST | `/ai/novelty-search/feature/comparison/generate` | request, tech_features | data, status, error_msg, error_code | — |

### 技术问答（2 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| AI36-1 | 技术问答-提交任务 | POST | `/ai/technical-qa/submit` | input, lang, model, rag_source, summary_check | data, status, error_msg, error_code | — |
| AI36-2 | 技术问答-查询任务 | POST | `/ai/technical-qa/report` | task_id | data, status, error_msg, error_code | — |

### 专利说明书撰写（5 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| AI37-1 | 专利说明书撰写(CNIPA)-初始化总结 | POST | `/ai/specification/init/cnipa` | claim, disclosure | data, status, error_msg, error_code | — |
| AI37-2 | 专利说明书撰写(CNIPA)-初始化总结结果获取 | POST | `/ai/specification/init-result/cnipa` | task_id | data, status, error_msg, error_code | — |
| AI37-3 | 专利说明书撰写(CNIPA)-获取技术特征 | POST | `/ai/specification/extract-feature/cnipa` | category, task_id | data, status, error_msg, error_code | — |
| AI37-4 | 专利说明书撰写(CNIPA)-生成报告 | POST | `/ai/specification/generate-report/cnipa` | benefit, category, classification, embodiments, feature_tree …(+6) | data, status, error_msg, error_code | — |
| AI37-5 | 专利说明书撰写(CNIPA)-下载报告 | POST | `/ai/specification/download-report` | task_id | data, status, error_msg, error_code | — |

### 外观专利侵权检索（3 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| AI39-1 | 外观防侵权检索-提交工作流任务 | POST | `/api/mcp/submit-workflow` | url, target_image_base64, image_urls, image_base64s, description …(+7) | code, status, country, message, success …(+2) | `design-fto-search-mcp/submit_workflow`, `patsnap-ip-searching/design_fto` |
| AI39-2 | 外观防侵权检索-查询工作流任务状态 | GET | `/api/mcp/task/status` | task_id | code, task, stages, status, message …(+2) | — |
| AI39-3 | 外观防侵权检索-获取阶段执行结果 | GET | `/api/mcp/task/stage/result` | task_id, stage, image_mode | code, data, status, message, success …(+1) | `design-fto-search-mcp/get_stage_result` |

### 外观专利侵权检索1v1（2 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| AI67-1 | 外观防侵权检索1V1-任务创建 | POST | `/ai/infringement-detection-1v1-creation` | patent_number, report_lang, url | data, status, error_msg, error_code | — |
| AI67-2 | 外观防侵权检索1V1-任务查询 | POST | `/ai/infringement-detection-1v1-query` | task_id | data, status, error_msg, error_code | — |

### 可行性分析助手（2 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| AI40-1 | 可行性分析助手-报告创建 | POST | `/ai/feasibility-analysis-creation` | lang, need_logo, text | data, status, error_msg, error_code | — |
| AI40-2 | 可行性分析助手-报告查询 | POST | `/ai/feasibility-analysis-query` | task_id | data, status, error_msg, error_code | — |

### AI 翻译（10 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| AI59-3 | 图片翻译-获取结果 | GET | `/image-translation/v1/tasks/{task_id}/result` | task_id | code, image, blocks, status, message …(+4) | — |
| AI59-2 | 图片翻译-查询任务状态 | GET | `/image-translation/v1/tasks/{task_id}` | task_id | code, state, message, task_id, direction …(+6) | — |
| AI62-2 | PDF 翻译-查询任务状态 | GET | `/pdf-translation/tasks/{task_id}` | — | lang, error, pages, phase, state …(+21) | — |
| AI62-1 | PDF 翻译-提交翻译任务 | POST | `/pdf-translation/translate` | pdf, pdf_url, source_lang, target_lang, pages …(+2) | lang, state, job_id, taskId, message …(+12) | — |
| AI59-1 | 图片翻译-提交任务 | POST | `/image-translation/v1/translate` | — | code, state, message, task_id, direction …(+6) | — |
| AI62-3 | PDF 翻译-获取翻译结果 | GET | `/pdf-translation/tasks/{task_id}/result` | response_format | state, task_id, filename, expires_at, expires_in …(+2) | — |
| AI61 | AI翻译 | POST | `/ai/translation` | source_lang, target_lang, text | data, status, error_msg, error_code | `document-processing/translation_docx`, `document-processing/translation_text` |
| T010 | 文本翻译 | POST | `/hiro_translation/translate` | content, sourceLanguageCode, targetLanguageCode, mode | state, progress, textOriginal, textTranslated, translatedCharacterCount | — |
| T011 | DOCX翻译 | POST | `/docx-translation/api/v1/translations` | file_content_base64, filename, sourceLanguageCode, targetLanguageCode, enable_async …(+5) | error, job_id, status, glossary, job_type …(+28) | — |
| T012 | DOCX翻译状态查询 | POST | `/docx-translation/api/v1/jobs/status` | job_id | error, job_id, status, glossary, job_type …(+28) | — |

### FTO 搜索（8 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| AI66-1 | 防侵权检索-创建任务 | POST | `/ai/fto/submit` | apd_end, apd_start, country, exclude_company, include_company …(+3) | data, status, error_msg, error_code | — |
| AI66-2 | 防侵权检索-提取技术特征 | POST | `/ai/fto/feature/extract` | task_id | data, status, error_msg, error_code | — |
| AI66-3 | 防侵权检索-确认技术特征 | POST | `/ai/fto/feature/confirm` | task_id, tech_features | data, status, error_msg, error_code | — |
| AI66-4 | 防侵权检索-启动FTO检索 | POST | `/ai/fto/search/agent` | task_id | data, status, error_msg, error_code | `patsnap-ip-searching/fto_review` |
| AI66-5 | 防侵权检索-获取FTO检索结果 | POST | `/ai/fto/search/agent/result` | task_id | data, status, error_msg, error_code | — |
| AI66-6 | 防侵权检索-创建报告 | POST | `/ai/fto/report/create` | final_res, task_id, title | data, status, error_msg, error_code | — |
| AI66-7 | 防侵权检索-下载报告 | POST | `/ai/fto/report/get` | task_id | data, status, error_msg, error_code | — |
| AI66-8 | 防侵权检索-添加对比文献或专利 | POST | `/ai/fto/feature/comparison` | pn, task_id | data, status, error_msg, error_code | — |

### 配方助手（2 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| M001-1 | 配方助手-报告创建 | POST | `/ai/formulation-agent-creation` | lang, text | data, status, error_msg, error_code | — |
| M001-2 | 配方助手-报告查询 | POST | `/ai/formulation-agent-query` | task_id | data, status, error_msg, error_code | — |

### 新颖性检查助手（2 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| M002-1 | 新颖性检查助手-报告创建 | POST | `/ai/novelty-check-agent-creation` | lang, text | data, status, error_msg, error_code | — |
| M002-2 | 新颖性检查助手-报告查询 | POST | `/ai/novelty-check-agent-query` | task_id | data, status, error_msg, error_code | — |

### 化学SAR提取（2 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| AI103-2 | 化学SAR提取-获取SAR文件详情 | POST | `/eurekals/open/sar/file/detail` | task_id | data, status, error_msg, error_code, error_params | — |
| AI103-1 | 化学SAR提取-提交SAR解析任务 | POST | `/eurekals/open/sar/file/extract` | — | data, status, error_msg, error_code, error_params | — |

### 其他（12 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| AI01 | 药物DDT抽取 | POST | `/ai/ner/ddt-ner` | lang, source, text | data, status, error_msg, error_code | `pharma-intelligence/ls_ner_nor_normalize` |
| AI03 | 新闻实体识别(NER) | POST | `/ai/ner/news-ner` | lang, text | data, status, error_msg, error_code | — |
| AI30 | 相似专利检索与比对 | POST | `/search/patent/similar-patent-comparison` | country, legal_status, limit, tech_effect, tech_means | data, status, error_msg, error_code | `report-gen/idea_validation_similar` |
| AI31 | 专利发明点总结 | POST | `/search/patent/patent-core-invention-points` | lang, patent_id, pn | data, status, error_msg, error_code | — |
| AI71 | 离线报告获取 | POST | `/ai/sso/agent/export-link` | agent_type, company_id, email, end_time, lang …(+4) | data, status, error_msg, error_code | — |
| AI72 | 离线历史记录获取-批量 | POST | `/ai/sso/agent/batch-history` | company_id, end_time, page, start_time, user_accounts | data, status, error_msg, error_code | — |
| AI72 | 离线历史记录获取 | POST | `/ai/sso/agent/history` | company_id, email, end_time, page, phone …(+1) | data, status, error_msg, error_code | — |
| AI88-1 | 获取企业简报列表 | GET | `/eureka/tech-monitor-api/company-monitors` | X-Site-Lang | data, status, error_msg, error_code | — |
| AI88-2 | 查询企业简报聚合信息 | GET | `/eureka/tech-monitor-api/company-monitor/aggregated-info` | tech-monitor-id, report_week, X-Site-Lang | data, status, error_msg, error_code | — |
| L016 | 文档解析 | POST | `/rd-llm/v1/documents/doc_parsing` | — | data, status, error_msg, error_code | — |
| L017 | 仅版面解析（不执行 OCR） | POST | `/rd-llm/v1/documents/layout_parsing` | — | data, status, error_msg, error_code | — |
| AI88-3 | 查询企业简报聚合信息 | GET | `/eureka-pulse/tech-monitor-api/company-monitor/aggregated-info` | tech-monitor-id, report_week, X-Site-Lang | data, status, error_msg, error_code | — |

### 通信（1 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| T001 | 通信标准必要专利（SEP）智能判断 | POST | `/open_api/task/aicc` | x-site-lang | data, status, error_code | — |

### 研发解决方案搜索（1 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| — | 解决方案检索（SolutionSearch） | POST | `/method-services/solution-search` | user_question, limit | data, status, error_msg, error_code | — |

### 防侵权搜索（11 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| AI66-1 | 防侵权检索-创建任务 | POST | `/fto_steps/create_task` | — | status, task_id | — |
| AI66-2 | 防侵权检索-方案润色 | POST | `/fto_steps/proposal_refine` | — | status, task_id, step_name | — |
| AI66-3 | 防侵权检索-特征提取 | POST | `/fto_steps/feature_extraction` | — | status, task_id, step_name | — |
| AI66-4 | 防侵权检索-关键词扩展 | POST | `/fto_steps/keyword_expansion` | — | status, task_id, step_name | `patsnap-ip-searching/fto_review` |
| AI66-5 | 防侵权检索-检索式生成 | POST | `/fto_steps/query_generation` | — | status, task_id, step_name | — |
| AI66-6 | 防侵权检索-检索式迭代优化 | POST | `/fto_steps/iterative_optimization` | — | status, task_id, step_name | — |
| AI66-7 | 防侵权检索-专利初筛 | POST | `/fto_steps/patent_screening` | — | status, task_id, step_name | — |
| AI66-8 | 防侵权检索-权利要求对比（内部ID） | POST | `/fto_steps/cc_analysis` | — | status, task_id, step_name | — |
| AI66-9 | 防侵权检索-按公开号权利要求对比 | POST | `/fto_steps/feature_comparison` | — | status, task_id, step_name | — |
| AI66-10 | 防侵权检索-报告生成 | POST | `/fto_steps/report_generation` | — | status, task_id, step_name | — |
| AI66-11 | 防侵权检索-查询步骤状态 | GET | `/fto_steps/result` | step_name, task_id | result, status, task_id, error_msg, step_name …(+1) | — |

### 智慧芽学社课程（3 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| AC01 | 获取课程列表 | GET | `/academy/course-list` | company_id, limit, page | data, status, error_msg, error_code | `ip-courses/course_list` |
| AC02 | 获取具体课程详情 | GET | `/academy/course-details` | company_id, course_id | data, status, error_msg, error_code | `ip-courses/course_details` |
| AC03 | 获取课程的课件 | GET | `/academy/attach-download` | company_id, courseware_id | — | `ip-courses/course_courseware` |

### 技术想法查新（3 个）

| 编号 | 名称 | 方法 | 路径 | 请求字段 | 响应字段 | MCP 封装 |
|------|------|------|------|----------|----------|----------|
| AI29-1 | 创建技术想法查新报告 | POST | `/search/patent/idea-validation/task/create` | country, legal_status, limit, tech_effect, tech_means | data, status, error_msg, error_code | `report-gen/idea_validation_create` |
| AI29-2 | 相似专利检索与比对 | POST | `/search/patent/idea-validation/similar-patent-comparison` | job_id | data, status, error_msg, error_code | — |
| AI29-3 | 下载技术想法查新报告 | POST | `/search/patent/idea-validation/job_id/status` | file_format, job_id | data, status, error_msg, error_code | `report-gen/idea_validation_download` |

---

*index.json v0.6.0 · 字段明细见 index.json 的 apis[]*
