# 智慧芽开放平台 API 索引

> **已归档（v0.6.0 起）**：本文是旧版人工整理，其中的 MCP / API 数量与映射口径已过时，请勿作为事实依据。当前口径（50 MCP / 411 tool / 376 API）以 [index.json](../index.json) 为唯一真相源；人读入口见 [getting-started.md](getting-started.md)，映射复核见 [api-mapping-review.md](api-mapping-review.md)。

生成时间：2026-05-29T08:51:13.025Z

- 接口条目：372
- 完整详情缺失：1
- 完整结构化数据：`zhihuiya_api_full_details.json`
- 完整 Markdown 参考：`zhihuiya_api_reference_full.md`


## AI / AI Agent / 智慧芽大模型

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| AI07 | [AI07]大模型(CC GPT) | POST | https://connect.zhihuiya.com/chat/cc-gpt-stream | ok | https://open.zhihuiya.com/devportal/api-reference/1fb50dcf642c4b92bb475b1b08fecfd1?category=95ba2a78e172eb84fb5c7c3ed654954a |
| AI20 | [AI20]生物医药大模型 | POST | https://connect.zhihuiya.com/chat/pharm-gpt-stream | ok | https://open.zhihuiya.com/devportal/api-reference/08daece5fdb8457f8b587695efb1b8ab?category=95ba2a78e172eb84fb5c7c3ed654954a |
| AI50 | [AI50]专利大模型(Pat GPT) | POST | https://connect.zhihuiya.com/chat/pat-gpt-stream | ok | https://open.zhihuiya.com/devportal/api-reference/dc06387a59654580bb2b2c1bce3dc29a?category=95ba2a78e172eb84fb5c7c3ed654954a |

## AI / AI Agent / 生物制药百科问答

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| AI68 | [AI68-1]生物医药百科问答-创建 | POST | https://connect.zhihuiya.com/chat/ai-ls-chat | ok | https://open.zhihuiya.com/devportal/api-reference/bc562c229d2b470db887897aa9c4235d?category=a8778fe3cd4d46eb47b3d9802bd7d3d0 |
| AI68 | [AI68-2]生物医药百科问答-获取结果 | POST | https://connect.zhihuiya.com/chat/ai-ls-stream | ok | https://open.zhihuiya.com/devportal/api-reference/3e6f39a160bd4a11841d65d795ff6361?category=a8778fe3cd4d46eb47b3d9802bd7d3d0 |

## AI / AI Agent / 技术交底书

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| AI32 | [AI32-1]重点内容提取 | POST | https://connect.zhihuiya.com/search/patent/patent-disclosure/tech-means | ok | https://open.zhihuiya.com/devportal/api-reference/7630d5ea42d5480fae359ff135add7d7?category=a8e854272387065ddc99e2451b8799ea |
| AI32 | [AI32-2]生成技术交底书 | POST | https://connect.zhihuiya.com/search/patent/patent-disclosure/generate | ok | https://open.zhihuiya.com/devportal/api-reference/e31969ed9c7d487fa80df3e266b481aa?category=a8e854272387065ddc99e2451b8799ea |
| AI32 | [AI32-3]下载技术交底书 | POST | https://connect.zhihuiya.com/search/patent/patent-disclosure/download | ok | https://open.zhihuiya.com/devportal/api-reference/550f9e6dc71148158c47d9d69c7932dd?category=a8e854272387065ddc99e2451b8799ea |
| AI32 | [AI32-4]技术交底书流式输出 | POST | https://connect.zhihuiya.com/search/patent/patent-disclosure/sse | ok | https://open.zhihuiya.com/devportal/api-reference/9da73ee497d94a9aba5da9fc2e08f39d?category=a8e854272387065ddc99e2451b8799ea |

## AI / AI Agent / 技术方案探索

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| AI33 | [AI33-1]技术方案探索创建（Beta） | POST | https://connect.zhihuiya.com/ai/find-solution/creation | ok | https://open.zhihuiya.com/devportal/api-reference/dfe9842c71cb4c58aff2441616635658?category=052fd47d1a4d2518afd1c3ac98857d24 |
| AI33 | [AI33-2]技术方案探索查询（Beta） | GET | https://connect.zhihuiya.com/ai/find-solution/query | ok | https://open.zhihuiya.com/devportal/api-reference/d6fc3b287b124fada87627724a67b18e?category=052fd47d1a4d2518afd1c3ac98857d24 |
| AI33 | [AI33-3]技术方案探索V2-创建Agent任务 | POST | https://connect.zhihuiya.com/ai/find-solution-agent-creation | ok | https://open.zhihuiya.com/devportal/api-reference/e799ba98c8b04ab1809d387e43ff1707?category=052fd47d1a4d2518afd1c3ac98857d24 |
| AI33 | [AI33-1]技术方案探索-创建任务 | POST | https://connect.zhihuiya.com/ai/find-solution/step1/v3 | ok | https://open.zhihuiya.com/devportal/api-reference/423097a91cb74416abcf6966633c466a?category=052fd47d1a4d2518afd1c3ac98857d24 |
| AI33 | [AI33-2]技术方案探索-获取推荐 | POST | https://connect.zhihuiya.com/ai/find-solution/step2/v3 | ok | https://open.zhihuiya.com/devportal/api-reference/87e50e29ee874f5ab4c4ab1f4e9af466?category=052fd47d1a4d2518afd1c3ac98857d24 |
| AI33 | [AI33-3]技术方案探索-选择推荐 | POST | https://connect.zhihuiya.com/ai/find-solution/step3-submit/v3 | ok | https://open.zhihuiya.com/devportal/api-reference/d1de1e678fca4dc395706525d5ea1d65?category=052fd47d1a4d2518afd1c3ac98857d24 |
| AI33 | [AI33-4]技术方案探索-获取方向 | POST | https://connect.zhihuiya.com/ai/find-solution/step3-query/v3 | ok | https://open.zhihuiya.com/devportal/api-reference/a56faf00cf27467999e42f6065e7ec66?category=052fd47d1a4d2518afd1c3ac98857d24 |
| AI33 | [AI33-5]技术方案探索-选择方向 | POST | https://connect.zhihuiya.com/ai/find-solution/step4/v3 | ok | https://open.zhihuiya.com/devportal/api-reference/e349c63a70054ddc9a996b337781e47e?category=052fd47d1a4d2518afd1c3ac98857d24 |
| AI33 | [AI33-6]技术方案探索-获取方案和细节 | POST | https://connect.zhihuiya.com/ai/find-solution/step5/v3 | ok | https://open.zhihuiya.com/devportal/api-reference/78b5ef85adc74d69bb9d5dcb39a2db5f?category=052fd47d1a4d2518afd1c3ac98857d24 |

## AI / AI Agent / 技术问答

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| AI33 | [AI33-4/AI36-4]技术方案探索/技术问答V2-Agent流式输出 | POST | https://connect.zhihuiya.com/ai/agent/sse | ok | https://open.zhihuiya.com/devportal/api-reference/dbbff4d8878240b58eb26c259aff92f1?category=e1bc335525a51e6d9b617f806854aff4 |
| AI36 | [AI36-1]技术问答 | POST | https://connect.zhihuiya.com/ai/technical-qa | ok | https://open.zhihuiya.com/devportal/api-reference/26293c18dba041bcaa246daed941d91d?category=e1bc335525a51e6d9b617f806854aff4 |
| AI36 | [AI36-2]技术问答-获取结果 | POST | https://connect.zhihuiya.com/ai/technical-qa-result | ok | https://open.zhihuiya.com/devportal/api-reference/39da1c049bf34b78b8e82bcc6cfcd8fd?category=e1bc335525a51e6d9b617f806854aff4 |
| AI36 | [AI36-3]技术问答V2-创建Agent任务 | POST | https://connect.zhihuiya.com/ai/technical-qa-agent-creation | ok | https://open.zhihuiya.com/devportal/api-reference/f997752317374f5a855eb879d6b9b5eb?category=e1bc335525a51e6d9b617f806854aff4 |
| AI33 | [AI33-4/AI36-4]技术方案探索/技术问答V2-Agent流式输出 | POST | https://connect.zhihuiya.com/ai/agent/sse | ok | https://open.zhihuiya.com/devportal/api-reference/dbbff4d8878240b58eb26c259aff92f1?category=e1bc335525a51e6d9b617f806854aff4 |
| AI36 | [AI36-1]技术问答-提交任务 | POST | https://connect.zhihuiya.com/ai/technical-qa/submit | ok | https://open.zhihuiya.com/devportal/api-reference/a00e8d5de42b46b6bdecfb8e100435e8?category=e1bc335525a51e6d9b617f806854aff4 |
| AI36 | [AI36-2]技术问答-查询任务 | POST | https://connect.zhihuiya.com/ai/technical-qa/report | ok | https://open.zhihuiya.com/devportal/api-reference/abc163a67af3482aa0a8fb665961439a?category=e1bc335525a51e6d9b617f806854aff4 |

## AI / AI Agent / 材料技术方案探索

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| AI73 | [AI73-1]材料技术方案探索-提交任务 | POST | https://connect.zhihuiya.com/ai/material/find-solution/submit | ok | https://open.zhihuiya.com/devportal/api-reference/920789990a544cbeb76eda6b824d0711?category=052fd47d1a4d2518afd1c3ac98857d25 |
| AI73 | [AI73-2]材料技术方案探索-获取推荐方案 | POST | https://connect.zhihuiya.com/ai/material/find-solution/recommend | ok | https://open.zhihuiya.com/devportal/api-reference/93ce9d4bf4604ecb8b39d8a0ba6aa20d?category=052fd47d1a4d2518afd1c3ac98857d25 |
| AI73 | [AI73-3]材料技术方案探索-确认推荐方案 | POST | https://connect.zhihuiya.com/ai/material/find-solution/confirm-recommend | ok | https://open.zhihuiya.com/devportal/api-reference/bad587097b214a0c9af6ec31642a9884?category=052fd47d1a4d2518afd1c3ac98857d25 |
| AI73 | [AI73-4]材料技术方案探索-获取思考过程 | POST | https://connect.zhihuiya.com/ai/material/find-solution/thinking | ok | https://open.zhihuiya.com/devportal/api-reference/d6a380ca51ee49b589344b677a58bc51?category=052fd47d1a4d2518afd1c3ac98857d25 |
| AI73 | [AI73-5]材料技术方案探索-获取脑图 | POST | https://connect.zhihuiya.com/ai/material/find-solution/mind | ok | https://open.zhihuiya.com/devportal/api-reference/a4e7ee1dfdef42dfbbf237a814e930a9?category=052fd47d1a4d2518afd1c3ac98857d25 |
| AI73 | [AI73-6]材料技术方案探索-获取节点引用文献列表 | POST | https://connect.zhihuiya.com/ai/material/find-solution/citation-reference-list | ok | https://open.zhihuiya.com/devportal/api-reference/dc8b1adae2f44c20af2154c3a186211a?category=052fd47d1a4d2518afd1c3ac98857d25 |
| AI73 | [AI73-7]材料技术方案探索-获取节点参考信息 | POST | https://connect.zhihuiya.com/ai/material/find-solution/node-reference | ok | https://open.zhihuiya.com/devportal/api-reference/fd9e5b680f4a4d3ebb7aa0d73e8b8ab4?category=052fd47d1a4d2518afd1c3ac98857d25 |
| AI73 | [AI73-8]材料技术方案探索-生成方案 | POST | https://connect.zhihuiya.com/ai/material/find-solution/implementation | ok | https://open.zhihuiya.com/devportal/api-reference/089bcf910d3c4bf0a53e9a2e7b95ca86?category=052fd47d1a4d2518afd1c3ac98857d25 |
| AI73 | [AI73-9]材料技术方案探索-获取结果 | POST | https://connect.zhihuiya.com/ai/material/find-solution/implementation-response | ok | https://open.zhihuiya.com/devportal/api-reference/6ebd6d533ad74a9fab56d07243deec3f?category=052fd47d1a4d2518afd1c3ac98857d25 |

## AI / AI Agent / 技术预研报告

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| AI34 | [AI34-1]预研报告创建（Beta） | POST | https://connect.zhihuiya.com/ai/quick-search-report/creation | ok | https://open.zhihuiya.com/devportal/api-reference/41df9b2e3db34261822aef2d433471ef?category=f85dbee77c2c8b6a13cb4f30c01f308b |
| AI34 | [AI34-2]预研报告创建-自定义目录（Beta） | POST | https://connect.zhihuiya.com/ai/quick-search-report/creation/custom-dir | ok | https://open.zhihuiya.com/devportal/api-reference/46872b4d9a424b5cb023bd11fb572e9b?category=f85dbee77c2c8b6a13cb4f30c01f308b |
| AI34 | [AI34-3]预研报告查询（Beta） | GET | https://connect.zhihuiya.com/ai/quick-search-report/query | ok | https://open.zhihuiya.com/devportal/api-reference/4da73b95c3154e3281b60433724aebe6?category=f85dbee77c2c8b6a13cb4f30c01f308b |

