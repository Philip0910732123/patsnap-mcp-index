# 智慧芽 MCP 工具矩阵

> **已归档（v0.6.0 起）**：本文是旧版人工整理，其中的 MCP / API 数量与映射口径已过时，请勿作为事实依据。当前口径（50 MCP / 411 tool / 376 API）以 [index.json](../index.json) 为唯一真相源；人读入口见 [getting-started.md](getting-started.md)，映射复核见 [api-mapping-review.md](api-mapping-review.md)。

> 59 个 MCP 服务下的全部工具清单，按领域分组。每个工具列出名称和简要说明。

---

## 一、IP 智能（Ip-Intelligence）

### 1. core-patents（20 工具）

| 工具 | 说明 |
|------|------|
| `search_patents` | 专利检索（按公开号/关键词） |
| `bibliography` | 著录项目（标题/申请人/发明人/日期/分类号） |
| `claims` | 权利要求全文 |
| `claim_translated` | 权利要求中文翻译 |
| `description` | 说明书全文 |
| `description_translated` | 说明书中文翻译 |
| `abstract_translated` | 摘要中文翻译 |
| `abstract_image` | 摘要附图 |
| `fulltext_image` | 全文附图 |
| `family` | 同族专利 |
| `forward_citation` | 前向引证 |
| `legal_data` | 法律状态数据 |
| `get_patent_legal_status` | 获取专利法律状态 |
| `license_data` | 许可数据 |
| `transfer_data` | 转移数据 |
| `pledge_data` | 质押数据 |
| `reexamination_invalidation` | 复审无效 |
| `customs_data` | 海关备案数据 |
| `award_data` | 获奖数据 |
| `pdf` | 专利 PDF 下载 |

### 2. design-fto-search-mcp（4 工具）

| 工具 | 说明 |
|------|------|
| `create_image_upload_url` | 创建图片上传 URL |
| `submit_workflow` | 提交外观 FTO 检索工作流 |
| `get_task_status` | 获取任务状态 |
| `get_stage_result` | 获取各阶段结果 |

### 3. document-processing（4 工具）

| 工具 | 说明 |
|------|------|
| `documents_parsing` | 文档解析（Layout/OCR） |
| `translation_text` | 文本流式翻译（18 种语言互译） |
| `translation_docx` | DOCX 文档翻译 |
| `translation_docx_status` | DOCX 翻译状态查询 |

### 4. intangible-assets（5 工具）

| 工具 | 说明 |
|------|------|
| `enterprise_trademark` | 企业商标 |
| `software_copyright` | 软件著作权 |
| `new_plant_variety` | 植物新品种 |
| `ic_design` | 集成电路布图设计 |
| `potential_buyer` | 潜在买家推荐 |

### 5. ip-courses（3 工具）

| 工具 | 说明 |
|------|------|
| `course_list` | 课程列表 |
| `course_details` | 课程详情 |
| `course_courseware` | 课件下载 |

### 6. landscape-projects（6 工具）

| 工具 | 说明 |
|------|------|
| `landscape_job_create` | 创建全景分析任务 |
| `landscape_job_status` | 查看任务状态 |
| `landscape_job_result` | 读取分析结果 |
| `landscape_facet_list` | 分面列表 |
| `landscape_facet_detail` | 分面详情 |
| `landscape_patents` | 专利列表 |

### 7. novelty-search-lite（13 工具）

| 工具 | 说明 |
|------|------|
| `novelty_feature_extract` | 技术特征提取 |
| `novelty_keywords_extract` | 检索关键词提取 |
| `novelty_lite_search` | 综合检索 |
| `novelty_lite_semantic_search` | 语义检索 |
| `novelty_lite_boolean_search` | 布尔检索 |
| `novelty_lite_paper_search` | 文献检索 |
| `novelty_lite_website_search` | 网页检索 |
| `novelty_lite_get` | 获取检索结果 |
| `novelty_lite_submit` | 提交检索任务 |
| `novelty_feature_comparison` | 特征对比 |
| `novelty_review_with_suggestions` | 审查建议 |
| `novelty_summary` | 查新摘要 |
| `novelty_lite_report_generate` | 报告生成 |

