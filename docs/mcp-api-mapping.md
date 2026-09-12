# 智慧芽 MCP Tool → API 接口映射表

本表将 MCP 工具映射到智慧芽开放平台 API 接口，帮助开发者理解 MCP 工具底层的 API 调用关系。

> 完整 API 索引见 [zhihuiya-api-index.md](./zhihuiya-api-index.md)（372 条接口）。

## 一、IP 智能领域

### core-patents（核心专利数据）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `bibliography` | 著录项目 | P012 | 专利著录项目数据 |
| `claims` | 权利要求 | P018 | 权利要求全文 |
| `abstract_image` | 摘要附图 | P021 | 摘要附图获取 |
| `fulltext_image` | 全文附图 | P042 | 全文附图获取 |
| `legal_data` | 法律状态 | P013 | 法律状态数据 |
| `family` | 专利家族 | P014 | 专利家族信息 |
| `forward_citation` | 专利被引用 | P015 | 前向引证数据 |
| `pdf` | PDF全文 | P020 | PDF 全文下载 |
| `search_patents` | 检索式检索专利 | P002 | 专利检索 |
| `customs_data` | 海关备案 | — | 海关备案数据 |
| `license_data` | 许可数据 | — | 专利许可信息 |
| `pledge_data` | 质押数据 | — | 专利质押信息 |
| `reexamination_invalidation` | 复审无效 | — | 复审无效记录 |
| `award_data` | 获奖数据 | — | 专利获奖信息 |
| `description` | 说明书 | — | 说明书全文 |
| `description_translated` | 说明书翻译 | — | 说明书中文翻译 |
| `claim_translated` | 权利要求翻译 | — | 权利要求中文翻译 |
| `abstract_translated` | 摘要翻译 | — | 摘要中文翻译 |
| `transfer_data` | 转让数据 | — | 专利转让信息 |

### patent-briefing（专利速览简报）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `bibliography` | 著录项目 | P012 | 著录项目速览 |
| `claims` | 权利要求 | P018 | 权利要求速览 |
| `legal_status` | 法律状态 | P013/P041 | 法律状态速览 |
| `family` | 专利家族 | P014 | 家族信息速览 |
| `search_patents` | 检索式检索专利 | P002 | 专利检索 |
| `abstract_image` | 摘要附图 | P021 | 摘要附图 |
| `abstract_translated` | 摘要翻译 | — | 摘要翻译 |
| `claim_translated` | 权利要求翻译 | — | 权利要求翻译 |
| `description` | 说明书 | — | 说明书速览 |
| `description_translated` | 说明书翻译 | — | 说明书翻译 |
| `tech_summary` | — | — | 技术三要素（MCP 专属） |
| `intelligent_image` | 全文附图 | P042 | 智能附图 |

### patent-landscape（专利全景分析）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `search_patents_v3` | 检索式检索专利 | P002 | V3 检索 |
| `search_patents_with_detail` | 检索式检索并筛选 | P003 | 检索+详情 |
| `search_patents_facet` | — | — | 分面检索（MCP 专属） |
| `search_patents_statistics` | 检索式统计专利量 | P001 | 统计量 |
| `detail` | 著录项目 | P012 | 专利详情 |
| `detail_aggregation` | — | — | 聚合统计（MCP 专属） |
| `trend` | — | — | 趋势分析（MCP 专属） |
| `technology_constitute` | — | — | 技术构成（MCP 专属） |
| `applicant_rank` | — | — | 申请人排名（MCP 专属） |
| `domain_map` | — | — | 技术地图（MCP 专属） |
| `technology_life_cycle` | — | — | 技术生命周期（MCP 专属） |

### patsnap-ip-searching（查新/FTO 检索）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `novelty_search` | 查新检索-创建查询 | AI35-2 | 查新检索 |
| `fto_review` | 防侵权检索-启动FTO检索 | AI66-4 | FTO 检索 |
| `design_fto` | 外观防侵权检索-提交任务 | AI39-1 | 外观 FTO |
| `upload_image` | 上传图片获取检索URL | P010 | 图片上传 |
| `get_task` | — | — | 任务状态查询（MCP 专属） |