## AI / AI Agent / 查新检索

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| AI35 | [AI35-1]查新检索-技术特征 | POST | https://connect.zhihuiya.com/ai/novelty-search/tech-feature | ok | https://open.zhihuiya.com/devportal/api-reference/fbe46be1d0724063b078caa1940c688f?category=4a5521d130830a95b40040a694552868 |
| AI35 | [AI35-2]查新检索-创建查询 | POST | https://connect.zhihuiya.com/ai/novelty-search/create-query | ok | https://open.zhihuiya.com/devportal/api-reference/28b41cd2043e459b8fa4c12db515b831?category=4a5521d130830a95b40040a694552868 |
| AI35 | [AI35-3]查新检索-查询 | POST | https://connect.zhihuiya.com/ai/novelty-search/query | ok | https://open.zhihuiya.com/devportal/api-reference/9b03a11f06d84c948b3d5a565677cbcd?category=4a5521d130830a95b40040a694552868 |
| AI35 | [AI35-4]查新检索-创建报告 | POST | https://connect.zhihuiya.com/ai/novelty-search/report | ok | https://open.zhihuiya.com/devportal/api-reference/3230ef53a96c43298b6c2ba648381706?category=4a5521d130830a95b40040a694552868 |
| AI35 | [AI35-5]查新检索-下载报告 | POST | https://connect.zhihuiya.com/ai/novelty-search/download | ok | https://open.zhihuiya.com/devportal/api-reference/02b4b716ee8640dc817c03ce5e6b1ac8?category=4a5521d130830a95b40040a694552868 |
| AI35 | [AI35-1]查新检索-创建任务 | POST | https://connect.zhihuiya.com/ai/novelty-search/submit | ok | https://open.zhihuiya.com/devportal/api-reference/8fb043c347ae45259ecee8f4bfb775ff?category=4a5521d130830a95b40040a694552868 |
| AI35 | [AI35-2]查新检索-总结技术要点 | POST | https://connect.zhihuiya.com/ai/novelty-search/tech-solution/get | ok | https://open.zhihuiya.com/devportal/api-reference/b9a91703828645d796ddc43f3b49e7f6?category=4a5521d130830a95b40040a694552868 |
| AI35 | [AI35-3]查新检索-确认技术要点 | POST | https://connect.zhihuiya.com/ai/novelty-search/tech-solution/update | ok | https://open.zhihuiya.com/devportal/api-reference/f088b6801ce64a3988b7bb817caad397?category=4a5521d130830a95b40040a694552868 |
| AI35 | [AI35-4]查新检索-提取技术特征 | POST | https://connect.zhihuiya.com/ai/novelty-search/feature/extract | ok | https://open.zhihuiya.com/devportal/api-reference/5cb06baf89fa4586adca58afe461bbc0?category=4a5521d130830a95b40040a694552868 |
| AI35 | [AI35-5]查新检索-确认技术特征 | POST | https://connect.zhihuiya.com/ai/novelty-search/feature/confirm | ok | https://open.zhihuiya.com/devportal/api-reference/4fa9fd7d17a1459fbfa8a90bb4b23c00?category=4a5521d130830a95b40040a694552868 |
| AI35 | [AI35-6]查新检索-提取检索要素 | POST | https://connect.zhihuiya.com/ai/novelty-search/retrieval/elements | ok | https://open.zhihuiya.com/devportal/api-reference/760f912872fd4cb892f78ddc5af85a40?category=4a5521d130830a95b40040a694552868 |
| AI35 | [AI35-7]查新检索-确认检索要素 | POST | https://connect.zhihuiya.com/ai/novelty-search/agent-search | ok | https://open.zhihuiya.com/devportal/api-reference/0e517c0739e545f8a5b947aab623163e?category=4a5521d130830a95b40040a694552868 |
| AI35 | [AI35-8]查新检索-获取检索策略与筛选列表与特征对比 | POST | https://connect.zhihuiya.com/ai/novelty-search/agent-result | ok | https://open.zhihuiya.com/devportal/api-reference/8dd86fbd20a44f81a31966cd074a0c73?category=4a5521d130830a95b40040a694552868 |
| AI35 | [AI35-9]查新检索-确认筛选列表与特征对比 | POST | https://connect.zhihuiya.com/ai/novelty-search/feature/comparison/confirm | ok | https://open.zhihuiya.com/devportal/api-reference/f4c307de06d94bbf85c7f8cf5dd8fb54?category=4a5521d130830a95b40040a694552868 |
| AI35 | [AI35-10]查新检索-创建报告 | POST | https://connect.zhihuiya.com/ai/novelty-search/export | ok | https://open.zhihuiya.com/devportal/api-reference/82ddd5b1959641c9b117cffb2337c560?category=4a5521d130830a95b40040a694552868 |
| AI35 | [AI35-11]查新检索-下载报告 | POST | https://connect.zhihuiya.com/ai/novelty-search/report/get | ok | https://open.zhihuiya.com/devportal/api-reference/5a1cc75475a9429283278456f346fab5?category=4a5521d130830a95b40040a694552868 |
| AI35 | [AI35-12]查新检索-添加对比文献或专利 | POST | https://connect.zhihuiya.com/ai/novelty-search/feature/comparison/generate | ok | https://open.zhihuiya.com/devportal/api-reference/f9243e2023804965ad5f985a65996f91?category=4a5521d130830a95b40040a694552868 |

## AI / AI Agent / 专利说明书撰写

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| AI37 | [AI37-1]专利说明书撰写(CNIPA)-初始化总结 | POST | https://connect.zhihuiya.com/ai/specification/init/cnipa | ok | https://open.zhihuiya.com/devportal/api-reference/6ed277c2ea6841e29f8f45bdec5a5528?category=8da258e659976702fa0070378908b963 |
| AI37 | [AI37-2]专利说明书撰写(CNIPA)-初始化总结结果获取 | POST | https://connect.zhihuiya.com/ai/specification/init-result/cnipa | ok | https://open.zhihuiya.com/devportal/api-reference/8f8d0f6f3cc046f4b652817d77ba9039?category=8da258e659976702fa0070378908b963 |
| AI37 | [AI37-3]专利说明书撰写(CNIPA)-获取技术特征 | POST | https://connect.zhihuiya.com/ai/specification/extract-feature/cnipa | ok | https://open.zhihuiya.com/devportal/api-reference/a9b6b424f8f44221b04102ab46663b75?category=8da258e659976702fa0070378908b963 |
| AI37 | [AI37-4]专利说明书撰写(CNIPA)-生成报告 | POST | https://connect.zhihuiya.com/ai/specification/generate-report/cnipa | ok | https://open.zhihuiya.com/devportal/api-reference/276deeaaf4ac495585c786b744fef16c?category=8da258e659976702fa0070378908b963 |
| AI37 | [AI37-5]专利说明书撰写(CNIPA)-下载报告 | POST | https://connect.zhihuiya.com/ai/specification/download-report | ok | https://open.zhihuiya.com/devportal/api-reference/fe820ca7ac55419e86833080bffaaa55?category=8da258e659976702fa0070378908b963 |

## AI / AI Agent / 外观专利侵权检索

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| AI39 | [AI39-1]外观防侵权检索-任务创建 | POST | https://connect.zhihuiya.com/ai/infringement-detection-creation | ok | https://open.zhihuiya.com/devportal/api-reference/8f022aa5e09d445d971db8812975cb94?category=56d0fa0a485700264f2deff3d3724ad9 |
| AI39 | [AI39-2]外观防侵权检索-任务查询 | POST | https://connect.zhihuiya.com/ai/infringement-detection-query | ok | https://open.zhihuiya.com/devportal/api-reference/d32f096273df438b838ebf5a45fccce7?category=56d0fa0a485700264f2deff3d3724ad9 |
| AI39 | [AI39-1] 外观防侵权检索升级版-提交完整FTO工作流任务 | POST | https://connect.zhihuiya.com/api/mcp/submit-workflow | ok | https://open.zhihuiya.com/devportal/api-reference/cb33e5d091d94226bacdd51be10b2fbb?category=56d0fa0a485700264f2deff3d3724ad9 |
| AI39 | [AI39-2] 外观防侵权检索升级版-查询MCP工作流任务状态 | GET | https://connect.zhihuiya.com/api/mcp/task/{task_id}/status | ok | https://open.zhihuiya.com/devportal/api-reference/9eb9e646c55f48b5bd7add1954dc9502?category=56d0fa0a485700264f2deff3d3724ad9 |
| AI39 | [AI39-3] 外观防侵权检索升级版-获取MCP工作流Stage结果 | GET | https://connect.zhihuiya.com/api/mcp/task/{task_id}/stage/{stage}/result | ok | https://open.zhihuiya.com/devportal/api-reference/3f7905bc465a47bda2e69c2b1c740ca2?category=56d0fa0a485700264f2deff3d3724ad9 |
| AI39 | [AI39-1]外观防侵权检索-提交任务 | POST | https://connect.zhihuiya.com/ai/image-search/submit | ok | https://open.zhihuiya.com/devportal/api-reference/f993ff63fb2a4c9c8bcb4fed288b3da4?category=56d0fa0a485700264f2deff3d3724ad9 |
| AI39 | [AI39-2]外观防侵权检索-获取结果 | POST | https://connect.zhihuiya.com/ai/image-search/report | ok | https://open.zhihuiya.com/devportal/api-reference/66cdeca8e9aa498c83e39a27990f8f94?category=56d0fa0a485700264f2deff3d3724ad9 |

## AI / AI Agent / 外观专利侵权检索1v1

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| AI67 | [AI67-1]外观防侵权检索1V1-任务创建 | POST | https://connect.zhihuiya.com/ai/infringement-detection-1v1-creation | ok | https://open.zhihuiya.com/devportal/api-reference/0a2a1e51aa8d4501b9f1ec7530540d3b?category=0cf93e1d6f2a532a8cc6f4b9c8061b15 |
| AI67 | [AI67-2]外观防侵权检索1V1-任务查询 | POST | https://connect.zhihuiya.com/ai/infringement-detection-1v1-query | ok | https://open.zhihuiya.com/devportal/api-reference/1e1a6e9fff3142b4912c1e0a7e48bb06?category=0cf93e1d6f2a532a8cc6f4b9c8061b15 |

## AI / AI Agent / 可行性分析助手

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| AI40 | [AI40-1]可行性分析助手-报告创建 | POST | https://connect.zhihuiya.com/ai/feasibility-analysis-creation | ok | https://open.zhihuiya.com/devportal/api-reference/39caf858c8af47bdb7e50c068d3c25a6?category=ae12fd36cc7567f4e2c7aac5f7360fd9 |
| AI40 | [AI40-2]可行性分析助手-报告查询 | POST | https://connect.zhihuiya.com/ai/feasibility-analysis-query | ok | https://open.zhihuiya.com/devportal/api-reference/2a849d24514344d9948036a6faec7a06?category=ae12fd36cc7567f4e2c7aac5f7360fd9 |

## AI / AI Agent / 智慧芽 OCR

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| AI60 | [AI60]下载OCR识别结果 | GET | https://connect.zhihuiya.com/ai/ocr/job_id/status | ok | https://open.zhihuiya.com/devportal/api-reference/29cae5c7af1749b3a370bcfc5a1abce3?category=ccb109b7a1937e1f6aeded4cb0982172 |
| AI60 | [AI60]创建OCR识别任务 | POST | https://connect.zhihuiya.com/ai/ocr/task/create | ok | https://open.zhihuiya.com/devportal/api-reference/8e9c4b1e2bcc49e086bded1a738400b1?category=ccb109b7a1937e1f6aeded4cb0982172 |

## AI / AI Agent / AI 翻译

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| AI61 | [AI61]AI翻译 | POST | https://connect.zhihuiya.com/ai/translation | ok | https://open.zhihuiya.com/devportal/api-reference/fb798e843a3d42a5ac880a6245ddb822?category=23bb4253d8ed6bec285381af81eef98e |

## AI / AI Agent / FTO 搜索

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| AI66 | [AI66-1]防侵权检索-创建任务 | POST | https://connect.zhihuiya.com/ai/fto/submit | ok | https://open.zhihuiya.com/devportal/api-reference/dedbedc3016e47138791523e4d18b206?category=71dc7aa2caa748c881c954bc31ad3608 |
| AI66 | [AI66-2]防侵权检索-提取技术特征 | POST | https://connect.zhihuiya.com/ai/fto/feature/extract | ok | https://open.zhihuiya.com/devportal/api-reference/299306da68294c3a990cc4c6b26625da?category=71dc7aa2caa748c881c954bc31ad3608 |
| AI66 | [AI66-3]防侵权检索-确认技术特征 | POST | https://connect.zhihuiya.com/ai/fto/feature/confirm | ok | https://open.zhihuiya.com/devportal/api-reference/cb49929664d64a0ba7255696bb21e889?category=71dc7aa2caa748c881c954bc31ad3608 |
| AI66 | [AI66-4]防侵权检索-启动FTO检索 | POST | https://connect.zhihuiya.com/ai/fto/search/agent | ok | https://open.zhihuiya.com/devportal/api-reference/a8fd91a78c8a4fcc85bf4356e75905c0?category=71dc7aa2caa748c881c954bc31ad3608 |
| AI66 | [AI66-5]防侵权检索-获取FTO检索结果 | POST | https://connect.zhihuiya.com/ai/fto/search/agent/result | ok | https://open.zhihuiya.com/devportal/api-reference/4a52faeee213426f91ed003aac862a25?category=71dc7aa2caa748c881c954bc31ad3608 |
| AI66 | [AI66-6]防侵权检索-创建报告 | POST | https://connect.zhihuiya.com/ai/fto/report/create | ok | https://open.zhihuiya.com/devportal/api-reference/71a3f9e869714fada80d388694aa0144?category=71dc7aa2caa748c881c954bc31ad3608 |
| AI66 | [AI66-7]防侵权检索-下载报告 | POST | https://connect.zhihuiya.com/ai/fto/report/get | ok | https://open.zhihuiya.com/devportal/api-reference/8e2cdaaf3f854e6cbecfd077de3fa473?category=71dc7aa2caa748c881c954bc31ad3608 |
| AI66 | [AI66-8]防侵权检索-添加对比文献或专利 | POST | https://connect.zhihuiya.com/ai/fto/feature/comparison | ok | https://open.zhihuiya.com/devportal/api-reference/dc344c06544d438a936ce47081ef96f9?category=71dc7aa2caa748c881c954bc31ad3608 |

## AI / AI Agent / 配方助手

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| M001 | [M001-1]配方助手-报告创建 | POST | https://connect.zhihuiya.com/ai/formulation-agent-creation | ok | https://open.zhihuiya.com/devportal/api-reference/44fb154deccc4edb98d963a0fc6aa315?category=ea8c5c274e635affb3f447b516959659 |
| M001 | [M001-2]配方助手-报告查询 | POST | https://connect.zhihuiya.com/ai/formulation-agent-query | ok | https://open.zhihuiya.com/devportal/api-reference/915d25b7c6fe46ffa3822b5b2d01ed23?category=ea8c5c274e635affb3f447b516959659 |

## AI / AI Agent / 新颖性检查助手

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| M002 | [M002-1]新颖性检查助手-报告创建 | POST | https://connect.zhihuiya.com/ai/novelty-check-agent-creation | ok | https://open.zhihuiya.com/devportal/api-reference/6b80ba4535894e1187d2b63232437ebc?category=138af7398c8cb1fd58f78d42869eb296 |
| M002 | [M002-2]新颖性检查助手-报告查询 | POST | https://connect.zhihuiya.com/ai/novelty-check-agent-query | ok | https://open.zhihuiya.com/devportal/api-reference/778a69818b46425e92c37ee610729cc4?category=138af7398c8cb1fd58f78d42869eb296 |

