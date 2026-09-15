# zane-skills

Zane's personal Claude skills. This repo is a [Claude Code plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces) hosting one or more plugins; each plugin bundles one or more skills.

## Skills

| Skill | What it does |
| --- | --- |
| [`eq`](skills/eq/SKILL.md) | Communication coach. Helps me model the other person, clarify what I actually want, and draft messages that land. |
| [`getmylifetogether`](skills/getmylifetogether/SKILL.md) | Chief of staff for work and home. Takes messy end-of-day recaps and new todos, remembers them locally, and gives me a clustered "what's on my list" each morning. Behavior lives in editable prompt files. |

More to come.

## Install

In Claude Code (or Cowork), add this repo as a marketplace and install the plugin:

```text
/plugin marketplace add zreyn/claude-skills
/plugin install zane-skills@zane-skills
```

The first argument to `install` is the plugin name; the second is the marketplace name. Both are `zane-skills` here.

## Update

In Claude Code (or Cowork):

```text
/plugin marketplace update zane-skills
```

Then you will be prompted to `/reload-plugins` (or restart).

## Memory location

Both skills keep private memory on disk, never in this repo. Where it lives depends on how you run Claude, because Cowork runs the agent in a sandbox where `~` is not your home directory (cloud sessions are discarded when they end; local sessions live in a VM you can't browse).

| Environment | Memory root | Setup |
| --- | --- | --- |
| Claude Code (CLI, desktop app, IDE) on your machine | `~/.claude/` | None. Stores are created on first use: `~/.claude/eq/people/` and `~/.claude/getmylifetogether/`. |
| Cowork | `claude-memory/` inside a folder you attach | Once: create a folder you'll keep, e.g. `~/Documents/Claude/`, and an empty `claude-memory/` inside it. Every session: attach that folder. The skills find `claude-memory/` and create their stores under it on first use. |

Resolution order, for both skills: a `claude-memory/` folder at the top of the working directory or an attached folder wins; otherwise `~/.claude/` when it's the Claude Code config directory; otherwise the skill asks you where memory should go rather than writing somewhere that won't persist.

To share one set of memory between Claude Code and Cowork, point the CLI at the Cowork folder:

```sh
mkdir -p ~/Documents/Claude/claude-memory
ln -s ~/Documents/Claude/claude-memory/eq ~/.claude/eq
ln -s ~/Documents/Claude/claude-memory/getmylifetogether ~/.claude/getmylifetogether
```

If you've already been using a skill from the CLI, move the existing folder into `claude-memory/` first, then create the symlink.

## Repo layout

```text
claude-skills/
├── .claude-plugin/
│   └── marketplace.json     # the marketplace catalog
├── skills/
│   ├── eq/
│   │   ├── SKILL.md         # the skill itself
│   │   └── references/      # optional book-specific notes
│   └── getmylifetogether/
│       ├── SKILL.md         # memory layout, routing, invariants
│       ├── prompts/         # one editable prompt per mode
│       └── references/      # memory store formats
├── scripts/
│   └── validate.py          # frontmatter + marketplace validator
├── tests/
│   └── test_validate.py     # unit tests for the validator
├── .github/workflows/ci.yml # CI: validate + markdown lint
├── CONTRIBUTING.md
└── README.md
```

## Develop

```sh
# Run every check CI runs, locally.
# First run creates .venv/ and installs requirements-dev.txt; ~10s.
# Subsequent runs are fast.
./scripts/check.sh
```

Optional: `brew install markdownlint-cli2` to skip the npx fallback on the markdown lint step.

CI runs the same checks on every push and PR to `main`. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add a new skill.

## License

MIT — see [LICENSE](LICENSE).
