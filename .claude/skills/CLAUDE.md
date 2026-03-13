# 全栈工作流入口

执行全栈开发流程时，按以下顺序使用本目录下的 skills；每步产出作为下一步输入。

1. **需求分析**：使用 `requirements-analysis`。产出功能点与细节要求。
2. **技术选型**：使用 `technology-selection`。先询问用户：全栈 / 仅前端 / 仅后端，再进入对应技术选择与模板。
3. **程序设计**：使用 `program-design`。根据技术选型结果，设计程序结构、流程与工程目录。
4. **单元测试**：使用 `unit-testing`。根据程序设计产出测试用例与预期结果。
5. **代码开发**：使用 `code-development`。根据单元测试编写并通过测试的代码。

**状态与文档**：每步产出写入 **`docs/{current_iteration_id}/`**，阶段文件名带 phase id；**`docs/history.json`** 记录当前迭代、各阶段 id 与状态（含创建/更新时间），避免重复生成。无当前迭代时先新建迭代再执行。约定见 [docs-convention.md](docs-convention.md)。

各 skill 的详细说明见各自目录下的 `SKILL.md`；模板与引导在各自 `templates/` 中。
