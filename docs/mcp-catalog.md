# MCP 服务目录（全量 tool 明细）

> 本文件由 `scripts/build_docs.py` 从 `index.json`（机读真相源）自动生成，请勿手改。结构与内容请在 `index.json` 中修改后重跑脚本。

> 数据版本 v0.6.0 · 生成时间 2026-11-08T08:46:13Z · 数据源：open.zhihuiya.com（免登录）

共 **50** 个原生 MCP / **411** 个 tool。每个 tool 的入参 schema 与 API 对应关系以 `index.json` 为准。

## 概览

| 能力域 | 主干 | MCP 数 | tool 数 |
|--------|------|--------|---------|
| 专利检索与分析 | `core-patents` | 23 | 218 |
| 医药情报 | `pharma-intelligence` | 11 | 78 |
| 金融 | `company-profile` | 8 | 80 |
| 材料 | `materials-search-mcp` | 2 | 3 |
| 研发 | `patsnap-search` | 6 | 32 |

## 专利检索与分析（`patent`，23 个 MCP）

### `core-patents` · 🌳 主干

- **名称**：全球核心专利库 / Global Core Patent Database
- **官方分类**：`Ip-Intelligence` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：20 · **上下文权重**：`high`
- **MCP 地址**：`https://connect.zhihuiya.com/1458a4/mcp`
- **能力**：面向高频专利工作场景的核心专利数据工具。可查看检索结果、全文附图、法律状态、许可、转移、质押、复审无效等关键信息，帮助团队快速完成专利核查与事实查证。适合用于日常检索、案件研究、法务支持和运营分析。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `forward_citation` | 用于获取专利被引用-v3相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, patent_number | — ·待确认 |
| `transfer_data` | 用于获取专利转移相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, patent_number | P029 ·高 |
| `reexamination_invalidation` | 用于获取复审无效相关信息，便于判断专利状态变化、专利稳定性及潜在法律风险。 | patent_id, patent_number | P027 ·高 |
| `pledge_data` | 可以通过输入patent_id或patent_number查询具体某条专利的质押信息。包含：质押登记号、质押保全类型、质押生效日期、质押人、出质人。 | patent_id, patent_number | — ·待确认 |
| `pdf` | 用于获取PDF全文相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | patent_id, patent_number | P020 ·高 |
| `license_data` | 用于获取专利许可相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, patent_number | P028 ·高 |
| `legal_data` | 用于获取法律详情相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | patent_id, patent_number | P026 ·高 |
| `fulltext_image` | 用于获取全文附图相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | patent_id, offset, patent_number, limit | P042 ·高 |
| `description_translated` | 用于获取说明书翻译相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | patent_id, replace_by_related, patent_number, **lang** | P045 ·高 |
| `customs_data` | 用于获取海关备案相关信息，便于判断专利状态变化、专利稳定性及潜在法律风险。 | patent_id, patent_number | P031 ·高 |
| `claim_translated` | 用于获取权利要求翻译相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | patent_id, replace_by_related, patent_number, **lang** | P044 ·高 |
| `award_data` | 用于获取专利奖相关数据，便于了解主体或专利的荣誉情况和外部认可度。 | patent_id, patent_number | P032 ·高 |
| `abstract_translated` | 用于获取摘要翻译相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, replace_by_related, patent_number, **lang** | P043 ·高 |
| `family` | 用于获取专利家族信息，便于查看同族关系、地域布局和家族覆盖范围。 | patent_id, patent_number | P014 ·低 |
| `abstract_image` | 用于获取摘要附图相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, patent_number | P021 ·高 |
| `description` | 用于获取说明书相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | patent_id, replace_by_related, patent_number | P019 ·高 |
| `get_patent_legal_status` | 用于获取简单法律状态相关信息，便于判断专利状态变化、专利稳定性及潜在法律风险。 | patent_id, patent_number | P041 ·高 |
| `claims` | 用于获取权利要求相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | patent_id, replace_by_related, patent_number | P018 ·高 |
| `bibliography` | 用于获取著录项目相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | patent_id, patent_number | P012 ·高 |
| `search_patents` | 用于检索式检索专利，返回匹配结果，便于快速筛选、比对和继续分析。 | collapse_order_authority, offset, sort_field, limit, stemming, collapse_order, sort_order, **query_text**, collapse_type, collapse_by | P002 ·低 |

### `design-fto-search-mcp` · 分支

- **名称**：外观专利侵权风险检索 / Design Patent Infringement Search
- **官方分类**：`Ip-Intelligence` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：4 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/937ec6/mcp`
- **能力**：AI 驱动的跨境电商外观专利侵权风险检索系统。提供产品图片 URL 或图片 base64 后，系统会自动执行完整 FTO 流程：线稿转换、专利图像检索、AI 重排与风险分析、报告生成，帮助卖家在上架前识别潜在相似外观专利并获取结构化风险评估。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `create_image_upload_url` | 返回临时 PUT 上传地址。客户端将图片通过 HTTP PUT 上传至该地址，上传成功后把返回的图片 URL 传给 submit_workflow。该工具只申请上传地址，不接收图片二进制或大段 base64。 | content_type, file_extension, expire_seconds | P010 ·低 |
| `submit_workflow` | 提交完整 FTO 工作流任务。url 与 target_image_base64 至少提供一个，同时提供时优先使用 url。task_id 由服务端自动生成，提交成功后使用 get_task_status 轮询状态，并使 | country, loc_items, target_image_base64, apply_end_time, apply_start_time, title, simple_legal_status, url | AI39-1 ·低 |
| `get_stage_result` | 获取指定 Stage 的完整执行结果。最终报告请使用 stage=generate_report。generate_report 完成后，结果中可能包含 report_export.download_url 和 repo | **stage**, **task_id**, image_mode | AI39-3 ·中 |
| `get_task_status` | 查询工作流任务状态。轻量返回任务整体状态和各 Stage 摘要，不返回大体积 result_data，适合轮询。 | **task_id** | — ·工作流不可推断 |

### `document-processing` · 分支

- **名称**：文档处理 / Document Processing
- **官方分类**：`Ip-Intelligence` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：4 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/8fe1eb/logic-mcp`
- **能力**：文档解析（Layout/OCR）与专利文本翻译。支持图片、PDF、Office 文档解析，以及 18 种语言的专利文本流式互译（SSE）。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `translation_docx_status` | 按 job_id 查询一次 DOCX 翻译任务状态，立即返回，不等待、不轮询。在 translation_docx 异步提交后调用。每次返回当前状态（queued / working / ready / delivere | **job_id** | — ·工作流不可推断 |
| `translation_docx` | 将中文 DOCX 专利文档整篇翻译为英文。调用时提供源文件的公网 HTTPS URL，可选提供以 .docx 结尾的文件名；调用完成后返回翻译结果和译文 DOCX 下载地址。译文保留原文档版式与图片。文件 URL 仅支持 | **file_url**, filename | AI61 ·低 |
| `documents_parsing` | 对文档执行完整解析（Layout + OCR），返回结构化结果与 Markdown 汇总。当用户上传图片、PDF 或 Office 文件并需要提取正文与版面结构时使用。 | **file**, output_format | — ·工作流不可推断 |
| `translation_text` | 流式翻译专利文本。以 SSE（text/event-stream）滑动窗口顺序翻译，更强调整篇上下文一致性。适用于权利要求、说明书、摘要等。源语言与目标语言须不同，支持 18 种语言代码。 | **sourceLanguageCode**, **content**, **targetLanguageCode** | AI61 ·低 |

### `drafting` · 分支

- **名称**：专利撰写助手 / Patent Drafting MCP
- **官方分类**：`Ip-Intelligence` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：18 · **上下文权重**：`high`
- **MCP 地址**：`https://connect.zhihuiya.com/145d9b/mcp`
- **能力**：提供中国专利撰写的项目、附件解析、权利要求、说明书章节和单幅附图生成及标引能力。输出须经技术复核。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `draft_protection_points` | 从技术交底中提炼核心及次要发明点，形成保护点分析。 | **project_id**, output_language, **text** | — ·工作流不可推断 |
| `project_create` | 创建专利撰写项目，用于组织撰写材料与生成内容。 | conversation_summary, idempotency_key, **title** | — ·工作流不可推断 |
| `plan_drawing_description` | 依据技术方案和权利要求规划附图及其说明。 | **project_id**, output_language, **text** | — ·工作流不可推断 |
| `label_figure_from_draft` | 按专利初稿中整理的标记要求标引一幅已有图片，保持原图结构。 | **figure**, size, output_format, **project_id**, **file_id**, patent_office | — ·工作流不可推断 |
| `label_figure_from_description` | 按附图说明为一幅已有图片添加或修正附图标记，保持原图结构。 | **figure**, size, output_format, **project_id**, **file_id**, patent_office | — ·工作流不可推断 |
| `generate_figure_from_draft` | 按专利初稿中整理的图示内容生成一幅黑白线条专利附图。 | **figure**, size, output_format, **project_id**, file_id, patent_office, figure_category | — ·工作流不可推断 |
| `generate_figure_from_description` | 按附图说明生成一幅黑白线条专利附图。 | **figure**, size, output_format, **project_id**, file_id, patent_office, figure_category | — ·工作流不可推断 |
| `draft_title` | 根据权利要求或技术交底拟定发明名称。 | **project_id**, output_language, **text** | — ·工作流不可推断 |
| `draft_summary` | 撰写发明内容，包括技术问题、技术方案及有益效果。 | **project_id**, output_language, **text** | — ·工作流不可推断 |
| `attachment_complete` | 确认已直传的附件，校验文件并关联项目、启动 OCR。 重复确认不会重复入库或重启 OCR。 | **project_id**, **attachment_id**, wait_seconds | — ·工作流不可推断 |
| `draft_embodiments` | 根据技术材料撰写具体实施方式。 | **project_id**, output_language, **text**, technical_fields | — ·工作流不可推断 |
| `draft_claim_tree` | 根据技术交底规划独立权利要求及其从属层级。 仅在用户明确要求生成或查看权利要求树时使用。 | **project_id**, output_language, **text**, tree_scope | — ·工作流不可推断 |
| `draft_claim_set` | 根据技术材料撰写一套权利要求。 | **project_id**, output_language, **text**, technical_fields | — ·工作流不可推断 |
| `draft_background` | 根据技术交底撰写背景技术。 | **project_id**, output_language, **text** | — ·工作流不可推断 |
| `build_claims_document` | 合并或规范化已有权利要求，统一编号和引用关系，形成完整权利要求书。 | **project_id**, output_language, **text** | — ·工作流不可推断 |
| `attachment_prepare` | 申请附件直传上传地址；仅支持 PUT 原始文件字节，完成直传后再确认上传。 | **filename**, **size**, mime_type, **project_id**, category | — ·工作流不可推断 |
| `attachment_list` | 查询项目附件及其解析状态，不展开 OCR 子图片。 | **project_id** | — ·工作流不可推断 |
| `attachment_detail` | 读取项目附件的 OCR 正文和图片详情；只查询已有解析结果，不等待或启动 OCR。 | **project_id**, **file_id**, text_offset, text_limit, include_images | — ·工作流不可推断 |

### `fto-search` · 分支

- **名称**：防侵权检索 / FTO Search
- **官方分类**：`Ip-Intelligence` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：12 · **上下文权重**：`medium`
- **MCP 地址**：`https://connect.zhihuiya.com/30af1e/mcp`
- **能力**：专利自由实施（FTO）风险分析服务。输入一段技术方案，即可完成专利检索、风险专利筛查、权利要求逐项比对，并产出可交付的 Word 分析报告。方案润色、特征提取、关键词扩展、检索式生成与优化、专利初筛、Claim Chart 比对、报告导出均为独立步骤，供 Agent 按需组合。检索范围可按国家/地区、申请日、法律状态、权利人限定。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `fto_cc_analysis` | 对筛选出的专利做 Claim Chart 逐项比对，判定侵权风险等级。单次最多 10 篇，返回高风险专利的详细比对内容；高、中、低风险的完整结果都会保存，专利较多时可复用同一任务分批分析。 | mode, input_lang, **patent_ids**, top_k, **technical_proposal**, task_id | — ·工作流不可推断 |
| `fto_fetch_missed_patent_details` | 取回仍未被检索到的专利的标题、摘要和分类号，便于找出它们的共同特征、补上遗漏的检索角度。适用于检索式调优的收尾阶段。 | input_lang, **missed_ids**, task_id | — ·工作流不可推断 |
| `fto_patent_screening` | 从检索结果中筛出真正值得逐项比对的专利：排除无关技术领域、按内容相似度过滤、再评估权利要求的相关程度，输出保留专利清单。可选深度筛选或快速筛选。 | mode, input_lang, country, search_page_rows, **technical_proposal**, query_result_count, task_id, **aggregated_query** | — ·工作流不可推断 |
| `fto_report_generation` | 汇总分析结果生成 FTO 分析报告，导出 Word 文档并返回下载链接。报告会纳入同一任务下已完成的全部权利要求比对结果；特征、检索式等章节若未提供对应内容，会标注为待补充。 | input_lang, claim_analysis_results, retrieval_queries, **technical_proposal**, task_id, expanded_keywords, feature_extraction | — ·工作流不可推断 |
| `fto_diagnose_missed` | 分析漏检原因，指出检索式里是哪些条件把相关专利挡在外面，并按影响范围排序，便于有针对性地放宽。 | input_lang, **missed_ids**, task_id, **aggregated_query** | — ·工作流不可推断 |
| `fto_estimate_recall` | 用参考专利集检验检索式的覆盖情况，给出命中数量、覆盖率、漏掉了哪些专利，以及检索式偏宽还是偏窄的判断。 | input_lang, chunk_size, task_id, **aggregated_query**, **sample_ids** | — ·工作流不可推断 |
| `fto_feature_extraction` | 从技术方案中拆出用于检索的技术特征：所属技术领域、核心创新点、关键实现手段和支撑技术。执行过程中实时回传进度。可单独使用。 | input_lang, **technical_proposal**, task_id | — ·工作流不可推断 |
| `fto_keyword_expansion` | 为每个技术特征扩展同义词、近义表述和行业惯用说法，避免因为用词不同而漏掉相关专利。输入取自特征提取的结果。 | input_lang, **search_elements**, **technical_proposal**, task_id, region | — ·工作流不可推断 |
| `fto_proposal_refine` | 把粗略的技术方案描述润色成表述清晰、术语准确的检索输入。支持文字配附图，图片以 base64 传入。可单独使用。 | input_lang, **technical_proposal**, image_files, task_id | — ·工作流不可推断 |
| `fto_query_generation` | 把扩展后的关键词组装成可直接执行的专利检索式，自动校验语法并补充相关分类号，输出分层检索式和一条聚合检索式。可限定受理局和法律状态。 | input_lang, country, **search_elements_with_keywords**, **technical_proposal**, task_id, legal_status | — ·工作流不可推断 |
| `fto_sample_set_init` | 用语义检索为当前技术方案建立一批参考专利，作为后续判断检索式好坏的基准。结果缓存两小时，同一方案反复调优不必重复生成。 | input_lang, country, **technical_proposal**, apd_end, sample_limit, task_id, legal_status, apd_start | — ·工作流不可推断 |
| `fto_validate_and_fix_query` | 校验改写后检索式的语法并自动修正常见写法错误，同时确认受理局、法律状态、专利类型等限定条件没有被误改。返回修正后的检索式和命中数量。 | input_lang, original_query, **new_query**, task_id | — ·工作流不可推断 |