## AI / AI Agent / 化学SAR提取

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
|  | 提交SAR解析任务 | POST | https://connect.zhihuiya.com/eurekals/open/sar/file/extract | ok | https://open.zhihuiya.com/devportal/api-reference/f1d441432bd34dd2a1cc0e30ca97ce73?category=138af7398c8cb1fd58f78d42869eb297 |
|  | 获取SAR文件详情 | POST | https://connect.zhihuiya.com/eurekals/open/sar/file/detail | ok | https://open.zhihuiya.com/devportal/api-reference/5f0ee5a1bded45928d174a625b9bd6dd?category=138af7398c8cb1fd58f78d42869eb297 |

## AI / AI Agent / 其他

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| AI01 | [AI01]药物DDT抽取 | POST | https://connect.zhihuiya.com/ai/ner/ddt-ner | ok | https://open.zhihuiya.com/devportal/api-reference/093cf512189949ef84fc9ba6d65a2ec8?category=955d5552c833b6fbdd56be5d1347b0dd |
| AI71 | [AI71]离线报告获取 | POST | https://connect.zhihuiya.com/ai/sso/agent/export-link | ok | https://open.zhihuiya.com/devportal/api-reference/805cadae6f3f4aa686258e10651e43f0?category=955d5552c833b6fbdd56be5d1347b0dd |
| AI72 | [AI72]离线历史记录获取 | POST | https://connect.zhihuiya.com/ai/sso/agent/history | ok | https://open.zhihuiya.com/devportal/api-reference/6db1bde8185f4ab3b6cf55d4516f8496?category=955d5552c833b6fbdd56be5d1347b0dd |
| AI72 | [AI72]离线历史记录获取-批量 | POST | https://connect.zhihuiya.com/ai/sso/agent/batch-history | ok | https://open.zhihuiya.com/devportal/api-reference/f7615ec196b14757a5541274868c9d61?category=955d5552c833b6fbdd56be5d1347b0dd |
| AI88 | [AI88-1]获取企业简报列表 | GET | https://connect.zhihuiya.com/eureka/tech-monitor-api/company-monitors | ok | https://open.zhihuiya.com/devportal/api-reference/d70a0d8bb48a4ca89a40d37cb2e60e00?category=955d5552c833b6fbdd56be5d1347b0dd |
| AI88 | [AI88-2]查询企业简报聚合信息 | GET | https://connect.zhihuiya.com/eureka/tech-monitor-api/company-monitor/aggregated-info | ok | https://open.zhihuiya.com/devportal/api-reference/7d7f162c51bc4c739ab16d610a4bb89f?category=955d5552c833b6fbdd56be5d1347b0dd |
| AI03 | [AI03]新闻实体识别(NER) | POST | https://connect.zhihuiya.com/ai/ner/news-ner | ok | https://open.zhihuiya.com/devportal/api-reference/6485153ce6384fff94a83c9b7647f5cc?category=955d5552c833b6fbdd56be5d1347b0dd |
| AI30 | [AI30]相似专利检索与比对 | POST | https://connect.zhihuiya.com/search/patent/similar-patent-comparison | ok | https://open.zhihuiya.com/devportal/api-reference/9febebfb9ab14e4e8a47d051e8fa811d?category=955d5552c833b6fbdd56be5d1347b0dd |
| AI31 | [AI31]专利发明点总结 | POST | https://connect.zhihuiya.com/search/patent/patent-core-invention-points | ok | https://open.zhihuiya.com/devportal/api-reference/cf1cbf8ad617442986a2c49e63a462cc?category=955d5552c833b6fbdd56be5d1347b0dd |

## AI / AI Agent / 通信

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| T001 | [T001]通信标准必要专利（SEP）智能判断 | POST | https://connect.zhihuiya.com/open_api/task/aicc | ok | https://open.zhihuiya.com/devportal/api-reference/4da77dc3593c4aa3a8dddf87b22a7e1f?category=955d5552c833b6fbdd56be5d1347b0de |

## DATA / 数据 / 专利数据检索

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| P062 | [P062]获取图像批量检索结果 | POST | https://connect.zhihuiya.com/search/patent/image-search/single-batch-result | ok | https://open.zhihuiya.com/devportal/api-reference/723780e001cd40b0a447bcafc8b6bbab?category=efc9973a23144eda91f38ad303264bba |
| P072 | [P072]分类号检索助手 | GET | https://connect.zhihuiya.com/search/patent/classification/helper-search | ok | https://open.zhihuiya.com/devportal/api-reference/6a1ced708ea44f069634afc43527ebaa?category=efc9973a23144eda91f38ad303264bba |
| P071 | [P071]分类号助手查询 | GET | https://connect.zhihuiya.com/search/patent/classification/helper-section-subclass | ok | https://open.zhihuiya.com/devportal/api-reference/073d4d3aca7142268460d221921ae49f?category=efc9973a23144eda91f38ad303264bba |
| P075 | [P075]检索式检索专利嵌套版 | POST | https://connect.zhihuiya.com/search/patent/nested-search-patent | ok | https://open.zhihuiya.com/devportal/api-reference/8963c005e50e4703a815064a1da047b0?category=efc9973a23144eda91f38ad303264bba |
| P001 | [P001]检索式统计专利量 | POST | https://connect.zhihuiya.com/search/patent/query-search-count/v2 | ok | https://open.zhihuiya.com/devportal/api-reference/a361d842a4064da586d97e89e107b75e?category=efc9973a23144eda91f38ad303264bba |
| P002 | [P002]检索式检索专利 | POST | https://connect.zhihuiya.com/search/patent/query-search-patent/v2 | ok | https://open.zhihuiya.com/devportal/api-reference/c7b19fe7bca2413e9b9451add624ffb3?category=efc9973a23144eda91f38ad303264bba |
| P004 | [P004]公司申请人检索专利 | POST | https://connect.zhihuiya.com/search/patent/company-search-patent/v2 | ok | https://open.zhihuiya.com/devportal/api-reference/5a6b29620f734e1e981255c69f406569?category=efc9973a23144eda91f38ad303264bba |
| P005 | [P005]公司专利权人检索专利 | POST | https://connect.zhihuiya.com/search/patent/current-search-patent/v2 | ok | https://open.zhihuiya.com/devportal/api-reference/06ec570bf0074fcfba7906329ea476e6?category=efc9973a23144eda91f38ad303264bba |
| P007 | [P007]专利号检索相似专利 | POST | https://connect.zhihuiya.com/search/patent/similar-search-patent/v2 | ok | https://open.zhihuiya.com/devportal/api-reference/09c2678e78964fb6b904009ce1c96097?category=efc9973a23144eda91f38ad303264bba |
| P008 | [P008]语义检索相似专利 | POST | https://connect.zhihuiya.com/search/patent/semantic-search-patent/v2 | ok | https://open.zhihuiya.com/devportal/api-reference/f4c97687975a4715a48c73db19bf56c3?category=efc9973a23144eda91f38ad303264bba |
| P010 | [P010]上传图片获取专利图像检索URL | POST | https://connect.zhihuiya.com/image-search/image-upload | ok | https://open.zhihuiya.com/devportal/api-reference/8d391a763e674860bcd19ac1a26dbb27?category=efc9973a23144eda91f38ad303264bba |
| P061 | [P061]专利图像检索-多图 | POST | https://connect.zhihuiya.com/search/patent/image-multiple | ok | https://open.zhihuiya.com/devportal/api-reference/9ea5be8b5ade44ee853b42996b870147?category=efc9973a23144eda91f38ad303264bba |
| P006 | [P006]国防专利检索 | POST | https://connect.zhihuiya.com/search/patent/company-search-defense-patent/v2 | ok | https://open.zhihuiya.com/devportal/api-reference/643b98038e11450796631468f4ed6806?category=efc9973a23144eda91f38ad303264bba |
| P060 | [P060]专利图像检索-单图 | POST | https://connect.zhihuiya.com/search/patent/image-single | ok | https://open.zhihuiya.com/devportal/api-reference/a60fb01ada6f42c78373177eac1c7b90?category=efc9973a23144eda91f38ad303264bba |
| P003 | [P003]检索式检索专利并筛选 | POST | https://connect.zhihuiya.com/search/patent/query/v2 | ok | https://open.zhihuiya.com/devportal/api-reference/d722e46193404654af5649c03beab778?category=efc9973a23144eda91f38ad303264bba |
| P069 | [P069] 智慧芽标准专利号查询 | POST | https://connect.zhihuiya.com/search/patent/patent-search-pn | ok | https://open.zhihuiya.com/devportal/api-reference/d6da9151532f4aa2bcf99d36170ac402?category=efc9973a23144eda91f38ad303264bba |
| P070 | [P070]关键词助手 | POST | https://connect.zhihuiya.com/search/patent/keyword-suggest | ok | https://open.zhihuiya.com/devportal/api-reference/26d5a7d5ff4746b79e6212d201a81f83?category=efc9973a23144eda91f38ad303264bba |
| P062 | [P062]生成图像批量检索任务 | POST | https://connect.zhihuiya.com/search/patent/image-search/single-batch-create | ok | https://open.zhihuiya.com/devportal/api-reference/22f081ab4d8c4071a26338102cbc2a29?category=efc9973a23144eda91f38ad303264bba |
| P060 | [P060]专利图像检索-单图形搜升级版 | POST | https://connect.zhihuiya.com/search/patent/image-single/beta | ok | https://open.zhihuiya.com/devportal/api-reference/c037fd731ffd41c1a428c5b49035a810?category=efc9973a23144eda91f38ad303264bba |

## DATA / 数据 / 专利基础数据

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| P021 | [P021]摘要附图 | GET | https://connect.zhihuiya.com/basic-patent-data/abstract-image | ok | https://open.zhihuiya.com/devportal/api-reference/d5156a0eeb834d458c2fb81a8e988bf8?category=66c86b965a8e4297a04a918363648f2f |
| P012 | [P012]著录项目 | GET | https://connect.zhihuiya.com/basic-patent-data/bibliography | ok | https://open.zhihuiya.com/devportal/api-reference/d610ed5b057046d2abbcb054cabda38a?category=66c86b965a8e4297a04a918363648f2f |
| P020 | [P020]PDF全文 | GET | https://connect.zhihuiya.com/basic-patent-data/pdf-data | ok | https://open.zhihuiya.com/devportal/api-reference/2a5d0a85b88f4b8b9dd7591c9a3256e8?category=66c86b965a8e4297a04a918363648f2f |
| P015 | [P015]专利被引用（Beta） | GET | https://connect.zhihuiya.com/basic-patent-data/forward-citation/v3 | ok | https://open.zhihuiya.com/devportal/api-reference/9f8bf84192194344a3b44e01ab592ab8?category=66c86b965a8e4297a04a918363648f2f |
| P042 | [P042]全文附图 | POST | https://connect.zhihuiya.com/basic-patent-data/fulltext-image | ok | https://open.zhihuiya.com/devportal/api-reference/661a2501e83b4a8dab5e8730591ae9fe?category=66c86b965a8e4297a04a918363648f2f |
| P041 | [P041]简单法律状态 | GET | https://connect.zhihuiya.com/basic-patent-data/simple-legal-status | ok | https://open.zhihuiya.com/devportal/api-reference/e26b615bcb404d9891dc3fa0ef92e203?category=66c86b965a8e4297a04a918363648f2f |
| P016 | [P016]智慧芽专利引用-文献 | GET | https://connect.zhihuiya.com/advanced-patent-data/forward-citation/npl | ok | https://open.zhihuiya.com/devportal/api-reference/85990c1f0f82499684af7d018e7b57af?category=66c86b965a8e4297a04a918363648f2f |
| P013 | [P013]法律状态 | GET | https://connect.zhihuiya.com/basic-patent-data/legal-status | ok | https://open.zhihuiya.com/devportal/api-reference/b2f1f242138a4d56be3e43537d1fd3c2?category=66c86b965a8e4297a04a918363648f2f |
| P018 | [P018]权利要求 | GET | https://connect.zhihuiya.com/basic-patent-data/claim-data | ok | https://open.zhihuiya.com/devportal/api-reference/cadb3df3bd584fc28c67d86fd484082b?category=66c86b965a8e4297a04a918363648f2f |
| P014 | [P014]专利家族 | GET | https://connect.zhihuiya.com/basic-patent-data/patent-family | ok | https://open.zhihuiya.com/devportal/api-reference/89d0816de42c4b7cb8a00b7220a15379?category=66c86b965a8e4297a04a918363648f2f |
| P011 | [P011]简单著录项 | GET | https://connect.zhihuiya.com/basic-patent-data/simple-bibliography | ok | https://open.zhihuiya.com/devportal/api-reference/728e672703004329ab7aeb1a7e3a074a?category=66c86b965a8e4297a04a918363648f2f |
| P019 | [P019]说明书 | GET | https://connect.zhihuiya.com/basic-patent-data/description-data | ok | https://open.zhihuiya.com/devportal/api-reference/1642c67943c34bf8b64e69e2d3fafed3?category=66c86b965a8e4297a04a918363648f2f |
| P043 | [P043]摘要翻译 | GET | https://connect.zhihuiya.com/basic-patent-data/abstract-data-translated | ok | https://open.zhihuiya.com/devportal/api-reference/27b56e8f541c498ea5bcd7b9bd9c343b?category=66c86b965a8e4297a04a918363648f2f |
| P044 | [P044]权利要求翻译 | GET | https://connect.zhihuiya.com/basic-patent-data/claim-data-translated | ok | https://open.zhihuiya.com/devportal/api-reference/c05574ffbf254c56aa0fb9115c2ef72a?category=66c86b965a8e4297a04a918363648f2f |
| P045 | [P045]说明书翻译 | GET | https://connect.zhihuiya.com/basic-patent-data/description-data-translated | ok | https://open.zhihuiya.com/devportal/api-reference/8c6cda14fa524df78b391540dd2ea841?category=66c86b965a8e4297a04a918363648f2f |
| P073 | [P073]全文导航位置信息 | GET | https://connect.zhihuiya.com/basic-patent-data/description-offset | ok | https://open.zhihuiya.com/devportal/api-reference/04fb46f6b3e148208ddb5058b63340c7?category=66c86b965a8e4297a04a918363648f2f |
| P042 | [P042]全文内嵌附图 | GET | https://connect.zhihuiya.com/basic-patent-data/fulltext-inline-image | ok | https://open.zhihuiya.com/devportal/api-reference/1f21a1f21c0147e1918ec3e8f07e6310?category=66c86b965a8e4297a04a918363648f2f |

