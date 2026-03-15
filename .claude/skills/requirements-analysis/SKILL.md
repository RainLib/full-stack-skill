---
name: requirements-analysis
description: 从产品原型或用户描述中梳理功能点与细节要求，产出结构化需求文档。全栈工作流第 1 阶段。
user-invocable: false
allowed-tools: Read, Write
---

# 需求分析

## 何时使用

- 用户描述了产品想法、提供了原型文档或需求草稿，需要整理成可执行需求时。
- 全栈工作流第 1 阶段，由编排器调用。

## 执行要点

1. **原型/文档识别**：若用户提供了产品原型截图、PRD 文档或草稿，先提取其中的功能描述与页面流程。
2. **功能点梳理**：按「功能模块 → 功能点」提取列表，不遗漏、不臆造。每个功能点含简要描述与输入输出。
3. **用户故事**：核心功能点转写为用户故事格式（As a ... I want ... So that ...）。
4. **验收标准**：每个功能点附 1～3 条验收标准（Given/When/Then 或要点式）。
5. **细节追问**：对模糊点（角色、边界、数据来源、异常情况）用 1～3 轮简短提问补全。
6. **输出格式**：使用 [templates/requirements-template.md](templates/requirements-template.md) 填写并产出需求文档。

## 细节引导（可对用户提问）

- 用户角色与权限？（未登录/登录/管理员/多角色）
- 核心业务流程的步骤与异常分支？
- 数据来源与持久化要求？（仅前端 / 需要后端与数据库）
- 非功能：性能指标、安全要求、部署环境、浏览器/设备兼容？
- 是否有现成原型、设计稿或参考系统？

## 产出

- 一份按模板填写的需求文档，供「技术选型」与后续阶段使用。

## 文档与状态

- 产出写入 `docs/{current_iteration_id}/requirements-{requirements_id}.md`。
- 开始前：调用 `history-manager` skill 的 `get-phase requirements` 和 `check-file` 确认是否已完成。
- 完成后：调用 `history-manager` skill 的 `set-phase requirements {requirements_id}` 记录并推进状态。