### `intangible-assets` · 分支

- **名称**：企业无形资产档案 / Corporate Intangible Assets
- **官方分类**：`Ip-Intelligence` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：5 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/9fc1e7/mcp`
- **能力**：聚焦企业无形资产和可转化成果的档案工具。覆盖商标、软件著作权、植物新品种、集成电路布图设计以及潜在买家推荐等信息，帮助用户更完整地评估企业的非专利资产储备和商业化可能。适合用于资产盘点、交易准备和企业价值补充分析。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `enterprise_trademark` | 用于获取获取科创企业商标数据相关数据，便于快速查看核心信息并支持后续分析。 | nice_code, reg_num, sort, applicant, ipoffice, mode, us_code, apdt, size, app_num, vienna_code, page, mark, status | — ·工作流不可推断 |
| `ic_design` | 用于获取科创企业集成电路布图设计相关数据，便于快速查看核心信息并支持后续分析。 | page_number, company_name, credit_code, org_number, page_size | C033 ·高 |
| `new_plant_variety` | 用于获取企业植物新品种保护授权信息相关数据，便于快速查看核心信息并支持后续分析。 | page_number, **company_name**, page_size | C034 ·高 |
| `potential_buyer` | 用于获取潜在买家推荐相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, pn | C046 ·中 |
| `software_copyright` | 用于获取获取科创企业软件著作权数据相关数据，便于快速查看核心信息并支持后续分析。 | page_number, company_name, credit_code, org_number, page_size | — ·待确认 |

### `ip-courses` · 分支

- **名称**：知识产权课程中心 / IP & Innovation Courses
- **官方分类**：`Ip-Intelligence` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：3 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/588922/mcp`
- **能力**：提供知识产权与创新主题课程、详情和课件的一站式学习入口。适合帮助团队系统了解专利、检索、分析和业务应用的基础方法，降低新用户上手门槛。可用于内部培训、客户教育和知识沉淀。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `course_courseware` | 用于获取获取课程的课件相关内容，便于学习、培训和内部知识传播。 | **courseware_id**, **company_id** | AC03 ·高 |
| `course_details` | 用于获取获取具体课程详情相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | **course_id**, **company_id** | AC02 ·高 |
| `course_list` | 用于获取获取课程列表，便于批量查看、筛选和进一步处理。 | **company_id**, **limit**, **page** | AC01 ·中 |

### `landscape-projects` · 分支

- **名称**：专利全景任务分析 / Patent Landscape Projects
- **官方分类**：`Ip-Intelligence` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：6 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/4eaa49/mcp`
- **能力**：将专利全景分析做成可跟踪的任务流。支持创建分析任务、查看状态、读取分面结果和完整专利列表，便于团队对大型技术主题开展持续分析和复用。适合用于项目制研究、团队协作和批量化输出。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `landscape_facet_detail` | 用于获取获取 Landscape 分面详情相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | cf_field_id, **job_id**, filter_expired, **name**, length, start, **facet_type** | — ·工作流不可推断 |
| `landscape_facet_list` | 用于获取获取 Landscape 分面列表，便于批量查看、筛选和进一步处理。 | filter, **job_id**, length, start, **facet_type** | — ·工作流不可推断 |
| `landscape_job_create` | 创建 Landscape 分析任务。 | oq, time_type, gid, exclude_expired_patent, request_type, time_start, description, par_job_id, title, rows, expired_collapse, q, job_id, stemming, filter_query, time_stop, lang, dashboard_id | — ·工作流不可推断 |
| `landscape_job_result` | 用于获取 Landscape 任务结果，便于继续分析、导出或交付。 | label_num, **job_id**, lang, job_seq | — ·工作流不可推断 |
| `landscape_job_status` | 用于查看 Landscape 任务状态，便于跟踪执行进度并决定下一步操作。 | **job_id**, job_seq | — ·工作流不可推断 |
| `landscape_patents` | 用于获取获取 Landscape 全部专利列表，便于批量查看、筛选和进一步处理。 | all_legal, **job_id**, length, start, patent_value | — ·工作流不可推断 |

### `novelty-search-lite` · 分支

- **名称**：查新检索 / Novelty Search
- **官方分类**：`Ip-Intelligence` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：11 · **上下文权重**：`medium`
- **MCP 地址**：`https://connect.zhihuiya.com/299425/mcp`
- **能力**：将研发技术提案转化为专利申请决策依据。面向企业研发、知识产权及创新管理团队，查新检索通过模型上下文协议（MCP），向 AI 应用和智能代理提供智慧芽新颖性检索工具及工作流能力，帮助企业在投入专利申请前，快速评估技术方案的创新价值与申请潜力。用户无需掌握专利数据库字段、分类号或复杂的检索语法，也无需人工拆解技术方案、反复调整检索式。只需提供研发技术提案、发明交底材料或相关技术文档，AI 应用和智能代理即可调用标准化工具，完成技术方案理解、关键技术特征提取、检索要素生成、专利及科技文献检索、现有技术对比，以及新颖性与创造性初步分析。查新结果可帮助团队识别潜在的现有技术风险，初步判断技术方案的专利申

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `novelty_lite_boolean_search` | 基于检索要素执行渐进式布尔专利检索，支持结合前序轮次的检索式和命中结果调整本轮策略，返回本轮及累计候选专利，为逐步收敛现有技术范围提供依据。 | **data**, task_id | P002 ·低 |
| `novelty_lite_paper_search` | 根据技术方案摘要和检索要素检索相关科技论文，返回候选非专利文献，为识别专利文献之外的现有技术提供依据。 | **data**, task_id | — ·工作流不可推断 |
| `novelty_lite_semantic_search` | 根据技术方案的结构化摘要执行语义专利检索，返回技术内容相近的候选专利，为现有技术筛选与特征对比提供候选文献。 | **data**, task_id | P008 ·低 |
| `novelty_lite_website_search` | 根据技术方案摘要和检索要素检索相关互联网资料，包括网页、新闻和技术文章，返回候选非专利文献，为补充公开的现有技术提供依据。 | **data**, task_id | — ·工作流不可推断 |
| `novelty_review_with_suggestions` | 综合技术方案、查新要点及候选文献的特征对比结果，生成新颖性与创造性初步评述，并提出可用于优化技术方案和专利申请策略的改进建议。 | **data**, task_id | — ·工作流不可推断 |
| `novelty_feature_comparison` | 将技术方案的关键特征与候选专利进行比对，识别现有技术已公开的特征和区别点；每次最多支持 5 篇专利比对，超过 5 篇时服务端自动截取前 5 篇。 | **data**, task_id | — ·工作流不可推断 |
| `novelty_feature_extract` | 保持从结构化摘要中提取并分类关键技术特征，兼容现有调用方。 | **data**, task_id | AI35-4 ·低 |
| `novelty_keywords_extract` | 从技术特征中提取关键词、同义词、扩展词和 IPC 分类，生成专利及科技文献检索所需的检索要素。 | **data**, task_id | AI35-6 ·低 |
| `novelty_lite_get` | 根据 task_id 查询或轮询查新检索任务进展和结果，支持返回全部步骤，或指定步骤的状态和结果。 | include_step_results, **task_id**, step_ids | — ·工作流不可推断 |
| `novelty_lite_submit` | 提交查新检索端到端任务。输入技术方案文本和可选图片后，后台依次完成技术方案理解、关键技术特征提取、检索要素生成、专利及科技文献检索、现有技术对比和初步评估，并返回 task_id 供查询任务进展和结果。 | **data**, task_id | — ·工作流不可推断 |
| `novelty_summary` | 对研发技术提案、发明交底材料或相关技术文档进行理解，提取技术问题、技术方案和技术效果，形成结构化摘要，为后续关键技术特征提取与检索要素生成提供依据。 | **data**, task_id | — ·工作流不可推断 |

### `patent-analysis` · 分支

- **名称**：专利分析 / Patent Analysis
- **官方分类**：`Ip-Intelligence` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：2 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/e14e5f/logic-mcp`
- **能力**：提供专利数据集的聚合统计和文本挖掘能力，用于趋势、分布、交叉表、关键词词云和创新旭日图分析。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `aggregate_patents` | 对自然语言专利需求、已有 Boolean Query 或单个 Workspace 文件夹，按一个或两个维度做聚合统计，支持趋势、分布、排名和交叉表分析。 | limit_per_dimension, **source**, sorts, **dimensions** | P001 ·低 |
| `mine_patent_text` | 对自然语言专利需求或已有 Boolean Query 做专利文本挖掘分析，支持关键词词云和创新旭日图主题结构。 | **subtype**, chart_limit, **source** | — ·工作流不可推断 |

### `patent-briefing` · 分支

- **名称**：专利速览简报 / Patent Briefing
- **官方分类**：`Ip-Intelligence` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：12 · **上下文权重**：`medium`
- **MCP 地址**：`https://connect.zhihuiya.com/958a46/mcp`
- **能力**：用于快速阅读和理解单件专利或专利家族的速览工具。可汇总著录项目、法律状态、家族信息、技术三要素、附图，以及说明书、摘要和权利要求翻译，帮助非专利背景用户也能迅速把握技术重点。适合用于内部沟通、项目初筛、专利培训和客户汇报。
- **工具重复**：可替代 core-patents

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `abstract_image` | 用于获取摘要附图相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, patent_number | P021 ·高 |
| `abstract_translated` | 用于获取摘要翻译相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, replace_by_related, patent_number, **lang** | P043 ·高 |
| `bibliography` | 用于获取著录项目相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | patent_id, patent_number | P012 ·高 |
| `claims` | 用于获取权利要求相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | patent_id, replace_by_related, patent_number | P018 ·高 |
| `claim_translated` | 用于获取权利要求翻译相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | patent_id, replace_by_related, patent_number, **lang** | P044 ·高 |
| `description` | 用于获取说明书相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | patent_id, replace_by_related, patent_number | P019 ·高 |
| `description_translated` | 用于获取说明书翻译相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | patent_id, replace_by_related, patent_number, **lang** | P045 ·高 |
| `family` | 用于获取专利家族信息，便于查看同族关系、地域布局和家族覆盖范围。 | patent_id, patent_number | P014 ·低 |
| `intelligent_image` | 用于获取获取专利智能附图相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, lang, pn | P042 ·低 |
| `legal_status` | 用于获取简单法律状态相关信息，便于判断专利状态变化、专利稳定性及潜在法律风险。 | patent_id, patent_number | P041 ·高 |
| `search_patents` | 用于检索式检索专利，返回匹配结果，便于快速筛选、比对和继续分析。 | collapse_order_authority, offset, sort_field, limit, stemming, collapse_order, sort_order, **query_text**, collapse_type, collapse_by | P002 ·低 |
| `tech_summary` | 用于获取专利技术三要素相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, patent_number, lang | P025 ·高 |

### `patent-dispute` · 分支

