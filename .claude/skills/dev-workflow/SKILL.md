---
name: dev-workflow
description: 全栈开发工作流编排器，按 8 阶段顺序执行：需求分析 → 技术选型 → 技术评审 → 程序设计 → 任务拆分 → 单元测试 → 代码开发 → 自我验证。
argument-hint: [iteration-id]
disable-model-invocation: true
allowed-tools: Read, Write, Grep, Glob
---

# 全栈开发工作流

用户通过 `/dev-workflow` 启动。可选传入 iteration-id 恢复已有迭代。

## 启动流程

1. 调用 `history-manager` skill 执行 `init`（确保 `docs/history.json` 存在）。
2. 若传入 `$ARGUMENTS` 且为有效 iteration id，恢复该迭代；否则调用 `history-manager` 执行 `new-iter` 创建新迭代。
3. 调用 `history-manager` 执行 `status` 读取当前迭代的 `state`，从该阶段继续执行。

## 阶段执行顺序

| 顺序 | 阶段 | Skill | 执行方式 | 说明 |
|:----:|------|-------|----------|------|
| 1 | 需求分析 | requirements-analysis | inline | 与用户对话，梳理功能点 |
| 2 | 技术选型 | technology-selection | inline | 询问全栈/前端/后端，选定技术栈 |
| 3 | 技术评审 | technical-review | fork/Explore | 评审架构可行性、API 契约、风险项 |
| 4 | 程序设计 | program-design | inline | 设计模块分层、流程、工程目录 |
| 5 | 任务拆分 | task-breakdown | fork/Plan | 将设计拆为可管理的开发单元 |
| 6 | 单元测试 | unit-testing | fork | 按任务单元设计测试用例 |
| 7 | 代码开发 | code-development | inline | 按测试驱动实现代码 |
| 8 | 自我验证 | self-verification | fork/Explore | 运行测试、集成验证、质量自检 |

## 执行规则

- **Inline 阶段必须与用户对话**：需求分析、技术选型、程序设计、代码开发（阶段 1、2、4、7）均在主对话中执行，需**等待用户输入或确认后再产出/推进**，不得跳过用户直接生成结果。技术选型必须先问「全栈/仅前端/仅后端」并得到明确答复。
- **状态恢复**：每个阶段开始前，调用 `history-manager` 的 `get-phase` 和 `check-file` 检查该阶段是否已完成。若已完成则跳过，直接进入下一阶段。
- **状态写入**：每个阶段完成后，调用 `history-manager` 的 `set-phase <phase> <phase_id>` 更新 history。
- **阶段 id 生成**：使用 `{阶段缩写}-001` 格式（如 `req-001`、`ts-001`）。同一迭代内递增。
- **自我验证失败**：若 self-verification 报告有未通过项，回退到 code-development 修复后重新验证。
- **产出位置**：所有阶段文档写入 `docs/{current_iteration_id}/`。
