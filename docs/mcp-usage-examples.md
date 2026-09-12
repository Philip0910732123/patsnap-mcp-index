# 智慧芽 MCP 调用示例

> 以下示例展示典型场景的 MCP 工具调用流程。所有示例基于 Eureka runtime 的 `tool_load` → `tool_invoke` 模式。

---

## 场景一：专利著录检索

**需求**：输入专利号，获取著录信息和权利要求全文。

```
# 1. 加载工具 schema
tool_load(server="core-patents", tool_name="bibliography")

# 2. 调用 bibliography 获取著录
tool_invoke(
  tool="mcp_core-patents__bibliography",
  arguments={"patent_number": "US10123456B2"}
)
# → 返回：标题、申请人、发明人、申请日、公开日、IPC/CPC 等

# 3. 加载 claims 工具
tool_load(server="core-patents", tool_name="claims")

# 4. 调用 claims 获取权利要求
tool_invoke(
  tool="mcp_core-patents__claims",
  arguments={"patent_number": "US10123456B2", "replace_by_related": 0}
)
# → 返回：独立权利要求 + 从属权利要求全文
```

---

## 场景二：查新检索

**需求**：给定技术方案，检索相关现有技术。

```
# 1. 特征提取
tool_load(server="novelty-search-lite", tool_name="novelty_feature_extract")
tool_invoke(
  tool="mcp_novelty-search-lite__novelty_feature_extract",
  arguments={"tech_proposal": "一种基于CRISPR-Cas9的gRNA设计方法..."}
)
# → 返回：关键技术特征列表

# 2. 关键词提取
tool_load(server="novelty-search-lite", tool_name="novelty_keywords_extract")
tool_invoke(
  tool="mcp_novelty-search-lite__novelty_keywords_extract",
  arguments={"feature_data": "<上一步返回的特征>"}
)
# → 返回：中英文检索关键词

# 3. 语义检索
tool_load(server="novelty-search-lite", tool_name="novelty_lite_semantic_search")
tool_invoke(
  tool="mcp_novelty-search-lite__novelty_lite_semantic_search",
  arguments={"keywords": "<上一步返回的关键词>", "limit": 20}
)
# → 返回：相关专利列表

# 4. 特征对比
tool_load(server="novelty-search-lite", tool_name="novelty_feature_comparison")
tool_invoke(
  tool="mcp_novelty-search-lite__novelty_feature_comparison",
  arguments={"target_patents": "<上一步返回的专利>", "features": "<特征>"}
)
# → 返回：特征对比矩阵

# 5. 报告生成
tool_load(server="novelty-search-lite", tool_name="novelty_lite_report_generate")
tool_invoke(
  tool="mcp_novelty-search-lite__novelty_lite_report_generate",
  arguments={"comparison_result": "<对比结果>"}
)
# → 返回：查新报告
```

---

## 场景三：FTO 风险分析

**需求**：针对产品技术方案，分析自由实施风险。

```
# 1. 发明 FTO 分析
tool_load(server="patsnap-ip-searching", tool_name="fto_review")
tool_invoke(
  tool="mcp_patsnap-ip-searching__fto_review",
  arguments={
    "tech_description": "一种使用抗体重链第214位半胱氨酸定点偶联的ADC药物...",
    "country": "US",
    "legal_status": "active",
    "filing_date_after": "2010-01-01"
  }
)
# → 返回：风险专利列表 + 风险等级

# 2. 获取风险专利权利要求
tool_load(server="core-patents", tool_name="claims")
tool_invoke(
  tool="mcp_core-patents__claims",
  arguments={"patent_number": "<风险专利号>"}
)
# → 返回：权利要求全文，逐项对比

# 3. 法律状态核查
tool_load(server="patent-status", tool_name="legal_data")
tool_invoke(
  tool="mcp_patent-status__legal_data",
  arguments={"patent_number": "<风险专利号>"}
)
# → 返回：当前法律状态、年费缴纳情况
```

---

## 场景四：专利全景分析

**需求**：分析某技术领域的专利竞争格局。

```
# 1. 检索领域专利
tool_load(server="patent-landscape", tool_name="search_patents_v3")
tool_invoke(
  tool="mcp_patent-landscape__search_patents_v3",
  arguments={"query": "ADC antibody drug conjugate", "limit": 500}
)
# → 返回：专利列表

# 2. 申请趋势分析
tool_load(server="patent-landscape", tool_name="trend")
tool_invoke(
  tool="mcp_patent-landscape__trend",
  arguments={"patent_ids": "<上一步返回的ID列表>"}
)
# → 返回：年度申请趋势

# 3. 技术构成分析
tool_load(server="patent-landscape", tool_name="technology_constitute")
tool_invoke(
  tool="mcp_patent-landscape__technology_constitute",
  arguments={"patent_ids": "<ID列表>"}
)
# → 返回：技术分支分布

# 4. 申请人排名
tool_load(server="patent-landscape", tool_name="applicant_rank")
tool_invoke(
  tool="mcp_patent-landscape__applicant_rank",
  arguments={"patent_ids": "<ID列表>", "top_n": 20}
)
# → 返回：主要申请人排名

# 5. 技术地图
tool_load(server="patent-landscape", tool_name="domain_map")
tool_invoke(
  tool="mcp_patent-landscape__domain_map",
  arguments={"patent_ids": "<ID列表>"}
)
# → 返回：技术领域分布地图
```

---

## 场景五：MinerU OCR 提取

**需求**：对扫描件 PDF 进行 OCR 提取。

```
# 1. 加载 MinerU 工具
tool_load(server="mineru", tool_name="parse_documents")

# 2. 调用 OCR
tool_invoke(
  tool="mcp_mineru__parse_documents",
  arguments={
    "file_sources": [{"file": "/path/to/oa.pdf"}],
    "enable_ocr": true,
    "language": "en",
    "output_dir": "/session/ocr_output/"
  }
)
# → 返回：Markdown 格式的 OCR 结果（含表格保留）

# 注意：
# - 每次只传 1 个 file_source 条目（多条目有 Bug）
# - 必传 output_dir，否则结果在 ~20,000 字符处截断
# - 超过 200 页需用 pages 参数分批
```

---

## 场景六：药物情报检索

**需求**：查询某靶点的在研药物和临床试验。

```
# 1. 药物搜索
tool_load(server="drug-asset", tool_name="drug_search")
tool_invoke(
  tool="mcp_drug-asset__drug_search",
  arguments={"keyword": "HER2", "target": "ERBB2"}
)
# → 返回：相关在研药物列表

# 2. 药物详情
tool_load(server="drug-asset", tool_name="drug_fetch")
tool_invoke(
  tool="mcp_drug-asset__drug_fetch",
  arguments={"drug_id": "<上一步返回的drug_id>"}
)
# → 返回：药物详情（机制/靶点/适应症/研发状态）

# 3. 临床试验
tool_load(server="clinical-trials", tool_name="clinical_trial_search")
tool_invoke(
  tool="mcp_clinical-trials__clinical_trial_search",
  arguments={"drug_name": "<药物名>", "status": "recruiting"}
)
# → 返回：相关临床试验列表
```

---

## 通用调用模式

所有 MCP 工具调用遵循统一模式：

```
1. tool_load(server="<服务名>", tool_name="<工具名>") → 获取 input_schema
2. tool_invoke(tool="mcp_<服务名>__<工具名>", arguments={...}) → 执行调用
```

- 同一 turn 内已加载的 schema 可复用，不需要重复 `tool_load`
- 新 turn 需要重新 `tool_load` 才能调用
- 调用参数必须严格匹配 `tool_load` 返回的 `input_schema`