### novelty-search-lite（查新检索轻量版）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `novelty_lite_search` | 查新检索-创建任务 | AI35-1 | 查新提交 |
| `novelty_lite_semantic_search` | 语义检索相似专利 | P008 | 语义检索 |
| `novelty_lite_boolean_search` | 检索式检索专利 | P002 | 布尔检索 |
| `novelty_lite_paper_search` | — | — | 文献检索（MCP 专属） |
| `novelty_feature_extract` | 查新检索-提取技术特征 | AI35-4 | 技术特征提取 |
| `novelty_keywords_extract` | 查新检索-提取检索要素 | AI35-6 | 检索要素提取 |
| `novelty_feature_comparison` | — | — | 特征对比（MCP 专属） |
| `novelty_summary` | — | — | 总结（MCP 专属） |
| `novelty_review_with_suggestions` | — | — | 审查建议（MCP 专属） |
| `novelty_lite_report_generate` | 查新检索-创建报告 | AI35-10 | 报告生成 |
| `novelty_lite_website_search` | — | — | 网页检索（MCP 专属） |

### document-processing（文档解析与翻译）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `documents_parsing` | OCR识别 | AI60 | 文档解析 |
| `translation_text` | AI翻译 | AI61 | 文本翻译 |
| `translation_docx` | AI翻译 | AI61 | Word 文档翻译 |

### patent-status（专利法律状态）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `legal_data` | 法律状态 | P013 | 法律状态 |
| `fee_info` | — | — | 年费信息（MCP 专属） |
| `get_sep_data` | 通信标准必要专利SEP | T001 | SEP 数据 |
| `litigation_data` | — | — | 诉讼数据（MCP 专属） |
| `overseas_patent_documents` | — | — | 海外审查文件（MCP 专属） |
| `re_examination_data` | — | — | 复审数据（MCP 专属） |
| `transfer_data` | — | — | 转让数据（MCP 专属） |
| `license_data` | — | — | 许可数据（MCP 专属） |
| `pledge_data` | — | — | 质押数据（MCP 专属） |
| `award_data` | — | — | 获奖数据（MCP 专属） |
| `customs_data` | — | — | 海关备案（MCP 专属） |
| `unified_patent_court_status` | — | — | UPC 状态（MCP 专属） |

### patent-analysis（专利聚合统计）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `aggregate_patents` | 检索式统计专利量 | P001 | 聚合统计 |
| `mine_patent_text` | — | — | 文本挖掘（MCP 专属） |

### patent-mining（专利技术挖掘）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `tech_problem_benefit_summary` | 专利发明点总结 | AI31 | 技术问题-手段-效果 |
| `technology_topic` | — | — | 技术主题（MCP 专属） |
| `application_domain` | — | — | 应用领域（MCP 专属） |
| `classification_description` | 分类号助手查询 | P071 | 分类号说明 |
| `enhanced_data` | — | — | 增强数据（MCP 专属） |
| `material_ontology` | — | — | 材料本体（MCP 专属） |
| `material_substance` | — | — | 材料物质（MCP 专属） |
| `seic_classification` | — | — | 战新分类（MCP 专属） |
| `intelligent_attached_image` | 全文附图 | P042 | 智能附图 |

### patent-dispute（专利纠纷）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `search_patents` | 检索式检索专利 | P002 | 专利检索 |
| `legal_status` | 法律状态 | P013/P041 | 法律状态 |
| `reexam_invalidation` | — | — | 复审无效（MCP 专属） |
| `valuation_get_patent_valuation` | — | — | 专利估值（MCP 专属） |
| 其余工具同 core-patents | — | — | — |

### patent-visual（专利可视化）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `trends` | — | — | 趋势图（MCP 专属） |
| `word_cloud` | — | — | 词云（MCP 专属） |
| `applicant_ranking` | — | — | 申请人排名（MCP 专属） |
| `portfolio_value` | — | — | 组合价值（MCP 专属） |
| `most_cited` | 专利被引用 | P015 | 最常被引（MCP 专属） |
| `most_asserted` | — | — | 最常主张（MCP 专属） |

### patent-value（专利价值评估）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `valuation` | — | — | 价值评分（MCP 专属） |
| `tech_innovation_indicators` | — | — | 技术创新指标 |
| `legal_indicators` | — | — | 法律指标 |
| `market_indicators` | — | — | 市场指标 |
| `strategic_indicators` | — | — | 战略指标 |
| `ability_indicators` | — | — | 能力指标 |
| `economic_indicators` | — | — | 经济指标 |

### landscape-projects（全景分析项目）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `landscape_job_create` | — | — | 创建分析任务 |
| `landscape_job_status` | — | — | 任务状态 |
| `landscape_facet_list` | — | — | 分面列表 |
| `landscape_facet_detail` | — | — | 分面详情 |
| `landscape_patents` | — | — | 专利列表 |

