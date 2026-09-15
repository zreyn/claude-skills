# Prompts for `workout`

These files are the skill's behavior, one per mode. They're in git on purpose: as you use the skill and notice it asking too much, programming badly, or nagging, edit the file for that mode, commit, and run `/plugin marketplace update zane-skills` (then `/reload-plugins`).

| File | Governs |
| --- | --- |
| [`onboarding.md`](onboarding.md) | The first-run conversation that builds the profile. |
| [`checkin.md`](checkin.md) | What gets asked before a workout, and how the answers shape it. |
| [`generate.md`](generate.md) | How today's workout is planned, presented, revised, and recorded once accepted. |
| [`debrief.md`](debrief.md) | The optional "how did it go" afterward, and what it updates in the store. |
| [`review.md`](review.md) | Progress toward goals on demand, and the quarterly check-in on stats and capabilities. |

Programming knowledge (weekly balance, progression, intensity, substitutions) lives in [`../references/programming.md`](../references/programming.md). Edit that when the *workouts* are wrong; edit a prompt when the *conversation* is wrong.

## Conventions

- **Each file is loaded fresh when its mode starts.** The model does not carry a copy between sessions, so an edit takes effect the next time the mode runs after the plugin is updated.
- **`SKILL.md` invariants win.** A prompt can change how something is asked or shown; it can't make the skill ignore a limitation, record a workout before it's accepted, or invent a number. If you want to change one of those, change `SKILL.md`.
- **Say why, not just what.** The model generalizes from reasoning better than from rules.
- **Keep each file short.** Under ~80 lines. If it's growing past that, the mode is probably doing two jobs.
- **One worked example per file.**

## Editing from inside a session

If you tell the skill mid-session "from now on, do X," it will do X for the rest of that session and tell you which file to change, with a suggested line. If you're in this repo when you say it, it can make the edit for you. Personal facts (weight, equipment, goals, review cadence) don't need a prompt edit — they live in `profile.md` in the memory store.
