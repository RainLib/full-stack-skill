# Full-Stack Skills - Project Management
# Works on macOS (make built-in) and Windows (via Git Bash / WSL / choco install make)

PYTHON    ?= python3
HISTORY   := .claude/skills/history-manager/scripts/history_manager.py
DOCS_DIR  := docs

.PHONY: help init status new-iter set-phase get-phase check-file \
        clean-iter list-iters validate-schema tree

# ──────────────────────────────────────────────
# Default target
# ──────────────────────────────────────────────

help: ## Show this help
	@echo ""
	@echo "Full-Stack Skills - Makefile Commands"
	@echo "======================================"
	@echo ""
	@echo "Iteration Management:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  make %-18s %s\n", $$1, $$2}'
	@echo ""
	@echo "Examples:"
	@echo "  make init                          Initialize history.json"
	@echo "  make new-iter                      Create a new iteration"
	@echo "  make status                        Show current progress"
	@echo "  make set-phase PHASE=requirements PHASE_ID=req-001"
	@echo "  make get-phase PHASE=requirements"
	@echo "  make check-file PHASE=requirements PHASE_ID=req-001"
	@echo ""

# ──────────────────────────────────────────────
# Iteration Management (wraps history-manager)
# ──────────────────────────────────────────────

init: ## Initialize docs/history.json
	@$(PYTHON) $(HISTORY) init

status: ## Show current iteration status and phase progress
	@$(PYTHON) $(HISTORY) status

new-iter: ## Create a new iteration (e.g. iter-001)
	@$(PYTHON) $(HISTORY) new-iter

set-phase: ## Set phase complete: PHASE=xxx PHASE_ID=xxx
	@test -n "$(PHASE)" || (echo "Error: PHASE is required" && exit 1)
	@test -n "$(PHASE_ID)" || (echo "Error: PHASE_ID is required" && exit 1)
	@$(PYTHON) $(HISTORY) set-phase $(PHASE) $(PHASE_ID)

get-phase: ## Get phase id: PHASE=xxx
	@test -n "$(PHASE)" || (echo "Error: PHASE is required" && exit 1)
	@$(PYTHON) $(HISTORY) get-phase $(PHASE)

check-file: ## Check if phase doc exists: PHASE=xxx PHASE_ID=xxx
	@test -n "$(PHASE)" || (echo "Error: PHASE is required" && exit 1)
	@test -n "$(PHASE_ID)" || (echo "Error: PHASE_ID is required" && exit 1)
	@$(PYTHON) $(HISTORY) check-file $(PHASE) $(PHASE_ID)

# ──────────────────────────────────────────────
# Project Utilities
# ──────────────────────────────────────────────

tree: ## Show project directory structure (skills + docs)
	@echo "=== Skills ==="
	@find .claude/skills -type f -name '*.md' -o -name '*.py' | sort
	@echo ""
	@echo "=== Docs ==="
	@find $(DOCS_DIR) -type f | sort

list-iters: ## List all iteration directories
	@find $(DOCS_DIR) -maxdepth 1 -type d -name 'iter-*' | sort

validate-schema: ## Validate history.json against schema (requires python jsonschema)
	@$(PYTHON) -c "\
import json, sys; \
try: \
    from jsonschema import validate; \
    schema = json.load(open('$(DOCS_DIR)/history.schema.json')); \
    data = json.load(open('$(DOCS_DIR)/history.json')); \
    validate(instance=data, schema=schema); \
    print('history.json is valid'); \
except ImportError: \
    print('Install jsonschema: pip install jsonschema'); sys.exit(1); \
except Exception as e: \
    print(f'Validation failed: {e}'); sys.exit(1)"

clean-iter: ## Remove a specific iteration: ITER=iter-001
	@test -n "$(ITER)" || (echo "Error: ITER is required (e.g. make clean-iter ITER=iter-001)" && exit 1)
	@test -d "$(DOCS_DIR)/$(ITER)" || (echo "Error: $(DOCS_DIR)/$(ITER) does not exist" && exit 1)
	@echo "Removing $(DOCS_DIR)/$(ITER)/ ..."
	@rm -rf "$(DOCS_DIR)/$(ITER)"
	@echo "Done. Note: history.json is NOT updated. Edit it manually if needed."