### 8. patent-analysis（2 工具）

| 工具 | 说明 |
|------|------|
| `aggregate_patents` | 专利聚合统计 |
| `mine_patent_text` | 专利文本挖掘 |

### 9. patent-briefing（12 工具）

| 工具 | 说明 |
|------|------|
| `search_patents` | 专利检索 |
| `bibliography` | 著录项目 |
| `claims` | 权利要求 |
| `claim_translated` | 权利要求翻译 |
| `description` | 说明书 |
| `description_translated` | 说明书翻译 |
| `abstract_translated` | 摘要翻译 |
| `abstract_image` | 摘要附图 |
| `family` | 同族信息 |
| `legal_status` | 法律状态 |
| `intelligent_image` | 智能附图 |
| `tech_summary` | 技术三要素摘要 |

### 10. patent-dispute（21 工具）

| 工具 | 说明 |
|------|------|
| `search_patents` | 专利检索 |
| `bibliography` | 著录项目 |
| `claims` | 权利要求 |
| `claim_translated` | 权利要求翻译 |
| `description` | 说明书 |
| `desc_translated` | 说明书翻译 |
| `abstract_translated` | 摘要翻译 |
| `abstract_image` | 摘要附图 |
| `fulltext_image` | 全文附图 |
| `family` | 同族专利 |
| `forward_citation` | 前向引证 |
| `legal_data` | 法律数据 |
| `legal_status` | 法律状态 |
| `license_data` | 许可数据 |
| `transfer_data` | 转移数据 |
| `pledge_data` | 质押数据 |
| `reexam_invalidation` | 复审无效 |
| `customs_data` | 海关备案 |
| `award_data` | 获奖数据 |
| `pdf` | PDF 下载 |
| `valuation_get_patent_valuation` | 专利价值评估 |

### 11. patent-landscape（24 工具）

| 工具 | 说明 |
|------|------|
| `search_patents_v3` | V3 专利检索 |
| `search_patents_facet` | 分面检索 |
| `search_patents_statistics` | 检索统计 |
| `search_patents_with_detail` | 带详情检索 |
| `detail` | 专利详情 |
| `detail_aggregation` | 聚合详情 |
| `detail_text` | 详情文本 |
| `trend` | 申请趋势 |
| `technology_constitute` | 技术构成 |
| `applicant_rank` | 申请人排名 |
| `applicant_trend` | 申请人趋势 |
| `applicant_technology_analysis` | 申请人技术分析 |
| `cooperation_applicant_analysis` | 合作申请人分析 |
| `tech_applicant_dist` | 技术-申请人分布 |
| `technology_life_cycle` | 技术生命周期 |
| `domain_map` | 技术领域地图 |
| `map_3d` | 3D 地图 |
| `famn_rank` | 同族排名 |
| `refered_rank` | 被引排名 |
| `rec_office` | 受理局 |
| `get_rec_office_year` | 受理局年度 |
| `info` | 专利信息 |
| `list` | 专利列表 |
| `pdf` | PDF 下载 |

### 12. patent-mining（9 工具）

| 工具 | 说明 |
|------|------|
| `technology_topic` | 技术主题 |
| `tech_problem_benefit_summary` | 技术-问题-效果三要素 |
| `application_domain` | 应用领域 |
| `classification_description` | 分类号说明 |
| `seic_classification` | 战略性新兴产业分类 |
| `material_ontology` | 材料本体 |
| `material_substance` | 材料物质 |
| `enhanced_data` | 增强数据 |
| `intelligent_attached_image` | 智能附图 |

### 13. patent-status（12 工具）

