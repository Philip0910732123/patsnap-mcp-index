#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
refresh_all.py — 一键完成整套刷新（推荐入口）。

为什么需要编排
--------------
推断映射要基于「最新抓到的 tool 描述」，而 apply_catalog.py 又是消费映射的
一方，所以必须先写一次官方事实、再推断、再合并一次。起步包/场景推荐又依赖
合并后的映射来反查 API 编号，因此排在最后。手工按顺序敲命令容易漏步，
这里把顺序固定下来，对外只暴露一条命令。

链路：
  fetch_catalog.py          纯 HTTP 抓 50 个详情页 + OpenAPI（免登录）
  apply_catalog.py          第 1 次：把最新官方事实写入 index.json
  infer_api_mapping.py      基于最新 index.json 推断 MCP -> API 映射
  apply_catalog.py          第 2 次：把映射合并进 index.json（幂等）
  build_recommendations.py  起步包 / 场景推荐 / 上下文成本（读人工策展表）
  build_docs.py             重出 5 份 Markdown + llms.txt + AGENTS.md

人工确认保存在两个文件里，本脚本不会覆盖：
  data/manual-overrides.json   MCP→API 映射的实测结论
  data/recommendations.json    起步包与场景的「该装什么」判断

用法：python scripts/refresh_all.py
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = sys.executable

STEPS = [
    ("抓取官方全量数据（免登录）", "scripts/fetch_catalog.py"),
    ("写入 index.json · 官方事实", "scripts/apply_catalog.py"),
    ("推断 MCP → API 映射", "scripts/infer_api_mapping.py"),
    ("写入 index.json · 合并映射", "scripts/apply_catalog.py"),
    ("计算起步包 / 场景推荐 / 上下文成本", "scripts/build_recommendations.py"),
    ("重出 Markdown 文档与 AI 入口文件", "scripts/build_docs.py"),
]


def main():
    for i, (label, script) in enumerate(STEPS, 1):
        print(f"\n[{i}/{len(STEPS)}] {label}  ({script})")
        r = subprocess.run([PY, script], cwd=ROOT)
        if r.returncode != 0:
            print(f"\nFAILED at step {i}: {script} (exit {r.returncode})")
            return r.returncode
    print("\n=== 刷新完成 ===")
    print("人工实测结论请编辑 data/manual-overrides.json；")
    print("起步包与场景调整请编辑 data/recommendations.json；改完重跑本脚本即可。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
