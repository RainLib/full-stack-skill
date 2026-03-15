#!/usr/bin/env python3
"""
Cross-platform (macOS / Windows) utility for managing docs/history.json.

Usage:
    python history_manager.py init                              # create initial history.json
    python history_manager.py status                            # print current iteration status
    python history_manager.py new-iter                          # create a new iteration
    python history_manager.py set-phase <phase> <phase_id>      # set phase id + advance state
    python history_manager.py get-phase <phase>                 # get current phase id (or "null")
    python history_manager.py check-file <phase> <phase_id>     # check if phase doc file exists

Phases (in order):
    requirements, technology_selection, technical_review,
    program_design, task_breakdown, unit_testing,
    code_development, self_verification
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

PHASES_ORDER = [
    "requirements",
    "technology_selection",
    "technical_review",
    "program_design",
    "task_breakdown",
    "unit_testing",
    "code_development",
    "self_verification",
]

PHASE_ID_FIELD = {
    "requirements": "requirements_id",
    "technology_selection": "technology_selection_id",
    "technical_review": "technical_review_id",
    "program_design": "program_design_id",
    "task_breakdown": "task_breakdown_id",
    "unit_testing": "unit_testing_id",
    "code_development": "code_development_id",
    "self_verification": "self_verification_id",
}

PHASE_FILE_PREFIX = {
    "requirements": "requirements",
    "technology_selection": "technology-selection",
    "technical_review": "technical-review",
    "program_design": "program-design",
    "task_breakdown": "task-breakdown",
    "unit_testing": "unit-testing",
    "code_development": "code-development",
    "self_verification": "self-verification",
}

PHASE_ID_PREFIX = {
    "requirements": "req",
    "technology_selection": "ts",
    "technical_review": "tr",
    "program_design": "pd",
    "task_breakdown": "tb",
    "unit_testing": "ut",
    "code_development": "cd",
    "self_verification": "sv",
}


def find_project_root() -> Path:
    """Walk up from this script to find the project root (parent of docs/)."""
    current = Path(__file__).resolve().parent
    for _ in range(10):
        if (current / "docs").is_dir() or (current / ".claude").is_dir():
            return current
        current = current.parent
    return Path.cwd()


def docs_dir() -> Path:
    return find_project_root() / "docs"


def history_path() -> Path:
    return docs_dir() / "history.json"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_history() -> dict:
    hp = history_path()
    if not hp.exists():
        return None
    with open(hp, "r", encoding="utf-8") as f:
        return json.load(f)


def save_history(data: dict) -> None:
    data["last_updated"] = now_iso()
    hp = history_path()
    hp.parent.mkdir(parents=True, exist_ok=True)
    with open(hp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def empty_history() -> dict:
    ts = now_iso()
    return {
        "schema_version": "1.0",
        "current_iteration_id": None,
        "iterations": [],
        "created_at": ts,
        "last_updated": ts,
    }


def cmd_init():
    hp = history_path()
    if hp.exists():
        print(f"history.json already exists at {hp}")
        return
    save_history(empty_history())
    print(f"Initialized {hp}")


def next_iter_id(history: dict) -> str:
    max_num = 0
    for it in history.get("iterations", []):
        parts = it["id"].split("-")
        if len(parts) == 2 and parts[1].isdigit():
            max_num = max(max_num, int(parts[1]))
    return f"iter-{max_num + 1:03d}"


def cmd_new_iter():
    history = load_history()
    if history is None:
        history = empty_history()

    iter_id = next_iter_id(history)
    ts = now_iso()
    iteration = {
        "id": iter_id,
        "state": "requirements",
        "phases": {v: None for v in PHASE_ID_FIELD.values()},
        "created_at": ts,
        "updated_at": ts,
    }
    history["iterations"].append(iteration)
    history["current_iteration_id"] = iter_id

    iter_dir = docs_dir() / iter_id
    iter_dir.mkdir(parents=True, exist_ok=True)

    save_history(history)
    print(f"Created iteration {iter_id}")
    print(f"Directory: {iter_dir}")


def get_current_iteration(history: dict) -> dict | None:
    cid = history.get("current_iteration_id")
    if not cid:
        return None
    for it in history["iterations"]:
        if it["id"] == cid:
            return it
    return None


def next_state(current_phase: str) -> str:
    idx = PHASES_ORDER.index(current_phase)
    if idx + 1 < len(PHASES_ORDER):
        return PHASES_ORDER[idx + 1]
    return "done"


def cmd_set_phase(phase: str, phase_id: str):
    if phase not in PHASE_ID_FIELD:
        print(f"Unknown phase: {phase}", file=sys.stderr)
        print(f"Valid phases: {', '.join(PHASES_ORDER)}", file=sys.stderr)
        sys.exit(1)

    history = load_history()
    if history is None:
        print("history.json not found. Run 'init' first.", file=sys.stderr)
        sys.exit(1)

    iteration = get_current_iteration(history)
    if iteration is None:
        print("No current iteration. Run 'new-iter' first.", file=sys.stderr)
        sys.exit(1)

    field = PHASE_ID_FIELD[phase]
    iteration["phases"][field] = phase_id
    iteration["state"] = next_state(phase)
    iteration["updated_at"] = now_iso()

    save_history(history)
    print(f"Set {field}={phase_id} for {iteration['id']}, state -> {iteration['state']}")


def cmd_get_phase(phase: str):
    if phase not in PHASE_ID_FIELD:
        print(f"Unknown phase: {phase}", file=sys.stderr)
        sys.exit(1)

    history = load_history()
    if history is None:
        print("null")
        return

    iteration = get_current_iteration(history)
    if iteration is None:
        print("null")
        return

    field = PHASE_ID_FIELD[phase]
    val = iteration["phases"].get(field)
    print(val if val else "null")


def cmd_check_file(phase: str, phase_id: str):
    if phase not in PHASE_FILE_PREFIX:
        print(f"Unknown phase: {phase}", file=sys.stderr)
        sys.exit(1)

    history = load_history()
    if history is None:
        print("no_history")
        return

    iteration = get_current_iteration(history)
    if iteration is None:
        print("no_iteration")
        return

    prefix = PHASE_FILE_PREFIX[phase]
    filepath = docs_dir() / iteration["id"] / f"{prefix}-{phase_id}.md"
    if filepath.exists():
        print(f"exists:{filepath}")
    else:
        print(f"missing:{filepath}")


def cmd_status():
    history = load_history()
    if history is None:
        print("No history.json found.")
        return

    cid = history.get("current_iteration_id")
    total = len(history.get("iterations", []))
    print(f"Total iterations: {total}")
    print(f"Current iteration: {cid or '(none)'}")

    if cid:
        iteration = get_current_iteration(history)
        if iteration:
            print(f"  State: {iteration['state']}")
            print(f"  Created: {iteration['created_at']}")
            print(f"  Updated: {iteration['updated_at']}")
            print("  Phases:")
            for phase in PHASES_ORDER:
                field = PHASE_ID_FIELD[phase]
                val = iteration["phases"].get(field, None)
                marker = "x" if val else " "
                print(f"    [{marker}] {phase}: {val or '(not started)'}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "init":
        cmd_init()
    elif cmd == "new-iter":
        cmd_new_iter()
    elif cmd == "set-phase":
        if len(sys.argv) < 4:
            print("Usage: set-phase <phase> <phase_id>", file=sys.stderr)
            sys.exit(1)
        cmd_set_phase(sys.argv[2], sys.argv[3])
    elif cmd == "get-phase":
        if len(sys.argv) < 3:
            print("Usage: get-phase <phase>", file=sys.stderr)
            sys.exit(1)
        cmd_get_phase(sys.argv[2])
    elif cmd == "check-file":
        if len(sys.argv) < 4:
            print("Usage: check-file <phase> <phase_id>", file=sys.stderr)
            sys.exit(1)
        cmd_check_file(sys.argv[2], sys.argv[3])
    elif cmd == "status":
        cmd_status()
    else:
        print(f"Unknown command: {cmd}", file=sys.stderr)
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