## DATA / 数据 / 专利挖掘数据

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| P023 | [P023]应用领域分类V2 | GET | https://connect.zhihuiya.com/high-value-data/application-domain-v2 | ok | https://open.zhihuiya.com/devportal/api-reference/aeb2706fa7aa4cfbac6b4806681da3be?category=6351c8358f964774924d8e17d903cb77 |
| P025 | [P025]专利技术三要素 | GET | https://connect.zhihuiya.com/high-value-data/tech-problem-and-benefit-summary | ok | https://open.zhihuiya.com/devportal/api-reference/a9d21b54cca64ef188b5015771301071?category=6351c8358f964774924d8e17d903cb77 |
| P022 | [P022]战略新兴产业分类 | GET | https://connect.zhihuiya.com/high-value-data/seic-classification | ok | https://open.zhihuiya.com/devportal/api-reference/5520026e2a3c437389edf96247f67902?category=6351c8358f964774924d8e17d903cb77 |
| P024 | [P024]技术主题分类 | GET | https://connect.zhihuiya.com/high-value-data/technology-topic | ok | https://open.zhihuiya.com/devportal/api-reference/82bfca8574d146e794eb078675133580?category=6351c8358f964774924d8e17d903cb77 |
| P066 | [P066]专利分类号说明 | POST | https://connect.zhihuiya.com/high-value-data/patent-classification-description | ok | https://open.zhihuiya.com/devportal/api-reference/023b617df73e44888e76d653e06f2251?category=6351c8358f964774924d8e17d903cb77 |
| P064 | [P064]专利增值数据 | GET | https://connect.zhihuiya.com/basic-patent-data/patent_enhanced_data | ok | https://open.zhihuiya.com/devportal/api-reference/38b59d43bff041e18635f345e95bc1cc?category=6351c8358f964774924d8e17d903cb77 |
| P101 | [P101]材料工作流 | POST | https://connect.zhihuiya.com/material/material-ontology | ok | https://open.zhihuiya.com/devportal/api-reference/0b0bb4d4e6e84f35aa57cb6c0a2e1bdf?category=6351c8358f964774924d8e17d903cb77 |
| P100 | [P100]专利PUM | POST | https://connect.zhihuiya.com/material/patent-pum | ok | https://open.zhihuiya.com/devportal/api-reference/7b2c313794904297a0e33342b02a024e?category=6351c8358f964774924d8e17d903cb77 |
| P103 | [P103]专利SPUM | POST | https://connect.zhihuiya.com/material/material-spum | ok | https://open.zhihuiya.com/devportal/api-reference/c1d6cf7cc8e4486bb59e368df78c4a2b?category=6351c8358f964774924d8e17d903cb77 |
| P102 | [P102]材料物质 | POST | https://connect.zhihuiya.com/material/material-substance | ok | https://open.zhihuiya.com/devportal/api-reference/f4d88c6775fb42c592500e1e75b484c7?category=6351c8358f964774924d8e17d903cb77 |
| P063 | [P063]专利智能附图 | POST | https://connect.zhihuiya.com/search/patent/intelligent-attached-image | ok | https://open.zhihuiya.com/devportal/api-reference/e28542de3d454e7d9bee5b2d38038c6d?category=6351c8358f964774924d8e17d903cb77 |

## DATA / 数据 / 专利法律详情

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| P033 | [P033]标准必要专利(SEP) | GET | https://connect.zhihuiya.com/advanced-patent-data/sep-data | ok | https://open.zhihuiya.com/devportal/api-reference/7ef9cf09bbd64f90871e0a7997e04d26?category=42d537e6fbd446c2b6fb6bd0e908672d |
| P031 | [P031]海关备案 | GET | https://connect.zhihuiya.com/advanced-patent-data/customs-data | ok | https://open.zhihuiya.com/devportal/api-reference/683c7965a0f54970950f154a189ff7c1?category=42d537e6fbd446c2b6fb6bd0e908672d |
| P046 | [P046]欧洲统一法院状态 | GET | https://connect.zhihuiya.com/advanced-patent-data/status-of-unified-patent-court | ok | https://open.zhihuiya.com/devportal/api-reference/b11f8b945936451a8c63c698d079abb5?category=42d537e6fbd446c2b6fb6bd0e908672d |
| P030 | [P030]专利质押 | GET | https://connect.zhihuiya.com/advanced-patent-data/pledge-data | ok | https://open.zhihuiya.com/devportal/api-reference/816109e71d8c4eb5af154257d9a3c2ba?category=42d537e6fbd446c2b6fb6bd0e908672d |
| P047 | [P047]专利缴费结果获取 | POST | https://connect.zhihuiya.com/fee/get_fee | ok | https://open.zhihuiya.com/devportal/api-reference/97836bb0a6c94bc095bc387074244b9e?category=42d537e6fbd446c2b6fb6bd0e908672d |
| P026 | [P026]法律详情 | GET | https://connect.zhihuiya.com/advanced-patent-data/legal-data | ok | https://open.zhihuiya.com/devportal/api-reference/7fe29b1d698947deb87e77b77263fb6f?category=42d537e6fbd446c2b6fb6bd0e908672d |
| P032 | [P032]专利奖 | GET | https://connect.zhihuiya.com/advanced-patent-data/award-data | ok | https://open.zhihuiya.com/devportal/api-reference/e0b0af52a081461a835fa6b8c9440549?category=42d537e6fbd446c2b6fb6bd0e908672d |
| P028 | [P028]专利许可 | GET | https://connect.zhihuiya.com/advanced-patent-data/license-data | ok | https://open.zhihuiya.com/devportal/api-reference/5b491603d85d4f0b95e774bde7889d42?category=42d537e6fbd446c2b6fb6bd0e908672d |
| P029 | [P029]专利转移 | GET | https://connect.zhihuiya.com/advanced-patent-data/transfer-data | ok | https://open.zhihuiya.com/devportal/api-reference/a5c65b1085fa473492873691f9e95c24?category=42d537e6fbd446c2b6fb6bd0e908672d |
| P034 | [P034]诉讼数据 | GET | https://connect.zhihuiya.com/high-value-data/litigation | ok | https://open.zhihuiya.com/devportal/api-reference/74c1b26358f74e10a7f4403a4da6d3cc?category=42d537e6fbd446c2b6fb6bd0e908672d |
| P047 | [P047]专利缴费信息请求 | POST | https://connect.zhihuiya.com/fee/apno_input | ok | https://open.zhihuiya.com/devportal/api-reference/149d8956ac1e46558238105a2c04042c?category=42d537e6fbd446c2b6fb6bd0e908672d |
| P027 | [P027]复审无效 | GET | https://connect.zhihuiya.com/advanced-patent-data/re-examination-and-invalidation | ok | https://open.zhihuiya.com/devportal/api-reference/fcadddbb2d134444bd1ced1fe41f3e91?category=42d537e6fbd446c2b6fb6bd0e908672d |
| P048 | [P048]海外专利审查文件 | POST | https://connect.zhihuiya.com/advanced-patent-data/overseas-patent-documents | ok | https://open.zhihuiya.com/devportal/api-reference/0c8c0c49b5b04e57847cd55e5f049fbe?category=42d537e6fbd446c2b6fb6bd0e908672d |

## DATA / 数据 / 专利价值评估

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| P037 | [P037]法律指标 | GET | https://connect.zhihuiya.com/patent-valuation-data/legal_indicators | ok | https://open.zhihuiya.com/devportal/api-reference/6687b33c3e2a4908b6a2b6821f581d19?category=79e7b001cd3f44c0bdacfd6b44d79355 |
| P040 | [P040]经济指标 | GET | https://connect.zhihuiya.com/patent-valuation-data/economic_indicators | ok | https://open.zhihuiya.com/devportal/api-reference/9b228a4b5caa4a8eba1d07dd0b49305d?category=79e7b001cd3f44c0bdacfd6b44d79355 |
| P038 | [P038]市场指标 | GET | https://connect.zhihuiya.com/patent-valuation-data/market_indicators | ok | https://open.zhihuiya.com/devportal/api-reference/222b0e78f09341cb8036057c6c579695?category=79e7b001cd3f44c0bdacfd6b44d79355 |
| P035 | [P035]专利价值 | GET | https://connect.zhihuiya.com/patent-valuation-data/patent_valuation | ok | https://open.zhihuiya.com/devportal/api-reference/725139c24c0549529278ca4bd5b86ef2?category=79e7b001cd3f44c0bdacfd6b44d79355 |
| P051 | [P051]专利申请前评估-可专利性 | POST | https://connect.zhihuiya.com/patent-valuation-data/patent_ability | ok | https://open.zhihuiya.com/devportal/api-reference/4a7cdd16769e4aec8ef4f9885e681a71?category=79e7b001cd3f44c0bdacfd6b44d79355 |
| P039 | [P039]战略指标 | GET | https://connect.zhihuiya.com/patent-valuation-data/strategic_indicators | ok | https://open.zhihuiya.com/devportal/api-reference/da3cde30f0fa455b958d722c101bfbe6?category=79e7b001cd3f44c0bdacfd6b44d79355 |
| P053 | [P053]专利申请前评估-运营情况 | POST | https://connect.zhihuiya.com/patent-valuation-data/operation_situation | ok | https://open.zhihuiya.com/devportal/api-reference/bb70cea083f54f6eb9bd8abd8a39e5f3?category=79e7b001cd3f44c0bdacfd6b44d79355 |
| P036 | [P036]技术指标 | GET | https://connect.zhihuiya.com/patent-valuation-data/technology_indicators | ok | https://open.zhihuiya.com/devportal/api-reference/17188e944aff4f7784ba28c1483da934?category=79e7b001cd3f44c0bdacfd6b44d79355 |
| P050 | [P050]专利申请前评估-技术创新性 | POST | https://connect.zhihuiya.com/patent-valuation-data/tech_innovation | ok | https://open.zhihuiya.com/devportal/api-reference/32187e4dc57844c98decd92ecea601df?category=79e7b001cd3f44c0bdacfd6b44d79355 |
| P052 | [P052]专利申请前评估-市场前景 | POST | https://connect.zhihuiya.com/patent-valuation-data/market_prospect | ok | https://open.zhihuiya.com/devportal/api-reference/dbcd7b3fd00747f1aa4ea20670a6eede?category=79e7b001cd3f44c0bdacfd6b44d79355 |

## DATA / 数据 / 专利监控导出

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| P055 | [P055]获取专利导出详情 | GET | https://connect.zhihuiya.com/patent-search/task | ok | https://open.zhihuiya.com/devportal/api-reference/dcd0c25baa29413cbd323c4e66829f0f?category=0f688a923ecf42c9a88a746a507198fc |
| P059 | [P059]删除专利监控项目 | DELETE | https://connect.zhihuiya.com/patent-alert/delete | ok | https://open.zhihuiya.com/devportal/api-reference/bb733ac6d5314724990536bcad928c19?category=0f688a923ecf42c9a88a746a507198fc |
| P055 | [P055]检索式创建专利导出任务 | POST | https://connect.zhihuiya.com/patent-search/export/V2 | ok | https://open.zhihuiya.com/devportal/api-reference/1a059d0faf754fd1af6f508ffe318f84?category=0f688a923ecf42c9a88a746a507198fc |
| P057 | [P057]查询监控项更新状态 | GET | https://connect.zhihuiya.com/patent-alert/check | ok | https://open.zhihuiya.com/devportal/api-reference/a998af2f3c224b8497dde81893e5c93c?category=0f688a923ecf42c9a88a746a507198fc |
| P056 | [P056]创建专利监控预警项目v2 | POST | https://connect.zhihuiya.com/patent-alert/creation | ok | https://open.zhihuiya.com/devportal/api-reference/4986cefb4a814a31a75cbe703434d9e2?category=0f688a923ecf42c9a88a746a507198fc |
| P058 | [P058]编辑专利监控项目v2 | POST | https://connect.zhihuiya.com/patent-alert/update/v2 | ok | https://open.zhihuiya.com/devportal/api-reference/7b512b6579d9490b87f4229d556a7767?category=0f688a923ecf42c9a88a746a507198fc |

