---
name: history-manager
description: Manage workflow iteration state and history. Use when any phase skill needs to check progress, create iterations, update phase status, or verify document existence. Invoked by dev-workflow and all phase skills.
user-invocable: false
allowed-tools: Read, Write, Bash(python *)
---

# History Manager

Provides iteration and phase state management for the full-stack workflow. Other skills invoke this skill to read/write `docs/history.json` instead of managing state directly.

## Available Commands

All commands use the bundled cross-platform Python 3 script (macOS + Windows):

```bash
python ${CLAUDE_SKILL_DIR}/scripts/history_manager.py <command> [args]
```

### init

Initialize `docs/history.json` if it does not exist.

```bash
python ${CLAUDE_SKILL_DIR}/scripts/history_manager.py init
```

### status

Print the current iteration state, showing which phases are completed and which is next.

```bash
python ${CLAUDE_SKILL_DIR}/scripts/history_manager.py status
```

### new-iter

Create a new iteration (e.g. `iter-001`), create its `docs/iter-xxx/` directory, and set it as current.

```bash
python ${CLAUDE_SKILL_DIR}/scripts/history_manager.py new-iter
```

### set-phase `<phase>` `<phase_id>`

Record a phase as completed: set its id in the current iteration and advance the state to the next phase.

```bash
python ${CLAUDE_SKILL_DIR}/scripts/history_manager.py set-phase requirements req-001
```

Valid phase names: `requirements`, `technology_selection`, `technical_review`, `program_design`, `task_breakdown`, `unit_testing`, `code_development`, `self_verification`.

### get-phase `<phase>`

Get the current phase id for a given phase (returns `null` if not yet started).

```bash
python ${CLAUDE_SKILL_DIR}/scripts/history_manager.py get-phase requirements
```

### check-file `<phase>` `<phase_id>`

Check whether the document file for a given phase exists in the current iteration directory.

```bash
python ${CLAUDE_SKILL_DIR}/scripts/history_manager.py check-file requirements req-001
```

Returns `exists:<path>` or `missing:<path>`.

## How Other Skills Should Use This

1. **Before starting a phase**: Invoke `history-manager` to run `get-phase <phase_name>` and `check-file` to determine if the phase was already completed. Skip if both the id exists and the file exists.
2. **After completing a phase**: Invoke `history-manager` to run `set-phase <phase_name> <phase_id>` to record completion and advance the state machine.
3. **dev-workflow orchestrator**: Invokes `history-manager` for `init`, `new-iter`, and `status` at startup, then delegates phase state updates to each phase skill (which in turn invokes `history-manager`).

## Current Status

!`python ${CLAUDE_SKILL_DIR}/scripts/history_manager.py status`
