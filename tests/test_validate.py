"""Unit tests for scripts/validate.py.

These tests build tiny throwaway skill directories in tmp_path and run the
validator against them. They protect against regressions in the validator
itself — if someone tightens or loosens a check, these will scream.
"""

from __future__ import annotations

import json
import sys
import textwrap
from pathlib import Path

import pytest

# Make `scripts` importable when pytest is run from the repo root.
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts import validate as v  # noqa: E402


def _write_skill(
    base: Path,
    name: str,
    *,
    frontmatter: dict | None = None,
    body: str = "Body.",
    folder_name: str | None = None,
) -> Path:
    folder = base / "skills" / (folder_name or name)
    folder.mkdir(parents=True, exist_ok=True)
    fm = frontmatter if frontmatter is not None else {
        "name": name,
        "description": "A perfectly valid description.",
    }
    fm_text = "\n".join(f"{k}: {json.dumps(val)}" for k, val in fm.items())
    (folder / "SKILL.md").write_text(f"---\n{fm_text}\n---\n\n{body}\n")
    return folder


def _write_marketplace(base: Path, plugins: list[dict] | None = None) -> Path:
    plugin_dir = base / ".claude-plugin"
    plugin_dir.mkdir(parents=True, exist_ok=True)
    data = {
        "name": "test-marketplace",
        "owner": {"name": "Test", "email": "test@example.com"},
        "plugins": plugins
        or [
            {
                "name": "test-plugin",
                "description": "x",
                "source": "./",
                "skills": ["./skills/eq"],
            }
        ],
    }
    path = plugin_dir / "marketplace.json"
    path.write_text(json.dumps(data, indent=2))
    return path


# --- Skill validation -------------------------------------------------------

def test_valid_skill_passes(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(v, "REPO_ROOT", tmp_path)
    folder = _write_skill(tmp_path, "eq")
    assert v.validate_skill(folder) == []


def test_missing_skill_md(tmp_path: Path) -> None:
    folder = tmp_path / "skills" / "eq"
    folder.mkdir(parents=True)
    errors = v.validate_skill(folder)
    assert any("missing SKILL.md" in e for e in errors)


def test_missing_frontmatter(tmp_path: Path) -> None:
    folder = tmp_path / "skills" / "eq"
    folder.mkdir(parents=True)
    (folder / "SKILL.md").write_text("just some markdown, no frontmatter\n")
    errors = v.validate_skill(folder)
    assert any("frontmatter" in e for e in errors)


def test_name_must_be_kebab_case(tmp_path: Path) -> None:
    folder = _write_skill(
        tmp_path,
        "EQ_Bad",
        frontmatter={"name": "EQ_Bad", "description": "x"},
        folder_name="EQ_Bad",
    )
    errors = v.validate_skill(folder)
    assert any("kebab-case" in e for e in errors)


def test_folder_name_must_match_frontmatter(tmp_path: Path) -> None:
    folder = _write_skill(
        tmp_path,
        "eq",
        frontmatter={"name": "eq", "description": "x"},
        folder_name="something-else",
    )
    errors = v.validate_skill(folder)
    assert any("does not match" in e for e in errors)


def test_unexpected_frontmatter_key_is_rejected(tmp_path: Path) -> None:
    folder = _write_skill(
        tmp_path,
        "eq",
        frontmatter={"name": "eq", "description": "x", "bogus": "1"},
    )
    errors = v.validate_skill(folder)
    assert any("unexpected frontmatter" in e for e in errors)


def test_nested_skill_md_is_rejected(tmp_path: Path) -> None:
    folder = _write_skill(tmp_path, "eq")
    nested = folder / "sub"
    nested.mkdir()
    (nested / "SKILL.md").write_text("---\nname: nested\ndescription: x\n---\n")
    errors = v.validate_skill(folder)
    assert any("extra SKILL.md" in e for e in errors)


# --- Marketplace validation -------------------------------------------------

def test_valid_marketplace_passes(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(v, "REPO_ROOT", tmp_path)
    _write_skill(tmp_path, "eq")
    market_path = _write_marketplace(tmp_path)
    assert v.validate_marketplace(market_path) == []


def test_marketplace_missing_plugin_skill_path(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(v, "REPO_ROOT", tmp_path)
    # No skill on disk, but the marketplace references one.
    market_path = _write_marketplace(
        tmp_path,
        plugins=[
            {
                "name": "p",
                "description": "x",
                "source": "./",
                "skills": ["./skills/does-not-exist"],
            }
        ],
    )
    errors = v.validate_marketplace(market_path)
    assert any("not a directory" in e for e in errors)


def test_marketplace_invalid_json(tmp_path: Path) -> None:
    plugin_dir = tmp_path / ".claude-plugin"
    plugin_dir.mkdir()
    bad = plugin_dir / "marketplace.json"
    bad.write_text("{ not json")
    errors = v.validate_marketplace(bad)
    assert any("invalid JSON" in e for e in errors)


def test_marketplace_duplicate_plugin_name(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(v, "REPO_ROOT", tmp_path)
    _write_skill(tmp_path, "eq")
    market_path = _write_marketplace(
        tmp_path,
        plugins=[
            {"name": "p", "description": "x", "source": "./", "skills": ["./skills/eq"]},
            {"name": "p", "description": "x", "source": "./", "skills": ["./skills/eq"]},
        ],
    )
    errors = v.validate_marketplace(market_path)
    assert any("duplicate plugin name" in e for e in errors)