## DATA / 数据 / 专利技术全景分析

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| A011 | [A011]专利类型趋势分析 | POST | https://connect.zhihuiya.com/insights/patent-type-trend | ok | https://open.zhihuiya.com/devportal/api-reference/2f2715fc8ae84363b632eb5f5d7899ce?category=5a492cc39ed14d5c9100502c997e06b7 |
| A106 | [A106]企业被引用最多的专利 | GET | https://connect.zhihuiya.com/insights-company/most-cited-latest | ok | https://open.zhihuiya.com/devportal/api-reference/abd33fd9c2ba4073abb16e76d73e31ec?category=5a492cc39ed14d5c9100502c997e06b7 |
| A104 | [A104]企业专利申请趋势 | GET | https://connect.zhihuiya.com/insights-company/patent-trends | ok | https://open.zhihuiya.com/devportal/api-reference/b8d342c19ef14b319a8f9d0ea16e1a60?category=5a492cc39ed14d5c9100502c997e06b7 |
| A109 | [A109]企业简单法律状态统计 | GET | https://connect.zhihuiya.com/insights-company/simple-legal-status | ok | https://open.zhihuiya.com/devportal/api-reference/b0a3aa3abd6c4f198d2e3b7dc9381cd6?category=5a492cc39ed14d5c9100502c997e06b7 |
| A010 | [A010]专利价值分布 | GET | https://connect.zhihuiya.com/insights/portfolio-value | ok | https://open.zhihuiya.com/devportal/api-reference/c3f7f5e9dad5420eaaa8ac3d9f32ecde?category=5a492cc39ed14d5c9100502c997e06b7 |
| A007 | [A007]申请人排名分析 | GET | https://connect.zhihuiya.com/insights/applicant-ranking | ok | https://open.zhihuiya.com/devportal/api-reference/f3ea05e846a3409a99c34567c5f2e215?category=5a492cc39ed14d5c9100502c997e06b7 |
| A009 | [A009]最多诉讼专利 | GET | https://connect.zhihuiya.com/insights/most-asserted | ok | https://open.zhihuiya.com/devportal/api-reference/b2d9d05497504f6281b186165ec8c1f6?category=5a492cc39ed14d5c9100502c997e06b7 |
| A107 | [A107]最多引用该企业专利的公司 | GET | https://connect.zhihuiya.com/insights-company/most-cited | ok | https://open.zhihuiya.com/devportal/api-reference/9ae9b5b310f14886b22fc6e259e84d14?category=5a492cc39ed14d5c9100502c997e06b7 |
| A004 | [A004]技术来源国/地区排名 | GET | https://connect.zhihuiya.com/insights/priority-country | ok | https://open.zhihuiya.com/devportal/api-reference/4e0afb6dabd146e4b4978f4a321e1147?category=5a492cc39ed14d5c9100502c997e06b7 |
| A003 | [A003]旭日图 | GET | https://connect.zhihuiya.com/insights/wheel-of-innovation | ok | https://open.zhihuiya.com/devportal/api-reference/72e9a634177d4ede930e6905bb0a3c18?category=5a492cc39ed14d5c9100502c997e06b7 |
| A001 | [A001]专利趋势分析（检索式检索） | POST | https://connect.zhihuiya.com/insights-openapi/patent-trends-query | ok | https://open.zhihuiya.com/devportal/api-reference/0fbf46c2a615467e9bae0e5861e846b8?category=5a492cc39ed14d5c9100502c997e06b7 |
| A105 | [A105]企业专利总申请布局 | GET | https://connect.zhihuiya.com/insights-company/patent-portfolio-overview | ok | https://open.zhihuiya.com/devportal/api-reference/7ccbb9a124864482a5b2b11edb486ffa?category=5a492cc39ed14d5c9100502c997e06b7 |
| A102 | [A102]企业创新战略雷达图 | GET | https://connect.zhihuiya.com/insights-company/strategy-map | ok | https://open.zhihuiya.com/devportal/api-reference/e05cd8a9b8d94583b7f54c3b4acc978a?category=5a492cc39ed14d5c9100502c997e06b7 |
| A110 | [A110]企业专利转入转出 | GET | https://connect.zhihuiya.com/insights-company/acquisition-divestiture | ok | https://open.zhihuiya.com/devportal/api-reference/2aa26883a2194be9858a9e611678b82c?category=5a492cc39ed14d5c9100502c997e06b7 |
| A101 | [A101]企业创新词云 | GET | https://connect.zhihuiya.com/insights-company/word-cloud | ok | https://open.zhihuiya.com/devportal/api-reference/333049b3053840038199aa433aed31cc?category=5a492cc39ed14d5c9100502c997e06b7 |
| A008 | [A008]简单法律状态统计 | GET | https://connect.zhihuiya.com/insights/simple-legal-status | ok | https://open.zhihuiya.com/devportal/api-reference/b973e5a1f9c84263bcada4260f3c00c1?category=5a492cc39ed14d5c9100502c997e06b7 |
| A006 | [A006]发明人排名分析 | GET | https://connect.zhihuiya.com/insights/inventor-ranking | ok | https://open.zhihuiya.com/devportal/api-reference/c96a922163c842c1a342b8ee6c62be3e?category=5a492cc39ed14d5c9100502c997e06b7 |
| A005 | [A005]被引用最多的专利 | GET | https://connect.zhihuiya.com/insights/most-cited | ok | https://open.zhihuiya.com/devportal/api-reference/910bccc1389f4889bbfd400d9e3d0925?category=5a492cc39ed14d5c9100502c997e06b7 |
| A002 | [A002]创新词云（检索式搜索） | POST | https://connect.zhihuiya.com/insights/word-cloud-query | ok | https://open.zhihuiya.com/devportal/api-reference/0174353399ec4652807bbf4ed22ee334?category=5a492cc39ed14d5c9100502c997e06b7 |
| A108 | [A108]企业规模最大的专利家族 | GET | https://connect.zhihuiya.com/insights-company/largest-patent-family | ok | https://open.zhihuiya.com/devportal/api-reference/4ad1817223ca4059ba187dd9e358fd67?category=5a492cc39ed14d5c9100502c997e06b7 |
| A103 | [A103]企业技术构成分析 | GET | https://connect.zhihuiya.com/insights-company/key-technology-overview | ok | https://open.zhihuiya.com/devportal/api-reference/8d753bbe11934ccda6041442fb585b5a?category=5a492cc39ed14d5c9100502c997e06b7 |
| A201 | [A201]技术效果分布 | POST | https://connect.zhihuiya.com/search/company/technology-effect-Distribution | ok | https://open.zhihuiya.com/devportal/api-reference/febc0b29368c478dbb8a0e9126d84788?category=5a492cc39ed14d5c9100502c997e06b7 |
| A202 | [A202]技术领域词云 | POST | https://connect.zhihuiya.com/search/company/technology-field-word-cloud | ok | https://open.zhihuiya.com/devportal/api-reference/367de19839934204897affd9ae1bb6e7?category=5a492cc39ed14d5c9100502c997e06b7 |
| A012 | [A012]技术功效短语分布 | POST | https://connect.zhihuiya.com/insights/technology-effect-Distribution | ok | https://open.zhihuiya.com/devportal/api-reference/dd61eb5a710140459d2ee1a8362b9c2d?category=5a492cc39ed14d5c9100502c997e06b7 |

## DATA / 数据 / 文献数据

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| L011 | [L011]文献作者和机构 | POST | https://connect.zhihuiya.com/literature/author-affiliation | ok | https://open.zhihuiya.com/devportal/api-reference/0c3fb28f7cb748e4ba1e9e095e1e152d?category=ceb6fd95d1e04ef79d8ea8a9ef6e6d19 |
| L010 | [L010]文献著录信息 | POST | https://connect.zhihuiya.com/literature/bibliography | ok | https://open.zhihuiya.com/devportal/api-reference/f6298582535b4f61afb8a92c6853a544?category=ceb6fd95d1e04ef79d8ea8a9ef6e6d19 |
| L012 | [L012]文献引用 | POST | https://connect.zhihuiya.com/literature/citation | ok | https://open.zhihuiya.com/devportal/api-reference/b4c2e84cf937459ebcba72054b4bc5ec?category=ceb6fd95d1e04ef79d8ea8a9ef6e6d19 |
| L014 | [L014]文献期刊 | POST | https://connect.zhihuiya.com/literature/journal | ok | https://open.zhihuiya.com/devportal/api-reference/a44fcfd8ca7049b591f80b1a359847b0?category=ceb6fd95d1e04ef79d8ea8a9ef6e6d19 |
| L001 | [L001]文献检索 | POST | https://connect.zhihuiya.com/search/literature/query-search | ok | https://open.zhihuiya.com/devportal/api-reference/34d6724de3b541bc9032126c7251feb1?category=ceb6fd95d1e04ef79d8ea8a9ef6e6d19 |

## DATA / 数据 / 智慧芽学社课程

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| AC01 | [AC01]获取课程列表 | GET | https://connect.zhihuiya.com/academy/course-list | ok | https://open.zhihuiya.com/devportal/api-reference/577cc8d4f5b24012a713aa5207e4ba9f?category=39db220beba84f19909d17eb203f55ea |
| AC02 | [AC02]获取具体课程详情 | GET | https://connect.zhihuiya.com/academy/course-details | ok | https://open.zhihuiya.com/devportal/api-reference/51c0905919304b0795754c8dda136a4e?category=39db220beba84f19909d17eb203f55ea |
| AC03 | [AC03]获取课程的课件 |  |  | unavailable | https://open.zhihuiya.com/devportal/api-reference/4c3443e5a3d94b1d81c883b992f0b750?category=39db220beba84f19909d17eb203f55ea |

## DATA / 数据 / 定制聚合数据

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| D005 | [D005]专利检索 | POST | https://connect.zhihuiya.com/search/patent/query-search-patent/v3 | ok | https://open.zhihuiya.com/devportal/api-reference/d31dea3840654a8b8d9d02d0b4a4567c?category=58b932c5e5b3438ea399d2c08110876c |
| D007 | [D007]专利详情接口 | GET | https://connect.zhihuiya.com/basic-patent-data/patent-detail | ok | https://open.zhihuiya.com/devportal/api-reference/ebd2f40ba3aa4fd181386e06d6444400?category=58b932c5e5b3438ea399d2c08110876c |
| D101 | [D101]技术生命周期 | POST | https://connect.zhihuiya.com/shhgy/reportdata/life-cycle | ok | https://open.zhihuiya.com/devportal/api-reference/76644e6ce3a6445eb703f57372aae6f3?category=58b932c5e5b3438ea399d2c08110876c |
| D102 | [D102]申请人排名 | POST | https://connect.zhihuiya.com/shhgy/reportdata/applicant-rank | ok | https://open.zhihuiya.com/devportal/api-reference/e6629742e1964c9f98cfd9762986b752?category=58b932c5e5b3438ea399d2c08110876c |
| D103 | [D103]主要申请人技术分析 | POST | https://connect.zhihuiya.com/shhgy/reportdata/applicant-technology-analysis | ok | https://open.zhihuiya.com/devportal/api-reference/76e2858b49024c14b3da7033b9656890?category=58b932c5e5b3438ea399d2c08110876c |
| D104 | [D104]主要申请人申请趋势 | POST | https://connect.zhihuiya.com/shhgy/reportdata/applicant-trend | ok | https://open.zhihuiya.com/devportal/api-reference/7b8c72d5c84e498799ba992c23c8e5d7?category=58b932c5e5b3438ea399d2c08110876c |
| D105 | [D105]合作申请分析 | POST | https://connect.zhihuiya.com/shhgy/reportdata/cooperation-applicant-analysis | ok | https://open.zhihuiya.com/devportal/api-reference/44c43ba3651a401f8112c3017b855125?category=58b932c5e5b3438ea399d2c08110876c |
| D106 | [D106]专利趋势 | POST | https://connect.zhihuiya.com/shhgy/reportdata/patent-trend | ok | https://open.zhihuiya.com/devportal/api-reference/d88709f47c5342e4a2217a09d78de4c2?category=58b932c5e5b3438ea399d2c08110876c |
| D107 | [D107]重要技术分支主要申请人分布 | POST | https://connect.zhihuiya.com/shhgy/reportdata/technology-applicant-distribution | ok | https://open.zhihuiya.com/devportal/api-reference/dc0469f5c13e46438cf481cd6921f430?category=58b932c5e5b3438ea399d2c08110876c |
| D108 | [D108]技术构成 | POST | https://connect.zhihuiya.com/shhgy/reportdata/technology-constitute | ok | https://open.zhihuiya.com/devportal/api-reference/f5af0b088d7d481ab1b357f410c99b64?category=58b932c5e5b3438ea399d2c08110876c |
| D110 | [D110]受理局统计（按照年） | POST | https://connect.zhihuiya.com/shhgy/reportdata/rec-office-year | ok | https://open.zhihuiya.com/devportal/api-reference/869f3a9ac0d84deda21f07d683d4baa1?category=58b932c5e5b3438ea399d2c08110876c |
| D111 | [D111]被引用数排名 | POST | https://connect.zhihuiya.com/shhgy/reportdata/refered-rank | ok | https://open.zhihuiya.com/devportal/api-reference/6de65b54cf3248ab8c1771ebdb7bd864?category=58b932c5e5b3438ea399d2c08110876c |
| D109 | [D109]受理局统计 | POST | https://connect.zhihuiya.com/shhgy/reportdata/rec-office | ok | https://open.zhihuiya.com/devportal/api-reference/d7285c2e47754602bf5054ba18d59c08?category=58b932c5e5b3438ea399d2c08110876c |
| D113 | [D113]专利列表 | POST | https://connect.zhihuiya.com/shhgy/reportdata/patent-list | ok | https://open.zhihuiya.com/devportal/api-reference/a9278af0b2cc4f33b8885e165042e2fb?category=58b932c5e5b3438ea399d2c08110876c |
| D112 | [D112]同族排名 | POST | https://connect.zhihuiya.com/shhgy/reportdata/famn-rank | ok | https://open.zhihuiya.com/devportal/api-reference/71a443efb73a448f9d7fe99dfc39b39b?category=58b932c5e5b3438ea399d2c08110876c |
| D115 | [D115]领域地图 | POST | https://connect.zhihuiya.com/shhgy/reportdata/domain-map | ok | https://open.zhihuiya.com/devportal/api-reference/e740376eac9c4432bd03d4c3d13f5d92?category=58b932c5e5b3438ea399d2c08110876c |
| D114 | [D114]专利字段详情（仅包含大文本） | POST | https://connect.zhihuiya.com/shhgy/reportdata/patent-info | ok | https://open.zhihuiya.com/devportal/api-reference/43fa4e74c4e445178dc3f2cb9205a2d3?category=58b932c5e5b3438ea399d2c08110876c |
| D116 | [D116]3D地图分析 | POST | https://connect.zhihuiya.com/shhgy/reportdata/3d-map | ok | https://open.zhihuiya.com/devportal/api-reference/b12fb4f891e240509b45345efd3ddb60?category=58b932c5e5b3438ea399d2c08110876c |
|  | 对账单V2 | POST | https://connect.zhihuiya.com/open-user/statement/v2 | ok | https://open.zhihuiya.com/devportal/api-reference/49dc0776e42a40a4954c9e055608b860?category=58b932c5e5b3438ea399d2c08110876c |
| D201 | [D201]专利详情文本 | POST | https://connect.zhihuiya.com/jdf/patent_detail_text | ok | https://open.zhihuiya.com/devportal/api-reference/fb383a8dbb0447dd84824a16c48081d1?category=58b932c5e5b3438ea399d2c08110876c |
| D301 | [D301]专利详情聚合 | GET | https://connect.zhihuiya.com/basic-patent-data/patent-detail-aggregation | ok | https://open.zhihuiya.com/devportal/api-reference/e7b1079402494186a81c30f1cc0e422c?category=58b932c5e5b3438ea399d2c08110876c |
| D006 | [D006]专利检索统计 | POST | https://connect.zhihuiya.com/search/patent/query-search-patent-facet | ok | https://open.zhihuiya.com/devportal/api-reference/bc49d79734764895923e383140ee4494?category=58b932c5e5b3438ea399d2c08110876c |
| D008 | [D008]专利 PDF | GET | https://connect.zhihuiya.com/basic-patent-data/patent-pdf | ok | https://open.zhihuiya.com/devportal/api-reference/3a9a3a8db0654223a034cd570f47133c?category=58b932c5e5b3438ea399d2c08110876c |
| D009 | [D009]专利检索及详情 | POST | https://connect.zhihuiya.com/search/patent/query-search-patent-detail | ok | https://open.zhihuiya.com/devportal/api-reference/472a652245934c0fa81a5580a6a2aeb2?category=58b932c5e5b3438ea399d2c08110876c |
| D010 | [D010]专利统计 | POST | https://connect.zhihuiya.com/search/patent/query-search-facet | ok | https://open.zhihuiya.com/devportal/api-reference/f81aa9dcc41d488ea8680a8bc7ed9e03?category=58b932c5e5b3438ea399d2c08110876c |