- **名称**：专利纠纷与SEP / Patent Disputes & SEP
- **官方分类**：`Ip-Intelligence` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：21 · **上下文权重**：`high`
- **MCP 地址**：`https://connect.zhihuiya.com/4f9217/mcp`
- **能力**：聚焦专利纠纷、诉讼与标准必要专利（SEP）信息的专题工具。可查看 SEP、诉讼、复审无效、许可、转移、年费和 UPC 状态等数据，帮助用户理解专利稳定性和争议强度。适合用于诉讼研判、许可谈判、标准领域竞争分析和风险排查。
- **工具重复**：可替代 core-patents

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `forward_citation` | 用于获取专利被引用-v3相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, offset, patent_number, limit | — ·待确认 |
| `transfer_data` | 用于获取专利转移相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, patent_number | P029 ·高 |
| `search_patents` | 用于检索式检索专利，返回匹配结果，便于快速筛选、比对和继续分析。 | collapse_order_authority, offset, sort_field, limit, stemming, collapse_order, sort_order, **query_text**, collapse_type, collapse_by | P002 ·低 |
| `reexam_invalidation` | 用于获取复审无效相关信息，便于判断专利状态变化、专利稳定性及潜在法律风险。 | patent_id, patent_number | P027 ·高 |
| `pledge_data` | 用于获取专利质押相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, patent_number | P030 ·高 |
| `pdf` | 用于获取PDF全文相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | patent_id, patent_number | P020 ·高 |
| `patent_valuation` | 用于获取专利价值相关数据，便于从多个维度做企业、专利或项目评估。 | patent_id, patent_number | P035 ·高 |
| `license_data` | 用于获取专利许可相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, patent_number | P028 ·高 |
| `legal_status` | 用于获取简单法律状态相关信息，便于判断专利状态变化、专利稳定性及潜在法律风险。 | patent_id, patent_number | P041 ·高 |
| `legal_data` | 用于获取法律详情相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | patent_id, patent_number | P026 ·高 |
| `fulltext_image` | 用于获取全文附图相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | patent_id, offset, patent_number, limit | P042 ·高 |
| `abstract_image` | 用于获取摘要附图相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, patent_number | P021 ·高 |
| `family` | 用于获取专利家族信息，便于查看同族关系、地域布局和家族覆盖范围。 | patent_id, patent_number | P014 ·低 |
| `desc_translated` | 用于获取说明书翻译相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | patent_id, replace_by_related, patent_number, lang | P045 ·高 |
| `description` | 用于获取说明书相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | patent_id, replace_by_related, patent_number | P019 ·高 |
| `customs_data` | 用于获取海关备案相关信息，便于判断专利状态变化、专利稳定性及潜在法律风险。 | patent_id, patent_number | P031 ·高 |
| `claim_translated` | 用于获取权利要求翻译相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | patent_id, replace_by_related, patent_number, lang | P044 ·高 |
| `claims` | 用于获取权利要求相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | patent_id, replace_by_related, patent_number | P018 ·高 |
| `bibliography` | 用于获取著录项目相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | patent_id, patent_number | P012 ·高 |
| `award_data` | 用于获取专利奖相关数据，便于了解主体或专利的荣誉情况和外部认可度。 | patent_id, patent_number | P032 ·高 |
| `abstract_translated` | 用于获取摘要翻译相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, replace_by_related, patent_number, lang | P043 ·高 |

### `patent-landscape` · 分支

- **名称**：专利技术全景分析 / Patent Landscape Analytics
- **官方分类**：`Ip-Intelligence` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：24 · **上下文权重**：`high`
- **MCP 地址**：`https://connect.zhihuiya.com/59100a/mcp`
- **能力**：将专利检索结果转化为可直接使用的专利全景分析。支持申请趋势、技术构成、主要申请人、地域与专利局分布、技术分支、技术地图和技术生命周期等多个维度，帮助团队快速理解一个技术赛道的竞争格局和演进方向。适合用于赛道研究、竞品分析、技术布局和项目预研。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `search_patents_with_detail` | 用于专利检索及详情，返回匹配结果，便于快速筛选、比对和继续分析。 | patent_id, offset, replace_by_related, stemming, sort, **lang**, **query_text**, pn, collapse_type, collapse_by, posiofpat | D009 ·中 |
| `search_patents_v3` | 用于专利检索，返回匹配结果，便于快速筛选、比对和继续分析。 | offset, stemming, sort, **query_text**, collapse_type, collapse_by | D005 ·中 |
| `search_patents_statistics` | 用于分析专利统计，帮助判断活跃度变化、重点主体和发展方向。 | **field**, limit, stemming, lang, **query_text**, collapse_type, collapse_by | D010 ·中 |
| `search_patents_facet` | 用于专利检索统计，返回匹配结果，便于快速筛选、比对和继续分析。 | **field**, offset, limit, stemming, sort, lang, **query_text**, collapse_type, collapse_by | D006 ·中 |
| `rec_office_year` | 用于分析受理局统计(按年)，帮助判断活跃度变化、重点主体和发展方向。 | collapse_order_authority, sort, collapse_order, **query_text**, collapse_type, collapse_by | — ·待确认 |
| `rec_office` | 用于分析受理局统计，帮助判断活跃度变化、重点主体和发展方向。 | collapse_order_authority, sort, collapse_order, **query_text**, collapse_type, collapse_by | — ·待确认 |
| `pdf` | 用于获取专利PDF相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, replace_by_related, patent_number | P020 ·低 |
| `trend` | 用于分析专利趋势，帮助判断活跃度变化、重点主体和发展方向。 | collapse_order_authority, sort, collapse_order, **query_text**, collapse_type, collapse_by | — ·待确认 |
| `tech_applicant_dist` | 用于分析重要技术分支主要申请人分布，帮助理解结构分布、热点方向和整体格局。 | collapse_order_authority, sort, collapse_order, **query_text**, collapse_type, collapse_by | — ·待确认 |
| `technology_life_cycle` | 用于分析技术生命周期，帮助理解结构分布、热点方向和整体格局。 | collapse_order_authority, sort, collapse_order, **query_text**, collapse_type, collapse_by | — ·待确认 |
| `technology_constitute` | 用于分析技术构成，帮助理解结构分布、热点方向和整体格局。 | collapse_order_authority, sort, collapse_order, **query_text**, collapse_type, collapse_by | — ·待确认 |
| `refered_rank` | 用于分析被引用数排名，帮助判断活跃度变化、重点主体和发展方向。 | collapse_order_authority, sort, collapse_order, **query_text**, collapse_type, collapse_by | — ·待确认 |
| `applicant_rank` | 用于分析申请人排名，帮助判断活跃度变化、重点主体和发展方向。 | collapse_order_authority, sort, collapse_order, **query_text**, collapse_type, collapse_by | — ·待确认 |
| `map_3d` | 用于分析3D地图分析，帮助理解结构分布、热点方向和整体格局。 | collapse_order_authority, sort, collapse_order, **query_text**, collapse_type, collapse_by | — ·待确认 |
| `list` | 用于获取专利列表，便于批量查看、筛选和进一步处理。 | collapse_order_authority, offset, limit, sort, collapse_order, **query_text**, collapse_type, collapse_by | D113 ·中 |
| `info` | 用于获取专利字段详情相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | **patent_number** | D114 ·中 |
| `famn_rank` | 用于分析同族排名，帮助判断活跃度变化、重点主体和发展方向。 | collapse_order_authority, sort, collapse_order, **query_text**, collapse_type, collapse_by | — ·待确认 |
| `domain_map` | 用于分析领域地图，帮助理解结构分布、热点方向和整体格局。 | collapse_order_authority, sort, collapse_order, **query_text**, collapse_type, collapse_by | — ·待确认 |
| `detail_text` | 用于获取专利详情文本相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | patent_id, patent_number | D201 ·高 |
| `detail_aggregation` | 用于获取专利详情聚合相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | patent_id, patent_number | D301 ·高 |
| `detail` | 用于获取专利详情相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | patent_id, replace_by_related, patent_number, lang | P012 ·低 |
| `cooperation_applicant_analysis` | 用于获取合作申请分析相关数据，便于快速查看核心信息并支持后续分析。 | collapse_order_authority, sort, collapse_order, **query_text**, collapse_type, collapse_by | D105 ·高 |
| `applicant_trend` | 用于分析主要申请人申请趋势，帮助判断活跃度变化、重点主体和发展方向。 | collapse_order_authority, sort, collapse_order, **query_text**, collapse_type, collapse_by | — ·待确认 |
| `applicant_technology_analysis` | 用于获取主要申请人技术分析相关数据，便于快速查看核心信息并支持后续分析。 | collapse_order_authority, sort, collapse_order, **query_text**, collapse_type, collapse_by | D103 ·高 |

### `patent-mining` · 分支

- **名称**：专利深度挖掘 / Deep Patent Mining
- **官方分类**：`Ip-Intelligence` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：7 · **上下文权重**：`medium`
- **MCP 地址**：`https://connect.zhihuiya.com/7cc6ae/mcp`
- **能力**：用于从专利文本和分类信息中进一步挖掘技术内容。支持技术主题、技术问题/技术手段/技术效果三要素、战略性新兴产业、材料物质、应用领域和分类号说明等分析，帮助用户把“检索到专利”进一步转成“读懂技术”。适合用于技术拆解、领域研究和研发启发。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `application_domain` | 用于获取应用领域分类相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, patent_number, lang | — ·待确认 |
| `classification_description` | 用于获取专利分类号说明相关数据，便于快速查看核心信息并支持后续分析。 | **code**, **type**, replace_by_merge | P066 ·高 |
| `enhanced_data` | 用于获取专利增值数据相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, patent_number, fields | P064 ·高 |
| `intelligent_attached_image` | 用于获取获取专利智能附图相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, **lang**, pn | P042 ·低 |
| `seic_classification` | 用于获取战略新兴产业分类相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, patent_number, lang | P022 ·高 |
| `technology_topic` | 用于获取技术主题分类相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, patent_number, lang | P024 ·高 |
| `tech_problem_benefit_summary` | 用于获取专利技术三要素相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, patent_number, lang | P025 ·高 |

### `patent-status` · 分支

- **名称**：专利法律状态与年费 / Patent Legal Status & Annuity
- **官方分类**：`Ip-Intelligence` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：12 · **上下文权重**：`medium`
- **MCP 地址**：`https://connect.zhihuiya.com/30096b/mcp`
- **能力**：聚焦专利法律状态、年费和核心法律文档核查的工具。可查看年费缴纳信息、法律状态、全文、说明书和权利要求，并结合被引等信息辅助判断专利是否维持有效、是否存在权利变更或失效风险。适合用于专利维持管理、交易核验、许可谈判和尽调审查。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `award_data` | 用于获取专利奖相关数据，便于了解主体或专利的荣誉情况和外部认可度。 | patent_id, patent_number | P032 ·高 |
| `customs_data` | 用于获取海关备案相关信息，便于判断专利状态变化、专利稳定性及潜在法律风险。 | patent_id, patent_number | P031 ·高 |
| `fee_info` | 用于获取专利缴费信息请求相关信息，便于判断专利状态变化、专利稳定性及潜在法律风险。 | **apnos** | P047 ·高 |
| `get_sep_data` | 用于获取标准必要专利(SEP)相关数据，便于评估标准参与情况、制定进展和行业影响力。 | patent_id, patent_number | P033 ·高 |
| `legal_data` | 用于获取法律详情相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | patent_id, patent_number | P026 ·高 |
| `license_data` | 用于获取专利许可相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, patent_number | P028 ·高 |
| `litigation_data` | 用于获取诉讼数据相关信息，便于判断专利状态变化、专利稳定性及潜在法律风险。 | patent_id, patent_number | P034 ·高 |
| `overseas_patent_documents` | 用于获取海外专利审查文件相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, offset, patent_number, doc_code, limit, date_to, apno, date_from | P048 ·高 |
| `pledge_data` | 用于获取专利质押相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, patent_number | P030 ·高 |
| `re_examination_data` | 用于获取复审无效相关信息，便于判断专利状态变化、专利稳定性及潜在法律风险。 | patent_id, patent_number | P027 ·高 |
| `transfer_data` | 用于获取专利转移相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, patent_number | P029 ·高 |
| `unified_patent_court_status` | 用于获取欧洲统一法院状态相关信息，便于判断专利状态变化、专利稳定性及潜在法律风险。 | patent_id, patent_number | P046 ·高 |

### `patent-value` · 分支

- **名称**：专利价值评分 / Patent Valuation Scorecard
- **官方分类**：`Ip-Intelligence` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：10 · **上下文权重**：`medium`
- **MCP 地址**：`https://connect.zhihuiya.com/67d1b4/mcp`
- **能力**：将专利价值拆解为技术、法律稳定性、市场、战略、保护范围和转化前景等多个维度进行评分。帮助用户更系统地比较专利质量与商业化潜力，而不是只看单一指标。适合用于项目筛选、资产分级、交易评估和组合管理。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `ability_indicators` | 用于查看与保护范围相关的评估指标，便于从法律稳定性和可保护范围等角度辅助评价专利。 | **patent_info**, claim_cnt_threshold | P051 ·中 |
| `economic_indicators` | 用于获取经济指标相关数据，便于从多个维度做企业、专利或项目评估。 | patent_id, patent_number | P040 ·高 |
| `legal_indicators` | 用于获取法律指标相关数据，便于从多个维度做企业、专利或项目评估。 | patent_id, patent_number | P037 ·高 |
| `market_indicators` | 用于获取市场指标相关数据，便于从多个维度做企业、专利或项目评估。 | patent_id, patent_number | P038 ·高 |
| `market_prospect_indicators` | 用于获取转化前景-市场前景指标相关数据，便于从多个维度做企业、专利或项目评估。 | **patent_info**, year_threshold, ipc_cnt_threshold | P052 ·中 |
| `operation_situation_indicators` | 用于获取转化前景-运营情况指标相关数据，便于从多个维度做企业、专利或项目评估。 | **patent_info**, family_threshold | P053 ·中 |
| `strategic_indicators` | 用于获取战略指标相关数据，便于从多个维度做企业、专利或项目评估。 | patent_id, patent_number | P039 ·高 |
| `technology_indicators` | 用于获取技术指标相关数据，便于从多个维度做企业、专利或项目评估。 | patent_id, patent_number | P036 ·高 |
| `tech_innovation_indicators` | 用于获取技术创新性指标相关数据，便于从多个维度做企业、专利或项目评估。 | relevancy_threshold, **patent_info**, cited_by_threshold | P050 ·中 |
| `valuation` | 用于获取专利价值相关数据，便于从多个维度做企业、专利或项目评估。 | patent_id, patent_number | P035 ·高 |

### `patent-visual` · 分支