| 工具 | 说明 |
|------|------|
| `legal_data` | 法律状态数据 |
| `fee_info` | 年费缴纳信息 |
| `get_sep_data` | SEP 数据 |
| `litigation_data` | 诉讼数据 |
| `license_data` | 许可数据 |
| `pledge_data` | 质押数据 |
| `re_examination_data` | 复审数据 |
| `transfer_data` | 转移数据 |
| `customs_data` | 海关备案 |
| `award_data` | 获奖数据 |
| `overseas_patent_documents` | 海外专利审查文件 |
| `unified_patent_court_status` | UPC 统一专利法院状态 |

### 14. patent-value（10 工具）

| 工具 | 说明 |
|------|------|
| `valuation` | 综合价值评估 |
| `technology_indicators` | 技术维度指标 |
| `tech_innovation_indicators` | 技术创新指标 |
| `legal_indicators` | 法律稳定性指标 |
| `market_indicators` | 市场指标 |
| `market_prospect_indicators` | 市场前景指标 |
| `strategic_indicators` | 战略指标 |
| `ability_indicators` | 能力指标 |
| `operation_situation_indicators` | 运营指标 |
| `economic_indicators` | 经济指标 |

### 15. patent-visual（24 工具）

| 工具 | 说明 |
|------|------|
| `trends` | 趋势 |
| `type_trend` | 类型趋势 |
| `applicant_ranking` | 申请人排名 |
| `inventor_ranking` | 发明人排名 |
| `most_cited` | 最高被引 |
| `most_asserted` | 最多主张 |
| `word_cloud` | 词云 |
| `company_word_cloud` | 企业词云 |
| `company_tech_field_word_cloud` | 企业技术领域词云 |
| `technology_effect_distribution` | 技术-效果分布 |
| `company_tech_effect_dist` | 企业技术-效果分布 |
| `simple_legal_status` | 简单法律状态 |
| `company_simple_legal_status` | 企业简单法律状态 |
| `priority_country` | 优先权国家 |
| `portfolio_value` | 专利组合价值 |
| `wheel_of_innovation` | 创新轮盘 |
| `company_patent_trends` | 企业专利趋势 |
| `company_portfolio_overview` | 企业组合概览 |
| `company_strategy_map` | 企业战略地图 |
| `company_key_technology` | 企业关键技术 |
| `company_largest_patent_family` | 企业最大专利族 |
| `company_most_cited` | 企业最高被引 |
| `company_most_cited_latest` | 企业最新最高被引 |
| `company_acquisition_divestiture` | 企业收购/剥离 |

### 16. patsnap-analytics（1 工具）

| 工具 | 说明 |
|------|------|
| `fetch_patent_lifecycle` | 专利生命周期事件 |

### 17. patsnap-ip-searching（5 工具）

| 工具 | 说明 |
|------|------|
| `novelty_search` | 查新检索 |
| `fto_review` | 发明 FTO 分析 |
| `design_fto` | 外观设计 FTO |
| `upload_image` | 上传图片 |
| `get_task` | 获取任务 |

### 18. patsnap-web-search（1 工具）

| 工具 | 说明 |
|------|------|
| `web_search` | 实时网页搜索 |

### 19. patsnap-workspace（5 工具）

| 工具 | 说明 |
|------|------|
| `list_workspace_spaces` | 列出工作空间 |
| `list_workspace_folders` | 列出目录 |
| `list_workspace_fields` | 列出可用字段 |
| `get_workspace_patents` | 检索目录内专利 |
| `get_workspace_annotations` | 获取标引和注释 |

### 20. s-telecom-mcp-tools（4 工具）

| 工具 | 说明 |
|------|------|
| `search_tdocs` | TDoc 语义/元数据检索 |
| `fetch_tdocs` | TDoc 详情读取 |
| `search_standards` | 标准检索 |
| `fetch_standard_section` | 标准章节正文读取 |

### 21. s-telecom-mcp-tools-sep（1 工具）

| 工具 | 说明 |
|------|------|
| `standard_claim_charting` | SEP Claim Charting |

---

## 二、生命科学（Life-Sciences）

### 1. biology-modality（8 工具）