## DATA / 数据 / 商标数据

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| T002 | [T002]商标图搜 | POST | https://connect.zhihuiya.com/trademark/image-search | ok | https://open.zhihuiya.com/devportal/api-reference/00f8cf545a36466fadb04131cec5742f?category=279ef4736eb1462ea904d4500080e87b |
| T001 | [T001]商标字段检索 | POST | https://connect.zhihuiya.com/trademark/search | ok | https://open.zhihuiya.com/devportal/api-reference/a959211a6569420dbf708aa2c568d41b?category=279ef4736eb1462ea904d4500080e87b |
| T010 | [T010]商标详情 | GET | https://connect.zhihuiya.com/trademark/data/detail | ok | https://open.zhihuiya.com/devportal/api-reference/bde64bdc56ef47708fad6208114c69cf?category=279ef4736eb1462ea904d4500080e87b |

## DATA / 数据 / 科创企业评估

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| C028 | [C028]企业专利风险预警回溯 | POST | https://connect.zhihuiya.com/company/enterprise-patent-risk-warning-backtracking | ok | https://open.zhihuiya.com/devportal/api-reference/5678e3bfaa2e4a1ab474cdf92f2ff459?category=03cfc0add04a443eafb085c801ef207d |
| C029 | [C029]企业专利风险预警趋势 | POST | https://connect.zhihuiya.com/company/enterprise-patent-risk-warning-trend | ok | https://open.zhihuiya.com/devportal/api-reference/ab78959bc0c64eabb026139131252d1e?category=03cfc0add04a443eafb085c801ef207d |
| C027 | [C027]企业专利风险预警 | POST | https://connect.zhihuiya.com/company/enterprise-patent-risk-warning | ok | https://open.zhihuiya.com/devportal/api-reference/04cd2ece0bfa43d4b2e4f380ee7ba7a3?category=03cfc0add04a443eafb085c801ef207d |
| C024 | [C024]科创企业评估指标（全球） | POST | https://connect.zhihuiya.com/company/technology-evaluation-indicators-global | ok | https://open.zhihuiya.com/devportal/api-reference/96fd752e6d0d4fe5bdafd9711293e031?category=03cfc0add04a443eafb085c801ef207d |
| C022 | [C022]科创企业评估（全球） | POST | https://connect.zhihuiya.com/company/technology-evaluation-global | ok | https://open.zhihuiya.com/devportal/api-reference/b2048151f93047c3be92adb7714425a8?category=03cfc0add04a443eafb085c801ef207d |
| C023 | [C023]科创企业指标（全球） | POST | https://connect.zhihuiya.com/company/technology-indicators-global | ok | https://open.zhihuiya.com/devportal/api-reference/2884c029fbae42e8b3c6a151f3ac71fc?category=03cfc0add04a443eafb085c801ef207d |
| C025 | [C025]科创企业集团穿透（全球） | POST | https://connect.zhihuiya.com/company/global-company-group-technology-evaluation-indicators | ok | https://open.zhihuiya.com/devportal/api-reference/b1a920f9e4c0477eaa63a4d3a30142e0?category=03cfc0add04a443eafb085c801ef207d |
| C026 | [C026]科创企业回溯（全球） | POST | https://connect.zhihuiya.com/company/technology-evaluation-indicators-backtracking-global | ok | https://open.zhihuiya.com/devportal/api-reference/b5a17fa0bdbc4c20b56ea0bb19e4e3dc?category=03cfc0add04a443eafb085c801ef207d |

## DATA / 数据 / 企业基础数据

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| C002 | [C002]对外投资 | POST | https://connect.zhihuiya.com/company/outbound-investment | ok | https://open.zhihuiya.com/devportal/api-reference/a43fe178e9e44d3d94ad2397fbc0b828?category=025c200d78ca475ebca231ee13ea3e62 |
| C020 | [C020]标准信息 | POST | https://connect.zhihuiya.com/company/standard-information | ok | https://open.zhihuiya.com/devportal/api-reference/4b4bb369784b4b4eb0410eaf98f19220?category=025c200d78ca475ebca231ee13ea3e62 |
| C013 | [C013]融资信息 | POST | https://connect.zhihuiya.com/company/financing-information | ok | https://open.zhihuiya.com/devportal/api-reference/f5bd829b15564051acc006436da38974?category=025c200d78ca475ebca231ee13ea3e62 |
| C019 | [C019]IPO进程 | POST | https://connect.zhihuiya.com/company/ipo-process | ok | https://open.zhihuiya.com/devportal/api-reference/85c3733430f44d9aa831de1266272216?category=025c200d78ca475ebca231ee13ea3e62 |
| C021 | [C021]资质证书 | POST | https://connect.zhihuiya.com/company/qualification-certificate | ok | https://open.zhihuiya.com/devportal/api-reference/b4a2147339ab48d7a2329ca4379c35b0?category=025c200d78ca475ebca231ee13ea3e62 |
| C001 | [C001]工商信息 | POST | https://connect.zhihuiya.com/company/registration-information | ok | https://open.zhihuiya.com/devportal/api-reference/a1ce672f0111418aa96bca03c20cbda6?category=025c200d78ca475ebca231ee13ea3e62 |
| C003 | [C003]股东信息 | POST | https://connect.zhihuiya.com/company/shareholder-information | ok | https://open.zhihuiya.com/devportal/api-reference/de5b7e528bba46188f78202dc7ecb8e3?category=025c200d78ca475ebca231ee13ea3e62 |
| C018 | [C018]上市信息 | POST | https://connect.zhihuiya.com/company/listing-Information | ok | https://open.zhihuiya.com/devportal/api-reference/e3cee0d123884fa1ba09902eeb1affb0?category=025c200d78ca475ebca231ee13ea3e62 |
| C014 | [C014]科技资质 | POST | https://connect.zhihuiya.com/company/technology-qualification | ok | https://open.zhihuiya.com/devportal/api-reference/33c16c814f2340ae8e60e870a0b13efe?category=025c200d78ca475ebca231ee13ea3e62 |
| C015 | [C015]获奖信息 | POST | https://connect.zhihuiya.com/company/awards-information | ok | https://open.zhihuiya.com/devportal/api-reference/9a4adc5ce145429a9e6daf151dcee225?category=025c200d78ca475ebca231ee13ea3e62 |
| C016 | [C016]主要人员 | POST | https://connect.zhihuiya.com/company/main-member | ok | https://open.zhihuiya.com/devportal/api-reference/781018f23f5a49c8b79c4b3e4c4e6b8d?category=025c200d78ca475ebca231ee13ea3e62 |
| C017 | [C017]核心团队 | POST | https://connect.zhihuiya.com/company/core-member | ok | https://open.zhihuiya.com/devportal/api-reference/907fcd5e113a43bbb203598205f2a4ac?category=025c200d78ca475ebca231ee13ea3e62 |
| C037 | [C037]企业搜索接口 | POST | https://connect.zhihuiya.com/company/search | ok | https://open.zhihuiya.com/devportal/api-reference/7811d19137e743fd893106971b20b524?category=025c200d78ca475ebca231ee13ea3e62 |
| C038 | [C038]投资信息 | POST | https://connect.zhihuiya.com/company/investment-information | ok | https://open.zhihuiya.com/devportal/api-reference/b2afc80e6a4548c2ab104f9f8fa5b1a5?category=025c200d78ca475ebca231ee13ea3e62 |

## DATA / 数据 / 科创企业画像标签

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| C007 | [C007]行业分类 | POST | https://connect.zhihuiya.com/company/industry-classification | ok | https://open.zhihuiya.com/devportal/api-reference/2ebb8ab5c2384a94abd8e24a6176e89a?category=11620b2f8d86408f89c85cbd5afe0b06 |
| C005 | [C005]科技认定 | POST | https://connect.zhihuiya.com/company/technology-label | ok | https://open.zhihuiya.com/devportal/api-reference/4121dd8301704b959756b36f678fb5a5?category=11620b2f8d86408f89c85cbd5afe0b06 |
| C010 | [C010]标准制定 | POST | https://connect.zhihuiya.com/company/standard-development | ok | https://open.zhihuiya.com/devportal/api-reference/76410e0ebe3d4f52849389eeafae989a?category=11620b2f8d86408f89c85cbd5afe0b06 |
| C004 | [C004]企业属性 | POST | https://connect.zhihuiya.com/company/attribute | ok | https://open.zhihuiya.com/devportal/api-reference/a5401242f1a84600add5d12322667c87?category=11620b2f8d86408f89c85cbd5afe0b06 |
| C006 | [C006]获奖情况 | POST | https://connect.zhihuiya.com/company/awards | ok | https://open.zhihuiya.com/devportal/api-reference/28ebff24a75949b681dd29771d677028?category=11620b2f8d86408f89c85cbd5afe0b06 |
| C009 | [C009]产业技术链节点 | POST | https://connect.zhihuiya.com/company/industrial-technology-chain | ok | https://open.zhihuiya.com/devportal/api-reference/82184a6794bc49d5a5994167d38e2bec?category=11620b2f8d86408f89c85cbd5afe0b06 |
| C011 | [C011]知识产权 | POST | https://connect.zhihuiya.com/company/intellectual-property | ok | https://open.zhihuiya.com/devportal/api-reference/a8c24dce5a4f4f19921a4bd031d7cfcb?category=11620b2f8d86408f89c85cbd5afe0b06 |
| C008 | [C008]产品技术分类 | POST | https://connect.zhihuiya.com/company/product-technical-classification | ok | https://open.zhihuiya.com/devportal/api-reference/5dc3a722a1464d41a8ebec6040fa46a4?category=11620b2f8d86408f89c85cbd5afe0b06 |

## DATA / 数据 / 科创企业知识产权

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| C034 | [C034]企业植物新品种保护申请信息 | POST | https://connect.zhihuiya.com/special-ip-data/new-plant-variety/application | ok | https://open.zhihuiya.com/devportal/api-reference/d124a3307c68474283c74090768f1801?category=cbf06026bf2e4502a0a7811fcacf0a5a |
| C034 | [C034]企业植物新品种保护授权信息 | POST | https://connect.zhihuiya.com/special-ip-data/new-plant-variety/issue | ok | https://open.zhihuiya.com/devportal/api-reference/b482661be5e548038ab334f00cd1cb82?category=cbf06026bf2e4502a0a7811fcacf0a5a |
| C033 | [C033]科创企业集成电路布图设计 | POST | https://connect.zhihuiya.com/special-ip-data/ic-design | ok | https://open.zhihuiya.com/devportal/api-reference/3a52cff3823b438fac0e02527830a1e4?category=cbf06026bf2e4502a0a7811fcacf0a5a |
| C031 | [C031]科创企业商标数据 | POST | https://connect.zhihuiya.com/special-ip-data/enterprise-trademark | ok | https://open.zhihuiya.com/devportal/api-reference/4e359d31ff0f4ff78adf7ca08792ed5a?category=cbf06026bf2e4502a0a7811fcacf0a5a |
| C032 | [C032]科创企业软件著作权 | POST | https://connect.zhihuiya.com/special-ip-data/software-copyright | ok | https://open.zhihuiya.com/devportal/api-reference/ff03a07ad06948b29c5acc50918d6e5f?category=cbf06026bf2e4502a0a7811fcacf0a5a |
| C046 | [C046]潜在买家推荐接口 | POST | https://connect.zhihuiya.com/search/patent/potential-buyer | ok | https://open.zhihuiya.com/devportal/api-reference/b0311e4f53794ad3841f0d97b92d5097?category=cbf06026bf2e4502a0a7811fcacf0a5a |

## DATA / 数据 / 企业科创力分析

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| C112 | [C112]企业核心专利 | POST | https://connect.zhihuiya.com/innovation/company/core_patent | ok | https://open.zhihuiya.com/devportal/api-reference/c9b7825dcf164cac9e3a971afdd15c76?category=7698cbaaf3dd48659f442d29b4b430b7 |
| C114 | [C114]企业产学研分析 | POST | https://connect.zhihuiya.com/company/industry-university-research | ok | https://open.zhihuiya.com/devportal/api-reference/8a0fb45b503449c2815633d6ff32ca2e?category=7698cbaaf3dd48659f442d29b4b430b7 |
| C115 | [C115]企业产学研研发技术分析 | POST | https://connect.zhihuiya.com/company/industry-university-research-ipc | ok | https://open.zhihuiya.com/devportal/api-reference/4b9e3e4e34da42efb39738dd9f0a5f91?category=7698cbaaf3dd48659f442d29b4b430b7 |
| C116 | [C116]企业产学研共同申请地域分布 | POST | https://connect.zhihuiya.com/company/industry-university-research-region-distribution | ok | https://open.zhihuiya.com/devportal/api-reference/b496b25641f94221abdf2929890baf6e?category=7698cbaaf3dd48659f442d29b4b430b7 |

## DATA / 数据 / 生物医药检索

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| B043 | [B043] 医药新闻检索 | POST | https://connect.zhihuiya.com/synapse/news/search | ok | https://open.zhihuiya.com/devportal/api-reference/90cbd33f72be46a5b3c4978229c79371?category=bfb260a6b3214626bff57350e25d982a |
| B045 | [B045] 医药交易检索 | POST | https://connect.zhihuiya.com/synapse/drug-deal/search | ok | https://open.zhihuiya.com/devportal/api-reference/f56e605a9c294e048c5d8162267b33f9?category=bfb260a6b3214626bff57350e25d982a |
| B012 | [B012] 临床试验检索 | POST | https://connect.zhihuiya.com/synapse/clinical-trial/search | ok | https://open.zhihuiya.com/devportal/api-reference/7cee83ebfa7a48b29e9b73df812784bd?category=bfb260a6b3214626bff57350e25d982a |
| B011 | [B011] 医药文献检索 | POST | https://connect.zhihuiya.com/synapse/paper/search | ok | https://open.zhihuiya.com/devportal/api-reference/4c71e1ff69d14e20ab96287a364e2f6d?category=bfb260a6b3214626bff57350e25d982a |
| B007 | [B007] 药物搜索 | POST | https://connect.zhihuiya.com/synapse/drug/search | ok | https://open.zhihuiya.com/devportal/api-reference/fc81b81c526b462881e3b6de58c694de?category=bfb260a6b3214626bff57350e25d982a |
| B009 | [B009] 药物核心专利检索 | POST | https://connect.zhihuiya.com/synapse/patent/core/search | ok | https://open.zhihuiya.com/devportal/api-reference/a9e3ea3138764562b7ca80bae9014c5e?category=bfb260a6b3214626bff57350e25d982a |
| B044 | [B044] 临床结果检索 | POST | https://connect.zhihuiya.com/synapse/ct-result/search | ok | https://open.zhihuiya.com/devportal/api-reference/6223113f7b184e8abfa132222e4c3119?category=bfb260a6b3214626bff57350e25d982a |
| B009 | [B009-1]药物核心专利聚合 | POST | https://connect.zhihuiya.com/synapse/patent/core/aggregation | ok | https://open.zhihuiya.com/devportal/api-reference/36fba2455dc24433a545754cdd2c8f7c?category=bfb260a6b3214626bff57350e25d982a |
| B069 | [B069] 转化医学检索 | POST | https://connect.zhihuiya.com/synapse/translational/medicine/search | ok | https://open.zhihuiya.com/devportal/api-reference/f222c43773564575b8267c7c63fecca4?category=bfb260a6b3214626bff57350e25d982a |