- **名称**：专利图表分析 / Patent Visual Analytics
- **官方分类**：`Ip-Intelligence` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：24 · **上下文权重**：`high`
- **MCP 地址**：`https://connect.zhihuiya.com/3fd502/mcp`
- **能力**：将专利数据转化为更直观的图表分析结果。可从趋势、类型、价值、诉讼、被引、技术效果短语等维度进行可视化展示，帮助用户更快发现集中度、热点和异常点。适合用于管理层汇报、客户展示和专题分析。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `company_word_cloud` | 用于分析企业创新词云，帮助理解结构分布、热点方向和整体格局。 | company_name, credit_code, org_number, apply_end_time, apply_start_time, patent_type, lang, simple_legal_status | — ·待确认 |
| `word_cloud` | 用于分析创新词云，帮助理解结构分布、热点方向和整体格局。 | keywords, authority, apply_end_time, apply_start_time, **lang**, ipc, query_text | — ·待确认 |
| `wheel_of_innovation` | 用于获取旭日图相关数据，便于快速查看核心信息并支持后续分析。 | keywords, authority, apply_end_time, apply_start_time, **lang**, ipc, query_text | A003 ·高 |
| `type_trend` | 用于分析专利类型趋势分析，帮助判断活跃度变化、重点主体和发展方向。 | **query**, **start_year**, **end_year** | — ·待确认 |
| `trends` | 用于分析专利趋势分析，帮助判断活跃度变化、重点主体和发展方向。 | keywords, public_start_time, authority, apply_end_time, apply_start_time, **lang**, ipc, query_text, public_end_time | — ·待确认 |
| `technology_effect_distribution` | 用于统计专利文本中技术效果短语的分布情况，便于识别常见技术效果、热点方向和差异化卖点。 | collapse_order_authority, sort, lang, collapse_order, **query_text**, collapse_type, collapse_by | A012 ·中 |
| `simple_legal_status` | 用于分析简单法律状态统计，帮助判断活跃度变化、重点主体和发展方向。 | keywords, authority, apply_end_time, apply_start_time, **lang**, ipc, query_text | — ·待确认 |
| `priority_country` | 用于分析技术来源国/地区排名，帮助判断活跃度变化、重点主体和发展方向。 | keywords, authority, apply_end_time, apply_start_time, **lang**, ipc, query_text | — ·待确认 |
| `portfolio_value` | 用于分析专利价值分布，帮助理解结构分布、热点方向和整体格局。 | keywords, authority, apply_end_time, apply_start_time, **lang**, ipc, query_text | — ·待确认 |
| `most_cited` | 用于获取被引用最多的专利相关数据，便于快速查看核心信息并支持后续分析。 | keywords, authority, apply_end_time, apply_start_time, **lang**, ipc, query_text | A005 ·高 |
| `most_asserted` | 用于获取最多诉讼专利相关信息，便于判断专利状态变化、专利稳定性及潜在法律风险。 | keywords, authority, apply_end_time, apply_start_time, **lang**, ipc, query_text | A009 ·高 |
| `inventor_ranking` | 用于分析发明人排名分析，帮助判断活跃度变化、重点主体和发展方向。 | keywords, authority, apply_end_time, apply_start_time, **lang**, ipc, query_text | — ·待确认 |
| `applicant_ranking` | 用于分析申请人排名分析，帮助判断活跃度变化、重点主体和发展方向。 | keywords, authority, apply_end_time, apply_start_time, **lang**, ipc, query_text | — ·待确认 |
| `company_tech_field_word_cloud` | 用于分析技术领域词云，帮助理解结构分布、热点方向和整体格局。 | **company_name**, lang | A202 ·中 |
| `company_tech_effect_dist` | 用于统计企业专利组合中技术效果相关表述的分布情况，便于观察该企业重点强调的技术效果和应用方向。 | **company_name**, **apply_end_time**, **apply_start_time**, lang | A201 ·中 |
| `company_strategy_map` | 用于分析企业创新战略雷达图，帮助理解结构分布、热点方向和整体格局。 | company_name, credit_code, org_number, apply_end_time, apply_start_time, patent_type, lang, simple_legal_status | — ·待确认 |
| `company_simple_legal_status` | 用于分析企业简单法律状态统计，帮助判断活跃度变化、重点主体和发展方向。 | company_name, credit_code, org_number, apply_end_time, apply_start_time, patent_type, lang, simple_legal_status | — ·待确认 |
| `company_portfolio_overview` | 用于获取企业专利总申请布局相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number, apply_end_time, apply_start_time, patent_type, lang, simple_legal_status | A105 ·高 |
| `company_patent_trends` | 用于分析企业专利申请趋势，帮助判断活跃度变化、重点主体和发展方向。 | company_name, credit_code, org_number, apply_end_time, apply_start_time, patent_type, lang, simple_legal_status | — ·待确认 |
| `company_most_cited_latest` | 用于获取企业被引用最多的专利相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number, apply_end_time, apply_start_time, patent_type, lang, simple_legal_status | A106 ·高 |
| `company_most_cited` | 用于获取最多引用该企业专利的公司相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number, apply_end_time, apply_start_time, patent_type, lang, simple_legal_status | A107 ·高 |
| `company_largest_patent_family` | 用于获取企业规模最大的专利家族信息，便于查看同族关系、地域布局和家族覆盖范围。 | company_name, credit_code, org_number, apply_end_time, apply_start_time, patent_type, lang, simple_legal_status | — ·待确认 |
| `company_key_technology` | 用于分析企业技术构成分析，帮助理解结构分布、热点方向和整体格局。 | company_name, credit_code, org_number, apply_end_time, apply_start_time, patent_type, lang, simple_legal_status | — ·待确认 |
| `company_acquisition_divestiture` | 用于获取企业专利转入转出相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number, apply_end_time, apply_start_time, patent_type, lang, simple_legal_status | A110 ·高 |

### `patsnap-analytics` · 分支

- **名称**：智慧芽分析 / PatSnap Analytics
- **官方分类**：`Ip-Intelligence` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：1 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/2ff4d4/logic-mcp`
- **能力**：由 Analytics 提供的 PatSnap 产品专属 MCP Server。当前仅提供 fetch_patent_lifecycle 工具，用于读取单件专利的法律事件、许可、转让、质押、复审和无效记录。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `fetch_patent_lifecycle` | 读取单件专利的法律事件、许可或转让记录，以及质押或无效记录。 | **patent_id**, format, language | — ·待确认 |

### `patsnap-ip-searching` · 分支

- **名称**：智慧芽专利检索与报告 / Patsnap Patent Research
- **官方分类**：`Ip-Intelligence` · **版本**：`v0.1.0` · **状态**：`active` · **tool 数**：5 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/f176d7/mcp`
- **能力**：面向知识产权检索与分析场景的 MCP 服务，统一提供查新检索、发明 FTO 分析和外观设计 FTO 分析能力。
查新检索：根据技术方案、发明交底书或权利要求文本执行查新检索，并返回摘要、特征提取、候选专利、对比和报告等步骤结果。
发明 FTO 分析：针对产品或技术实现描述进行自由实施风险分析，支持国家、申请日、法律状态、权利人等过滤条件。
外观设计 FTO：基于单张产品或外观设计图片执行外观风险检索与分析。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `upload_image` | 通用图片上传辅助 tool，用于在调用具体业务 tool 前将客户端本地图片转换为 URL。当用户或客户端持有本地图片文件，而业务 tool 需要图片 URL 时使用 upload_image，例如调用 design_f | content_type, file_extension, expire_seconds | P010 ·低 |
| `design_fto` | 基于产品或外观图片进行外观设计 FTO 分析，支持国家、申请日、法律状态和洛迦诺分类过滤。仅使用 input.images 中的首张图片；异步任务可通过 get_task 查询。 | output, **input**, execution, filters | AI39-1 ·低 |
| `fto_review` | 分析产品或技术实现的专利侵权风险，支持国家、申请日、法律状态和权利人过滤。search.mode 支持 lite 快速初筛和 pro 完整分析；异步任务可通过 get_task 查询。 | output, **input**, execution, search, task_id, filters | AI66-4 ·低 |
| `get_task` | 查询异步任务的状态与结果。overview 返回状态摘要，detail 返回步骤与结果明细。 | view, **task_id** | — ·工作流不可推断 |
| `novelty_search` | 检索技术方案、发明交底书或权利要求的新颖性，支持文本及可选图片输入，并返回相关专利与分析结果。异步任务可通过 get_task 查询。 | output, **input**, execution, search, task_id | AI35-2 ·低 |

### `patsnap-web-search` · 分支

- **名称**：智慧芽网页搜索 / PatSnap Web Search
- **官方分类**：`Ip-Intelligence` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：1 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/80d0cd/mcp`
- **能力**：用于检索当前、实时公开网页信息的 MCP。适合查询近期事件、最新发布或版本、当前价格、政策更新、公司动态，以及其他可能超过模型记忆或无法仅凭记忆可靠回答的事实。返回按相关性排序的网页结果，包括标题、链接、摘要片段和发布日期。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `web_search` | 检索公开网页中的当前、实时的信息。当用户询问近期事件、最新发布或版本、当前价格，或任何可能超过模型记忆时效的信息时使用。结果按相关性排序返回，包含标题、链接、摘要片段和发布日期。 | end_date, **query**, max_results, freshness, start_date | — ·工作流不可推断 |

### `patsnap-workspace` · 分支

- **名称**：工作空间专利集合读取 / PatSnap Workspace
- **官方分类**：`Ip-Intelligence` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：11 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/48a232/logic-mcp`
- **能力**：浏览工作空间，检索专利并读取标引与注释，将专利列表或检索结果保存到指定目录；支持自动更新设置，以及专利、注释、自定义字段和标引值的编辑，写入前先预览确认。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `automatic_update_and_expansion` | 为文件夹设置检索式自动更新、文件夹并集／交集／差集计算，以及同族／同申请拓展。预览结果规模后确认设置。 | preview_token, **changes**, dry_run, **target_folder** | — ·工作流不可推断 |
| `edit_annotations` | 为单篇或批量专利编辑自定义字段值，支持覆盖、仅填空值、追加、移除指定值和清空。可统一赋值或逐篇设置，预览后确认执行。 | **field_id**, max_count, values_by_patent, preview_token, **action**, **patents**, dry_run, **target_folder**, value | — ·工作流不可推断 |
| `edit_comments` | 为单篇或批量专利新增、修改或删除普通主注释，支持统一内容或逐篇设置。修改和删除作用于有权操作的全部主注释，预览后确认执行。 | max_count, preview_token, **action**, **patents**, dry_run, **target_folder**, content | — ·工作流不可推断 |
| `edit_custom_fields` | 创建、修改或删除个人自定义字段，支持字段改名及选项、层级节点的新增、改名和删除。删除节点时包含子树，预览影响后确认执行。 | field_id, preview_token, changes, **action**, definition, dry_run | — ·工作流不可推断 |
| `edit_patents` | 删除、复制或移动单篇或批量专利，也可删除同申请或同族专利。执行前预览影响范围并确认。 | max_count, **source_folder**, preview_token, delete_scope, **action**, **patents**, dry_run, target_folder | — ·工作流不可推断 |
| `save_patents_to_workspace` | 将专利列表或自然语言、检索式命中的全部或指定范围专利保存到工作空间目录。保存前预览数量及最多 5 条样例，确认后提交。 | max_count, preview_token, start, limit, expected_count, dry_run, **source**, **target_folder**, sort | — ·工作流不可推断 |
| `get_workspace_annotations` | 读取指定工作空间目录内专利的 AI 标引或自定义字段值；可按需同时读取注释。没有值的专利会返回空 annotations。 | patent_ids, offset, all_pages, limit, **folder_id**, **space_id**, field_ids, max_items, include_comments | — ·工作流不可推断 |
| `get_workspace_patents` | 检索并获取工作空间目录内的专利，支持自然语言查询、自定义字段和注释筛选、同族合并、排序及分页。 | offset, comment_filters, limit, comment_filter_logic, **folder_id**, keyword, family_grouping, **space_id**, custom_filters, sort_order, query_text, custom_filter_logic | — ·工作流不可推断 |
| `list_workspace_fields` | 列出指定工作空间下的标准字段、自定义字段和特殊字段。字段列表可用于理解可读字段；自定义字段和 AI 标引字段值通过 get_workspace_annotations 读取。 | **space_id** | — ·工作流不可推断 |
| `list_workspace_folders` | 列出指定工作空间下的目录，支持目录名称模糊搜索。 | search_name, **space_id** | — ·工作流不可推断 |
| `list_workspace_spaces` | 列出当前用户可访问的工作空间，支持按 all/self/shared/public 类型过滤和名称模糊搜索。 | search_name, type | — ·工作流不可推断 |

### `s-telecom-mcp-sep` · 分支

- **名称**：通信SEP专利对标分析工具 / Telecom SEP Claim Charting Tool
- **官方分类**：`Ip-Intelligence` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：1 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/9b35b1/sep-mcp`
- **能力**：提供 3GPP TS/TR、ITU（含音视频）和 IEEE WiFi 的 SEP 技术对标。PN 必填；自动推荐、section 召回、AICC 端到端分析，或从指定标准/section 开始。默认 3gpp，由下游决定 CC 执行方式。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `standard_claim_charting` | 提供 3GPP TS/TR、ITU（含音视频）和 IEEE WiFi 的 SEP 技术对标。PN 必填；自动推荐、section 召回、AICC 端到端分析，或从指定标准/section 开始。默认 3gpp，由下游决定 | section_id, lang, **PN**, TS, claim_num | — ·工作流不可推断 |

### `s-telecom-mcp-tools` · 分支

- **名称**：通信标准与 TDoc 检索工具 / Telecom MCP Tools
- **官方分类**：`Ip-Intelligence` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：4 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/b4ba15/fundamental-mcp`
- **能力**：提供 3GPP TDoc 与标准文档检索能力，包括 TDoc 详情读取、TDoc 语义或元数据检索、标准检索以及标准章节正文读取。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `fetch_standard_section` | 获取 3GPP、ITU（H.26X）或 IEEE（Wi-Fi）标准章节正文。提供 section_id 获取指定章节，或者同时提供 number 和 version 获取某个标准版本的全部章节；不要空参数调用。单次最多接 | number, section_id, source, version | — ·工作流不可推断 |
| `fetch_tdocs` | 根据官方 TDoc number 获取一个或多个 TDoc 的详情，返回 metadata、CR 字段、revision 字段和可用的全文内容。 | **tdoc_number** | — ·工作流不可推断 |
| `search_standards` | 检索 3GPP、ITU（H.26X）或 IEEE（Wi-Fi）标准，返回标准元数据和完整章节列表，不返回章节正文。必须至少提供一个检索条件：3GPP 可使用 text、number、version、release、pro | number, release, start, project, text, source, work_group, rows, version | — ·工作流不可推断 |
| `search_tdocs` | 按语义查询或结构化元数据过滤条件检索 TDoc，返回匹配 TDoc 的核心字段。 | mode, query, start, filters, rows | — ·工作流不可推断 |

