# Full-Stack Skills

**[English](README.md)**

一个开源的 [Claude Code Skills](https://code.claude.com/docs/en/skills) 插件，将完整的全栈开发生命周期——从产品原型到自我验证——编排为结构化、有状态的 8 阶段工作流。

## 它做什么

在 Claude Code 中运行 `/dev-workflow`，启动一个引导式工作流，从产品想法到经过验证的代码：

```
/dev-workflow → 需求分析 → 技术选型 → 技术评审 → 程序设计
             → 任务拆分 → 单元测试 → 代码开发 → 自我验证 → 完成
```

每个阶段在 `docs/` 中产出带版本的文档，完整的状态追踪让你可以随时暂停、恢复，永不丢失进度。

## 特性

- **8 阶段编排工作流**，覆盖完整的软件开发生命周期
- **有状态的迭代管理**，通过 `docs/history.json` 实现——随时从中断处继续
- **子 Agent 隔离**——评审、规划和验证阶段在 fork 子 agent 中运行，保持干净的上下文隔离
- **丰富的模板**，每个阶段都有结构化的输出格式
- **跨平台**——Python 3 工具脚本在 macOS 和 Windows 上均可运行
- **基于官方 Claude Code Skills 规范**——正确的 frontmatter、`context: fork`、`disable-model-invocation` 等

## 工作流阶段

| 序号 | 阶段 | Skill | 执行方式 | 产出 |
|:----:|------|-------|----------|------|
| 1 | 需求分析 | `requirements-analysis` | inline | 结构化需求文档（含用户故事和验收标准） |
| 2 | 技术选型 | `technology-selection` | inline | 技术栈选型清单（全栈/仅前端/仅后端） |
| 3 | 技术评审 | `technical-review` | fork / Explore | 架构评审、API 契约、数据模型、风险评估 |
| 4 | 程序设计 | `program-design` | inline | 模块设计、数据流、API 规格、工程目录 |
| 5 | 任务拆分 | `task-breakdown` | fork / Plan | 有序开发任务（含优先级、依赖、批次分组） |
| 6 | 单元测试 | `unit-testing` | fork | 按任务的测试用例（含 Mock 策略和覆盖率目标） |
| 7 | 代码开发 | `code-development` | inline | 按任务顺序的测试驱动实现 |
| 8 | 自我验证 | `self-verification` | fork / Explore | 全量测试、集成验证、代码质量报告 |

## 安装

### 快速安装（推荐）

```bash
npx skills add RainLib/full-stack-skill
```

### 作为项目级 Skill

将本仓库克隆到项目的 `.claude/skills/` 目录下：

```bash
git clone <repo-url> .claude/skills/full-stack-skills
```

或将本仓库的 `.claude/skills/` 内容复制到你的项目中。

### 作为个人 Skill

克隆到个人 skills 目录，所有项目均可使用：

```bash
git clone <repo-url> ~/.claude/skills/full-stack-skills
```

## 使用方式

### 启动新工作流

```
/dev-workflow
```

创建一个新迭代（如 `iter-001`），然后按顺序引导你完成每个阶段。

### 恢复已有迭代

```
/dev-workflow iter-001
```

从中断处继续，已完成的阶段会自动跳过。

### Makefile 命令

所有工程管理操作均可通过 `make` 执行：

```bash
make help             # 查看所有可用命令
make init             # 初始化 docs/history.json
make new-iter         # 创建新迭代
make status           # 查看当前迭代进度
make set-phase PHASE=requirements PHASE_ID=req-001
make get-phase PHASE=requirements
make check-file PHASE=requirements PHASE_ID=req-001
make list-iters       # 列出所有迭代目录
make validate-schema  # 校验 history.json
make tree             # 显示项目结构（skills + docs）
make clean-iter ITER=iter-001  # 删除指定迭代
```

### 查看当前状态

工作流启动时会读取 `docs/history.json`，显示哪些阶段已完成、下一步是什么。也可以直接运行 `make status`。

## 项目结构

```
Makefile                         # 工程管理命令（make help）
.claude/skills/
├── dev-workflow/                 # 编排入口（/dev-workflow）
│   └── SKILL.md
├── requirements-analysis/        # 阶段 1：需求分析
│   ├── SKILL.md
│   └── templates/
├── technology-selection/         # 阶段 2：技术选型
│   ├── SKILL.md
│   └── templates/
├── technical-review/             # 阶段 3：技术评审
│   ├── SKILL.md
│   └── templates/
├── program-design/               # 阶段 4：程序设计
│   ├── SKILL.md
│   └── templates/
├── task-breakdown/               # 阶段 5：任务拆分
│   ├── SKILL.md
│   └── templates/
├── unit-testing/                 # 阶段 6：单元测试设计
│   ├── SKILL.md
│   └── templates/
├── code-development/             # 阶段 7：代码开发
│   ├── SKILL.md
│   └── templates/
├── self-verification/            # 阶段 8：自我验证
│   ├── SKILL.md
│   └── templates/
├── history-manager/             # 状态管理 skill（被其他 skill 调用）
│   ├── SKILL.md
│   └── scripts/
│       └── history_manager.py   # 跨平台 Python 3 工具
├── CLAUDE.md                     # Agent 入口
├── SKILL_META.md                 # Frontmatter 规范参考
├── docs-convention.md            # 文档与状态管理约定
├── README.md                     # Skills 目录总览
└── task.md                       # 工作流设计说明

docs/
├── history.json                  # 迭代与阶段状态追踪
├── history.schema.json           # JSON Schema（用于校验）
├── README.md                     # 文档目录说明
└── iter-001/                     # 按迭代组织的产出（运行时创建）
    ├── requirements-req-001.md
    ├── technology-selection-ts-001.md
    └── ...
```

## 状态管理

所有阶段产出写入 `docs/{iteration-id}/`，使用唯一的阶段 ID 防止重复生成：

```json
{
  "current_iteration_id": "iter-001",
  "iterations": [{
    "id": "iter-001",
    "state": "program_design",
    "phases": {
      "requirements_id": "req-001",
      "technology_selection_id": "ts-001",
      "technical_review_id": "tr-001",
      "program_design_id": null,
      "task_breakdown_id": null,
      "unit_testing_id": null,
      "code_development_id": null,
      "self_verification_id": null
    }
  }]
}
```

状态由 **`history-manager`** skill（`user-invocable: false`）管理，所有阶段 skill 和编排器通过调用它来读写 history。它封装了一个跨平台 Python 3 脚本，支持 `init`、`new-iter`、`set-phase`、`get-phase`、`check-file` 和 `status` 命令。

## 环境要求

- [Claude Code](https://code.claude.com/)（支持 skills 功能）
- Python 3.8+（用于 `history_manager.py` 工具）
- GNU Make（macOS/Linux 内置；Windows 可通过 Git Bash、WSL 或 `choco install make` 安装）

## 参与贡献

欢迎贡献。请确保：

1. 新 skill 遵循 `SKILL_META.md` 中的 frontmatter 规范
2. 模板放在 skill 目录的 `templates/` 子目录中
3. SKILL.md 文件保持在 500 行以内（将细节移到辅助文件中）
4. 脚本在 macOS 和 Windows 上均可运行

## 许可证

MIT
