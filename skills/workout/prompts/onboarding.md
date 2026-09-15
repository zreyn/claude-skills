# Onboarding — building the profile

Load this on first run, or whenever `profile.md` is mostly empty. The goal is a profile complete enough to program safely and specifically. The method is a conversation — two or three questions at a time, follow-ups where the first answer was thin — not a form. Plan on five or six exchanges, not one giant questionnaire.

Say up front, in a sentence, what you're doing and why: "A few questions so I can program for you rather than for a generic person. Skip anything you'd rather not answer."

## What the profile needs

Work through these in roughly this order. Each one has a reason; if the user asks why, say it.

1. **Name, birth year, gender.** Birth year, not age, so it never goes stale. Gender only as it informs programming defaults; "prefer not to say" is fine.
2. **Weight**, with the unit they use. Optionally height. Dated when stored.
3. **Equipment.** What they actually have access to, where. A home setup and a gym membership are different days — record both if both exist. Follow up on specifics that change programming: dumbbell range, whether the kettlebell is one fixed weight, whether there's somewhere to hang or run.
4. **Preferred style.** How long a workout should usually be, and what it should mostly be made of — lifting, circuits, running, mobility, some mix. Follow up: how many days a week they're realistically going to train, and whether there are fixed days (a run club, a class).
5. **Capabilities.** What they can do now, in their words, with numbers where they have them: "I can do 8 pull-ups", "I run 5k in about 28 minutes", "I've never deadlifted". Ask for two or three anchors, not an inventory. These seed `progress.md`.
6. **Limitations.** Injuries, past or present; movements or joints to avoid; anything a doctor has told them. Follow up on anything vague: "bad knee" → which movements bother it, and is it a hard no or a "go easy"? Record each as a dated line with its scope.
7. **Goals.** What they want to be true in three to six months. Push gently toward something checkable: "get stronger" → "add 20 kg to my squat" or "do 10 clean pull-ups"; "lose weight" → a number and a rough date, or a non-scale marker they'd accept. Two or three goals, ranked. Note anything they say about *why* — it helps when motivation dips.

## How to run it

- **Two or three questions per message.** Group naturally (name/birth year/gender together; equipment on its own; capabilities and limitations together).
- **Follow up once on thin answers**, then move on. "Some dumbbells" → "what's the range?" is worth it; a third follow-up is not.
- **Reflect back before writing.** After the last exchange, show the profile as you'll record it — compact, one line per field — and ask for corrections. Then write `profile.md` and seed `progress.md` with the capability anchors.
- **Set the review date.** `next_review` is today plus three months. Say once that you'll ask to refresh stats and capabilities then.
- **Don't program yet** unless they ask. Onboarding ends with the profile; the first workout is a separate check-in so they get the normal experience.

## Worked example

**Skill:** "A few questions so I can program for you, not for a generic person — skip anything you'd rather not answer. First: what should I call you, what year were you born, and how would you like me to think about gender for programming purposes?"

**User:** "Zane, 1985, male."

**Skill:** "Thanks. What equipment do you have — at home, at a gym, or both? And what's a good workout look like for you: how long, and mostly what kind of thing?"

**User:** "Home: adjustable dumbbells up to 50 lb each, a bench, a pull-up bar, one 24 kg kettlebell. 40 minutes, mostly lifting, I run twice a week on my own."

**Skill:** "Good setup. Two more: a few numbers on where you are now — say, pull-ups, a lift you know, your 5k — and anything I should avoid or go easy on: injuries, joints, doctor's orders."

…and so on, ending with the read-back and the write.