## 医药情报（`pharma`，11 个 MCP）

### `pharma-intelligence` · 🌳 主干

- **名称**：医药情报 / Pharma Intelligence
- **官方分类**：`Life-Sciences` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：36 · **上下文权重**：`high`
- **MCP 地址**：`https://connect.zhihuiya.com/096456/logic-mcp`
- **能力**：医药情报终端提供结构化搜索、语义向量搜索和实体检索，涵盖临床试验、药物、靶点、疾病、专利、论文、交易、FDA药品说明书、流行病学、医学指南、财务报告、新闻和转化医学等领域。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `ls_evidence_fetch` | 获取选定来源的证据详情。 | translational_medicine_ids, **evidence_type**, news_ids, trial_ids, drug_deal_ids, registration_number, result_ids | — ·工作流不可推断 |
| `ls_evidence_by_semantic_search` | 按语义检索选定来源的证据。 | **query**, top_k, **source**, **lang** | — ·待确认 |
| `ls_evidence_by_entity_search` | 按实体条件检索选定来源的证据。 支持 corporate_financing 企业融资事件检索，可按融资公司、投资机构、融资类型和公告日期筛选，支持同轮共同投资。融资默认每页10条，最多100条。 | field_options, mechanism_action, country, study_first_posted_date_from, study_identifier, investor_ids, **evidence_type**, brief_title, funding_type_mapping_codes, deal_date_from, investors, study_status, drug, published_date_to, top_k, drug_type, post_date_from, limit, drug_disease, study_first_posted_date_to, lang, therapeutic_area, keyword, study_code, phase, disease, offset, licensee, route_of_administration, deal_type, query, licensor, deal_disease, date_to, organization_ids, target, dosage_form, deal_date_to, post_date_to, organization, organizations, register_number, control_drug, published_date_from, date_from | — ·工作流不可推断 |
| `ls_entity_search` | 按药物条件搜索药物、靶点、机构或疾病。 | field_options, mechanism_action, country, atc_code, highest_phase, disease, offset, dev_status, action_type, org_type, org_roll_up, modification, drug, target, highest_phase_date_from, **entity_type**, organization, drug_type, limit, highest_phase_date_to | — ·待确认 |
| `ls_entity_fetch` | 获取药物、靶点、疾病或机构详情。 | drug_ids, **entity_type**, disease, organization, disease_ids, target_ids, organization_ids, drug, target | — ·工作流不可推断 |
| `ls_news_search` | 此工具已弃用，将由 `ls_evidence_by_entity_search` 替代。请使用 `ls_evidence_by_entity_search`，设置 `evidence_type="news"`，并沿用相同 | field_options, disease, offset, post_date_to, organization, drug_type, post_date_from, limit, keyword, drug, target | — ·待确认 |
| `ls_organization_pipeline_fetch` | 获取指定机构的药物研发管线信息（含在研药物、靶点、疾病以及按国家维度的开发状态）。当用户已知 `organization_id` 或提供机构名称 `organization` 时使用。必须提供二者之一。 | offset, organization_id, organization, limit | — ·待确认 |
| `ls_drug_milestone_fetch` | 获取指定药物的研发里程碑历史记录（时间线）。当用户已知 `drug_id` 或提供药物名称 `drug` 时使用。必须提供二者之一。 | drug_id, offset, limit, drug | — ·待确认 |
| `ls_ner_nor_normalize` | 从用户查询文本中识别并规范化实体。识别并规范化靶点、药物、疾病、公司、药物类型、作用机制、作用类型、专利号和临床试验号等实体，并行运行NER-NOR API和LLM关键词提取，通过自动补全合并去重结果。 | **user_input** | AI01 ·低 |
| `ls_paper_fetch` | 通过论文ID批量获取完整的论文详情记录。 | **paper_ids** | — ·工作流不可推断 |
| `ls_news_vector_search` | 此工具将被移除。推荐使用 ls_evidence_by_entity_search(evidence_type="news") 进行结构化新闻检索；将 query/top_k 改为 keyword（字符串列表）和 off | **query**, top_k, **lang** | — ·工作流不可推断 |
| `ls_organization_fetch` | 通过机构ID或机构名称批量获取完整的机构详情记录。 | organization, organization_ids | — ·工作流不可推断 |
| `ls_fda_label_vector_search` | 向量相似度搜索FDA药品标签。使用语义相似度搜索FDA药品标签，适用于复杂的自然语言查询，调用统一向量搜索接口并返回相关文本片段。 | **query**, top_k, **lang** | — ·工作流不可推断 |
| `ls_paper_search` | 搜索学术论文。当用户需要通过药物、靶点、疾病、机构、期刊、作者或发表年份查找论文时使用。适用于证据检索查询，例如"近期Nature Medicine关于KRAS抑制剂的论文"或"Dana-Farber关于PD-1的论文" | field_options, disease, offset, inchi_keys, year_to, drug, target, year_from, journal, drug_type, organization, limit, authors, sequence_numbers | — ·待确认 |
| `ls_paper_vector_search` | 向量相似度搜索学术论文。使用语义相似度搜索学术论文，适用于复杂的自然语言查询，调用统一向量搜索接口并返回相关文本片段。 | **query**, top_k, **lang** | — ·工作流不可推断 |
| `ls_patent_fetch` | 通过专利ID或专利号批量获取完整的专利详情记录。 | patent_ids, pn | P012 ·低 |
| `ls_patent_search` | 通过语义、关键词和结构化生命科学条件搜索专利。根据 semantic_query、keywords、filters/domain_filters 自动选择检索方式；不接受 domain 或布尔检索。limit 为 1–1 | semantic_query, keywords, offset, domain_filters, collapse_family, limit, filters, sort | P002 ·低 |
| `ls_patent_vector_search` | 此工具将被 ls_patent_search 替代。推荐调用 ls_patent_search(semantic_query="EGFR inhibitor", limit=20)；将 query 改为 semantic | **query**, top_k, **lang** | — ·工作流不可推断 |
| `ls_target_fetch` | 通过靶点ID或靶点名称批量获取完整的靶点详情记录。 | target_ids, target | — ·工作流不可推断 |
| `ls_translational_medicine_fetch` | 通过转化医学ID批量获取完整的详情记录。 | **translational_medicine_ids** | — ·工作流不可推断 |
| `ls_translational_medicine_search` | 搜索转化医学信息。当用户需要通过药物、靶点、疾病、申办方或发表时间窗口查找转化医学记录时使用。适用于实体提取后的结构化跟进查询，例如按特定疾病领域、申办方或发表时间窗口缩小结果范围。 | field_options, mechanism_action, published_date_to, disease, offset, drug_type, organization, limit, published_date_from, drug, target | — ·待确认 |
| `ls_web_search` | 搜索网络实时信息。当用户需要搜索特定主题的网络实时信息时使用，返回相关网络搜索结果列表。 | **query** | — ·待确认 |
| `ls_news_fetch` | 通过新闻ID批量获取完整的新闻详情记录。 | **news_ids** | — ·工作流不可推断 |
| `ls_financial_report_vector_search` | 向量相似度搜索财务报告。使用语义相似度搜索财务报告和招股说明书，适用于复杂的自然语言查询，调用统一向量搜索接口并返回相关文本片段。 | **query**, top_k, **lang** | — ·工作流不可推断 |
| `ls_clinical_guideline_vector_search` | 向量相似度搜索临床指南。使用语义相似度搜索临床指南，适用于复杂的自然语言查询，调用统一向量搜索接口并返回相关文本片段。 | **query**, top_k, **lang** | — ·工作流不可推断 |
| `ls_epidemiology_vector_search` | 向量相似度搜索流行病学数据。使用语义相似度搜索流行病学内容，适用于复杂的自然语言查询，调用统一向量搜索接口并返回相关文本片段。 | **query**, top_k, **lang** | — ·工作流不可推断 |
| `ls_drug_search` | 搜索药物信息。当用户需要通过药物名称、靶点、疾病、机构、开发阶段或里程碑日期查找药物资产时使用。适用于结构化管线筛选，例如"中国三期PD-1药物"或"某公司已获批药物"。 | field_options, mechanism_action, country, atc_code, highest_phase, disease, dev_status, offset, action_type, org_type, modification, drug, target, highest_phase_date_from, organization, drug_type, highest_phase_date_to, limit | — ·待确认 |
| `ls_drug_fetch` | 通过药物ID或药物名称批量获取完整的药物详情记录。 | drug_ids, drug | — ·工作流不可推断 |
| `ls_drug_deal_search` | 搜索药物交易信息。当用户需要查找与药物、靶点、疾病或公司相关的许可、合作、收购或期权交易时使用。适用于结构化商务拓展查询，例如"2021年后美国ADC许可交易"或"涉及诺华的KRAS二期交易"。 | field_options, phase, mechanism_action, country, licensee, offset, deal_type, licensor, deal_disease, deal_date_from, drug, target, deal_date_to, drug_type, drug_disease, limit | — ·待确认 |
| `ls_drug_deal_fetch` | 通过交易ID批量获取完整的药物交易详情记录。 | **drug_deal_ids** | — ·工作流不可推断 |
| `ls_disease_fetch` | 通过疾病ID或疾病名称批量获取完整的疾病详情记录。 | disease, disease_ids | — ·工作流不可推断 |
| `ls_clinical_trial_vector_search` | 向量相似度搜索临床试验。使用语义相似度搜索临床试验，适用于复杂的自然语言查询，调用统一向量搜索接口并返回相关文本片段。 | **query**, top_k, **lang** | — ·工作流不可推断 |
| `ls_clinical_trial_search` | 搜索临床试验信息。当用户需要通过研究药物、对照药物、靶点、疾病、申办方、阶段或地区检索已注册临床试验时使用。适用于结构化试验筛选，例如"美国EGFR二期试验"或"默克申办的PD-1研究"。 | field_options, phase, mechanism_action, country, study_first_posted_date_from, disease, study_identifier, offset, route_of_administration, brief_title, study_status, drug, target, dosage_form, drug_type, organization, limit, register_number, study_first_posted_date_to, therapeutic_area, control_drug | — ·待确认 |
| `ls_clinical_trial_result_search` | 搜索临床试验结果信息。当用户需要通过药物、靶点、疾病、申办方、阶段或评估结论检索已发布或已收录的临床试验结果时使用。适用于以结果为中心的问题，例如"黑色素瘤PD-1三期试验结果"或"2022年后EGFR阳性试验读出"。 | field_options, phase, mechanism_action, disease, offset, drug, target, published_date_to, drug_type, organization, limit, register_number, therapeutic_area, control_drug, published_date_from, study_code | — ·待确认 |
| `ls_clinical_trial_result_fetch` | 通过临床试验结果ID批量获取完整的详情记录。 | **result_ids** | — ·工作流不可推断 |
| `ls_clinical_trial_fetch` | 通过临床试验ID或注册号批量获取完整的临床试验详情记录。 | trial_ids, registration_number | — ·工作流不可推断 |

### `biology-modality` · 分支

- **名称**：生物序列 / Biology Modality
- **官方分类**：`Life-Sciences` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：11 · **上下文权重**：`medium`
- **MCP 地址**：`https://connect.zhihuiya.com/06e741/logic-mcp`
- **能力**：生物序列智能平台，涵盖生物序列分析、蛋白质与核苷酸搜索、翻译后修饰分析、抗体-抗原相互作用发现以及多组学生物实体检索。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `ls_patent_fetch` | 通过专利ID或专利号批量获取完整的专利详情记录。 | patent_ids, pn | — ·待确认 |
| `ls_patent_search` | 通过语义、关键词和结构化生命科学条件搜索专利。根据 semantic_query、keywords、filters/domain_filters 自动选择检索方式；不接受 domain 或布尔检索。limit 为 1–1 | semantic_query, keywords, offset, domain_filters, collapse_family, limit, filters, sort | — ·待确认 |
| `ls_sequence_search` | 统一序列与修饰条件检索入口，支持等待、续查和分页。search.search_type 默认为 SEQUENCE，须提供 sequence_type、query_type、sequence；MODIFICATION 模式 | result_options, wait_timeout_seconds, search, job_id | — ·工作流不可推断 |
| `ls_patent_sequence_fetch` | 当用户提供专利 `patent_id` 或专利号 `pn` 时使用，可通过 `sequence_number` 筛选指定序列，并支持分页查询。 filter_claimed=true 时仅返回 claimed=true  | sequence_number, patent_id, offset, limit, filter_claimed, pn | — ·待确认 |
| `ls_sequence_alignment` | 对生物序列进行比对。当用户需要进行成对比对（PSA）或多序列比对（MSA）时使用。成对比对需要提供 `query_sequence`。 | **sequence_type**, query_sequence, **alignment_type**, **sequences** | — ·工作流不可推断 |
| `ls_sequence_fetch` | 当用户提供序列号列表时使用。单次最多 100 个序列号。 | **sequence_numbers** | — ·工作流不可推断 |
| `ls_antibody_antigen_search` | 当用户需要查找与特定抗原靶点相关的抗体，并可选择通过facet过滤器缩小结果范围时使用。 | filter, **target_name**, offset, limit | — ·工作流不可推断 |
| `ls_modification_search_submit` | 即将弃用，推荐使用 ls_sequence_search 替代。通过修饰条件搜索生物序列记录，可选择性地通过序列长度或查询序列缩小结果范围。 | sequence, **sequence_type**, **database**, subject_length, **modification_location**, limit | — ·工作流不可推断 |
| `ls_sequence_search_check_status` | 即将弃用，推荐使用 ls_sequence_search 替代。在提交序列或修饰搜索任务后使用此工具轮询任务状态。 | **job_id** | — ·工作流不可推断 |
| `ls_sequence_search_get_results` | 即将弃用，推荐使用 ls_sequence_search 替代。在ls_sequence_search_check_status返回成功状态后使用此工具获取结果。 | qcov_hsp_perc, perc_identity, offset, sort_field, scov_hsp_perc, q_perc_identity, **job_id**, limit, s_perc_identity, order | — ·工作流不可推断 |
| `ls_sequence_search_submit` | 即将弃用，推荐使用 ls_sequence_search 替代。提交后获取job_id，再通过ls_sequence_search_check_status轮询状态，成功后调用ls_sequence_search_get | qcov_hsp_perc, perc_identity, scov_hsp_perc, evalue, **query_type**, **sequence**, **sequence_type**, database, strand, subject_length, q_perc_identity, with_gaps, s_perc_identity, limit, has_modification | — ·工作流不可推断 |

