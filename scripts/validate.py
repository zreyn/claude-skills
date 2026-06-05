#!/usr/bin/env python3
"""Validate the marketplace, plugins, and every skill in this repo.

Runs in CI and is also useful locally:

    python scripts/validate.py

Exits non-zero on the first hard error and prints all problems found.
The checks are deliberately conservative — they catch the things that
will actually break installation or skill loading, not stylistic nits.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml")
    sys.exit(2)


REPO_ROOT = Path(__file__).resolve().parent.parent

# Mirror the rules in skill-creator's quick_validate.py: a packaged skill must
# contain exactly one SKILL.md at the skill root. Nested SKILL.md files inside
# excluded directories don't count.
EXCLUDED_DIR_PARTS = {"__pycache__", "node_modules"}
ROOT_EXCLUDED_DIR_PARTS = {"evals"}

# Valid frontmatter keys per the Skills spec. Anything else trips the check.
ALLOWED_FRONTMATTER_KEYS = {
    "name",
    "description",
    "license",
    "allowed-tools",
    "metadata",
    "compatibility",
}


class ValidationError(Exception):
    """Raised for any validation failure."""


def _counts_as_skill_md(rel_path: Path) -> bool:
    dir_parts = rel_path.parts[:-1]
    if any(part in EXCLUDED_DIR_PARTS for part in dir_parts):
        return False
    if dir_parts and dir_parts[0] in ROOT_EXCLUDED_DIR_PARTS:
        return False
    return True


def validate_skill(skill_dir: Path) -> list[str]:
    """Return a list of error strings for this skill. Empty list = OK."""
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.exists():
        return [f"{skill_dir}: missing SKILL.md"]

    # Reject nested SKILL.md files — the Skills API will reject them on upload.
    nested = [
        p
        for p in skill_dir.rglob("SKILL.md")
        if _counts_as_skill_md(p.relative_to(skill_dir))
        and p.resolve() != skill_md.resolve()
    ]
    if nested:
        names = ", ".join(str(p.relative_to(skill_dir)) for p in nested)
        errors.append(
            f"{skill_dir}: extra SKILL.md files found ({names}). "
            "A skill must have exactly one SKILL.md at its root."
        )

    content = skill_md.read_text(encoding="utf-8")
    if not content.startswith("---"):
        errors.append(f"{skill_md}: no YAML frontmatter (file must start with ---)")
        return errors

    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        errors.append(f"{skill_md}: malformed frontmatter (missing closing ---)")
        return errors

    try:
        frontmatter = yaml.safe_load(match.group(1))
    except yaml.YAMLError as e:
        errors.append(f"{skill_md}: invalid YAML in frontmatter: {e}")
        return errors

    if not isinstance(frontmatter, dict):
        errors.append(f"{skill_md}: frontmatter must be a YAML mapping")
        return errors

    unexpected = set(frontmatter) - ALLOWED_FRONTMATTER_KEYS
    if unexpected:
        errors.append(
            f"{skill_md}: unexpected frontmatter key(s): "
            f"{', '.join(sorted(unexpected))}. "
            f"Allowed: {', '.join(sorted(ALLOWED_FRONTMATTER_KEYS))}"
        )

    name = frontmatter.get("name")
    if not name:
        errors.append(f"{skill_md}: missing required field 'name'")
    elif not isinstance(name, str):
        errors.append(f"{skill_md}: 'name' must be a string")
    else:
        name = name.strip()
        if not re.match(r"^[a-z0-9-]+$", name):
            errors.append(
                f"{skill_md}: name '{name}' must be kebab-case "
                "(lowercase letters, digits, hyphens)"
            )
        if name.startswith("-") or name.endswith("-") or "--" in name:
            errors.append(
                f"{skill_md}: name '{name}' cannot start/end with a hyphen "
                "or contain consecutive hyphens"
            )
        if len(name) > 64:
            errors.append(
                f"{skill_md}: name is {len(name)} chars (max 64)"
            )
        # Folder name should match the frontmatter name — it's the convention
        # the Skills API enforces, and mismatches cause confusing install bugs.
        if name != skill_dir.name:
            errors.append(
                f"{skill_md}: frontmatter name '{name}' does not match "
                f"folder name '{skill_dir.name}'"
            )

    description = frontmatter.get("description")
    if not description:
        errors.append(f"{skill_md}: missing required field 'description'")
    elif not isinstance(description, str):
        errors.append(f"{skill_md}: 'description' must be a string")
    else:
        if "<" in description or ">" in description:
            errors.append(
                f"{skill_md}: description cannot contain angle brackets"
            )
        if len(description) > 1024:
            errors.append(
                f"{skill_md}: description is {len(description)} chars (max 1024)"
            )

    compatibility = frontmatter.get("compatibility")
    if compatibility is not None:
        if not isinstance(compatibility, str):
            errors.append(f"{skill_md}: 'compatibility' must be a string")
        elif len(compatibility) > 500:
            errors.append(
                f"{skill_md}: compatibility is {len(compatibility)} chars (max 500)"
            )

    return errors


def validate_marketplace(marketplace_path: Path) -> list[str]:
    """Validate the marketplace.json file and the plugins it declares."""
    errors: list[str] = []
    if not marketplace_path.exists():
        return [f"{marketplace_path}: file not found"]

    try:
        data = json.loads(marketplace_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"{marketplace_path}: invalid JSON: {e}"]

    if not isinstance(data, dict):
        return [f"{marketplace_path}: top-level must be an object"]

    for required in ("name", "owner", "plugins"):
        if required not in data:
            errors.append(f"{marketplace_path}: missing required field '{required}'")

    owner = data.get("owner")
    if isinstance(owner, dict):
        for required in ("name", "email"):
            if required not in owner:
                errors.append(
                    f"{marketplace_path}: owner missing required field '{required}'"
                )
    elif owner is not None:
        errors.append(f"{marketplace_path}: 'owner' must be an object")

    plugins = data.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        errors.append(f"{marketplace_path}: 'plugins' must be a non-empty array")
        return errors

    seen_names: set[str] = set()
    for i, plugin in enumerate(plugins):
        loc = f"{marketplace_path}: plugins[{i}]"
        if not isinstance(plugin, dict):
            errors.append(f"{loc}: must be an object")
            continue
        for required in ("name", "description", "source"):
            if required not in plugin:
                errors.append(f"{loc}: missing required field '{required}'")
        pname = plugin.get("name")
        if isinstance(pname, str):
            if pname in seen_names:
                errors.append(f"{loc}: duplicate plugin name '{pname}'")
            seen_names.add(pname)

        # Each declared skill path must point to a real skill directory.
        for sp in plugin.get("skills") or []:
            if not isinstance(sp, str):
                errors.append(f"{loc}: skill entries must be strings")
                continue
            # Skill paths are relative to the marketplace root (the repo root).
            skill_path = (REPO_ROOT / sp).resolve()
            if not skill_path.is_dir():
                errors.append(f"{loc}: skill path '{sp}' is not a directory")
                continue
            if not (skill_path / "SKILL.md").exists():
                errors.append(
                    f"{loc}: skill at '{sp}' has no SKILL.md"
                )

    return errors


def find_skills(root: Path) -> list[Path]:
    skills_dir = root / "skills"
    if not skills_dir.is_dir():
        return []
    return sorted(p for p in skills_dir.iterdir() if p.is_dir())


def main() -> int:
    print(f"Validating repo at {REPO_ROOT}")
    all_errors: list[str] = []

    marketplace = REPO_ROOT / ".claude-plugin" / "marketplace.json"
    all_errors.extend(validate_marketplace(marketplace))

    skills = find_skills(REPO_ROOT)
    if not skills:
        all_errors.append("no skills found under ./skills/")
    for skill_dir in skills:
        skill_errors = validate_skill(skill_dir)
        if skill_errors:
            all_errors.extend(skill_errors)
        else:
            print(f"  ok  {skill_dir.relative_to(REPO_ROOT)}")

    if all_errors:
        print("\nValidation failed:")
        for err in all_errors:
            print(f"  - {err}")
        return 1

    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