| 工具 | 说明 |
|------|------|
| `ls_sequence_search_submit` | 序列搜索提交 |
| `ls_sequence_search_check_status` | 检查搜索状态 |
| `ls_sequence_search_get_results` | 获取搜索结果 |
| `ls_sequence_fetch` | 序列获取 |
| `ls_sequence_alignment` | 序列比对 |
| `ls_patent_sequence_fetch` | 专利序列获取 |
| `ls_antibody_antigen_search` | 抗原-抗体搜索 |
| `ls_modification_search_submit` | 翻译后修饰搜索 |

### 2. chemical-molecular（7 工具）

| 工具 | 说明 |
|------|------|
| `ls_structure_search` | 化合物结构搜索 |
| `ls_structure_fetch` | 化合物结构获取 |
| `ls_patent_structure_fetch` | 专利结构获取 |
| `ls_admet_predict` | ADMET 预测 |
| `ls_chemical_mcs_analyze` | 最大公共子结构分析 |
| `ls_sar_submit` | SAR 提交 |
| `ls_sar_fetch` | SAR 结果获取 |

### 3. clinical-trials（4 工具）

| 工具 | 说明 |
|------|------|
| `clinical_trial_search` | 临床试验检索 |
| `clinical_trial_fetch` | 试验详情 |
| `clinical_trial_result_search` | 试验结果检索 |
| `clinical_trial_result_fetch` | 结果详情 |

### 4. company-deal-intelligence（5 工具）

| 工具 | 说明 |
|------|------|
| `organization_fetch` | 组织画像 |
| `organization_pipeline_fetch` | 研发管线 |
| `drug_deal_search` | 药物交易搜索 |
| `drug_deal_fetch` | 交易详情 |
| `financial_report_search` | 财报查询 |

### 5. current-awareness（2 工具）

| 工具 | 说明 |
|------|------|
| `news_search` | 新闻检索 |
| `news_fetch` | 新闻详情 |

### 6. drug-asset（3 工具）

| 工具 | 说明 |
|------|------|
| `drug_search` | 药物搜索 |
| `drug_fetch` | 药物详情 |
| `drug_milestone_fetch` | 研发里程碑 |

### 7. pharma-intelligence（30 工具）

| 工具 | 说明 |
|------|------|
| `ls_drug_search` | 药物搜索 |
| `ls_drug_fetch` | 药物详情 |
| `ls_drug_milestone_fetch` | 药物里程碑 |
| `ls_drug_deal_search` | 交易搜索 |
| `ls_drug_deal_fetch` | 交易详情 |
| `ls_clinical_trial_search` | 临床试验搜索 |
| `ls_clinical_trial_fetch` | 临床试验详情 |
| `ls_clinical_trial_result_search` | 结果搜索 |
| `ls_clinical_trial_result_fetch` | 结果详情 |
| `ls_clinical_trial_vector_search` | 临床试验语义检索 |
| `ls_disease_fetch` | 疾病详情 |
| `ls_target_fetch` | 靶点详情 |
| `ls_patent_search` | 专利搜索 |
| `ls_patent_fetch` | 专利详情 |
| `ls_patent_vector_search` | 专利语义检索 |
| `ls_paper_search` | 文献搜索 |
| `ls_paper_fetch` | 文献详情 |
| `ls_paper_vector_search` | 文献语义检索 |
| `ls_organization_fetch` | 组织详情 |
| `ls_organization_pipeline_fetch` | 组织管线 |
| `ls_translational_medicine_search` | 转化医学搜索 |
| `ls_translational_medicine_fetch` | 转化医学详情 |
| `ls_news_fetch` | 新闻详情 |
| `ls_news_vector_search` | 新闻语义检索 |
| `ls_web_search` | 网页搜索 |
| `ls_epidemiology_vector_search` | 流行病学语义检索 |
| `ls_fda_label_vector_search` | FDA 标签语义检索 |
| `ls_financial_report_vector_search` | 财报语义检索 |
| `ls_clinical_guideline_vector_search` | 临床指南语义检索 |
| `ls_ner_nor_normalize` | 实体归一化 |