### intangible-assets（无形资产）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `enterprise_trademark` | — | — | 商标信息 |
| `software_copyright` | — | — | 软件著作权 |
| `new_plant_variety` | — | — | 植物新品种 |
| `ic_design` | — | — | 集成电路布图 |
| `potential_buyer` | — | — | 潜在买家 |

### s-telecom-mcp-tools（通信标准检索）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `search_standards` | — | — | 标准检索 |
| `fetch_standard_section` | — | — | 标准章节 |
| `search_tdocs` | — | — | TDoc 检索 |
| `fetch_tdocs` | — | — | TDoc 详情 |

### s-telecom-mcp-tools-sep（通信 SEP 分析）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `standard_claim_charting` | 通信标准必要专利SEP | T001 | SEP 对标分析 |

### patsnap-analytics（生命周期）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `fetch_patent_lifecycle` | — | — | 专利生命周期事件 |

### patsnap-web-search（网页搜索）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `web_search` | — | — | 实时网页搜索 |

### patsnap-workspace（工作空间）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `list_workspace_spaces` | — | — | 工作空间列表 |
| `list_workspace_folders` | — | — | 目录列表 |
| `list_workspace_fields` | — | — | 字段列表 |
| `get_workspace_patents` | — | — | 目录内专利 |
| `get_workspace_annotations` | — | — | 标注信息 |

### design-fto-search-mcp（外观 FTO）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `create_image_upload_url` | 上传图片获取检索URL | P010 | 图片上传 |
| `submit_workflow` | 外观防侵权检索-提交完整FTO工作流 | AI39-1 | 工作流提交 |
| `get_task_status` | — | — | 任务状态 |
| `get_stage_result` | — | — | 阶段结果 |

### ip-courses（知识产权课程）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `course_list` | — | — | 课程列表 |
| `course_details` | — | — | 课程详情 |
| `course_courseware` | — | — | 课件下载 |

---

## 二、生命科学领域

### pharma-intelligence（医药情报终端）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `ls_patent_search` | 检索式检索专利 | P002 | 专利实体检索 |
| `ls_patent_fetch` | 著录项目 | P012 | 专利详情 |
| `ls_clinical_trial_search` | — | — | 临床试验检索 |
| `ls_clinical_trial_fetch` | — | — | 临床试验详情 |
| `ls_drug_search` | — | — | 药物检索 |
| `ls_drug_fetch` | — | — | 药物详情 |
| `ls_drug_milestone_fetch` | — | — | 药物里程碑 |
| `ls_target_fetch` | — | — | 靶点详情 |
| `ls_disease_fetch` | — | — | 疾病详情 |
| `ls_paper_search` | — | — | 文献检索 |
| `ls_paper_fetch` | — | — | 文献详情 |
| `ls_drug_deal_search` | — | — | 交易检索 |
| `ls_drug_deal_fetch` | — | — | 交易详情 |
| `ls_organization_fetch` | — | — | 组织详情 |
| `ls_organization_pipeline_fetch` | — | — | 组织管线 |
| `ls_news_fetch` | — | — | 新闻详情 |
| `ls_web_search` | — | — | 网页搜索 |
| `ls_ner_nor_normalize` | 药物DDT抽取 | AI01 | 实体识别 |
| `ls_clinical_guideline_vector_search` | — | — | 临床指南语义检索 |
| `ls_clinical_trial_vector_search` | — | — | 临床试验语义检索 |
| `ls_drug_vector_search` | — | — | 药物语义检索 |
| `ls_epidemiology_vector_search` | — | — | 流行病语义检索 |
| `ls_fda_label_vector_search` | — | — | FDA说明书语义检索 |
| `ls_financial_report_vector_search` | — | — | 财报语义检索 |
| `ls_news_vector_search` | — | — | 新闻语义检索 |
| `ls_paper_vector_search` | — | — | 文献语义检索 |
| `ls_patent_vector_search` | — | — | 专利语义检索 |
| `ls_translational_medicine_fetch` | — | — | 转化医学详情 |
| `ls_translational_medicine_search` | — | — | 转化医学检索 |

### drug-asset（药物资产情报）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `drug_search` | — | — | 药物检索 |
| `drug_fetch` | — | — | 药物详情 |
| `drug_milestone_fetch` | — | — | 药物里程碑 |