## DATA / 数据 / 化合物和生物序列

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| B067 | [B067-2]查询OCSR任务结果 | GET | https://connect.zhihuiya.com/eurekals/open/ocsr/task | ok | https://open.zhihuiya.com/devportal/api-reference/9b51416af31f46a0887e49e70ee355d1?category=3f28cda8bccc4d79be9b1c4c71955085 |
| B067 | [B067-1]创建OCSR识别任务 | POST | https://connect.zhihuiya.com/eurekals/open/ocsr/task/submit | ok | https://open.zhihuiya.com/devportal/api-reference/e0692921e5ca45b181807a51e0eeae68?category=3f28cda8bccc4d79be9b1c4c71955085 |
| B068 | [B068-1]创建三元组识别任务 | POST | https://connect.zhihuiya.com/eureka/material/docAnalyzer/submitPDF | ok | https://open.zhihuiya.com/devportal/api-reference/89da9b4b46fc4e00855729b7a991bcc2?category=3f28cda8bccc4d79be9b1c4c71955085 |
| B068 | [B068-2]查询三元组任务结果 | POST | https://connect.zhihuiya.com/eureka/material/docAnalyzer/getExtractMaterial | ok | https://open.zhihuiya.com/devportal/api-reference/99fa3b2bf31341298339f78b65150adf?category=3f28cda8bccc4d79be9b1c4c71955085 |
| B001 | [B001]化学结构式检索 | POST | https://connect.zhihuiya.com/chemical-openapi/compound | ok | https://open.zhihuiya.com/devportal/api-reference/48a0dd819b3e467084fea825fb878ff8?category=3f28cda8bccc4d79be9b1c4c71955085 |
| B003/4 | [B003/4-1]获取序列检索结果 | POST | https://connect.zhihuiya.com/bio-openapi/sequence/job/result | ok | https://open.zhihuiya.com/devportal/api-reference/c6c31c67b34c4288a546f015b533090b?category=3f28cda8bccc4d79be9b1c4c71955085 |
| B003 | [B003]生物序列Motif检索 | POST | https://connect.zhihuiya.com/bio-openapi/sequence/motif/job | ok | https://open.zhihuiya.com/devportal/api-reference/be646f6e7bfd40d884a4057b79b16f4d?category=3f28cda8bccc4d79be9b1c4c71955085 |
| B004 | [B004]生物序列普通检索 | POST | https://connect.zhihuiya.com/bio-openapi/sequence/job | ok | https://open.zhihuiya.com/devportal/api-reference/8dfd91e73d1b463c875df3aa0b24cd32?category=3f28cda8bccc4d79be9b1c4c71955085 |
| B002 | [B002]单个化学结构专利检索 | GET | https://connect.zhihuiya.com/chemical-openapi/compound/patents | ok | https://open.zhihuiya.com/devportal/api-reference/b20758f71a9e42029d4157a31afb78da?category=3f28cda8bccc4d79be9b1c4c71955085 |
| B014 | [B014]化合物基本信息 | GET | https://connect.zhihuiya.com/chemical-openapi/compound/detail | ok | https://open.zhihuiya.com/devportal/api-reference/4423d3004b0b47d9a4edd44671bd4f19?category=3f28cda8bccc4d79be9b1c4c71955085 |
| B005 | [B005]单个序列全部专利 | POST | https://connect.zhihuiya.com/bio-openapi/sequence/patent | ok | https://open.zhihuiya.com/devportal/api-reference/cf6741a291204d3a896ea6adfdb40694?category=3f28cda8bccc4d79be9b1c4c71955085 |
| B003/4 | [B003/4-0]后台检索任务状态 | GET | https://connect.zhihuiya.com/bio-openapi/sequence/job/status | ok | https://open.zhihuiya.com/devportal/api-reference/fb86b15491c8438bbac9c810b6cd4d1e?category=3f28cda8bccc4d79be9b1c4c71955085 |
| B063 | [B063]提取多篇专利生物序列 | POST | https://connect.zhihuiya.com/bio-openapi/patent/extract/multi | ok | https://open.zhihuiya.com/devportal/api-reference/3ad6f992305e41a1beded903ff9e366d?category=3f28cda8bccc4d79be9b1c4c71955085 |
| B062 | [B062]提取单篇专利生物序列 | POST | https://connect.zhihuiya.com/bio-openapi/patent/extract/single | ok | https://open.zhihuiya.com/devportal/api-reference/c1aa536aac634ff587e1d0b7c4308b5f?category=3f28cda8bccc4d79be9b1c4c71955085 |
| B016 | [B016]序列信息 | POST | https://connect.zhihuiya.com/bio/sequence/info | ok | https://open.zhihuiya.com/devportal/api-reference/c8d88f9dcbf34e6684a15604881b1199?category=3f28cda8bccc4d79be9b1c4c71955085 |
| B071 | [B071]提取单篇专利化学结构 | POST | https://connect.zhihuiya.com/synapse/patent/chemical/getSingleData | ok | https://open.zhihuiya.com/devportal/api-reference/de58d06ff6694cd7a159ba7d57b1c503?category=3f28cda8bccc4d79be9b1c4c71955085 |
| B072 | [B072-2]提取多篇专利化学结构-查询 | GET | https://connect.zhihuiya.com/synapse/patent/chemical/getTaskResult | ok | https://open.zhihuiya.com/devportal/api-reference/1da87029a86c412c942256d00755845c?category=3f28cda8bccc4d79be9b1c4c71955085 |
| B072 | [B072-1]提取多篇专利化学结构-创建 | POST | https://connect.zhihuiya.com/synapse/patent/chemical/submitTask | ok | https://open.zhihuiya.com/devportal/api-reference/bf6f90b3acd544e98c294899fdacf87a?category=3f28cda8bccc4d79be9b1c4c71955085 |
| B015 | [B015]化合物理化性质 | GET | https://connect.zhihuiya.com/synapse/drug/compound-physicochemical-props | ok | https://open.zhihuiya.com/devportal/api-reference/0cc0ad2fe2b04a43a20995e95e9a5397?category=3f28cda8bccc4d79be9b1c4c71955085 |
| B042 | [B042] 单个化学结构文献检索 | POST | https://connect.zhihuiya.com/synapse/chemical/paper/search | ok | https://open.zhihuiya.com/devportal/api-reference/b0324af6a4a445c5a6e7244b0913c5b2?category=3f28cda8bccc4d79be9b1c4c71955085 |
| B075 | [B075] 化合物合成路线 | POST | https://connect.zhihuiya.com/synapse/chemical/reaction/route | ok | https://open.zhihuiya.com/devportal/api-reference/d28f5273df1846b78d768f89c6e70315?category=3f28cda8bccc4d79be9b1c4c71955085 |
| B073 | [B073]化合物关键词检索 | POST | https://connect.zhihuiya.com/chemical-business/keyword/search | ok | https://open.zhihuiya.com/devportal/api-reference/86d100b2812245658b0a2fc099453f9f?category=3f28cda8bccc4d79be9b1c4c71955085 |
| B068 | [B068-1]PCC分子结构预测-发起任务 | POST | https://connect.zhihuiya.com/chat/pcc-molecule-task | ok | https://open.zhihuiya.com/devportal/api-reference/baac68ce1e424e8dbbcf59173f0f7df1?category=3f28cda8bccc4d79be9b1c4c71955085 |
| B068 | [B068-2]PCC分子结构预测-获取结果 | POST | https://connect.zhihuiya.com/chat/pcc-molecule-result | ok | https://open.zhihuiya.com/devportal/api-reference/25c8d2790ff643739f1e08695dd37358?category=3f28cda8bccc4d79be9b1c4c71955085 |

## DATA / 数据 / 药物基础数据

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| B018 | [B018] 药物基本信息 | GET | https://connect.zhihuiya.com/synapse/drug/detail | ok | https://open.zhihuiya.com/devportal/api-reference/a30570e0137343ba846530767c818752?category=f0bdea3c74b544a8a918861f914cfa9a |
| B019 | [B019] 药物批准信息 | GET | https://connect.zhihuiya.com/synapse/drug/approval | ok | https://open.zhihuiya.com/devportal/api-reference/7b98d10239c549e7a045ce2d49e83bdd?category=f0bdea3c74b544a8a918861f914cfa9a |
| B020 | [B020] 药物研发状态-V2 | GET | https://connect.zhihuiya.com/synapse/drug/highest-dev-status | ok | https://open.zhihuiya.com/devportal/api-reference/0a9dd145933846a2a401344c3f7e69b3?category=f0bdea3c74b544a8a918861f914cfa9a |
| B021 | [B021] 药物特殊审评 | GET | https://connect.zhihuiya.com/synapse/drug/special-approval | ok | https://open.zhihuiya.com/devportal/api-reference/77855af9319c42acb0802c4f964d437d?category=f0bdea3c74b544a8a918861f914cfa9a |
| B040 | [B040] 靶点基本信息 | GET | https://connect.zhihuiya.com/synapse/target/detail | ok | https://open.zhihuiya.com/devportal/api-reference/d2e2fc6dc726442a95e5a6ec3437c3aa?category=f0bdea3c74b544a8a918861f914cfa9a |
| B047 | [B047] 药物相关技术 | GET | https://connect.zhihuiya.com/synapse/drug/xdc | ok | https://open.zhihuiya.com/devportal/api-reference/9301a971588643beb50d429ca26db8a1?category=f0bdea3c74b544a8a918861f914cfa9a |
| B041 | [B041] 靶点竞争格局 | GET | https://connect.zhihuiya.com/synapse/target/analysis | ok | https://open.zhihuiya.com/devportal/api-reference/cbd4491a62da492db34e1879c792a63c?category=f0bdea3c74b544a8a918861f914cfa9a |
| B059 | [B059] 药物批准文件 | POST | https://connect.zhihuiya.com/synapse/drug/approval/file | ok | https://open.zhihuiya.com/devportal/api-reference/c664e8c86887474590a5359fef0926aa?category=f0bdea3c74b544a8a918861f914cfa9a |

## DATA / 数据 / 药物临床数据

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| B027 | [B027] 临床联系人 | GET | https://connect.zhihuiya.com/synapse/clinical-trial/contact | ok | https://open.zhihuiya.com/devportal/api-reference/a4f2af01602345fba6e105d98329d075?category=7accf3f4b4164897a1663dd410ba78b9 |
| B024 | [B024] 临床研究描述 | GET | https://connect.zhihuiya.com/synapse/clinical-trial/description | ok | https://open.zhihuiya.com/devportal/api-reference/1696cbfa56e044eb95086b30a494c647?category=7accf3f4b4164897a1663dd410ba78b9 |
| B026 | [B026] 临床研究方案与设计 | GET | https://connect.zhihuiya.com/synapse/clinical-trial/design | ok | https://open.zhihuiya.com/devportal/api-reference/838f6a9ad563433ead1b9262c684bc22?category=7accf3f4b4164897a1663dd410ba78b9 |
| B022 | [B022] 临床基本信息 | GET | https://connect.zhihuiya.com/synapse/clinical-trial/detail | ok | https://open.zhihuiya.com/devportal/api-reference/12459b66c18f4141bd34feaf84cee8f2?category=7accf3f4b4164897a1663dd410ba78b9 |
| B025 | [B025] 临床受试者信息与入排标准 | GET | https://connect.zhihuiya.com/synapse/clinical-trial/eligibility | ok | https://open.zhihuiya.com/devportal/api-reference/afed7afb563544e8a46cdc175b0d940d?category=7accf3f4b4164897a1663dd410ba78b9 |
| B023 | [B023] 临床相关实体 | GET | https://connect.zhihuiya.com/synapse/clinical-trial/related-entity | ok | https://open.zhihuiya.com/devportal/api-reference/d75905255604452d86cafd93db9a3878?category=7accf3f4b4164897a1663dd410ba78b9 |
| B032 | [B032] 药物临床结果基本信息 | GET | https://connect.zhihuiya.com/synapse/ct-result/detail | ok | https://open.zhihuiya.com/devportal/api-reference/887fc0687e674f41ba756cc98523e217?category=7accf3f4b4164897a1663dd410ba78b9 |
| B048 | [B048] 药物临床结果分组信息 | GET | https://connect.zhihuiya.com/synapse/ct-result/group | ok | https://open.zhihuiya.com/devportal/api-reference/0406141f83ee4c8695a367d7b91ee0c9?category=7accf3f4b4164897a1663dd410ba78b9 |

## DATA / 数据 / 药物挖掘数据

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| B031 | [B031] 医药新闻 | GET | https://connect.zhihuiya.com/synapse/news | ok | https://open.zhihuiya.com/devportal/api-reference/5d4b6fcfe5a642e7b9b7ff11cf9e0eaf?category=b635fd7e14ad40fc9fc9d8d0e8a352e6 |
| B039 | [B039] 药物交易信息 | GET | https://connect.zhihuiya.com/synapse/drug-deal | ok | https://open.zhihuiya.com/devportal/api-reference/529a586742774e838bb464c691dc1d82?category=b635fd7e14ad40fc9fc9d8d0e8a352e6 |
| B030 | [B030] 医药文献 | GET | https://connect.zhihuiya.com/synapse/paper/detail | ok | https://open.zhihuiya.com/devportal/api-reference/7839fcccb7ff4a15a148ea89c5af8a3a?category=b635fd7e14ad40fc9fc9d8d0e8a352e6 |
| B028 | [B028] 专利保护药物与专利分类 | GET | https://connect.zhihuiya.com/synapse/patent/detail | ok | https://open.zhihuiya.com/devportal/api-reference/f7c779d821254dd2b69e9cf33abf76e6?category=b635fd7e14ad40fc9fc9d8d0e8a352e6 |
| B070 | [B070] 转化医学详情 | GET | https://connect.zhihuiya.com/synapse/translational/medicine/detail | ok | https://open.zhihuiya.com/devportal/api-reference/80e34c042d76479ba0d3ec03eb181582?category=b635fd7e14ad40fc9fc9d8d0e8a352e6 |
| B066 | [B066] 亲和力检索 | GET | https://connect.zhihuiya.com/synapse/bio/affinity/search | ok | https://open.zhihuiya.com/devportal/api-reference/1c7be91963a9426aa2e6b5617d5207f3?category=b635fd7e14ad40fc9fc9d8d0e8a352e6 |
| B065 | [B065] 抗原-抗体配对检索 | GET | https://connect.zhihuiya.com/synapse/bio/antibody/search | ok | https://open.zhihuiya.com/devportal/api-reference/56e75d587dea4d06a0a74cfd888f31a8?category=b635fd7e14ad40fc9fc9d8d0e8a352e6 |

