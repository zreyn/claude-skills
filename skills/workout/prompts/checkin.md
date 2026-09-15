# Check-in — before a workout

Load this when the user asks for a workout. The check-in is one short message that gathers what today's plan depends on, with defaults from the profile so a one-word answer works. It's not a mood survey.

Before asking, read `profile.md`, `progress.md`, and the last two weeks of `log.md`. Two things to notice silently:

- **An undebriefed last workout.** If the most recent log line has no "went" note, fold one question into the check-in: "How did Tuesday's session go?" A word is enough; write it per `debrief.md` before planning today.
- **A due quarterly review.** If `next_review` is today or earlier, don't lead with it. Mention it after today's workout is accepted (see `generate.md`).

## What to ask

One message, at most three questions, each with the default in brackets:

1. **How are you feeling?** Energy, sleep, soreness — whatever they want to volunteer. This sets intensity. [normal]
2. **Anything different today?** Time available, equipment or location, a movement or joint to avoid. [usual: N minutes, usual equipment]
3. **Any preference?** Kind of session (lift, run, conditioning, mobility, "surprise me") and how hard. [you pick, based on the week]

If they gave all of this in the request ("40 minutes, home, shoulder's cranky, something lower body"), skip the questions entirely and go straight to `generate.md`. Don't ask what they've already told you.

## How answers shape the plan

- **Tired, poor sleep, unusually sore** → lower intensity (RPE cap around 7), fewer sets, no new movements, no max-effort work. Say why in one clause.
- **Feeling great** → a normal or hard day, if the log supports it. Two hard days in a row on the same pattern is still a no.
- **Less time** → keep the main lift, cut accessories, shorten rest. Don't cram.
- **Different equipment** → substitute per `references/programming.md`; keep the movement pattern, change the tool.
- **A joint or movement to avoid today** → treat as a limitation for this session and program around it. If it's the second time in two weeks, ask at the debrief whether it should become a standing limitation.
- **A preference** → honor it unless it collides with the week's balance or a limitation; if it does, say so and offer the nearest thing.

## Worked example

**User:** "workout please"

**Skill:**

```text
Quick check before I plan it:
1. How are you feeling — energy, sleep, soreness? [normal]
2. Anything different today — time, place, anything to avoid? [40 min, home gym]
3. Preference for what kind or how hard? [I'll pick — you're due a lower day]
Also, how did Tuesday's upper session go? A word is fine.
```

**User:** "tired, 30 min today, otherwise usual. tuesday was fine, presses felt heavy."

**Skill:** writes Tuesday's debrief ("fine; presses felt heavy"), then plans a 30-minute lower day at moderate intensity per `generate.md`.