### clinical-trials（临床试验检索）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `clinical_trial_search` | — | — | 临床试验检索 |
| `clinical_trial_fetch` | — | — | 临床试验详情 |
| `clinical_trial_result_search` | — | — | 临床结果检索 |
| `clinical_trial_result_fetch` | — | — | 临床结果详情 |

### company-deal-intelligence（企业交易情报）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `drug_deal_search` | — | — | 交易检索 |
| `drug_deal_fetch` | — | — | 交易详情 |
| `financial_report_search` | — | — | 财报检索 |
| `organization_fetch` | — | — | 组织详情 |
| `organization_pipeline_fetch` | — | — | 组织管线 |

### target-disease（靶点与疾病）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `target_fetch` | — | — | 靶点画像 |
| `disease_fetch` | — | — | 疾病画像 |
| `epidemiology_search` | — | — | 流行病学证据 |

### regulatory-guidelines（监管指南）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `clinical_guideline_search` | — | — | 临床指南检索 |
| `fda_label_search` | — | — | FDA说明书检索 |

### current-awareness（行业动态追踪）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `news_search` | — | — | 新闻检索 |
| `news_fetch` | — | — | 新闻详情 |

### chemical-molecular（化学分子智能平台）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `ls_structure_search` | — | — | 化合物搜索 |
| `ls_structure_fetch` | — | — | 结构详情 |
| `ls_sar_submit` | 提交SAR解析任务 | — | SAR 提取 |
| `ls_sar_fetch` | 获取SAR文件详情 | — | SAR 详情 |
| `ls_admet_predict` | — | — | ADMET 预测 |
| `ls_chemical_mcs_analyze` | — | — | 最大公共子结构 |
| `ls_patent_structure_fetch` | — | — | 专利结构提取 |

### sar-extraction（SAR 深度解析）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `sar_submit` | 提交SAR解析任务 | — | SAR 任务提交 |
| `sar_fetch` | 获取SAR文件详情 | — | SAR 结果获取 |

### scientific-translational-evidence（科学文献与转化）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `translational_medicine_search` | — | — | 转化医学检索 |
| `translational_medicine_fetch` | — | — | 转化医学详情 |

### biology-modality（生物序列智能平台）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `ls_sequence_search_submit` | — | — | 序列检索提交 |
| `ls_sequence_search_check_status` | — | — | 检索状态 |
| `ls_sequence_search_get_results` | — | — | 检索结果 |
| `ls_sequence_fetch` | — | — | 序列详情 |
| `ls_sequence_alignment` | — | — | 序列比对 |
| `ls_patent_sequence_fetch` | — | — | 专利序列提取 |
| `ls_antibody_antigen_search` | — | — | 抗原-抗体检索 |
| `ls_modification_search_submit` | — | — | 翻译后修饰检索 |

---

## 三、企业情报领域

### company-credit（企业信用档案）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `search_company` | — | — | 企业搜索 |
| `registration_information` | — | — | 工商信息 |
| `shareholder_information` | — | — | 股东信息 |
| `core_member` | — | — | 核心团队 |
| `financing_information` | — | — | 融资信息 |
| `listing_information` | — | — | 上市信息 |
| `ipo_process` | — | — | IPO 进程 |
| `investment_information` | — | — | 投资信息 |
| `outbound_investment` | — | — | 对外投资 |
| `qualification_certificate` | — | — | 资质证书 |
| `technology_qualification` | — | — | 科技资质 |
| `standard_information` | — | — | 标准信息 |
| `awards_information` | — | — | 获奖信息 |
| `main_member` | — | — | 主要成员 |

### company-profile（企业科技档案）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `attribute` | — | — | 企业属性 |
| `patent_simple_bibliography` | 著录项目 | P012 | 专利著录 |
| `patent_legal_status` | 法律状态 | P013/P041 | 专利法律状态 |
| `patent_valuation` | — | — | 专利估值 |
| `patent_transfer_data` | — | — | 专利转让 |
| `patent_license_data` | — | — | 专利许可 |
| `patent_pledge_data` | — | — | 专利质押 |
| `patent_reexamination` | — | — | 专利复审 |
| `enterprise_software_copyright` | — | — | 软件著作权 |
| `enterprise_trademark` | — | — | 商标 |
| `industry_classification` | — | — | 行业分类 |
| 其余工具同 company-credit | — | — | — |

