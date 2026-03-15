# Full-Stack Skills

**[中文文档](README_CN.md)**

An open-source [Claude Code Skills](https://code.claude.com/docs/en/skills) plugin that orchestrates the entire full-stack development lifecycle — from product prototype to self-verification — in a structured, stateful 8-phase workflow.

## What It Does

Run `/dev-workflow` in Claude Code to launch a guided workflow that takes you from a raw product idea to verified, tested code:

```
/dev-workflow → Requirements → Tech Selection → Tech Review → Program Design
             → Task Breakdown → Unit Testing → Code Development → Self-Verification → Done
```

Each phase produces a versioned document in `docs/`, with full state tracking so you can pause, resume, and never lose progress.

## Features

- **8-phase orchestrated workflow** covering the full software development lifecycle
- **Stateful iteration management** via `docs/history.json` — resume where you left off
- **Subagent isolation** — review, planning, and verification phases run in forked subagents for clean separation
- **Rich templates** for every phase with structured output formats
- **Cross-platform** — Python 3 utility script works on macOS and Windows
- **Built on the official Claude Code skills spec** — proper frontmatter, `context: fork`, `disable-model-invocation`, etc.

## Workflow Phases

| # | Phase | Skill | Execution | Output |
|:-:|-------|-------|-----------|--------|
| 1 | Requirements Analysis | `requirements-analysis` | inline | Structured requirements doc with user stories and acceptance criteria |
| 2 | Technology Selection | `technology-selection` | inline | Tech stack selection (fullstack / frontend-only / backend-only) |
| 3 | Technical Review | `technical-review` | fork / Explore | Architecture review, API contracts, data models, risk assessment |
| 4 | Program Design | `program-design` | inline | Module design, data flow, API specs, project structure |
| 5 | Task Breakdown | `task-breakdown` | fork / Plan | Ordered dev tasks with priority, dependencies, and batch grouping |
| 6 | Unit Testing | `unit-testing` | fork | Test cases per task with mock strategies and coverage targets |
| 7 | Code Development | `code-development` | inline | Test-driven implementation following task order |
| 8 | Self-Verification | `self-verification` | fork / Explore | Full test run, integration check, code quality report |

## Installation

### As a project skill (recommended)

Clone into your project's `.claude/skills/` directory:

```bash
git clone <repo-url> .claude/skills/full-stack-skills
```

Or copy the `.claude/skills/` contents from this repo into your project.

### As a personal skill

Clone to your personal skills folder so it's available across all projects:

```bash
git clone <repo-url> ~/.claude/skills/full-stack-skills
```

## Usage

### Start a new workflow

```
/dev-workflow
```

This creates a new iteration (e.g. `iter-001`), then walks you through each phase in order.

### Resume an existing iteration

```
/dev-workflow iter-001
```

Picks up from wherever you left off. Already-completed phases are skipped automatically.

### Makefile commands

All project management operations are available via `make`:

```bash
make help             # Show all available commands
make init             # Initialize docs/history.json
make new-iter         # Create a new iteration
make status           # Show current iteration progress
make set-phase PHASE=requirements PHASE_ID=req-001
make get-phase PHASE=requirements
make check-file PHASE=requirements PHASE_ID=req-001
make list-iters       # List all iteration directories
make validate-schema  # Validate history.json against schema
make tree             # Show project structure (skills + docs)
make clean-iter ITER=iter-001  # Remove a specific iteration
```

### Check current status

The workflow reads `docs/history.json` on startup and shows which phases are done and which is next. You can also run `make status` directly.

## Project Structure

```
Makefile                         # Project management commands (make help)
.claude/skills/
├── dev-workflow/                 # Orchestrator entry point (/dev-workflow)
│   └── SKILL.md
├── requirements-analysis/        # Phase 1: Requirements
│   ├── SKILL.md
│   └── templates/
├── technology-selection/         # Phase 2: Tech stack
│   ├── SKILL.md
│   └── templates/
├── technical-review/             # Phase 3: Architecture review
│   ├── SKILL.md
│   └── templates/
├── program-design/               # Phase 4: Program design
│   ├── SKILL.md
│   └── templates/
├── task-breakdown/               # Phase 5: Task decomposition
│   ├── SKILL.md
│   └── templates/
├── unit-testing/                 # Phase 6: Test design
│   ├── SKILL.md
│   └── templates/
├── code-development/             # Phase 7: Implementation
│   ├── SKILL.md
│   └── templates/
├── self-verification/            # Phase 8: Verification
│   ├── SKILL.md
│   └── templates/
├── history-manager/             # State management skill (invoked by other skills)
│   ├── SKILL.md
│   └── scripts/
│       └── history_manager.py   # Cross-platform Python 3 utility
├── CLAUDE.md                     # Agent entry point
├── SKILL_META.md                 # Frontmatter spec reference
├── docs-convention.md            # Document & state management conventions
├── README.md                     # Skills directory overview
└── task.md                       # Workflow design notes

docs/
├── history.json                  # Iteration & phase state tracking
├── history.schema.json           # JSON Schema for validation
├── README.md                     # Docs directory guide
└── iter-001/                     # Per-iteration output (created at runtime)
    ├── requirements-req-001.md
    ├── technology-selection-ts-001.md
    └── ...
```

## State Management

All phase outputs go to `docs/{iteration-id}/` with unique phase IDs to prevent duplicate generation:

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

State is managed by the **`history-manager`** skill (`user-invocable: false`), which all phase skills and the orchestrator invoke to read/write history. It wraps a cross-platform Python 3 script that supports `init`, `new-iter`, `set-phase`, `get-phase`, `check-file`, and `status` commands.

## Requirements

- [Claude Code](https://code.claude.com/) with skills support
- Python 3.8+ (for the `history_manager.py` utility)
- GNU Make (built-in on macOS/Linux; on Windows use Git Bash, WSL, or `choco install make`)

## Contributing

Contributions are welcome. Please ensure:

1. New skills follow the frontmatter spec in `SKILL_META.md`
2. Templates go in the skill's `templates/` directory
3. SKILL.md files stay under 500 lines (move detail to supporting files)
4. Scripts work on both macOS and Windows

## License

MIT
