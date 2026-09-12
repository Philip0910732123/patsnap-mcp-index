# 智慧芽 MCP 服务索引（非官方社区维护）

> 本仓库为社区维护的非官方智慧芽 MCP 服务索引，旨在帮助开发者快速了解和配置智慧芽 MCP 生态。MCP 服务清单和工具描述来自公开可访问的开发者环境。如需获取 API Key，请访问 [open.zhihuiya.com](https://open.zhihuiya.com)。

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <img src="https://img.shields.io/badge/MCP%20Servers-59-blue.svg" alt="MCP Servers: 59">
  <img src="https://img.shields.io/badge/Categories-5-green.svg" alt="Categories: 5">
  <img src="https://img.shields.io/badge/Tools-417-orange.svg" alt="Tools: 417">
  <img src="https://img.shields.io/badge/Platform-Cursor%20%7C%20Claude%20%7C%20Eureka-blueviolet.svg" alt="Platform">
</p>

## 这是什么？

智慧芽开放平台提供了 59 个 MCP（Model Context Protocol）服务，覆盖专利检索、法律状态、全景分析、FTO、OCR、化学结构、生物序列、临床试验、药物情报、文献检索、企业情报等数十个领域。但这些服务分散在官方市场页面中，缺乏一份统一的导航索引。

本仓库将这 59 个 MCP 服务整理为：

- **[服务总览表](docs/mcp-service-catalog.md)** — 按领域分组的 59 个 MCP 服务一览
- **[工具矩阵](docs/mcp-tool-matrix.md)** — 每个 MCP 服务下的全部工具清单及输入输出摘要
- **[配置指南](docs/mcp-setup-guide.md)** — 从获取 Key 到连接客户端的完整步骤
- **[已知约束](docs/mcp-known-constraints.md)** — 实战踩坑记录和已知限制
- **[调用示例](docs/mcp-usage-examples.md)** — 典型场景的 MCP 调用流程

## 快速开始

### 1. 获取 MCP Key

登录 [智慧芽开放平台](https://open.zhihuiya.com) → API 密钥页面 → 创建 MCP Key（格式：`sk-xxxxxxxxxxxx`）

### 2. 连接 MCP 服务

在 [MCP 服务市场](https://open.zhihuiya.com/marketplace/mcp-servers) 选择需要的服务，生成连接链接，按照 [快速接入指南](https://open.zhihuiya.com/devportal/guides/mcp-quickstart) 配置你的 AI 客户端。

### 3. 验证连通性

```bash
curl https://connect.zhihuiya.com/<service-id>/mcp \
  -H 'Authorization: Bearer YOUR_MCP_KEY' \
  -H 'accept: application/json, text/event-stream' \
  -H 'Content-Type: application/json' \
  -H 'mcp-protocol-version: 2025-11-25' \
  --data-raw '{"method": "tools/list", "params": {}, "jsonrpc": "2.0", "id": 1}'
```

详见 [配置指南](docs/mcp-setup-guide.md)。

## 服务分类总览

| 分类 | 服务数 | 典型场景 |
|------|--------|----------|
| 🔵 IP 智能 | 21 | 专利检索、法律状态、全景分析、FTO、查新、价值评估、文档解析 |
| 🟢 生命科学 | 11 | 药物管线、临床试验、靶点、疾病、生物序列、化学分子、文献 |
| 🟡 企业情报 | 7 | 工商档案、科技评估、风险预警、投行尽调 |
| 🟠 研发创新 | 6 | 文献检索、语义搜索、TRIZ 方案、报告生成、产学研合作 |
| ⚪ 工具与其他 | 14 | OCR、化学结构、分子描述符、临床数据库、NCCN 指南、PubMed 等 |

## 文档目录

| 文件 | 内容 |
|------|------|
| [docs/mcp-service-catalog.md](docs/mcp-service-catalog.md) | 59 个 MCP 服务按领域分组的完整目录 |
| [docs/mcp-tool-matrix.md](docs/mcp-tool-matrix.md) | 每个 MCP 服务的全部工具清单 |
| [docs/mcp-setup-guide.md](docs/mcp-setup-guide.md) | 获取 Key → 连接客户端 → 验证连通性 |
| [docs/mcp-known-constraints.md](docs/mcp-known-constraints.md) | 已知限制、踩坑记录、降级方案 |
| [docs/mcp-usage-examples.md](docs/mcp-usage-examples.md) | 专利检索 / FTO / 全景分析 / OCR 调用示例 |

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
