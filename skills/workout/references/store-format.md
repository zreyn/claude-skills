# Memory store format

The store is a `workout/` folder under the memory root that `SKILL.md` resolves (`~/.claude/` in Claude Code on the user's machine; a `claude-memory/` folder in an attached workspace in Cowork). Load this file when bootstrapping the store, when writing a file type you haven't written this session, or whenever you're unsure of a field. The user may hand-edit any of these files; keep them readable and don't fight their edits.

All dates are `YYYY-MM-DD`. Units are whatever the user uses; record them with the number every time.

## Layout

```text
<memory root>/workout/
├── README.md        # what this folder is; safe-to-edit note
├── profile.md       # who they are: stats, equipment, style, capabilities, limitations, goals, review dates
├── progress.md      # working numbers per movement, benchmarks, coaching notes
├── log.md           # one line per workout
└── workouts/
    └── YYYY-MM-DD.md   # full record of one day: check-in, accepted workout, debrief
```

## `profile.md`

```markdown
# Profile

- name: Zane
- born: 1985
- gender: male
- units: lb for dumbbells, kg for the kettlebell, miles for running
- days_per_week: 4
- fixed_days: run Tue and Sat (own plan)
- preferred_length: 40 min
- preferred_style: mostly lifting; two runs a week on my own; short conditioning finisher is fine
- last_review: 2026-09-15
- next_review: 2026-12-15

## Stats

- 2026-09-15 — weight 185 lb · height 5'11"

## Equipment

- Home: adjustable dumbbells 5–50 lb each, flat/incline bench, doorway pull-up bar, one 24 kg kettlebell, a few bands.
- Gym (occasional, weekends): full rack, barbells, cables, rower.

## Capabilities

- 2026-09-15 — pull-ups: 6 clean
- 2026-09-15 — 5k: about 28 min
- 2026-09-15 — DB bench: 50s × 8
- 2026-09-15 — has never deadlifted with a barbell

## Limitations

- 2026-09-15 — left shoulder: gets cranky after heavy pressing. Go easy: no overhead pressing two days in a row; no dips. (from onboarding)

## Goals

1. 10 clean pull-ups by 2026-11-01. Why: "I've never been able to."
2. Keep running base: 5k under 27 min by end of year.
3. Look better in a shirt — proxy: DB bench 55s × 10 and consistent 4 days/week.

## Review history

- 2026-09-15 — onboarding.
```

The top block is fixed fields, one per line. `born` is a year (or a full date if given); age is derived when needed. `last_review` / `next_review` drive the quarterly reminder; `next_review` is `last_review` plus three months. **Stats**, **Capabilities**, and **Limitations** are dated lines, newest first, so the trend and the staleness are both visible; a cleared limitation gets a dated `cleared` line rather than being deleted. **Goals** are ranked, with a measurable anchor and a date where the user could give one, and a `Why:` if they said it; a met goal moves to a dated `Achieved:` line at the bottom of the section. **Review history** gets a dated block from each quarterly check-in summarizing what changed.

## `progress.md`

```markdown
# Progress

## Working numbers

- Goblet squat — 24 kg × 12 (2026-09-10, solid → progress reps to 15 or move to gym for a heavier bell)
- DB bench — 50s × 8 (2026-09-13, hard but done → repeat)
- Chest-supported DB row — 45s × 10 (2026-09-15, easy → progress to 50s)
- Pull-ups — 3 × 7 (2026-09-12, last set 6 → repeat)
- Easy run — 4 mi @ ~9:30/mi (2026-09-13)

## Benchmarks

- 2026-09-10 — pull-ups max: 9
- 2026-09-06 — 5k: 27:40
- 2026-06-12 — pull-ups max: 6 (onboarding)

## Coaching notes

- 2026-09-15 — shoulder cranky the day after pressing; keep pressing to one day, pull the next. Carries are fine.
- 2026-09-08 — prefers to finish with a carry rather than a conditioning circuit.
- 2026-09-01 — hates walking lunges; split squats are fine.
```

**Working numbers**: one line per movement they do regularly — the last prescribed load and reps, the date, the debrief verdict, and the arrow saying what to do next time. Overwrite in place; the history lives in `workouts/`. **Benchmarks**: dated tests and bests, newest first; the goal anchors from onboarding go here too. **Coaching notes**: one-liners the generator should honor — preferences, what movements agree with them, what to avoid programming. Dated, newest first; prune when superseded.

## `log.md`

```markdown
# Log

- 2026-09-15 · lower + pull · 40 min · home · goblet squat, SL RDL, CS row, suitcase carry · went: good; rows easy
- 2026-09-13 · easy run · 38 min · 4 mi · went: fine
- 2026-09-12 · upper push · 40 min · home · DB bench, incline push-up, band pull-apart, pull-ups 3×7 · went: presses felt heavy
- 2026-09-10 · lower · 35 min · home · goblet squat, hip thrust, step-ups, carry · went: —
```

Newest first. One line: date, type of day, duration, place, the main movements, and `went:` from the debrief (`—` if none yet). This is what the generator scans for the last two weeks; keep it to one line so two weeks fits in a glance.

## `workouts/YYYY-MM-DD.md`

```markdown
# 2026-09-15 — lower + pull, 40 min, home

## Check-in

- feeling: slept badly, energy low
- constraints: 40 min; left shoulder cranky after yesterday's pressing — no pressing or overhead today
- preference: none

## Workout (accepted)

Lower + pull day at RPE 7: shoulder's cranky after a push day and sleep was poor.

Warm-up (6 min): 2 rounds — 10 bodyweight squats, 10 band pull-aparts, 30s dead hang (skip if shoulder complains).
Main (28 min):
1. Goblet squat — 4 × 10 @ 24 kg. Rest 90s.
2. Single-leg RDL, DBs — 3 × 8/side @ 20s. Rest 60s.
3. Chest-supported DB row — 3 × 10 @ 45s. Elbows tucked.
4. Suitcase carry — 4 × 40 m/side @ 24 kg. (swapped from KB swings — shoulder)
Cool-down (5 min): couch stretch, 90/90 hips, shoulder circles.

## Debrief

- overall: done as written
- effort: moderate
- notes: rows easy, could go heavier; shoulder fine on carries
- next time: rows to 50s
```

One file per accepted workout. The **Check-in** section keeps what they said that day so a later reader knows why the workout looks the way it does. **Workout (accepted)** is the final version after revisions, with swaps annotated. **Debrief** is added later if they report back; absent otherwise.

## Bootstrap templates

When the store doesn't exist, create the folder and `workouts/`, then write these, then run `prompts/onboarding.md` to fill in the profile.

`README.md`:

```markdown
# workout store

Maintained by the `workout` Claude skill. Safe to hand-edit; keep the formats
described in the skill's `references/store-format.md`. Nothing here is committed anywhere.
```

`profile.md`:

```markdown
# Profile

- name:
- born:
- gender:
- units:
- days_per_week:
- fixed_days:
- preferred_length:
- preferred_style:
- last_review:
- next_review:

## Stats

## Equipment

## Capabilities

## Limitations

## Goals

## Review history
```

`progress.md`:

```markdown
# Progress

## Working numbers

## Benchmarks

## Coaching notes
```

`log.md`:

```markdown
# Log
```