### `chemical-molecular` · 分支

- **名称**：化学分子 / Chemical Molecular
- **官方分类**：`Life-Sciences` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：7 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/713886/logic-mcp`
- **能力**：化学分子智能平台，涵盖化合物搜索、结构分析、理化性质检索以及分子相互作用分析。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `ls_patent_fetch` | 通过专利ID或专利号批量获取完整的专利详情记录。 | patent_ids, pn | — ·待确认 |
| `ls_patent_search` | 通过语义、关键词和结构化生命科学条件搜索专利。根据 semantic_query、keywords、filters/domain_filters 自动选择检索方式；不接受 domain 或布尔检索。limit 为 1–1 | semantic_query, keywords, offset, domain_filters, collapse_family, limit, filters, sort | — ·待确认 |
| `ls_patent_structure_fetch` | 批量获取与专利相关的化学结构。当用户提供 `patent_id` 或 `pn`（专利号）时使用，并支持分页查询。 | patent_id, offset, limit, pn | — ·待确认 |
| `ls_structure_fetch` | 当用户提供一组 `InChIKey` 标识符时使用。单次请求最多 100 个标识符。 | **inchi_keys** | — ·工作流不可推断 |
| `ls_structure_search` | 当用户需要通过化学结构搜索化合物时使用。使用SMILES格式提供查询结构，支持精确（EXT）和相似性（SIM）两种搜索类型。 | include_isotope, offset, **smiles**, include_charge, include_multi_component, limit, include_stereo, threshold, **type**, include_radical | — ·工作流不可推断 |
| `ls_admet_predict` | 预测小分子的ADMET属性。当用户需要评估小分子的类药性或药代动力学属性时使用，调用ADMET-AI模型预测每个输入SMILES的吸收、分布、代谢、排泄和毒性属性。 | **smiles** | — ·工作流不可推断 |
| `ls_chemical_mcs_analyze` | 从多个化学结构中分析高频片段组成。当用户需要从一组SMILES结构中分析高频片段分布时使用，返回每个片段在输入结构中出现的次数。 | **structures** | — ·工作流不可推断 |

### `clinical-trials` · 分支

- **名称**：临床试验 / Clinical Trials
- **官方分类**：`Life-Sciences` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：4 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/051cd3/logic-mcp`
- **能力**：临床试验智能检索系统，涵盖注册试验追踪、试验详情与结果分析，并支持临床医学语义检索。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `clinical_trial_fetch` | 通过临床试验ID或注册号批量获取完整的临床试验详情记录。 | trial_ids, registration_number | — ·工作流不可推断 |
| `clinical_trial_result_fetch` | 通过临床试验结果ID批量获取完整的详情记录。 | **result_ids** | — ·工作流不可推断 |
| `clinical_trial_result_search` | 搜索临床试验结果信息。当用户需要通过药物、靶点、疾病、申办方、阶段或评估结论检索已发布或已收录的临床试验结果时使用。适用于以结果为中心的问题，例如"黑色素瘤PD-1三期试验结果"或"2022年后EGFR阳性试验读出"。 | field_options, phase, mechanism_action, disease, offset, drug, target, published_date_to, drug_type, organization, limit, register_number, therapeutic_area, control_drug, published_date_from, study_code | — ·待确认 |
| `clinical_trial_search` | 搜索临床试验信息。当用户需要通过研究药物、对照药物、靶点、疾病、申办方、阶段或地区检索已注册临床试验时使用。适用于结构化试验筛选，例如"美国EGFR二期试验"或"默克申办的PD-1研究"。 | field_options, phase, mechanism_action, country, study_first_posted_date_from, disease, study_identifier, offset, route_of_administration, brief_title, study_status, drug, target, dosage_form, drug_type, organization, limit, register_number, study_first_posted_date_to, therapeutic_area, control_drug | — ·待确认 |

### `company-deal-intelligence` · 分支

- **名称**：公司与交易情报 / Company & Deal Intelligence
- **官方分类**：`Life-Sciences` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：5 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/1f8934/logic-mcp`
- **能力**：医药企业无形资产与商业情报档案工具，涵盖组织画像、研发管线、交易记录及财报证据查询。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `drug_deal_fetch` | 通过交易ID批量获取完整的药物交易详情记录。 | **drug_deal_ids** | — ·工作流不可推断 |
| `drug_deal_search` | 搜索药物交易信息。当用户需要查找与药物、靶点、疾病或公司相关的许可、合作、收购或期权交易时使用。适用于结构化商务拓展查询，例如"2021年后美国ADC许可交易"或"涉及诺华的KRAS二期交易"。 | field_options, phase, mechanism_action, country, licensee, offset, deal_type, licensor, deal_disease, deal_date_from, drug, target, deal_date_to, drug_type, drug_disease, limit | — ·待确认 |
| `financial_report_search` | 向量相似度搜索财务报告。使用语义相似度搜索财务报告和招股说明书，适用于复杂的自然语言查询，调用统一向量搜索接口并返回相关文本片段。 | **query**, top_k, **lang** | — ·工作流不可推断 |
| `organization_fetch` | 通过机构ID或机构名称批量获取完整的机构详情记录。 | organization, organization_ids | — ·工作流不可推断 |
| `organization_pipeline_fetch` | 获取指定机构的药物研发管线信息（含在研药物、靶点、疾病以及按国家维度的开发状态）。当用户已知 `organization_id` 或提供机构名称 `organization` 时使用。必须提供二者之一。 | offset, organization_id, organization, limit | — ·待确认 |

### `current-awareness` · 分支

- **名称**：行业动态 / 最新资讯 / Current Awareness
- **官方分类**：`Life-Sciences` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：2 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/401c6d/logic-mcp`
- **能力**：医药行业动态与前沿资讯追踪系统，涵盖全球医药新闻检索与新闻详情深度挖掘。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `news_fetch` | 通过新闻ID批量获取完整的新闻详情记录。 | **news_ids** | — ·工作流不可推断 |
| `news_search` | 检索生命科学新闻记录并获取有效新闻 ID。支持按全文关键词、药物、靶点、疾病、机构、药物类型和发布日期区间进行结构化检索，同一字段内多个值可配置 AND 或 OR 关系。 | field_options, disease, offset, post_date_to, organization, drug_type, post_date_from, limit, keyword, drug, target | — ·待确认 |

### `drug-asset` · 分支

- **名称**：药物与资产 / Drug & Asset
- **官方分类**：`Life-Sciences` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：4 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/30cd71/logic-mcp`
- **能力**：药物与资产情报检索平台，涵盖药物搜索、药物详情分析及研发里程碑追踪。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `adc_search` | 检索 ADC 药物及其技术组成，支持按 ADC 药物名称，或抗体/靶向部分靶点、Linker、Payload、Payload 靶点、抗体组分药物、靶向部分类型等技术条件检索，返回标准化的 ADC 技术结构与参考来源。 | field_options, linker, offset, payload, target_moiety_type, limit, payload_target, antibody_drug, moiety_target, drug | — ·工作流不可推断 |
| `drug_fetch` | 通过药物ID或药物名称批量获取完整的药物详情记录。 | drug_ids, drug | — ·工作流不可推断 |
| `drug_milestone_fetch` | 获取指定药物的研发里程碑历史记录（时间线）。当用户已知 `drug_id` 或提供药物名称 `drug` 时使用。必须提供二者之一。 | drug_id, offset, limit, drug | — ·待确认 |
| `drug_search` | 搜索药物信息。当用户需要通过药物名称、靶点、疾病、机构、开发阶段或里程碑日期查找药物资产时使用。适用于结构化管线筛选，例如"中国三期PD-1药物"或"某公司已获批药物"。 | field_options, mechanism_action, country, atc_code, highest_phase, disease, dev_status, offset, action_type, org_type, modification, drug, target, highest_phase_date_from, organization, drug_type, highest_phase_date_to, limit | — ·待确认 |

### `regulatory-guidelines` · 分支

- **名称**：监管与指南 / Regulatory & Guidelines
- **官方分类**：`Life-Sciences` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：2 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/6415c2/logic-mcp`
- **能力**：面向监管政策与临床规范的证据查询工具，涵盖临床指南和 FDA 药品说明书等语义证据检索。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `clinical_guideline_search` | 向量相似度搜索临床指南。使用语义相似度搜索临床指南，适用于复杂的自然语言查询，调用统一向量搜索接口并返回相关文本片段。 | **query**, top_k, **lang** | — ·工作流不可推断 |
| `fda_label_search` | 向量相似度搜索FDA药品标签。使用语义相似度搜索FDA药品标签，适用于复杂的自然语言查询，调用统一向量搜索接口并返回相关文本片段。 | **query**, top_k, **lang** | — ·工作流不可推断 |

### `sar-extraction` · 分支

- **名称**：SAR 提取 / SAR Extraction
- **官方分类**：`Life-Sciences` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：2 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/c8ffec/logic-mcp`
- **能力**：聚焦小分子专利文献的深度解析系统，专为长周期任务设计，支持 SAR 数据的自动化提取。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `sar_fetch` | SAR数据获取。用于提交SAR提取任务的ID，获取小分子专利文献中的化学结构与活性关系数据，应用于药物开发早期的结构筛选与专利风险预警。 | **task_id** | — ·工作流不可推断 |
| `sar_submit` | SAR任务提交。根据用户输入的小分子专利公开号启动SAR数据提取任务，并生成唯一任务ID供后续查询与跟踪。 | language, **pn** | — ·待确认 |

### `scientific-translational-evidence` · 分支

- **名称**：科学与转化证据 / Scientific & Translational Evidence
- **官方分类**：`Life-Sciences` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：2 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/9c333c/logic-mcp`
- **能力**：聚焦科学文献与转化成果的检索平台，涵盖学术论文查询和转化医学记录追踪。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `translational_medicine_fetch` | 通过转化医学ID批量获取完整的详情记录。 | **translational_medicine_ids** | — ·工作流不可推断 |
| `translational_medicine_search` | 搜索转化医学信息。当用户需要通过药物、靶点、疾病、申办方或发表时间窗口查找转化医学记录时使用。适用于实体提取后的结构化跟进查询，例如按特定疾病领域、申办方或发表时间窗口缩小结果范围。 | field_options, mechanism_action, published_date_to, disease, offset, drug_type, organization, limit, published_date_from, drug, target | — ·待确认 |

### `target-disease` · 分支

- **名称**：靶点与疾病 / Target & Disease
- **官方分类**：`Life-Sciences` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：3 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/2a2645/logic-mcp`
- **能力**：靶点与疾病画像分析工具，涵盖靶点特征分析、疾病画像构建以及流行病学证据检索。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `disease_fetch` | 通过疾病ID或疾病名称批量获取完整的疾病详情记录。 | disease, disease_ids | — ·工作流不可推断 |
| `epidemiology_search` | 向量相似度搜索流行病学数据。使用语义相似度搜索流行病学内容，适用于复杂的自然语言查询，调用统一向量搜索接口并返回相关文本片段。 | **query**, top_k, **lang** | — ·工作流不可推断 |
| `target_fetch` | 通过靶点ID或靶点名称批量获取完整的靶点详情记录。 | target_ids, target | — ·工作流不可推断 |

## 金融（`finance`，8 个 MCP）

### `company-profile` · 🌳 主干

- **名称**：企业科技360档案 / Company 360 Tech Profile
- **官方分类**：`Finance` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：24 · **上下文权重**：`high`
- **MCP 地址**：`https://connect.zhihuiya.com/e7d2b1/mcp`
- **能力**：提供企业科技相关信息的 360 度档案。可综合查看工商、股东、资质证书、科技资质、专利价值、专利转移、标准、软著等多类信息，帮助团队从经营主体、技术实力和无形资产多个维度理解企业。适合用于客户研究、项目尽调和销售支持。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `patent_legal_status` | 用于获取法律状态相关信息，便于判断专利状态变化、专利稳定性及潜在法律风险。 | patent_id, patent_number | P013 ·高 |
| `technology_qualification` | 用于获取科技资质相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number | C014 ·高 |
| `standard_information` | 用于获取标准信息相关数据，便于评估标准参与情况、制定进展和行业影响力。 | page_number, standard_type, company_name, credit_code, org_number | C020 ·高 |
| `shareholder_information` | 用于获取股东信息相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number | C003 ·高 |
| `registration_information` | 用于获取工商信息相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number | C001 ·高 |
| `qualification_certificate` | 用于获取资质证书相关数据，便于快速查看核心信息并支持后续分析。 | page_number, company_name, credit_code, org_number | C021 ·高 |
| `patent_valuation` | 用于获取专利价值相关数据，便于从多个维度做企业、专利或项目评估。 | patent_id, patent_number | P035 ·高 |
| `patent_transfer_data` | 用于获取专利转移相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, patent_number | P029 ·高 |
| `patent_simple_bibliography` | 用于获取简单著录项相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | patent_id, patent_number | P011 ·高 |
| `patent_reexamination` | 用于获取复审无效相关信息，便于判断专利状态变化、专利稳定性及潜在法律风险。 | patent_id, patent_number | P027 ·高 |
| `patent_pledge_data` | 用于获取专利质押相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, patent_number | P030 ·高 |
| `patent_license_data` | 用于获取专利许可相关数据，便于快速查看核心信息并支持后续分析。 | patent_id, patent_number | P028 ·高 |
| `awards_information` | 用于获取获奖信息相关数据，便于了解主体或专利的荣誉情况和外部认可度。 | company_name, credit_code, org_number | C015 ·高 |
| `outbound_investment` | 用于获取对外投资相关数据，便于了解企业资本运作、融资进展和市场化情况。 | company_name, credit_code, org_number | C002 ·高 |
| `listing_information` | 用于获取上市信息相关数据，便于了解企业资本运作、融资进展和市场化情况。 | company_name, credit_code, org_number | C018 ·高 |
| `ipo_process` | 用于获取IPO进程相关数据，便于了解企业资本运作、融资进展和市场化情况。 | company_name, credit_code, org_number | C019 ·高 |
| `industry_classification` | 用于获取行业分类相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number | C007 ·高 |
| `get_company_tech_eval_indicators_global` | 用于获取科创企业评估指标（全球）相关数据，便于从多个维度做企业、专利或项目评估。 | company_name, credit_code, org_number | C024 ·高 |
| `get_company_tech_eval_backtrack_global` | 用于获取科创企业回溯（全球）相关数据，便于快速查看核心信息并支持后续分析。 | date, company_name, credit_code, org_number | C026 ·高 |
| `get_company_attribute` | 用于获取企业属性相关数据，便于快速识别主体特征并进行筛选。 | company_name, credit_code, org_number | C004 ·高 |
| `financing_information` | 用于获取融资信息相关数据，便于了解企业资本运作、融资进展和市场化情况。 | company_name, credit_code, org_number | C013 ·高 |
| `enterprise_trademark` | 用于获取获取科创企业商标数据相关数据，便于快速查看核心信息并支持后续分析。 | mode, nice_code, apdt, reg_num, size, app_num, page, mark, applicant, ipoffice, status | — ·工作流不可推断 |
| `enterprise_software_copyright` | 用于获取获取科创企业软件著作权数据相关数据，便于快速查看核心信息并支持后续分析。 | page_number, company_name, credit_code, org_number, page_size | — ·待确认 |
| `core_member` | 用于获取核心团队相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number | C017 ·高 |

