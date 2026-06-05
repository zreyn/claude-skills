#!/usr/bin/env bash
# Run every check CI runs, in the same order, on your local machine.
# Exits non-zero on the first failure so you can fix one thing at a time.
#
# Manages its own Python virtualenv at .venv/ so it never touches your
# system Python. First run is a bit slower (creates the venv and installs
# requirements-dev.txt); subsequent runs are fast.
#
# Usage:
#   ./scripts/check.sh
#
# Requirements on PATH:
#   - python3  (3.10+ recommended; CI uses 3.12)
#   - markdownlint-cli2 OR npx  (we fall back to npx so a fresh Mac works)

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

VENV_DIR="$REPO_ROOT/.venv"
VENV_PY="$VENV_DIR/bin/python"
REQS="$REPO_ROOT/requirements-dev.txt"
# We touch this stamp file after a successful install so we don't reinstall
# on every run. We compare its mtime against requirements-dev.txt to detect
# changes — if the requirements file is newer, we reinstall.
STAMP="$VENV_DIR/.installed.stamp"

section() {
  printf '\n\033[1;34m==> %s\033[0m\n' "$1"
}

# --- Step 0: ensure venv exists and is up to date --------------------------

if [[ ! -x "$VENV_PY" ]]; then
  section "Creating virtualenv at .venv/"
  python3 -m venv "$VENV_DIR"
  "$VENV_PY" -m pip install --quiet --upgrade pip
fi

if [[ ! -f "$STAMP" || "$REQS" -nt "$STAMP" ]]; then
  section "Installing dev dependencies"
  "$VENV_PY" -m pip install --quiet -r "$REQS"
  touch "$STAMP"
fi

# --- Step 1-3: the actual checks -------------------------------------------

section "1/3  Validate marketplace + skills"
"$VENV_PY" scripts/validate.py

section "2/3  Run validator unit tests"
"$VENV_PY" -m pytest -q tests/

section "3/3  Lint markdown"
if command -v markdownlint-cli2 >/dev/null 2>&1; then
  markdownlint-cli2 "**/*.md" "!node_modules"
else
  # Fall back to npx so this still works on a fresh machine. The first
  # invocation downloads markdownlint-cli2 into npx's cache; subsequent
  # runs are fast.
  npx --yes markdownlint-cli2 "**/*.md" "!node_modules"
fi

printf '\n\033[1;32mAll checks passed.\033[0m\n'
