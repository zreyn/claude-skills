"""Unit tests for scripts/check_version_bump.py.

Only the pure decision function is tested; the git plumbing around it is thin.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.check_version_bump import plugins_needing_bump  # noqa: E402


def _plugin(name: str, version: str | None, skills: list[str]) -> dict:
    p = {"name": name, "description": "x", "source": "./", "skills": skills}
    if version is not None:
        p["version"] = version
    return p


def test_skill_change_without_bump_fails():
    base = [_plugin("zane-skills", "0.2.0", ["./skills/eq"])]
    head = [_plugin("zane-skills", "0.2.0", ["./skills/eq"])]
    problems = plugins_needing_bump(["skills/eq/SKILL.md"], base, head)
    assert len(problems) == 1
    assert "zane-skills" in problems[0]
    assert "0.2.0" in problems[0]


def test_skill_change_with_bump_passes():
    base = [_plugin("zane-skills", "0.2.0", ["./skills/eq"])]
    head = [_plugin("zane-skills", "0.3.0", ["./skills/eq"])]
    assert plugins_needing_bump(["skills/eq/SKILL.md"], base, head) == []


def test_new_skill_folder_counts_as_change():
    base = [_plugin("zane-skills", "0.2.0", ["./skills/eq"])]
    head = [_plugin("zane-skills", "0.2.0", ["./skills/eq", "./skills/new"])]
    problems = plugins_needing_bump(["skills/new/SKILL.md"], base, head)
    assert len(problems) == 1


def test_changes_outside_skills_dont_require_bump():
    base = [_plugin("zane-skills", "0.2.0", ["./skills/eq"])]
    head = [_plugin("zane-skills", "0.2.0", ["./skills/eq"])]
    changed = ["README.md", ".github/workflows/ci.yml", "skills-notes.md"]
    assert plugins_needing_bump(changed, base, head) == []


def test_unpinned_plugin_is_ignored():
    base = [_plugin("zane-skills", None, ["./skills/eq"])]
    head = [_plugin("zane-skills", None, ["./skills/eq"])]
    assert plugins_needing_bump(["skills/eq/SKILL.md"], base, head) == []


def test_newly_pinned_plugin_passes():
    # Base had no version; head declares one. That's a bump by definition.
    base = [_plugin("zane-skills", None, ["./skills/eq"])]
    head = [_plugin("zane-skills", "0.2.0", ["./skills/eq"])]
    assert plugins_needing_bump(["skills/eq/SKILL.md"], base, head) == []


def test_only_the_touched_plugin_is_flagged():
    base = [
        _plugin("a", "1.0.0", ["./skills/a-skill"]),
        _plugin("b", "1.0.0", ["./skills/b-skill"]),
    ]
    head = [
        _plugin("a", "1.0.0", ["./skills/a-skill"]),
        _plugin("b", "1.0.0", ["./skills/b-skill"]),
    ]
    problems = plugins_needing_bump(["skills/b-skill/prompts/x.md"], base, head)
    assert len(problems) == 1
    assert "'b'" in problems[0]