### 8. regulatory-guidelines（2 工具）

| 工具 | 说明 |
|------|------|
| `clinical_guideline_search` | 临床指南搜索 |
| `fda_label_search` | FDA 药品说明书搜索 |

### 9. sar-extraction（2 工具）

| 工具 | 说明 |
|------|------|
| `sar_submit` | 提交 SAR 提取任务 |
| `sar_fetch` | 获取 SAR 结果 |

### 10. scientific-translational-evidence（2 工具）

| 工具 | 说明 |
|------|------|
| `translational_medicine_search` | 转化医学检索 |
| `translational_medicine_fetch` | 转化医学详情 |

### 11. target-disease（3 工具）

| 工具 | 说明 |
|------|------|
| `target_fetch` | 靶点详情 |
| `disease_fetch` | 疾病详情 |
| `epidemiology_search` | 流行病学检索 |

---

## 三、企业情报（Finance）

### 1. company-credit（14 工具）

| 工具 | 说明 |
|------|------|
| `search_company` | 企业搜索 |
| `registration_information` | 工商注册信息 |
| `shareholder_information` | 股东信息 |
| `main_member` | 主要人员 |
| `core_member` | 核心团队 |
| `financing_information` | 融资信息 |
| `investment_information` | 投资记录 |
| `outbound_investment` | 对外投资 |
| `listing_information` | 上市信息 |
| `ipo_process` | IPO 进程 |
| `qualification_certificate` | 资质证书 |
| `technology_qualification` | 科技资质 |
| `standard_information` | 标准信息 |
| `awards_information` | 获奖信息 |

### 2. company-profile（24 工具）

| 工具 | 说明 |
|------|------|
| `attribute` | 企业属性 |
| `registration_information` | 工商注册 |
| `shareholder_information` | 股东信息 |
| `core_member` | 核心团队 |
| `financing_information` | 融资信息 |
| `listing_information` | 上市信息 |
| `ipo_process` | IPO 进程 |
| `outbound_investment` | 对外投资 |
| `industry_classification` | 行业分类 |
| `qualification_certificate` | 资质证书 |
| `technology_qualification` | 科技资质 |
| `standard_information` | 标准 |
| `awards_information` | 获奖 |
| `patent_simple_bibliography` | 专利简目 |
| `patent_legal_status` | 专利法律状态 |
| `patent_transfer_data` | 专利转移 |
| `patent_license_data` | 专利许可 |
| `patent_pledge_data` | 专利质押 |
| `patent_reexamination` | 专利复审 |
| `patent_valuation` | 专利价值 |
| `enterprise_software_copyright` | 软件著作权 |
| `enterprise_trademark` | 企业商标 |
| `get_company_tech_eval_backtrack_global` | 科技评估回溯 |
| `get_company_tech_eval_indicators_global` | 科技评估指标 |

### 3. company-risk（5 工具）

| 工具 | 说明 |
|------|------|
| `enterprise_indicators` | 企业指标 |
| `enterprise_risk_warning` | 风险预警 |
| `enterprise_valuation` | 企业估值 |
| `enterprise_valuation_full` | 完整估值 |
| `enterprise_valuation_with_indicators` | 带指标估值 |

### 4. company-tags（8 工具）

| 工具 | 说明 |
|------|------|
| `company_attribute` | 企业属性标签 |
| `company_awards` | 获奖标签 |
| `intellectual_property` | 知识产权标签 |
| `standard_development` | 标准制定标签 |
| `technology_label` | 技术标签 |
| `industrial_technology_chain` | 产业技术链 |
| `industry_classification` | 行业分类 |
| `product_technical_classification` | 产品技术分类 |

### 5. global-tech-eval（8 工具）

