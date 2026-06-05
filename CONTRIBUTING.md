# Contributing a new skill

This is a personal repo, but the conventions below are what keep it sane as it grows. They also keep CI green.

## 1. Scaffold the folder

```text
skills/<name>/
├── SKILL.md         # required
├── references/      # optional: longer docs loaded on demand
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

## 4. Run the checks locally

```sh
./scripts/check.sh
```

This runs the validator, the validator's unit tests, and markdownlint — the same three checks CI runs. Green locally = green in CI.

## 5. Commit and push

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
