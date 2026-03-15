---
name: program-design
description: 根据需求、技术选型与技术评审设计程序结构、流程与工程目录。全栈工作流第 4 阶段。
user-invocable: false
allowed-tools: Read, Write, Grep, Glob
---

# 程序设计

## 何时使用

- 全栈工作流第 4 阶段：技术评审通过后、任务拆分之前。
- 用户要求做架构设计、模块划分或工程结构时。

## 输入

读取当前迭代目录下的：
- 需求文档（`requirements-{id}.md`）
- 技术选型文档（`technology-selection-{id}.md`）
- 技术评审文档（`technical-review-{id}.md`）—— 特别关注 API 契约和数据模型。

## 执行要点

1. **模块分层**：按选型划分（如前端页面/组件、后端控制器/服务/仓储、数据模型）。
2. **API 设计**：基于评审中确定的 API 契约，细化请求/响应 schema。
3. **数据模型**：基于评审中确定的实体关系，写出完整字段定义。
4. **关键流程**：1～3 个核心业务流程的调用时序（涉及前后端模块）。
5. **错误处理**：全局错误码体系、前端错误展示策略、后端异常层次。
6. **工程目录**：给出推荐目录结构，与选型和分层一致。

## 产出

- 使用 [templates/design-template.md](templates/design-template.md) 产出设计文档，供「任务拆分」「单元测试」「代码开发」使用。

## 文档与状态

- 产出写入 `docs/{current_iteration_id}/program-design-{program_design_id}.md`。
- 开始前：调用 `history-manager` skill 的 `get-phase program_design` 和 `check-file` 确认是否已完成。
- 完成后：调用 `history-manager` skill 的 `set-phase program_design {program_design_id}` 记录并推进状态。