### `company-credit` · 分支

- **名称**：企业工商信用档案 / Corporate Registry & Credit Profile
- **官方分类**：`Finance` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：14 · **上下文权重**：`medium`
- **MCP 地址**：`https://connect.zhihuiya.com/ed1a0d/mcp`
- **能力**：聚焦企业工商、资质、团队、投资和信用信息的基础档案工具。可用于快速核验企业主体情况、上市与 IPO 进程、核心团队、投资记录和多类资质，为合作评估和商业审查提供基础依据。适合用于客户准入、合作核查和风险排查。
- **工具重复**：可替代 company-profile

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `awards_information` | 用于获取获奖信息相关数据，便于了解主体或专利的荣誉情况和外部认可度。 | company_name, credit_code, org_number | C015 ·高 |
| `core_member` | 用于获取核心团队相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number | C017 ·高 |
| `financing_information` | 用于获取融资信息相关数据，便于了解企业资本运作、融资进展和市场化情况。 | company_name, credit_code, org_number | C013 ·高 |
| `investment_information` | 用于获取投资信息相关数据，便于了解企业资本运作、融资进展和市场化情况。 | company_name, credit_code, org_number | C038 ·高 |
| `ipo_process` | 用于获取IPO进程相关数据，便于了解企业资本运作、融资进展和市场化情况。 | company_name, credit_code, org_number | C019 ·高 |
| `listing_information` | 用于获取上市信息相关数据，便于了解企业资本运作、融资进展和市场化情况。 | company_name, credit_code, org_number | C018 ·高 |
| `main_member` | 用于获取主要人员相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number | C016 ·高 |
| `outbound_investment` | 用于获取对外投资相关数据，便于了解企业资本运作、融资进展和市场化情况。 | company_name, credit_code, org_number | C002 ·高 |
| `qualification_certificate` | 用于获取资质证书相关数据，便于快速查看核心信息并支持后续分析。 | **page_number**, standard_type, company_name, credit_code, org_number | C021 ·高 |
| `registration_information` | 用于获取工商信息相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number | C001 ·高 |
| `search_company` | 用于企业搜索，返回匹配结果，便于快速筛选、比对和继续分析。 | country, founded_date_lower, city, reg_capital_upper, rating_global, rating, is_patent, key_word, province, reg_capital_lower, seic_lv2, seic_lv1, social_staff_num_upper, founded_date_upper, level, tech_tags, is_patsnap_company, gbc_lv1, list_status, gbc_lv2, social_staff_num_lower, **page_number**, **sort_field**, district, fin_process, entity_status | C037 ·中 |
| `shareholder_information` | 用于获取股东信息相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number | C003 ·高 |
| `standard_information` | 用于获取标准信息相关数据，便于评估标准参与情况、制定进展和行业影响力。 | **page_number**, standard_type, company_name, credit_code, org_number | C020 ·高 |
| `technology_qualification` | 用于获取科技资质相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number | C014 ·高 |

### `company-intelligence-mcp` · 分支

- **名称**：智慧芽企业科创力评估 / PatSnap Company Intelligence
- **官方分类**：`Finance` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：6 · **上下文权重**：`medium`
- **MCP 地址**：`https://connect.zhihuiya.com/2b74fe/mcp`
- **能力**：智慧芽企业科创力评估 MCP 面向 AI Agent、开发者及业务系统，提供企业主体查询与筛选、科创概要、公司竞争力分析、科技创新能力评估、技术风险识别及评估报告生成能力。支持通过企业名称、企业 ID、统一社会信用代码或组织机构代码确认企业主体，也支持按地区、行业、注册信息、科创评级、融资阶段和专利条件筛选企业。分析结果覆盖近十年创新趋势、研发稳定性、技术布局、技术质量、技术影响力及专利相关风险，可用于企业科创研究和技术尽调辅助，不构成法律、投资、信贷、资助、合作或采购建议。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `analyze_company_competitiveness` | 分析企业股权穿透、公司树、工商与经营基本面、核心团队、科技资质及融资情况，辅助评估公司竞争力与主体结构；可按维度选择，并返回覆盖状态与错误。 | **company_id**, certificate_limit, include_dimensions, locale | — ·工作流不可推断 |
| `analyze_innovation_capability` | 从研发规模与稳定性、技术布局、技术质量及技术影响力等维度，结合创新数据趋势综合评估企业科技创新能力、持续稳定性与成长潜力；可按维度选择，并返回覆盖状态与错误。 | **company_id**, include_dimensions, locale | — ·工作流不可推断 |
| `generate_innovation_report` | 基于一个或多个已调用分析 Tool 的完整结果，仅为实际传入的 Tool 结果生成对应的、有证据约束的企业科技创新能力与技术风险评估模块卡片，并返回有效期一周的自包含 HTML 地址；本 Tool 不再内部取数。 | country, **company_id**, **tool_results**, entity_scope, locale, decision_purpose | — ·工作流不可推断 |
| `get_innovation_overview` | 提供企业科创概要，包括国内/全球科创评级、行业排名、能力维度、技术主题、产业链、概要风险及近十年创新评分趋势。 | **company_id**, include_sections, locale | — ·工作流不可推断 |
| `get_risk_information` | 基于专利质押、转让、无效、诉讼、保全及诉讼专题等信号，提供研发与技术风险识别、分析和预警支持。 | **company_id**, include_sections, locale, detail_limit | — ·工作流不可推断 |
| `search_company` | 支持通过企业名称、统一社会信用代码等标识确认唯一企业主体，或按地区、行业、注册信息、科创评级、融资阶段等多维条件筛选和发现目标企业；主体确认与条件筛选两种策略不能混用。 | country, candidate_limit, pagination, company_id, credit_code, org_number, name, location, filters, locale, keyword | — ·工作流不可推断 |

### `company-risk` · 分支

- **名称**：企业科技评估与风险 / Enterprise Tech Evaluation & Risk
- **官方分类**：`Finance` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：5 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/624fc7/mcp`
- **能力**：将企业科技评估与风险预警放在同一视图中，帮助用户同时看“实力”和“风险”。可输出评估结果、关键指标和风险信号，便于快速识别高技术价值企业及需要重点关注的问题。适合用于投前尽调、授信评估、客户分层和风险管理。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `enterprise_indicators` | 用于获取科创企业指标相关数据，便于从多个维度做企业、专利或项目评估。 | company_name, credit_code, org_number | DP002 ·高 |
| `enterprise_risk_warning` | 用于获取科创企业风险预警相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number | DP003 ·高 |
| `enterprise_valuation` | 用于获取科创企业评估相关数据，便于从多个维度做企业、专利或项目评估。 | company_name, credit_code, org_number | DP001 ·高 |
| `enterprise_valuation_full` | 用于获取科创企业评估指标&风险预警相关数据，便于从多个维度做企业、专利或项目评估。 | company_name, credit_code, org_number | DP004 ·高 |
| `enterprise_valuation_with_indicators` | 用于获取科创企业评估指标相关数据，便于从多个维度做企业、专利或项目评估。 | company_name, credit_code, org_number | DP005 ·高 |

### `company-tags` · 分支

- **名称**：企业科技标签画像 / Enterprise Tech Profile Tags
- **官方分类**：`Finance` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：8 · **上下文权重**：`medium`
- **MCP 地址**：`https://connect.zhihuiya.com/3cfbf5/mcp`
- **能力**：通过科技认定、知识产权、标准、产业技术链、产品技术分类和企业属性等标签，为企业建立简明清晰的科技画像。帮助用户快速判断企业属于什么类型、拥有哪些技术特征以及在产业中的位置。适合用于客户分层、线索筛选和画像补充。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `company_awards` | 用于获取获奖情况相关数据，便于了解主体或专利的荣誉情况和外部认可度。 | company_name, credit_code, org_number | C006 ·高 |
| `get_company_attribute` | 用于获取企业属性相关数据，便于快速识别主体特征并进行筛选。 | company_name, credit_code, org_number | C004 ·高 |
| `industrial_technology_chain` | 用于获取产业技术链相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number | — ·待确认 |
| `industry_classification` | 用于获取行业分类相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number | C007 ·高 |
| `intellectual_property` | 用于获取知识产权相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number | C011 ·高 |
| `product_technical_classification` | 用于获取产品技术分类相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number | C008 ·高 |
| `standard_development` | 用于获取标准制定相关数据，便于评估标准参与情况、制定进展和行业影响力。 | company_name, credit_code, org_number | C010 ·高 |
| `technology_label` | 用于获取科技认定相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number | C005 ·高 |

### `global-tech-eval` · 分支

- **名称**：全球企业科技评估 / Global Enterprise Tech Evaluation
- **官方分类**：`Finance` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：8 · **上下文权重**：`medium`
- **MCP 地址**：`https://connect.zhihuiya.com/ac58e5/mcp`
- **能力**：面向全球企业的科技实力评估与风险识别工具。可查看全球评估结果、关键指标、集团穿透、历史回溯和专利风险趋势，帮助团队在跨区域场景下更一致地比较企业科技能力。适合用于国际合作筛选、海外尽调和全球客户研究。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `global_company_group_eval` | 用于获取科创企业集团穿透（全球）相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number | C025 ·高 |
| `patent_risk_warning` | 用于获取企业专利风险预警相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number | C027 ·高 |
| `patent_risk_warning_backtrack` | 用于获取企业专利风险预警回溯相关数据，便于快速查看核心信息并支持后续分析。 | **date**, company_name, credit_code, org_number | C028 ·高 |
| `patent_risk_warning_trend` | 用于分析企业专利风险预警趋势，帮助判断活跃度变化、重点主体和发展方向。 | company_name, credit_code, org_number | — ·待确认 |
| `technology_evaluation_global` | 用于获取科创企业评估（全球）相关数据，便于从多个维度做企业、专利或项目评估。 | company_name, credit_code, org_number | C022 ·高 |
| `technology_indicators_global` | 用于获取科创企业指标（全球）相关数据，便于从多个维度做企业、专利或项目评估。 | company_name, credit_code, org_number | C023 ·高 |
| `tech_eval_backtrack_global` | 用于获取科创企业回溯（全球）相关数据，便于快速查看核心信息并支持后续分析。 | **date**, company_name, credit_code, org_number | C026 ·高 |
| `tech_eval_indicators_global` | 用于获取科创企业评估指标（全球）相关数据，便于从多个维度做企业、专利或项目评估。 | company_name, credit_code, org_number | C024 ·高 |

### `patent-risk` · 分支

