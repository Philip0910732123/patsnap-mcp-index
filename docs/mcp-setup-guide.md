# 智慧芽 MCP 配置指南

> **已归档（v0.6.0 起）**：本文是旧版人工整理，其中的 MCP / API 数量与映射口径已过时，请勿作为事实依据。当前口径（50 MCP / 411 tool / 376 API）以 [index.json](../index.json) 为唯一真相源；人读入口见 [getting-started.md](getting-started.md)，映射复核见 [api-mapping-review.md](api-mapping-review.md)。

> 基于 [官方快速接入指南](https://open.zhihuiya.com/devportal/guides/mcp-quickstart) 整理，补充实战经验。

---

## 一、获取 MCP Key

1. 登录 [智慧芽开放平台](https://open.zhihuiya.com)
2. 进入 **API 密钥** 页面
3. 创建新的 MCP Key（格式：`sk-xxxxxxxxxxxx`）
4. 妥善保存——创建后将不再显示完整内容

> ⚠️ **安全警告**：请勿将 MCP Key 提交到代码仓库或分享给他人。如发生泄露，请立即在控制台撤销并重新生成。

---

## 二、连接 MCP 服务

### 方式一：智慧芽 MCP 服务市场（推荐）

1. 访问 [MCP 服务市场](https://open.zhihuiya.com/marketplace/mcp-servers)
2. 选择需要的 MCP 服务
3. 生成连接链接
4. 按照 [快速接入指南](https://open.zhihuiya.com/devportal/guides/mcp-quickstart) 配置你的 AI 客户端

### 方式二：手动配置

在 AI 客户端的 MCP 配置文件中添加智慧芽 MCP 服务 URL，格式为：

```
https://connect.zhihuiya.com/<service-id>/mcp
```

Header 配置：
- `Authorization: Bearer YOUR_MCP_KEY`
- `accept: application/json, text/event-stream`
- `Content-Type: application/json`
- `mcp-protocol-version: 2025-11-25`

也可通过 URL 参数传入 Key：`?apikey=YOUR_MCP_KEY`

---

## 三、验证连通性

使用以下 curl 命令获取可用工具列表，验证 MCP Key 是否有效：

```bash
curl https://connect.zhihuiya.com/<service-id>/mcp \
  -H 'Authorization: Bearer YOUR_MCP_KEY' \
  -H 'accept: application/json, text/event-stream' \
  -H 'Content-Type: application/json' \
  -H 'mcp-protocol-version: 2025-11-25' \
  --data-raw '{
    "method": "tools/list",
    "params": {},
    "jsonrpc": "2.0",
    "id": 1
  }'
```

成功响应格式：

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "tools": [
      {
        "name": "...",
        "description": "...",
        "inputSchema": { ... }
      }
    ]
  }
}
```

---

## 四、MinerU OCR MCP 配置（独立服务）

MinerU 是独立的 OCR 服务，不依赖智慧芽 API Key，使用自己的 Token。

### 配置方式

在 AI 客户端的 MCP 配置文件中添加：

```json
{
  "mcpServers": {
    "mineru": {
      "type": "streamableHttp",
      "url": "https://mcp.mineru.net/mcp",
      "env": {
        "MINERU_API_TOKEN": "your_token_here"
      }
    }
  }
}
```

### Token 获取

1. 访问 [mineru.net](https://mineru.net)
2. 注册/登录
3. 获取 API Token

### Token 模式差异

| 模式 | 限制 | 输出格式 |
|------|------|----------|
| 无 Token（Flash 模式） | 有服务限速 | 仅 Markdown |
| 有 Token | 200 页/次 | Markdown + HTML + LaTeX |

### 必传参数

| 参数 | 值 | 说明 |
|------|-----|------|
| `enable_ocr` | `true` | 强制 OCR（不传则扫描件可能跳过） |
| `language` | `"en"` 或 `"ch"` | OCR 语言代码 |
| `output_dir` | session 路径 | **必传**：不传则结果内联返回，~20,000 字符处截断 |

---

## 五、客户端配置示例

### Cursor

在 Cursor Settings → MCP 中添加智慧芽 MCP 服务 URL。

### Claude Desktop

在 `claude_desktop_config.json` 中添加：

```json
{
  "mcpServers": {
    "zhihuiya-patents": {
      "type": "streamableHttp",
      "url": "https://connect.zhihuiya.com/<service-id>/mcp",
      "headers": {
        "Authorization": "Bearer sk-your-key-here"
      }
    }
  }
}
```

### Eureka

在 Eureka 中通过 `/mcp` 命令或设置页配置 MCP 服务。

---

## 六、常见问题

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 连接超时 | 网络问题或 Key 无效 | 检查 Key 格式 `sk-` 开头，检查网络 |
| 返回 401 | Key 已失效或权限不足 | 重新生成 Key，确认已勾选对应 MCP 服务权限 |
| 工具列表为空 | 服务未授权 | 在开放平台确认已订阅该 MCP 服务 |
| OCR 结果被截断 | 未传 `output_dir` | 必须传 `output_dir` 参数到 session 路径 |
| `overseas_patent_documents` 返回 68300004 | 后端无该专利审查文件 | 非参数错误，该专利未入库，走手动上传路径 |
| Node.js 相关 MCP 安装失败 | 系统 PATH 无 Node.js | 使用完整路径：`C:\Users\hupan\node\node.exe` |
