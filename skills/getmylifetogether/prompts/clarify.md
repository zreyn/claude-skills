# Clarify — when a question is worth asking

The user wants to dump and leave. Every question costs them a little, and a skill that asks five things per capture won't get used. So the bar is specific:

**Ask only if the answer would change whether, when, or under which heading an item gets suggested later — or whether it can be matched to an existing item right now.**

Everything else you either infer (and flag in the confirmation so they can correct it) or leave blank.

## Worth asking

- **Which area or project**, when it isn't inferable from `projects.md` and the wording. A standing desk could be a work expense or a home purchase; those show up under different headings.
- **A real date that was implied but not given.** "Before the offsite" when you don't know when the offsite is. Ask for the date, then also record the offsite in the project status so you never have to ask again.
- **Which existing item they mean**, when "finished the doc" could close two things. Name both by id and title; let them pick.
- **Who they're waiting on and whether they need to chase**, when something is blocked. "Waiting on Sam" that the user needs to follow up on is an action; "waiting on Sam" that will resolve itself is not. This decides whether it appears as a nudge.
- **Whether it's a someday or a real todo**, when a new item is phrased wistfully but could be either. Only ask if it's genuinely ambiguous — "at some point" usually means someday; "I need to" usually means real.

## Not worth asking

- **Priority.** Infer nothing; they'll reorder at the briefing with a word.
- **Why.** Doesn't change scheduling.
- **A next step for something that's obviously one step.** "Call the plumber" doesn't need a `next`.
- **Confirmation of every parse.** The confirmation block already shows what was written; they'll correct what's wrong.
- **Anything they'll naturally tell you tomorrow.** If it's not needed for tomorrow's briefing, it can wait for tomorrow's capture.

## How to ask

- **After the confirmation block, not before.** They should see what was recorded first.
- **At most three questions**, numbered, each with a default in brackets. Say once that "defaults" takes all of them. If they answer some and not others, the unanswered ones take their defaults — don't re-ask.
- **One line each.** No preamble, no "just to make sure."
- **If nothing meets the bar, ask nothing.** Don't fill the silence with a soft question to seem thorough.

Apply answers directly and don't re-confirm them; a one-word acknowledgement is enough.

The once-a-day ideas question at the end of a recap (see `capture.md`) is a standing question, not a clarifying one. It doesn't count toward the three, and it always comes last.

## Worked example

**Confirmation just shown:** Added #17 Look into a standing desk (someday) and #18 Renew car registration (Home / Admin, due Sep 30).

**Skill:**

```text
One question: is the standing desk work (expense it) or home? [home]
```

**User:** "work actually, and I'd want it before the new office opens"

**Skill:** moves #17 to Work / Office, keeps it someday since no date is known, and asks the one follow-up that now matters: "When does the new office open? [unknown — I'll leave it undated]". If they know, #17 gets a date and stops being someday.
