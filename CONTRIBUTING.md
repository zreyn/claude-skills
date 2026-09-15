# Contributing a new skill

This is a personal repo, but the conventions below are what keep it sane as it grows. They also keep CI green.

## 1. Scaffold the folder

```text
skills/<name>/
├── SKILL.md         # required
├── references/      # optional: longer docs loaded on demand
├── prompts/         # optional: per-mode behavior files the user edits over time
├── scripts/         # optional: helper scripts the skill calls
└── assets/          # optional: templates, fonts, icons
```

The folder name must be kebab-case and must match the `name` field in the SKILL.md frontmatter exactly. The validator will fail CI if they disagree.

## 2. Write SKILL.md

Required frontmatter:

```yaml
---
name: my-skill
description: One paragraph. Should describe both what the skill does AND when Claude should reach for it. Be a little pushy about triggering — under-triggering is the more common failure.
---
```

Allowed (but rarely needed) frontmatter keys: `license`, `allowed-tools`, `metadata`, `compatibility`. Anything else fails validation.

A few things that tend to make a skill actually useful:

- **Explain *why*, not just *what*.** Today's models are smart. Telling them the reasoning behind a step lets them generalize when the situation doesn't match your examples exactly.
- **Keep the body under ~500 lines.** If it's longer, move detail into `references/<topic>.md` and tell the model when to load it.
- **Avoid heavy-handed MUSTs.** They feel safe but they make the skill brittle. Use them only when a step is genuinely non-negotiable.
- **Include 1–2 worked examples.** A short before/after is worth a page of theory.

## 3. Register the skill in the marketplace

Edit `.claude-plugin/marketplace.json` and add the skill path to an existing plugin's `skills` array, or define a new plugin if it doesn't fit:

```json
{
  "name": "zane-skills",
  "skills": [
    "./skills/eq",
    "./skills/your-new-skill"
  ]
}
```

## 4. Bump the plugin version

The plugin entry in `marketplace.json` declares a `version`. That pins it: Claude Code and claude.ai only pull an update when the string changes, so **every PR that touches anything under `skills/` must bump it**, or nobody gets the change. Semantic versioning, loosely:

- **patch** (`0.2.0` → `0.2.1`) — wording, prompt tweaks, fixes inside an existing skill
- **minor** (`0.2.0` → `0.3.0`) — a new skill, a new mode or prompt file, a memory-format change
- **major** — reserved for when a change would break an existing memory store

CI fails a PR that changes `skills/` without a bump (`scripts/check_version_bump.py`), and `./scripts/check.sh` runs the same check locally against `origin/main`.

## 5. Run the checks locally

```sh
./scripts/check.sh
```

This runs the validator, the unit tests, markdownlint, and (on a branch) the version-bump check — the same checks CI runs. Green locally = green in CI.

## 6. Commit and push

```sh
git add skills/<name>/ .claude-plugin/marketplace.json
git commit -m "add <name> skill"
git push
```

If CI is green, the skill is installable from this marketplace.

## Iterating on an existing skill

For substantive changes (new instructions, big rewrites), it's worth running a short eval pass with `skill-creator` to make sure the change actually helps. The cheap version: open Claude with the previous version, ask it to handle 2-3 representative prompts you care about, then do the same with the new version and compare outputs. The expensive version: use `skill-creator`'s eval viewer for a side-by-side benchmark.

## Removing a skill

Delete the folder and remove its entry from `marketplace.json`. The validator will fail if you delete one without the other.

## Branch protection

`main` is protected. Changes must go through a pull request, and the three CI checks (`Validate skills and marketplace`, `Lint markdown`, and `Plugin version bumped when skills change`) must pass before merge. Direct pushes to `main`, force-pushes, and branch deletion are blocked.

The policy lives at [`.github/rulesets/main-protection.json`](.github/rulesets/main-protection.json) so it's version-controlled. To apply it (once, or after editing):

```sh
gh api -X POST repos/zreyn/claude-skills/rulesets \
  --input .github/rulesets/main-protection.json
```

If a ruleset by that name already exists, you'll get a 422; in that case find the ID and update it:

```sh
RULESET_ID=$(gh api repos/zreyn/claude-skills/rulesets \
  --jq '.[] | select(.name == "main protection") | .id')
gh api -X PUT repos/zreyn/claude-skills/rulesets/$RULESET_ID \
  --input .github/rulesets/main-protection.json
```
