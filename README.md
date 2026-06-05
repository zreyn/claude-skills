# zane-skills

Zane's personal Claude skills. This repo is a [Claude Code plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces) hosting one or more plugins; each plugin bundles one or more skills.

## Skills

| Skill | What it does |
| --- | --- |
| [`eq`](skills/eq/SKILL.md) | Communication coach. Helps me model the other person, clarify what I actually want, and draft messages that land. |

More to come.

## Install

In Claude Code (or Cowork), add this repo as a marketplace and install the plugin:

```
/plugin marketplace add zgreyn/claude-skills
/plugin install zane-skills@zane-skills
```

The first argument to `install` is the plugin name; the second is the marketplace name. Both are `zane-skills` here.

## Repo layout

```
claude-skills/
├── .claude-plugin/
│   └── marketplace.json     # the marketplace catalog
├── skills/
│   └── eq/
│       ├── SKILL.md         # the skill itself
│       └── references/      # optional book-specific notes
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
# One-off validation
python scripts/validate.py

# Run the tests
pip install pyyaml pytest
pytest -q
```

CI runs both on every push and PR to `main`. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add a new skill.

## License

MIT — see [LICENSE](LICENSE).