### company-risk（企业风险评估）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `enterprise_indicators` | — | — | 企业指标 |
| `enterprise_risk_warning` | — | — | 风险预警 |
| `enterprise_valuation` | — | — | 企业估值 |
| `enterprise_valuation_full` | — | — | 完整估值 |
| `enterprise_valuation_with_indicators` | — | — | 估值+指标 |

### company-tags（企业标签画像）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `company_attribute` | — | — | 企业属性 |
| `company_awards` | — | — | 科技认定 |
| `industrial_technology_chain` | — | — | 产业技术链 |
| `industry_classification` | — | — | 行业分类 |
| `intellectual_property` | — | — | 知识产权 |
| `product_technology_classification` | — | — | 产品技术分类 |
| `standard_development` | — | — | 标准制定 |
| `technology_label` | — | — | 技术标签 |

### global-tech-eval（全球科技评估）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `technology_evaluation_global` | — | — | 全球科技评估 |
| `technology_indicators_global` | — | — | 全球指标 |
| `global_company_group_eval` | — | — | 集团穿透 |
| `patent_risk_warning` | — | — | 专利风险预警 |
| `patent_risk_warning_trend` | — | — | 风险趋势 |
| `tech_eval_backtrack_global` | — | — | 历史回溯 |
| `tech_eval_indicators_global` | — | — | 指标回溯 |

### patent-risk（专利风险趋势）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `patent_risk_trend` | — | — | 风险趋势 |
| `patent_risk_backtracking` | — | — | 历史回溯 |
| `modeling_get_tech_eval_backtracking` | — | — | 建模回溯 |

### tech-diligence（科创尽调）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `acquisition_get_group_tech_eval` | — | — | 集团评估 |
| `acquisition_get_tech_eval_indicators` | — | — | 指标评估 |
| `company_financing` | — | — | 融资信息 |
| `company_industry` | — | — | 行业信息 |
| `company_tech_label` | — | — | 技术标签 |
| `economic_indicators` | — | — | 经济指标 |
| `legal_indicators` | — | — | 法律指标 |
| `market_indicators` | — | — | 市场指标 |
| `patent_risk_warning` | — | — | 专利风险预警 |
| `patent_valuation` | — | — | 专利估值 |
| `strategic_indicators` | — | — | 战略指标 |
| `tech_indicators` | — | — | 技术指标 |

---

## 四、研发创新领域

### patsnap-search（融合检索）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `patsnap_search` | 检索式检索专利 | P002 | 专利+文献融合搜索 |
| `patsnap_fetch` | 著录项目 | P012 | 专利/文献详情 |

### literature-search（文献检索）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `search_literature` | — | — | 文献检索 |
| `literature_bibliography` | — | — | 文献著录 |
| `literature_citation` | — | — | 引用信息 |
| `literature_journal` | — | — | 期刊信息 |
| `literature_author_affiliation` | — | — | 作者机构 |

### patsnap-solution-engine（TRIZ 创新方案）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `run_triz_innovation_task` | 技术方案探索-创建任务 | AI33-1 | 创新攻关 |
| `fetch_triz_innovation_task_stream` | — | — | 任务流 |
| `fetch_triz_innovation_solution_detail` | — | — | 方案详情 |
| `run_triz_reduction_task` | — | — | 降本任务 |
| `fetch_triz_reduction_task_stream` | — | — | 降本流 |
| `fetch_triz_reduction_solution_detail` | — | — | 降本方案 |

### patsnap-triz-case-library（TRIZ 案例库）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `search_triz_case` | — | — | 案例检索 |
| `list_triz_search_terms` | — | — | 检索词列表 |

### report-gen（报告生成）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `company_report_create` | — | — | 企业报告 |
| `patent_report_create` | — | — | 专利价值报告 |
| `idea_validation_create` | — | — | 技术想法查新 |
| `idea_validation_download` | — | — | 查新下载 |
| `idea_validation_similar` | 相似专利检索与比对 | AI30 | 相似比对 |
| `pre_patent_evaluation_export` | — | — | 预评估导出 |

### tech-collab（产学研合作）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `industry_university_research` | — | — | 产学研分析 |
| `industry_university_research_ipc` | — | — | IPC 合作 |
| `industry_university_research_region` | — | — | 区域合作 |
| `company_core_patent` | — | — | 核心专利 |

---

## 五、工具与其他

### mineru（OCR 提取）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `parse_documents` | OCR识别 | AI60 | PDF/图片 OCR |
| `get_ocr_languages` | — | — | 支持语言列表 |

