---
name: code-development
description: 根据单元测试用例、任务拆分与程序设计实现代码，并通过测试验证。全栈工作流第 7 阶段。
user-invocable: false
allowed-tools: Read, Write, Grep, Glob, Bash(*)
---

# 代码开发

## 何时使用

- 全栈工作流第 7 阶段：单元测试设计完成后。
- 用户要求按测试或设计文档实现功能时。

## 与用户交流（必须）

本阶段在**主对话中执行**，开发过程中涉及范围或方案取舍时需先与用户确认。

- 若与设计文档冲突、需调整实现方式或暂缓某任务，**先说明原因并征求用户同意**再继续。
- 每完成一个 Batch 或关键功能，可简要汇报并询问是否继续下一批。

## 输入

读取当前迭代目录下的：
- 程序设计文档（`program-design-{id}.md`）—— 结构、流程、目录
- 任务拆分文档（`task-breakdown-{id}.md`）—— 开发顺序与批次
- 单元测试用例文档（`unit-testing-{id}.md`）—— 用例与预期

## 执行要点

1. **按任务顺序**：遵循任务拆分的批次和依赖顺序，先实现被依赖层。
2. **测试驱动**：每完成一个任务，运行对应测试用例，通过后再继续下一个任务。
3. **风格一致**：遵循项目选型约定（如 Java 21 语法、ESLint 规则、命名规范）。
4. **提交节奏**：每完成一个 Batch 后建议提交一次，附简要说明。
5. **问题记录**：开发中遇到与设计文档不一致或需要调整的，记录到产出文档中。

## 自检清单

见 [templates/development-checklist.md](templates/development-checklist.md)。

## 产出

- 可运行的代码与通过用例的测试。
- 在 `docs/{current_iteration_id}/code-development-{code_development_id}.md` 记录实现摘要、偏差说明、自检结果。

## 文档与状态

- 产出写入 `docs/{current_iteration_id}/code-development-{code_development_id}.md`。
- 开始前：调用 `history-manager` skill 的 `get-phase code_development` 和 `check-file` 确认是否已完成。
- 完成后：调用 `history-manager` skill 的 `set-phase code_development {code_development_id}` 记录并推进状态。
