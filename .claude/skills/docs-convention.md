# 文档与状态管理约定

工作流产出写入 `docs/`，状态与历史由 `docs/history.json` 管理。

## 1. history.json 结构

- **current_iteration_id**：当前进行中的迭代 id（如 `iter-001`）；新建迭代时生成并写入。
- **iterations**：数组，每项为一次迭代：
  - **id**：迭代 id，与目录 `docs/{id}/` 对应。
  - **state**：当前处于的阶段：`requirements` | `technology_selection` | `program_design` | `unit_testing` | `code_development` | `done`。
  - **phases**：各阶段对应 id（用于文件名、避免重复生成）：
    - `requirements_id`
    - `technology_selection_id`
    - `program_design_id`
    - `unit_testing_id`
    - `code_development_id`
  - **created_at**、**updated_at**：ISO 8601 时间（如 `2026-03-13T12:00:00Z`）。
- **created_at** / **last_updated**：文件级别的创建与最后更新时间。

## 2. 迭代与阶段 id 生成

- **迭代 id**：`iter-` + 三位数字，如 `iter-001`。新迭代取当前最大编号 +1。
- **阶段 id**：`{阶段缩写}-` + 三位数字，在同一迭代内唯一，例如：
  - 需求分析：`req-001`
  - 技术选型：`ts-001`
  - 程序设计：`pd-001`
  - 单元测试：`ut-001`
  - 代码开发：`cd-001`

## 3. 避免重复生成

- 执行某阶段前，先读 `history.json`，取 `current_iteration_id` 及该迭代的 `phases.xxx_id`。
- 若该阶段已有 `xxx_id` 且 `docs/{iteration_id}/{阶段名}-{xxx_id}.md` 已存在，则**不重新生成**该阶段产出，直接使用已有文件作为输入进入下一阶段；除非用户明确要求「重新做某阶段」。
- 若该阶段尚未有 id，则生成新 phase id、写入产出文件、在 `history.json` 中写入该 `phases.xxx_id`，并将 `state` 更新为下一阶段，`updated_at` 更新为当前时间。

## 4. 产出写入位置

- 根目录：项目下的 `docs/`（与 `.claude` 平级）。
- 当前迭代目录：`docs/{current_iteration_id}/`；若不存在则先创建。
- 文件名：`{阶段名}-{phase_id}.md`，例如 `requirements-req-001.md`。

## 5. 每次更新 history 时

- 更新该迭代的 `updated_at`。
- 更新全局 `last_updated`。
- 若新建迭代，则：生成新迭代 id（如 `iter-001`）、创建目录 `docs/iter-001/`、在 `iterations` 中 push `{ id, state: "requirements", phases: {}, created_at, updated_at }`、设置 `current_iteration_id`；若 history 初次使用，则设置全局 `created_at`、`last_updated`。