### chem-ocr（化学结构识别）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `recognize_single_molecule` | — | — | 单分子识别 |
| `recognize_markush_structure` | — | — | Markush 识别 |
| `recognize_chemical_reaction` | — | — | 化学反应识别 |

### rdkit（化学信息学）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `get_smiles_from_name` | — | — | 名称→SMILES |
| `get_molecule_descriptors_from_smiles` | — | — | 分子描述符 |
| `get_weight_from_smiles` | — | — | 分子量 |
| `smiles_to_image` | — | — | SMILES→图片 |
| `find_maximum_common_substructure` | — | — | 最大公共子结构 |
| `search_substructure` | — | — | 子结构搜索 |
| `visualize_chemical_reaction` | — | — | 反应可视化 |

### pubmed（文献检索）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `search` | — | — | PubMed 检索 |
| `get_article` | — | — | 文章详情 |
| `get_article_full_text` | — | — | 全文获取 |
| `europepmc_search` | — | — | Europe PMC 检索 |
| `find_related_articles` | — | — | 相关文章 |
| `lookup_citation` | — | — | 引用查找 |
| `convert_ids` | — | — | ID 转换 |
| `format_citations` | — | — | 引用格式化 |
| `get_lookup_mesh` | — | — | MESH 查找 |
| `spell_check` | — | — | 拼写检查 |

### ncbi-mcp（NCBI 检索）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `ESearch` | — | — | NCBI 检索 |
| `EFetch` | — | — | NCBI 获取 |
| `EInfo` | — | — | 数据库信息 |
| `ESummary` | — | — | 摘要 |

### chembl（ChEMBL 数据库）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `chembl_search_molecules` | — | — | 分子检索 |
| `chembl_search_targets` | — | — | 靶点检索 |
| `chembl_get_bioactivities` | — | — | 生物活性 |
| `chembl_get_assay` | — | — | 实验信息 |
| `chembl_get_drug_info` | — | — | 药物信息 |
| `chembl_dataframe_query` | — | — | 数据查询 |
| `chembl_dataframe_describe` | — | — | 数据描述 |

### uniprot-mcp（UniProt 蛋白质数据库）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `search_uniprot` | — | — | UniProt 检索 |
| `fetch_entry` | — | — | 条目获取 |
| `fetch_entry_flatfile` | — | — | Flat file |
| `get_sequence` | — | — | 序列获取 |
| `map_ids` | — | — | ID 映射 |

### otp-mcp（Open Targets）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `search_entities` | — | — | 实体搜索 |
| `query_open_targets_graphql` | — | — | GraphQL 查询 |
| `batch_query_open_targets_graphql` | — | — | 批量查询 |
| `get_open_targets_graphql_schema` | — | — | Schema 获取 |
| `get_type_dependencies` | — | — | 类型依赖 |

### aact-db（AACT 临床试验数据库）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `read_query` | — | — | SQL 查询 |
| `fetch_rows` | — | — | 行获取 |
| `search_columns` | — | — | 列搜索 |
| `list_tables` | — | — | 表列表 |
| `describe_table` | — | — | 表描述 |
| `get_column_values` | — | — | 列值 |
| `database_info` | — | — | 数据库信息 |

### clinicaltrialsgov（ClinicalTrials.gov）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `clinicaltrials_search_studies` | — | — | 试验检索 |
| `clinicaltrials_find_eligible` | — | — | 入组筛选 |
| `clinicaltrials_get_study_record` | — | — | 试验记录 |
| `clinicaltrials_get_study_results` | — | — | 试验结果 |
| `clinicaltrials_get_study_count` | — | — | 试验计数 |
| `clinicaltrials_get_field_definitions` | — | — | 字段定义 |
| `clinicaltrials_get_field_values` | — | — | 字段值 |

### fda-mcp-server（FDA 信息）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `fda_info` | — | — | FDA 信息查询 |

### globocan-mcp（全球癌症统计）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `get_cancer_statistics` | — | — | 癌症统计 |
| `get_prostate_cancer_stats` | — | — | 前列腺癌统计 |

### who-mcp-server（WHO 卫生数据）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `who-health` | — | — | WHO 卫生数据 |

### nccn-guidelines（NCCN 指南）

| MCP 工具 | 对应 API 接口 | API 号 | 说明 |
|----------|--------------|--------|------|
| `get_index` | — | — | 指南索引 |
| `download_pdf` | — | — | PDF 下载 |
| `extract_content` | — | — | 内容提取 |