| 工具 | 说明 |
|------|------|
| `technology_evaluation_global` | 全球科技评估 |
| `technology_indicators_global` | 全球科技指标 |
| `tech_eval_backtrack_global` | 评估回溯 |
| `tech_eval_indicators_global` | 指标回溯 |
| `global_company_group_eval` | 集团穿透评估 |
| `patent_risk_warning` | 专利风险预警 |
| `patent_risk_warning_backtrack` | 风险预警回溯 |
| `patent_risk_warning_trend` | 风险预警趋势 |

### 6. patent-risk（3 工具）

| 工具 | 说明 |
|------|------|
| `patent_risk_trend` | 专利风险趋势 |
| `patent_risk_backtracking` | 风险回溯 |
| `modeling_get_tech_eval_backtracking` | 科技评估回溯建模 |

### 7. tech-diligence（12 工具）

| 工具 | 说明 |
|------|------|
| `company_financing` | 企业融资 |
| `company_industry` | 企业行业 |
| `company_tech_label` | 企业技术标签 |
| `tech_indicators` | 技术指标 |
| `economic_indicators` | 经济指标 |
| `legal_indicators` | 法律指标 |
| `market_indicators` | 市场指标 |
| `strategic_indicators` | 战略指标 |
| `patent_valuation` | 专利价值 |
| `patent_risk_warning` | 专利风险预警 |
| `acquisition_get_group_tech_eval` | 集团科技评估 |
| `acquisition_get_tech_eval_indicators` | 科技评估指标 |

---

## 四、研发创新（R&D-Innovation）

### 1. literature-search（5 工具）

| 工具 | 说明 |
|------|------|
| `search_literature` | 文献检索 |
| `literature_bibliography` | 文献著录 |
| `literature_citation` | 引用信息 |
| `literature_journal` | 期刊信息 |
| `literature_author_affiliation` | 作者机构 |

### 2. patsnap-search（2 工具）

| 工具 | 说明 |
|------|------|
| `patsnap_search` | 专利+文献融合搜索 |
| `patsnap_fetch` | 获取专利/文献详情 |

### 3. patsnap-solution-engine（6 工具）

| 工具 | 说明 |
|------|------|
| `run_triz_innovation_task` | 启动创新攻关任务 |
| `fetch_triz_innovation_task_stream` | 获取创新任务流 |
| `fetch_triz_innovation_solution_detail` | 获取创新方案详情 |
| `run_triz_reduction_task` | 启动降本任务 |
| `fetch_triz_reduction_task_stream` | 获取降本任务流 |
| `fetch_triz_reduction_solution_detail` | 获取降本方案详情 |

### 4. patsnap-triz-case-library（2 工具）

| 工具 | 说明 |
|------|------|
| `search_triz_case` | TRIZ 案例检索 |
| `list_triz_search_terms` | 列出检索术语 |

### 5. report-gen（6 工具）

| 工具 | 说明 |
|------|------|
| `company_report_create` | 企业报告生成 |
| `patent_report_create` | 专利价值报告 |
| `idea_validation_create` | 技术查新报告 |
| `idea_validation_similar` | 相似专利比对 |
| `idea_validation_download` | 报告下载 |
| `pre_patent_evaluation_export` | 专利预评估导出 |

### 6. tech-collab（4 工具）

| 工具 | 说明 |
|------|------|
| `industry_university_research` | 产学研合作分析 |
| `industry_university_research_ipc` | 按 IPC 分析 |
| `industry_university_research_region` | 按地域分析 |
| `company_core_patent` | 企业核心专利 |

---

## 五、工具与其他（Other）

### 1. aact-db（7 工具）

| 工具 | 说明 |
|------|------|
| `list_tables` | 列出数据表 |
| `describe_table` | 表结构描述 |
| `search_columns` | 列搜索 |
| `get_column_values` | 列值获取 |
| `read_query` | SQL 查询 |
| `fetch_rows` | 获取行数据 |
| `database_info` | 数据库信息 |

### 2. chem-ocr（3 工具）

| 工具 | 说明 |
|------|------|
| `recognize_single_molecule` | 单分子结构识别 |
| `recognize_markush_structure` | Markush 结构识别 |
| `recognize_chemical_reaction` | 化学反应识别 |

