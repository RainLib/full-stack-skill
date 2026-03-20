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

## 与用户交流（必须）

本阶段在**主对话中执行**，设计中的关键假设或可选方案应与用户确认后再定稿。

### 交互原则

- **存在多种合理方案时，以结构化选项呈现**，让用户选择后再写入。
- 一次不超过 2～3 个问题，等用户回复后再继续。
- 定稿前向用户呈现设计摘要，确认后再产出完整文档。

### 结构化确认点

在设计过程中，以下决策点须以选项形式向用户确认：

**C1 — 分层粒度**（若有多种合理方式）
- A. 标准三层（Controller / Service / Repository）
- B. 增加 DTO 层（严格出入参隔离）
- C. DDD 领域驱动（聚合根 / 领域服务 / 仓储）
- D. 其他（请说明）

**C2 — 前端路由/页面方案**（若存在多种合理划分）
- A. 按功能模块划分路由（/orders, /users, /stats）
- B. 按角色划分入口（/admin/*, /user/*）
- C. 其他

**C3 — 状态管理策略**（若前端涉及复杂状态）
- A. 服务端状态为主（每次请求刷新，少量本地缓存）
- B. 客户端 store 缓存为主（减少请求，手动同步）
- C. 混合（关键数据实时请求，列表等可缓存）

**C4 — 定稿确认**
- 完成设计草案后，向用户呈现摘要（模块数、接口数、核心流程列表），让用户确认或补充后再产出完整文档。

## 输入

读取当前迭代目录下的：
- 需求文档（`requirements-{id}.md`）
- 技术选型文档（`technology-selection-{id}.md`）
- 技术评审文档（`technical-review-{id}.md`）—— 特别关注 API 契约和数据模型。

## 执行要点

1. **模块分层**：按选型划分（如前端页面/组件、后端控制器/服务/仓储、数据模型）。
2. **API 设计**：基于评审中确定的 API 契约，细化请求/响应 schema。
3. **数据模型**：基于评审中确定的实体关系，写出完整字段定义，并画 **Mermaid ER 图**。
4. **架构总览**：用 **Mermaid 架构图** 展示前端/后端/数据库/外部服务的整体关系。
5. **关键流程**：1～3 个核心业务流程，每个流程须提供 **Mermaid 流程图**（决策分支）和 **Mermaid 时序图**（模块间调用时序）。
6. **错误处理**：全局错误码体系、前端错误展示策略、后端异常层次。
7. **工程目录**：给出推荐目录结构，与选型和分层一致。

## 辅助资料

- 完整示例输出：[examples/sample-output.md](examples/sample-output.md) — 展示一份合格设计文档的完整结构与深度
- 设计参考：[reference.md](reference.md) — 分层架构参考、状态机设计、API 模式、前端封装模式、数据库设计注意事项

## 产出

- 使用 [templates/design-template.md](templates/design-template.md) 产出设计文档，供「任务拆分」「单元测试」「代码开发」使用。

## 文档与状态

- 产出写入 `docs/{current_iteration_id}/program-design-{program_design_id}.md`。
- 开始前：调用 `history-manager` skill 的 `get-phase program_design` 和 `check-file` 确认是否已完成。
- 完成后：调用 `history-manager` skill 的 `set-phase program_design {program_design_id}` 记录并推进状态。
