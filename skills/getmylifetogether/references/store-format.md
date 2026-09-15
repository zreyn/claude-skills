# Memory store format

The store is a `getmylifetogether/` folder under the memory root that `SKILL.md` resolves (`~/.claude/` in Claude Code on the user's machine; a `claude-memory/` folder in an attached workspace in Cowork). Load this file when bootstrapping the store, when writing a file type you haven't written this session, or whenever you're unsure of a field. The user may hand-edit any of these files; keep them readable and don't fight their edits.

All dates are `YYYY-MM-DD`. Ids are `#` followed by an integer, assigned by taking the highest id anywhere in `open.md`, `done.md`, or `dropped.md` and adding one. Ids are never reused.

## Layout

```text
<memory root>/getmylifetogether/
├── README.md        # what this folder is; safe-to-edit note
├── profile.md       # name, area order, thresholds, learned preferences
├── projects.md      # the cluster map: areas → projects with status lines
├── open.md          # every open item, grouped by area and project
├── done.md          # completed items, newest date first
├── dropped.md       # forgotten items, with drop and review dates
├── ideas.md         # cool ideas to explore later; never todos, never nag
└── journal/
    └── YYYY-MM-DD.md   # one file per captured day
```

## `profile.md`

```markdown
# Profile

- name: Zane
- areas: Work, Home
- stale_days: 14
- drop_review_days: 30
- drop_review: ask

## Preferences

- 2026-09-15 — Likes waiting-on items called out with how many days it's been.
```

`areas` is the display order for briefings. `stale_days` is how long an item can go untouched before the briefing's "gone quiet" line names it. `drop_review_days` is how long a dropped item waits before the drop review asks about it. `drop_review` is `ask` (default) or `auto` (delete candidates without asking; only the user sets this). Preferences are dated one-liners the skill proposes and the user approves; they're the "how I like this" notes that don't fit a field.

## `projects.md`

```markdown
# Projects

## Work

- **Q3 planning** — planning doc and offsite prep. Status: doc due Fri, then offsite Sep 24. Touched 2026-09-15.
- **Platform migration** — moving the API tier. Status: cutover pushed to October. Touched 2026-09-15.

## Home

- **House** — repairs and upkeep. Touched 2026-09-10.
- **Kids** — school and activities. Touched 2026-09-15.
- **Admin** — renewals, bills, paperwork. Touched 2026-09-15.

## People

- Priya — manager. Wants things before the offsite.
- Sam — owns the migration infra side.
```

One `##` per area, in the order from `profile.md`. Each project is one bullet: bold name, a short "what it is", an optional `Status:` clause with what's true right now, and `Touched`. The status line is where context that isn't a task goes when it changes what the project is about at the moment. `## People` is optional and short — only people who recur in items, with the one fact that helps interpret them.

## `open.md`

```markdown
# Open

## Work

### Q3 planning

- **#12 Finish planning doc** · next: add risks section · due 2026-09-19 · added 2026-09-01 · touched 2026-09-15
  - context: Priya wants it before the offsite. Headcount numbers came through 2026-09-14.
- **#15 Review Priya's PRD** · due 2026-09-17 · added 2026-09-14 · touched 2026-09-14

### Platform migration

- **#9 Schedule cutover meeting** · snoozed until 2026-10-01 · added 2026-09-02 · touched 2026-09-15
  - context: cutover pushed to October per Sam.

## Home

### Kids

- **#16 Sign field trip form** · due 2026-09-16 · added 2026-09-15 · touched 2026-09-15

### House

- **#3 Call plumber** · next: call again · added 2026-09-08 · touched 2026-09-15

### General

- **#17 Look into a standing desk** · someday · added 2026-09-15 · touched 2026-09-15
```

Item line, in order, fields separated by ` · `: bold `#id Title`; a status tag if not plain open (`someday`, `snoozed until DATE`, `waiting on WHO since DATE`); `next:` if set; `due DATE` if set; `added DATE`; `touched DATE`. Then an optional indented `context:` line, one or two sentences, only what changes how or when this gets done. Items with no project go under a `### General` heading at the end of their area. Remove empty project headings.

`touched` is updated by any write to the item. `added` never changes.

## `done.md`

```markdown
# Done

## 2026-09-15

- #11 Write migration runbook (Work / Platform migration) — added 2026-09-02.
- #16 Sign field trip form (Home / Kids) — added 2026-09-15.

## 2026-09-12

- #10 Book dentist (Home / Admin) — added 2026-09-01. Note: appointment Oct 3.
```

Newest date section first. One line per item: id, title, area / project, when it was added, and an optional `Note:` for anything worth remembering about the completion (an outcome, a follow-on date). This is the file for "did I ever…" questions and for undo.

## `dropped.md`

```markdown
# Dropped

- #3 Call plumber (Home / House) — dropped 2026-09-15 · reason: will handle with bathroom remodel · review 2026-10-15 · added 2026-09-08
- #5 Set up the old laptop for the kids (Home / Kids) — dropped 2026-08-01 · review 2026-10-01 · added 2026-07-20
```

One line per item, newest drop first. `reason` only if the user gave one. `review` is drop date plus `drop_review_days`, pushed forward each time the user defers in a drop review. Items leave this file only two ways: the user restores them (back to `open.md`) or the user says to delete them in a drop review (line removed, count noted in the journal).

## `ideas.md`

```markdown
# Ideas

- 2026-09-15 — Runbook that generates itself from the terraform. (Work / Platform migration) Why: half the runbook is already in the tf comments.
- 2026-09-12 — Family newsletter, once a quarter. (Home)
- 2026-09-03 — Learn Rust properly. → #19
- 2026-08-20 — Standing-desk treadmill. shelved 2026-09-10
```

One line per idea, newest first: date, the idea in the user's words, an optional area or project in parentheses, an optional `Why:` clause if they said what made it interesting. Two possible trailers: `→ #id` once it's been turned into an item, or `shelved DATE` if they retired it. Nothing in this file has a `next`, a `due`, or a status, and nothing here appears in a briefing beyond the count. Ideas are never deleted by the drop review; shelved ones just stay shelved.

## `journal/YYYY-MM-DD.md`

```markdown
# 2026-09-15

## Did

- Got the planning doc to Priya; she wants a risks section before Friday.
- Finished the migration runbook.

## Came up

- Field trip form due tomorrow.
- Standing desk — someday, for the new office.

## Context

- Migration cutover pushed to October (talked with Sam). Nothing to do on it until then.
- Plumber never called back.

## Ideas

- Runbook that generates itself from the terraform.

## Drop review

- Deleted #3; restored #5.
```

One file per day that had a capture or a drop review. Short bullets in the user's own terms. `## Did` and `## Came up` mirror what was written to `done.md` and `open.md`; `## Context` is the part that lives nowhere else — decisions, who said what, dates on the horizon, how a project is going. `## Ideas` records the answer to the once-a-day ideas question (`- none` if they had none) so the question isn't asked twice. `## Drop review` appears only on days a review ran. This is the source for "what did I do last week" and for reconstructing why a project is where it is.

## Bootstrap templates

When the store doesn't exist, create the directory and `journal/`, then write these. Fill in `name` once the user tells you what to call them.

`README.md`:

```markdown
# getmylifetogether store

Maintained by the `getmylifetogether` Claude skill. Safe to hand-edit; keep the formats
described in the skill's `references/store-format.md`. Nothing here is committed anywhere.
```

`profile.md`:

```markdown
# Profile

- name:
- areas: Work, Home
- stale_days: 14
- drop_review_days: 30
- drop_review: ask

## Preferences
```

`projects.md`:

```markdown
# Projects

## Work

## Home
```

`open.md`:

```markdown
# Open

## Work

## Home
```

`done.md`:

```markdown
# Done
```

`dropped.md`:

```markdown
# Dropped
```

`ideas.md`:

```markdown
# Ideas
```