- **名称**：专利风险趋势监测 / Patent Risk Trend Monitor
- **官方分类**：`Finance` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：3 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/a8a128/mcp`
- **能力**：围绕企业专利风险建立趋势化监测能力。可查看风险预警趋势、历史回溯以及相关企业变化，帮助用户判断风险是短期波动还是持续积累。适合用于客户监控、投后管理、合规预警和持续风控。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `modeling_get_tech_eval_backtracking` | 用于获取科创企业回溯（全球）相关数据，便于快速查看核心信息并支持后续分析。 | date, company_name, credit_code, org_number | C026 ·高 |
| `patent_risk_backtracking` | 用于获取企业专利风险预警回溯相关数据，便于快速查看核心信息并支持后续分析。 | date, company_name, credit_code, org_number | C028 ·高 |
| `patent_risk_trend` | 用于分析企业专利风险预警趋势，帮助判断活跃度变化、重点主体和发展方向。 | company_name, credit_code, org_number | — ·待确认 |

### `tech-diligence` · 分支

- **名称**：科创投资尽调 / Tech Investment Due Diligence
- **官方分类**：`Finance` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：12 · **上下文权重**：`medium`
- **MCP 地址**：`https://connect.zhihuiya.com/3faf81/mcp`
- **能力**：面向投行、PE/VC、产业投资和战略团队的科创尽调工具。可联动企业科技评估、集团股权穿透、专利价值、法律与市场指标、风险预警、融资和行业信息，帮助团队更系统地判断标的的技术实力、商业化潜力和主要风险。适合用于投前筛选、深度尽调、项目立项和投委会材料准备。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `acquisition_get_group_tech_eval` | 用于获取科创企业集团穿透（全球）相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number | C025 ·高 |
| `acquisition_get_tech_eval_indicators` | 用于获取科创企业评估指标（全球）相关数据，便于从多个维度做企业、专利或项目评估。 | company_name, credit_code, org_number | C024 ·高 |
| `company_financing` | 用于获取融资信息相关数据，便于了解企业资本运作、融资进展和市场化情况。 | company_name, credit_code, org_number | C013 ·高 |
| `company_industry` | 用于获取行业分类相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number | C007 ·高 |
| `company_tech_label` | 用于获取科技认定相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number | C005 ·高 |
| `economic_indicators` | 用于获取经济指标相关数据，便于从多个维度做企业、专利或项目评估。 | patent_id, patent_number | P040 ·高 |
| `legal_indicators` | 用于获取法律指标相关数据，便于从多个维度做企业、专利或项目评估。 | patent_id, patent_number | P037 ·高 |
| `market_indicators` | 用于获取市场指标相关数据，便于从多个维度做企业、专利或项目评估。 | patent_id, patent_number | P038 ·高 |
| `patent_risk_warning` | 用于获取企业专利风险预警相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number | C027 ·高 |
| `patent_valuation` | 用于获取专利价值相关数据，便于从多个维度做企业、专利或项目评估。 | patent_id, patent_number | P035 ·高 |
| `strategic_indicators` | 用于获取战略指标相关数据，便于从多个维度做企业、专利或项目评估。 | patent_id, patent_number | P039 ·高 |
| `tech_indicators` | 用于获取技术指标相关数据，便于从多个维度做企业、专利或项目评估。 | patent_id, patent_number | P036 ·高 |

## 材料（`materials`，2 个 MCP）

### `materials-search-mcp` · 🌳 主干

- **名称**：材料搜索 / Materials Search
- **官方分类**：`Material-Science` · **版本**：`v0.1.0` · **状态**：`active` · **tool 数**：2 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/df346b/mcp`
- **能力**：结合标准专利筛选条件、关键词及语义检索，查找包含目标材料名称、性能和合金成分的专利。然后，从专利文献中提取有原文证据支持的材料实体。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `fetch_document_material_evidence` | 从指定专利提取详细材料证据，用于现有技术检索、FTO 评估或材料比较中的成分、性能及来源核对；本工具本身不提供法律分析或权利要求解释。  输入 documents 为 1～10 个专利标识对象，每项包含 id 和 id_ | **documents** | — ·工作流不可推断 |
| `search_material_evidence` | 根据归一化的材料实体及文档级交集检索材料专利。支持合金成分、物质名称和性能名称，尽可能解析为规范的 substance_id/property_id 后检索。  必须同时提供 query 和 search。query 至 | **search**, **query** | — ·工作流不可推断 |

### `mat-cosmetics-regulatory` · 分支

- **名称**：化妆品法规 / Cosmetic regulatory
- **官方分类**：`Material-Science` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：1 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/372ebe/mcp`
- **能力**：覆盖多个国家或地区的化妆品法规查询工具

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `search_ingredient_regulation` | 查询某个INCI/CAS number/常用名在各个国家的法规情况 | **ingredient**, is_semantic, jurisdictions | — ·工作流不可推断 |

## 研发（`rnd`，6 个 MCP）

### `patsnap-search` · 🌳 主干

- **名称**：智慧芽专利&文献融合检索 / PatSnap Patent & Literature Search
- **官方分类**：`R&D-Innovation` · **版本**：`v3.5.0` · **状态**：`active` · **tool 数**：9 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/2b0355/logic-mcp`
- **能力**：搜索全球专利、期刊文献和专业信息，读取专利、文献基本信息及专利生命周期详情，并支持申请人标准化与集团层级确认。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `fetch_literature` | 读取文献基本信息，包括标题、摘要、作者、机构、期刊名等，适合获取文献摘要并进行核实。 | format, language, **paper_id** | — ·待确认 |
| `fetch_patent` | 按内部专利 ID 或公开号读取单件专利基本信息，例如标题、摘要、申请人、分类号和当前法律状态。 | **patent_id**, include, format, language | — ·待确认 |
| `fetch_patent_lifecycle` | 读取法律事件、年费、转让、许可、质押、诉讼、复审等生命周期信息，适合法律状态监测、交易风险评估和组合维护。 | **patent_id**, format, language | — ·待确认 |
| `build_patent_boolean_query` | 将完整的自然语言专利检索意图转换为可执行的 PatSnap Boolean 字段检索式。该工具只构造检索式，不检索专利；请将返回的 data.boolean_query 原样传给 search_patent，并设置 se | **text** | — ·待确认 |
| `describe_search_capability` | 描述指定专业专利检索领域支持的过滤字段、返回字段、操作符及操作数结构。使用非 general 的 domain 前应先调用；该工具只返回能力元数据，不执行专利检索。 | **domain**, corpus | — ·工作流不可推断 |
| `get_corptree_hierarchy` | 按已确认的 company_id 找到其直属父节点或根节点；不检索专利。 | company_filter, **company_id**, offset, max_depth, limit, direction | — ·工作流不可推断 |
| `get_standard_assignee_name` | 根据未确认专利申请人/权利人的公司或机构名称关键词，推荐company_id、ans_id、标准名称及匹配证据；不检索专利。 | **query**, limit | — ·工作流不可推断 |
| `search_literature` | 检索全球期刊文献库，支持语义、关键词和结构化过滤；可按作者、机构、发表日期和被引次数等条件筛选，并返回分页结果与元数据 | semantic_query, offset, keywords, search_strategy, limit, sort, filters | — ·待确认 |
| `search_patent` | 检索全球专利，支持语义、关键词、结构化过滤和 PatSnap 布尔检索，返回按相关性或指定字段排序的分页结果与元数据。collapse_family 默认为 false，设为 true 时每个专利同族返回一条结果；Boo | semantic_query, offset, keywords, search_strategy, collapse_family, domain_filters, domain, limit, sort, filters, boolean_query | — ·待确认 |

### `literature-search` · 分支

- **名称**：科研文献与期刊 / Scientific Literature & Journals
- **官方分类**：`R&D-Innovation` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：5 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/eba075/mcp`
- **能力**：提供科研文献、期刊、作者、机构和引用信息的统一检索入口。帮助用户快速找到相关研究、识别核心作者与机构，并理解一项研究的引用影响力。适合用于课题调研、文献综述、学术情报和选题支持。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `literature_author_affiliation` | 用于获取文献作者和机构相关数据，便于快速查看核心信息并支持后续分析。 | paper_id, doi | L011 ·高 |
| `literature_bibliography` | 用于获取文献著录信息相关的详细内容，便于核查原始字段、阅读全文和深入分析。 | paper_id, doi | L010 ·高 |
| `literature_citation` | 用于获取文献引用相关数据，便于快速查看核心信息并支持后续分析。 | page_number, paper_id, doi | L012 ·高 |
| `literature_journal` | 用于获取文献期刊相关数据，便于快速查看核心信息并支持后续分析。 | paper_id, doi | L014 ·高 |
| `search_literature` | 用于文献检索，返回匹配结果，便于快速筛选、比对和继续分析。 | date_time, offset, limit, text, type, query_text | L001 ·中 |

### `patsnap-solution-engine` · 分支

- **名称**：TRIZ概念方案生成 / patsnap-solution-engine
- **官方分类**：`R&D-Innovation` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：6 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/c18800/mcp`
- **能力**：面向研发难题攻关与产品降本的 TRIZ 概念方案生成 MCP。系统根据任务目标进入创新攻关或研发降本工作流：前者通过问题分析、案例匹配与 TRIZ 方法生成创新概念方案；后者基于产品结构、功能和成本信息，运用 TRIZ／DFMA 诊断与裁剪生成降本方案及收益测算。支持任务进度跟踪、候选方案获取和方案详情查询，帮助企业 Agent 高效产出可评估的概念方案。单次完整方案生成通常需要约 5–10 分钟，实际耗时可能因任务复杂度、输入信息完整度及系统负载有所浮动，请预留相应处理时间。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `fetch_triz_innovation_task_stream` | 根据创新任务的 job_id 流式获取异步执行进度、工具输出、助手消息和最终候选概念方案，并返回创新分析过程中的结构化模块结果。 | **job_id** | — ·工作流不可推断 |
| `fetch_triz_reduction_task_stream` | 根据降本任务的 job_id 流式获取异步执行进度、工具输出、助手消息和最终候选降本方案，并返回成本分析、裁剪分析及 DFMA 等结构化模块结果。 | **job_id** | — ·工作流不可推断 |
| `fetch_triz_innovation_solution_detail` | 根据创新任务的 job_id 和候选方案 idea_id，生成或获取选定创新概念方案的详细内容。 | **job_id**, **idea_id** | — ·工作流不可推断 |
| `fetch_triz_reduction_solution_detail` | 根据降本任务的 job_id 和候选方案 idea_id，生成或获取选定 TRIZ／DFMA 降本概念方案的详细内容。 | **job_id**, **idea_id** | — ·工作流不可推断 |
| `run_triz_innovation_task` | 创建并提交 TRIZ 创新任务。任务以自动模式在后台运行，中间选择点自动采用最高优先级选项；返回 job_id 后应调用 fetch_triz_innovation_task_stream 获取进度和候选概念方案。CN  | **user_input** | AI33-1 ·低 |
| `run_triz_reduction_task` | 创建并提交 TRIZ／DFMA 降本任务。任务以自动模式在后台运行，中间选择点自动采用最高优先级选项；返回 job_id 后应调用 fetch_triz_reduction_task_stream 获取进度和候选降本方案 | **user_input** | — ·工作流不可推断 |

### `patsnap-triz-case-library` · 分支

- **名称**：TRIZ案例库 / patsnap-triz-case-library
- **官方分类**：`R&D-Innovation` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：2 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/37b2d2/mcp`
- **能力**：面向研发创新的 TRIZ 跨领域案例检索 MCP。支持按技术矛盾、功能关系、技术功效、科学效应和关键词，从 4500 万+结构化专利案例中匹配可借鉴解法，返回案例摘要、创新点及 TRIZ 标注，为企业 Agent 提供有出处的创新启发和方案依据。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `list_triz_search_terms` | 列出 search_triz_case 的 efficacy 或 oxford_effects 字段可使用的常用标准检索词。 | **field** | — ·工作流不可推断 |
| `search_triz_case` | 按技术矛盾、SVOP、技术功效、科学效应、关键词及专利过滤条件检索 TRIZ 案例，并返回案例摘要和标注数据。 | oxford_effects, svop, limit, sort, filters, keyword, efficacy, technical_contradiction | — ·工作流不可推断 |

### `report-gen` · 分支

- **名称**：创新与专利报告生成 / Innovation Report Generator
- **官方分类**：`R&D-Innovation` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：6 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/1fadfc/mcp`
- **能力**：将分析结果进一步沉淀为可交付的报告和任务。支持生成企业报告、专利价值报告、技术想法查新报告，并可下载结果或结合相似专利比对，帮助团队更高效地产出标准化材料。适合用于客户交付、内部汇报和售前支持。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `company_report_create` | 用于创建企业报告任务，便于后台执行并在后续查询状态和结果。 | company_name, credit_code, org_number, **report_type** | — ·待确认 |
| `idea_validation_create` | 用于获取创建技术想法查新报告相关数据，便于快速查看核心信息并支持后续分析。 | country, tech_effect, limit, **tech_means**, legal_status | AI29-1 ·高 |
| `idea_validation_download` | 用于导出或下载技术想法查新报告，便于归档、分享和线下使用。 | **job_id**, file_format | AI29-3 ·中 |
| `idea_validation_similar` | 用于相似专利检索与比对，帮助快速找到相近对象，便于比对、查新和方案参考。 | **job_id** | AI30 ·低 |
| `patent_report_create` | 用于创建专利价值报告任务（无logo版），便于后台执行并在后续查询状态和结果。 | patent_id, patent_number, **report_type** | — ·待确认 |
| `pre_patent_evaluation_export` | 用于导出或下载专利申请前评估报告，便于归档、分享和线下使用。 | job_id | — ·工作流不可推断 |

### `tech-collab` · 分支

- **名称**：产学研合作分析 / Open Innovation Collaboration Analytics
- **官方分类**：`R&D-Innovation` · **版本**：`v1.0.0` · **状态**：`active` · **tool 数**：4 · **上下文权重**：`low`
- **MCP 地址**：`https://connect.zhihuiya.com/81cc1c/mcp`
- **能力**：聚焦企业与高校、科研机构之间合作关系的分析工具。可从合作研发、共同申请、技术主题和地域分布等角度观察产学研网络，帮助识别合作强度、技术来源和潜在伙伴。适合用于开放式创新布局、合作尽调和区域创新研究。

| tool | 能力 | 入参（必填加粗） | 对应 API（置信度） |
|------|------|------------------|--------------------|
| `company_core_patent` | 用于获取企业核心专利相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number | C112 ·高 |
| `industry_university_research` | 用于获取企业产学研分析相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number | C114 ·高 |
| `industry_university_research_ipc` | 用于获取企业产学研研发技术分析相关数据，便于快速查看核心信息并支持后续分析。 | company_name, credit_code, org_number | C115 ·高 |
| `industry_university_research_region` | 用于分析企业产学研共同申请地域分布，帮助理解结构分布、热点方向和整体格局。 | company_name, credit_code, org_number | — ·待确认 |

---

*index.json v0.6.0 · tool 入参 schema 见 index.json*