## DATA / 数据 / 药物研发机构

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| B033 | [B033] 机构管线信息 | POST | https://connect.zhihuiya.com/synapse/organization/pipeline | ok | https://open.zhihuiya.com/devportal/api-reference/8be2af6ccb9e43b0a8f8dac5a42a8f40?category=f8af26472f55497286ab23533ceb5e03 |
| B034 | [B034] 机构基本信息 | GET | https://connect.zhihuiya.com/synapse/organization/basic-info | ok | https://open.zhihuiya.com/devportal/api-reference/013548ba65f449dab722134c02e4a367?category=f8af26472f55497286ab23533ceb5e03 |
| B035 | [B035] 机构营收 | POST | https://connect.zhihuiya.com/synapse/organization/profit | ok | https://open.zhihuiya.com/devportal/api-reference/efaaac28c37e46ddb976586ef7b13c2d?category=f8af26472f55497286ab23533ceb5e03 |
| B036 | [B036] 科研基金 | POST | https://connect.zhihuiya.com/synapse/organization/grant-funding | ok | https://open.zhihuiya.com/devportal/api-reference/4ff57e830c294cff99a9a93f0d4917fb?category=f8af26472f55497286ab23533ceb5e03 |
| B037 | [B037] 投资 | POST | https://connect.zhihuiya.com/synapse/organization/investment | ok | https://open.zhihuiya.com/devportal/api-reference/615c14240b0449c682987a9150c892f8?category=f8af26472f55497286ab23533ceb5e03 |
| B038 | [B038] 融资 | POST | https://connect.zhihuiya.com/synapse/organization/financing | ok | https://open.zhihuiya.com/devportal/api-reference/6fb8406289b44045a24abd85a7340dbc?category=f8af26472f55497286ab23533ceb5e03 |

## DATA / 数据 / 药物可视化分析

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| B057 | [B057] 牛眼图分析 | POST | https://connect.zhihuiya.com/synapse/bull-eyes-plot | ok | https://open.zhihuiya.com/devportal/api-reference/0b371307a4dc41c687afd9e406935ab5?category=3101f4d62261438a9ee594f113457ff6 |
| B064 | [B064-1]创建药物监控 | POST | https://connect.zhihuiya.com/synapse/alert/drug_search/create | ok | https://open.zhihuiya.com/devportal/api-reference/106569996f1542969cc3ae5fb9f15df7?category=3101f4d62261438a9ee594f113457ff6 |
| B064 | [B064-2]编辑药物监控 | POST | https://connect.zhihuiya.com/synapse/alert/drug_search/edit | ok | https://open.zhihuiya.com/devportal/api-reference/7f972110567c4e1ca6ca6fe623dd706d?category=3101f4d62261438a9ee594f113457ff6 |
| B064 | [B064-3]查询药物监控 | POST | https://connect.zhihuiya.com/synapse/alert/drug_search/query | ok | https://open.zhihuiya.com/devportal/api-reference/a1a24d3ac863422c89bb68d9c97c4edd?category=3101f4d62261438a9ee594f113457ff6 |
| B074 | [B074] 药物里程碑 | POST | https://connect.zhihuiya.com/synapse/drug/milestone | ok | https://open.zhihuiya.com/devportal/api-reference/4507b1e9d3eb43f3b94a05f6bb36f08d?category=3101f4d62261438a9ee594f113457ff6 |

## DATA / 数据 / 智慧芽分析报告

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| R001 | [R001]创建企业科创力报告（无Logo版） | POST | https://connect.zhihuiya.com/innovation/company-report/task/create-no-logo | ok | https://open.zhihuiya.com/devportal/api-reference/3df480a8a377438bb482a4d3aee24a78?category=fa617fa8ef404736a39fc7c51658fe27 |
| R001 | [R001]创建企业科创力报告（智慧芽Logo） | POST | https://connect.zhihuiya.com/innovation/company-report/task/create | ok | https://open.zhihuiya.com/devportal/api-reference/56dabb4e55df45afaf54f5480337b0c3?category=fa617fa8ef404736a39fc7c51658fe27 |
| R002 | [R002]下载专利价值报告 | GET | https://connect.zhihuiya.com/patent-valuation-data/patent-report/job_id/status | ok | https://open.zhihuiya.com/devportal/api-reference/b0911f426e0d44f988cba0eb66fbfc09?category=fa617fa8ef404736a39fc7c51658fe27 |
| R001 | [R001]下载企业科创力报告 | GET | https://connect.zhihuiya.com/innovation/company-report/job_id/status | ok | https://open.zhihuiya.com/devportal/api-reference/c79f7ba124294cc4bb118cffb9242c50?category=fa617fa8ef404736a39fc7c51658fe27 |
| R002 | [R002]创建专利价值报告（智慧芽Logo） | POST | https://connect.zhihuiya.com/patent-valuation-data/patent-report/task/create | ok | https://open.zhihuiya.com/devportal/api-reference/338bce9dbbb04e30af97b6e7bdb03937?category=fa617fa8ef404736a39fc7c51658fe27 |
| R003 | [R003]创建专利申请前评估报告 | POST | https://connect.zhihuiya.com/patent-valuation-data/pre_patent-evaluation-create | ok | https://open.zhihuiya.com/devportal/api-reference/8a3678fb92b04533b805a99c6cb6c135?category=fa617fa8ef404736a39fc7c51658fe27 |
| R003 | [R003]下载专利申请前评估报告 | GET | https://connect.zhihuiya.com/patent-valuation-data/pre_patent-evaluation-export | ok | https://open.zhihuiya.com/devportal/api-reference/b3bca971b92a404e81a7c6696329bd2d?category=fa617fa8ef404736a39fc7c51658fe27 |
| R004 | [R004-3]技术想法查新-下载报告 | POST | https://connect.zhihuiya.com/search/patent/idea-validation/job_id/status | ok | https://open.zhihuiya.com/devportal/api-reference/79b960d161b04c7aa71641008458c6da?category=fa617fa8ef404736a39fc7c51658fe27 |
| R004 | [R004-1]技术想法查新-创建报告 | POST | https://connect.zhihuiya.com/search/patent/idea-validation/task/create | ok | https://open.zhihuiya.com/devportal/api-reference/2b31018547e74f9ea879d9f9a6cc7cd9?category=fa617fa8ef404736a39fc7c51658fe27 |
| R002 | [R002]创建专利价值报告（无logo） | POST | https://connect.zhihuiya.com/patent-valuation-data/patent-report/task/create-no-logo | ok | https://open.zhihuiya.com/devportal/api-reference/7e9584a9c578449f9838908673d2ceb3?category=fa617fa8ef404736a39fc7c51658fe27 |
| R004 | [R004-2]技术想法查新-相似专利 | POST | https://connect.zhihuiya.com/search/patent/idea-validation/similar-patent-comparison | ok | https://open.zhihuiya.com/devportal/api-reference/8ca4a8e1370442b98dc3f058b4536765?category=fa617fa8ef404736a39fc7c51658fe27 |

## DATA / 数据 / Insights公司报告

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
|  | 提交新的Landscape作业 | POST | https://connect.zhihuiya.com/landscape-api/jobs | ok | https://open.zhihuiya.com/devportal/api-reference/dd0e78bed9794dcf8271974ced34258e?category=bad337cea9894bb59bf706f261806aa9 |
|  | 获取Landscape作业结果 | GET | https://connect.zhihuiya.com/landscape-api/jobs/{job_id}/result | ok | https://open.zhihuiya.com/devportal/api-reference/8dfd0280c59841798bedcbb12dbca447?category=bad337cea9894bb59bf706f261806aa9 |
|  | 获取作业状态 | GET | https://connect.zhihuiya.com/landscape-api/jobs/{job_id}/status | ok | https://open.zhihuiya.com/devportal/api-reference/3c97c90f73a748efada3ff639d518b73?category=bad337cea9894bb59bf706f261806aa9 |
|  | 获取特定分面类型的所有列表 | GET | https://connect.zhihuiya.com/landscape-api/jobs/{job_id}/facets/{facet_type} | ok | https://open.zhihuiya.com/devportal/api-reference/d8303b1b63f24b1da21acfaeeb8a3bbf?category=bad337cea9894bb59bf706f261806aa9 |
|  | 获取作业的所有专利列表 | GET | https://connect.zhihuiya.com/landscape-api/jobs/{job_id}/patents | ok | https://open.zhihuiya.com/devportal/api-reference/a1fde5bbda1d4232876b5c85a91cdc51?category=bad337cea9894bb59bf706f261806aa9 |
|  | 获取特定Landscape分面的所有专利列表 | GET | https://connect.zhihuiya.com/landscape-api/jobs/{job_id}/facets/{facet_type}/detail | ok | https://open.zhihuiya.com/devportal/api-reference/94af95b58f6948fd95d4f662412d19ed?category=bad337cea9894bb59bf706f261806aa9 |

## DATA / 数据 / 企业科创评估(5级)

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| DP004 | [DP004]科创企业评估指标&风险预警 | POST | https://connect.zhihuiya.com/innovation/estimate/company-index-warning | ok | https://open.zhihuiya.com/devportal/api-reference/797c08432fea4767b5e7087ba92cd6ab?category=1d92109d4c6e49a3931adfef5b8a4bb8 |
| DP003 | [DP003]科创企业风险预警 | POST | https://connect.zhihuiya.com/innovation/company_warning | ok | https://open.zhihuiya.com/devportal/api-reference/5aba369d21ed4dee86d6e934990f9cbd?category=1d92109d4c6e49a3931adfef5b8a4bb8 |
| DP002 | [DP002]科创企业指标 | POST | https://connect.zhihuiya.com/innovation/company_valuation_indicators | ok | https://open.zhihuiya.com/devportal/api-reference/1d3b51518cb94f1b92c3dff0e8b960f5?category=1d92109d4c6e49a3931adfef5b8a4bb8 |
| DP001 | [DP001]科创企业评估 | POST | https://connect.zhihuiya.com/innovation/company_valuation | ok | https://open.zhihuiya.com/devportal/api-reference/77ebb2eebda54551b79645c10bcbe659?category=1d92109d4c6e49a3931adfef5b8a4bb8 |
| DP005 | [DP005]科创企业评估指标 | POST | https://connect.zhihuiya.com/innovation/estimate/company-index | ok | https://open.zhihuiya.com/devportal/api-reference/e3a4a3effc204536a9dac3bdf21e0d69?category=1d92109d4c6e49a3931adfef5b8a4bb8 |

## DATA / 数据 / 生物医药字典数据

| 接口号 | 名称 | 方法 | 地址 | 状态 | 文档 |
| --- | --- | --- | --- | --- | --- |
| B058 | [B058] 治疗领域 | POST | https://connect.zhihuiya.com/synapse/disease/therapeutic-area | ok | https://open.zhihuiya.com/devportal/api-reference/d340276ab49f4a3ba1db458e760753fe?category=a4b3690aa2394d879acab25e315c916d |
| B049 | [B049] 药物类型ID查询 | POST | https://connect.zhihuiya.com/synapse/drug-type/autocomplete | ok | https://open.zhihuiya.com/devportal/api-reference/658755968ea1442391332cd6ad8a991e?category=a4b3690aa2394d879acab25e315c916d |
| B050 | [B050] 适应症ID查询 | POST | https://connect.zhihuiya.com/synapse/disease/autocomplete | ok | https://open.zhihuiya.com/devportal/api-reference/f40b7156b3d24c8aa90a42e9c0ee5437?category=a4b3690aa2394d879acab25e315c916d |
| B051 | [B051] 靶点ID查询 | POST | https://connect.zhihuiya.com/synapse/target/autocomplete | ok | https://open.zhihuiya.com/devportal/api-reference/0e404a931834481eb5fd56cc20a1666a?category=a4b3690aa2394d879acab25e315c916d |
| B052 | [B052] 机构ID查询 | POST | https://connect.zhihuiya.com/synapse/organization/autocomplete | ok | https://open.zhihuiya.com/devportal/api-reference/5f76e173b56e428e854ed208bbab335f?category=a4b3690aa2394d879acab25e315c916d |
| B053 | [B053] 药物ID查询 | POST | https://connect.zhihuiya.com/synapse/drug/autocomplete | ok | https://open.zhihuiya.com/devportal/api-reference/153d97c55e4e4c0f80b50ced787021e9?category=a4b3690aa2394d879acab25e315c916d |
| B054 | [B054] 作用机制ID查询 | POST | https://connect.zhihuiya.com/synapse/mechanism-action/autocomplete | ok | https://open.zhihuiya.com/devportal/api-reference/80eaecf616844287adc3fab20b75b68c?category=a4b3690aa2394d879acab25e315c916d |
| B055 | [B055] 指标ID查询 | POST | https://connect.zhihuiya.com/synapse/outcome/autocomplete | ok | https://open.zhihuiya.com/devportal/api-reference/70c489ff76894c5bbd238ac383539d6f?category=a4b3690aa2394d879acab25e315c916d |
| B056 | [B056] 字典查询 | POST | https://connect.zhihuiya.com/synapse/dictionary/search | ok | https://open.zhihuiya.com/devportal/api-reference/fd7354574a734775b4ea0a54fed7d6f5?category=a4b3690aa2394d879acab25e315c916d |
| B056 | [B056-1]专利技术分类ID查询 | POST | https://connect.zhihuiya.com/synapse/patent/technology/autocomplete | ok | https://open.zhihuiya.com/devportal/api-reference/83134953a46745e38f7b94fa74fa9ef0?category=a4b3690aa2394d879acab25e315c916d |
