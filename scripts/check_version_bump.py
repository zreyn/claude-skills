#!/usr/bin/env python3
"""Fail if a plugin's skills changed but its version didn't.

A plugin entry in marketplace.json that declares a `version` is pinned to it:
installed copies only update when the string changes. So any change under a
plugin's skill directories has to come with a version bump, or nobody gets it.

Usage:

    python scripts/check_version_bump.py <base-ref>

Compares the working tree's marketplace.json and the files changed since
<base-ref> (e.g. origin/main) against marketplace.json as it was at <base-ref>.
Exits 1 with a message naming each plugin that needs a bump.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path, PurePosixPath

REPO_ROOT = Path(__file__).resolve().parent.parent
MARKETPLACE = ".claude-plugin/marketplace.json"


def _skill_dirs(plugin: dict) -> list[PurePosixPath]:
    return [PurePosixPath(s) for s in plugin.get("skills") or []]


def _touches(changed: str, skill_dir: PurePosixPath) -> bool:
    path = PurePosixPath(changed)
    return path == skill_dir or skill_dir in path.parents


def plugins_needing_bump(
    changed_files: list[str],
    base_plugins: list[dict],
    head_plugins: list[dict],
) -> list[str]:
    """Return messages for plugins whose skills changed without a version bump.

    Pure so it can be unit-tested without git. Paths are repo-relative and
    normalized (no leading "./").
    """
    base_by_name = {p["name"]: p for p in base_plugins if "name" in p}
    normalized = [PurePosixPath(f).as_posix().removeprefix("./") for f in changed_files]
    problems: list[str] = []

    for plugin in head_plugins:
        name = plugin.get("name", "<unnamed>")
        version = plugin.get("version")
        if version is None:
            # Unpinned: the version is the commit SHA, updates flow automatically.
            continue
        dirs = [PurePosixPath(d.as_posix().removeprefix("./")) for d in _skill_dirs(plugin)]
        touched = sorted(
            {f for f in normalized if any(_touches(f, d) for d in dirs)}
        )
        if not touched:
            continue
        base_version = base_by_name.get(name, {}).get("version")
        if base_version != version:
            continue
        shown = ", ".join(touched[:5]) + (" …" if len(touched) > 5 else "")
        problems.append(
            f"plugin '{name}' has changes under its skills ({shown}) "
            f"but its version is still {version!r}. Bump 'version' in {MARKETPLACE}."
        )
    return problems


def _git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, check=True, capture_output=True, text=True
    ).stdout


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2
    base_ref = argv[1]

    changed = [line for line in _git("diff", "--name-only", f"{base_ref}...HEAD").splitlines() if line]
    # Include uncommitted changes so the check is useful locally, not just in CI.
    changed += [line for line in _git("diff", "--name-only", "HEAD").splitlines() if line]
    changed += [line for line in _git("ls-files", "--others", "--exclude-standard").splitlines() if line]

    head_plugins = json.loads((REPO_ROOT / MARKETPLACE).read_text(encoding="utf-8")).get("plugins", [])
    try:
        base_plugins = json.loads(_git("show", f"{base_ref}:{MARKETPLACE}")).get("plugins", [])
    except subprocess.CalledProcessError:
        base_plugins = []  # marketplace.json didn't exist at base; nothing to compare.

    problems = plugins_needing_bump(changed, base_plugins, head_plugins)
    if problems:
        print("Version bump required:")
        for msg in problems:
            print(f"  - {msg}")
        return 1
    print(f"Plugin versions OK against {base_ref}.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
