---
name: task-breakdown
description: 将程序设计拆分为可管理的开发任务单元，定义优先级、依赖和开发顺序。在程序设计之后、单元测试之前使用。
user-invocable: false
allowed-tools: Read, Write, Grep, Glob
context: fork
agent: Plan
---

# 任务拆分

## 何时使用

- 全栈工作流第 5 阶段：程序设计完成后、单元测试之前。
- 用户要求将设计拆为可管理的开发节奏时。

## 输入

读取当前迭代目录下的：
- 需求文档（`requirements-{id}.md`）
- 技术评审文档（`technical-review-{id}.md`）
- 程序设计文档（`program-design-{id}.md`）

## 执行要点

1. **拆分粒度**：每个任务应在 1～4 小时内可完成，包含明确的输入和产出。
2. **依赖排序**：标注任务间依赖关系，生成执行顺序（可并行的标注为并行）。
3. **优先级**：P0（核心流程）、P1（重要功能）、P2（增强/优化）。
4. **验收标准**：每个任务附简要验收条件（与后续单元测试对应）。
5. **分批建议**：按开发批次（Sprint/Batch）组织，建议每批 3～7 个任务。

## 产出

- 使用 [templates/task-breakdown-template.md](templates/task-breakdown-template.md) 产出任务拆分文档，供「单元测试」和「代码开发」按顺序执行。

## 文档与状态

- 产出写入 `docs/{current_iteration_id}/task-breakdown-{task_breakdown_id}.md`。
- 开始前：调用 `history-manager` skill 的 `get-phase task_breakdown` 和 `check-file` 确认是否已完成。
- 完成后：调用 `history-manager` skill 的 `set-phase task_breakdown {task_breakdown_id}` 记录并推进状态。
