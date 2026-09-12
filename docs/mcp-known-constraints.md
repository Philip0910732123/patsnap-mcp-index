# 智慧芽 MCP 已知约束与实战经验

> 本文档记录使用智慧芽 MCP 服务过程中发现的已知限制、踩坑记录和降级方案。

---

## 一、智慧芽 MCP 服务约束

### 1. `overseas_patent_documents`（patent-status 服务）

| 约束 | 说明 |
|------|------|
| 68300004 错误码 | `Invalid parameter`——实际含义是后端无该专利审查文件，**不是参数错误**。不要反复重试 |
| 支持局限 | 路径 A 自动采集仅支持 US/EP/WO/AU 专利，KR/DE/TW/CA/GB/JP/IN 等局不支持 |
| 分页 | 使用 `offset` 参数分页，不要用 `page` |
| doc_count=0 | 表示该专利无审查文件，需走手动上传路径 |

### 2. 专利检索回退链路

拉取对比文件时可能遇到失败，完整回退链路：

```
Step 1: bibliography(patent_number=公开号)
  → 失败 → Step 2
Step 2: search_patents(query_text=公开号, limit=1) → 获取 patent_id UUID → 重试 bibliography
  → 失败 → Step 3
Step 3: 检查公开号格式（去国家前缀/去Kind Code/连字符变体）→ 重试 Step 1-2
  → 仍失败 → Step 4
Step 4: 标注「拉取失败，需手动核查」，继续处理其他文件
```

### 3. HTML 超链接 UUID 规则

| 规则 | 说明 |
|------|------|
| 必须用 UUID | 专利链接格式 `analytics.zhihuiya.com/patent-view/abst?patentId={uuid}`，**禁止用公开号** |
| UUID 来源 | `bibliography` 或 `search_patents` 返回的 `patent_id` 字段 |
| 降级处理 | 无法获取 UUID 时，链接降级为纯文本公开号，不挂链接 |

### 4. 限流与超时

| 场景 | 处理方式 |
|------|----------|
| API 限流（429） | 退避重试 3 次，间隔递增 5s/10s/20s |
| 鉴权失效（401） | 暂停，提示用户检查 MCP Key 状态 |
| 专利未公开 | 标注「未公开或号有误」，保留结构写明 |
| 公开号格式错误 | 去国家前缀/去 Kind Code/连字符变体重试 |

---

## 二、MinerU OCR 约束

### 1. 内容截断问题

| 场景 | 约束 | 解决方案 |
|------|------|----------|
| 内联模式（不传 output_dir） | ~20,000 字符处截断 | **必须传 `output_dir`** |
| 超过 10 页的 PDF | 末尾内容可能丢失 | 用 `pages` 参数分批 OCR |
| PTO-892 表格 | 位于 OA 最后一页，OCR 截断导致缺失 | 分批 OCR 或从驳回正文 fallback 提取 |

### 2. 单次调用约束

| 约束 | 说明 |
|------|------|
| 上限 200 页/次 | 超过需用 `pages` 参数分批 |
| 单 file_source | 每次只传 1 个 file_source 条目（多条目返回重复内容的 Bug） |
| 本地文件 | 直接传本地路径，不用 `file_url` 转 URL |
| 在线 URL | 仅当文件来源是在线 URL（如 Patsnap 签名链接）时才传 URL |

### 3. 扫描件处理

USPTO OA PDF 多为扫描件，PyMuPDF 无法提取文本层。判断方式：

```python
import fitz  # PyMuPDF
doc = fitz.open(pdf_path)
if doc[0].get_text().strip():
    # 有文本层，直接提取
else:
    # 扫描件，需 MinerU OCR
```

---

## 三、降级方案

### 无 MCP 时的降级

| 场景 | 降级方案 | 影响 |
|------|----------|------|
| 专利检索不可用 | 手动在 CNIPA/EPO/USPTO 官网检索 | 检索效率降低，结果需手动录入 |
| OA 文件无法自动获取 | 走路径 B 手动上传 PDF | 不影响后续分析流程 |
| 对比文件拉取失败 | 提示用户手动上传权利要求文本 | 审查员主张准确性判断无法自动完成 |
| MinerU 不可用 | 回退到本地 PyMuPDF + 正则提取 | 扫描件无法处理，仅适合有文本层 PDF |

---

## 四、工具选型建议

### 检索工具选择

| 需求 | 推荐工具 | 理由 |
|------|----------|------|
| 著录+权利要求 | `core-patents.bibliography` + `core-patents.claims` | 专用 API，返回结构化数据 |
| 语义搜索 | `patsnap-search.patsnap_search` | 自然语言/语义/关键词融合 |
| 查新检索 | `novelty-search-lite.*` | 完整查新流程：特征提取→检索→对比→报告 |
| FTO 分析 | `patsnap-ip-searching.fto_review` | 发明 FTO 专用工具 |
| 外观 FTO | `patsnap-ip-searching.design_fto` | 外观设计图片检索 |
| 全景分析 | `patent-landscape.*` | 趋势/构成/申请人/技术地图/生命周期 |
| 法律状态 | `patent-status.legal_data` | 年费/SEP/诉讼/许可/质押 |

### OCR 工具选择

| 工具 | 质量 | 推荐场景 |
|------|------|----------|
| MinerU MCP | ⭐⭐⭐⭐⭐ | 扫描件 PDF、表格提取（首选） |
| PyMuPDF | ⭐⭐⭐ | 有文本层的 PDF、快速文本提取 |
| document-processing MCP | ⭐⭐ | 已废弃，质量明显劣于 MinerU |
