# Debrief — how it went

Load this when the user reports on a workout, or when the check-in finds an undebriefed last session. The debrief is optional and cheap: a word is a valid answer. Its value is in what it updates — the next plan reads it.

## What to capture

Only what they give. Never ask for all of these; the first question is just "how did it go?"

- **Overall** — done as written, modified, cut short, skipped. One word is fine.
- **Effort** — how hard it felt, in their words or an RPE if they use them.
- **Specifics** — what felt easy, what felt heavy, sets or reps they didn't hit, anything they added.
- **Discomfort** — any pain, as opposed to soreness. This is the one thing worth a follow-up question if they mention it: where, which movement, sharp or dull, still there now?
- **Adjustments for next time** — anything they'd change: "less rest", "that weight was a joke", "never again on the lunges".

## What it updates

- **`log.md`** — the "went" field on that day's line: a few words.
- **`workouts/YYYY-MM-DD.md`** — a `## Debrief` section with the details.
- **`progress.md`** —
  - Working numbers: if a main movement was solid at the prescribed load, note it as the new baseline and mark it ready to progress; if it was a struggle, hold; if they missed reps, note it so next time backs off.
  - Benchmarks: a new best (a 5k time, a rep max) gets a dated line.
  - Coaching notes: any adjustment worth remembering, in one line.
- **`profile.md`** — pain that limits a movement becomes a dated limitation, with scope ("no overhead pressing until cleared"). Ask before adding it: "Want me to keep overhead pressing out until you say the shoulder's fine?" Remove it when they say it's cleared.

## Rules

- **Pain gets a plain response, not a diagnosis.** Stop the movement, record it, suggest they get it looked at if it persists more than a few days. Then move on; don't hover.
- **Don't editorialize about a missed or cut-short session.** Record it and plan the next one accordingly.
- **Confirm in one line** what changed in the store. If nothing needs changing beyond the log line, just say "logged".

## Worked example

**User:** "done. rows felt easy, could've gone heavier. shoulder was fine on the carries."

**Skill:** log line for today gets "went: good; rows easy". `progress.md` row entry: "45s × 10 easy on 2026-09-15 — progress to 50s". Coaching note: "shoulder OK on carries the day after a cranky press day."

```text
Logged. Rows go to 50s next time; noted the shoulder was fine on carries.
```
