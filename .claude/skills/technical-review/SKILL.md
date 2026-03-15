---
name: technical-review
description: 评审需求与技术选型的架构可行性，定义 API 契约、数据模型、识别风险项。在技术选型之后、程序设计之前使用。
user-invocable: false
allowed-tools: Read, Grep, Glob
context: fork
agent: Explore
---

# 技术评审

## 何时使用

- 全栈工作流第 3 阶段：技术选型完成后、程序设计之前。
- 用户要求评审架构、API 契约或风险分析时。

## 输入

读取当前迭代目录下的：
- 需求文档（`requirements-{id}.md`）
- 技术选型文档（`technology-selection-{id}.md`）

## 执行要点

1. **架构可行性**：技术选型能否满足需求中的功能与非功能要求（性能、安全、部署）。
2. **API 契约定义**：列出核心接口的路径、方法、请求/响应 schema、状态码约定。
3. **数据模型**：核心实体、字段、关系、索引建议。
4. **风险清单**：技术风险、依赖风险、未确认项，每条附建议对策。
5. **评审结论**：通过 / 有条件通过（列出必须修正项） / 不通过（需重做选型）。

## 产出

- 使用 [templates/review-template.md](templates/review-template.md) 产出评审文档，供「程序设计」使用。

## 文档与状态

- 产出写入 `docs/{current_iteration_id}/technical-review-{technical_review_id}.md`。
- 开始前：调用 `history-manager` skill 的 `get-phase technical_review` 和 `check-file` 确认是否已完成。
- 完成后：调用 `history-manager` skill 的 `set-phase technical_review {technical_review_id}` 记录并推进状态。