### 3. chembl（7 工具）

| 工具 | 说明 |
|------|------|
| `chembl_search_molecules` | 分子检索 |
| `chembl_search_targets` | 靶点检索 |
| `chembl_get_drug_info` | 药物信息 |
| `chembl_get_assay` | 实验信息 |
| `chembl_get_bioactivities` | 生物活性 |
| `chembl_dataframe_describe` | 数据表描述 |
| `chembl_dataframe_query` | 数据表查询 |

### 4. clinicaltrialsgov（7 工具）

| 工具 | 说明 |
|------|------|
| `clinicaltrials_search_studies` | 试验搜索 |
| `clinicaltrials_get_study_count` | 试验计数 |
| `clinicaltrials_get_study_record` | 试验记录 |
| `clinicaltrials_get_study_results` | 试验结果 |
| `clinicaltrials_find_eligible` | 入组资格筛选 |
| `clinicaltrials_get_field_definitions` | 字段定义 |
| `clinicaltrials_get_field_values` | 字段值 |

### 5. fda-mcp-server（1 工具）

| 工具 | 说明 |
|------|------|
| `fda_info` | FDA 药品信息 |

### 6. globocan-mcp（2 工具）

| 工具 | 说明 |
|------|------|
| `get_cancer_statistics` | 癌症统计 |
| `get_prostate_cancer_stats` | 前列腺癌统计 |

### 7. mineru（2 工具）

| 工具 | 说明 |
|------|------|
| `parse_documents` | PDF/图片 OCR 提取 |
| `get_ocr_languages` | 获取支持语言 |

### 8. ncbi-mcp（4 工具）

| 工具 | 说明 |
|------|------|
| `ESearch` | NCBI 搜索 |
| `EFetch` | NCBI 获取 |
| `EInfo` | 数据库信息 |
| `ESummary` | 摘要 |

### 9. nccn-guidelines（3 工具）

| 工具 | 说明 |
|------|------|
| `get_index` | 指南索引 |
| `extract_content` | 内容提取 |
| `download_pdf` | PDF 下载 |

### 10. otp-mcp（5 工具）

| 工具 | 说明 |
|------|------|
| `search_entities` | 实体搜索 |
| `query_open_targets_graphql` | GraphQL 查询 |
| `batch_query_open_targets_graphql` | 批量查询 |
| `get_open_targets_graphql_schema` | 获取 Schema |
| `get_type_dependencies` | 类型依赖 |

### 11. pubmed（10 工具）

| 工具 | 说明 |
|------|------|
| `search` | PubMed 搜索 |
| `get_article` | 获取文章 |
| `get_article_full_text` | 获取全文 |
| `europepmc_search` | Europe PMC 搜索 |
| `find_related_articles` | 相关文章 |
| `lookup_citation` | 引用查找 |
| `format_citations` | 引用格式化 |
| `convert_ids` | ID 转换 |
| `get_lookup_mesh` | MESH 查找 |
| `spell_check` | 拼写检查 |

### 12. rdkit（7 工具）

| 工具 | 说明 |
|------|------|
| `get_smiles_from_name` | 名称→SMILES |
| `smiles_to_image` | SMILES→图片 |
| `get_molecule_descriptors_from_smiles` | 分子描述符 |
| `get_weight_from_smiles` | 分子量 |
| `search_substructure` | 子结构搜索 |
| `find_maximum_common_substructure` | 最大公共子结构 |
| `visualize_chemical_reaction` | 化学反应可视化 |

### 13. uniprot-mcp（5 工具）

| 工具 | 说明 |
|------|------|
| `search_uniprot` | UniProt 搜索 |
| `fetch_entry` | 条目获取 |
| `fetch_entry_flatfile` | Flatfile 格式 |
| `get_sequence` | 序列获取 |
| `map_ids` | ID 映射 |

### 14. who-mcp-server（1 工具）

| 工具 | 说明 |
|------|------|
| `who-health` | WHO 健康数据 |

---
