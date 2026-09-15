# Capture — recording what happened and what's new

Load this when the user is telling you about their day, about something that came up, or about a new thing to do. This is often a voice-dictated stream at the end of the day: run-on, unpunctuated, mid-thought corrections, misheard words. Treat it as speech, not as a form. Don't correct their grammar, don't quote it back, and don't make them repeat themselves.

The goal of capture is that **tomorrow's briefing is right** without the user having to do anything else tonight.

## What to extract

Read the whole input first, then sort it into four buckets:

1. **Done** — things they finished. Match each against `open.md` before creating anything. "Got the doc to Priya" closes #12 if #12 is the doc. If it sounds partial ("got most of the doc done"), don't close it — update its `next:` instead. If it could be one of two items, that's a question worth asking (see `clarify.md`).
2. **New** — things they'll need to do. Extract a short, verb-first title. Assign area and project from `projects.md`; if it's clearly a new project, create it and say so in the confirmation. Record `when` only if a date was stated or is clearly implied by a real event ("before the trip" is real if the trip has a date; "soon" is not a date). Record `next` if they said what the first step is or it's obvious; otherwise leave it blank rather than inventing one.
3. **Updates** — new facts about existing items or projects: blocked on someone, waiting since when, a decision that changes the plan, a date that moved. Apply these to the item's fields and to the project's status line in `projects.md`.
4. **Context** — things that aren't tasks but will matter later: who said what, decisions, dates on the horizon, how they're feeling about a project. This goes in today's `journal/` entry, and a one-line version goes in the relevant project's status if it changes what the project is about right now.

Vague ideas ("I want to look into a standing desk at some point") are new items with `status: someday`. They're kept and never nag.

## Write, then confirm

Write the store first — `open.md`, `done.md`, `projects.md`, and today's `journal/YYYY-MM-DD.md` — following `references/store-format.md`. Assign ids by taking the highest id across `open.md`, `done.md`, and `dropped.md` and adding one.

Then confirm in one compact block. Three labeled lines at most, ids included, one line each for Done / Added / Updated, omitting any that are empty. Flag anything you *inferred* (a project you created, an item you closed on a guess) with a short note so it's easy to correct. Don't restate the day back to them; the journal has it.

Then run the question pass from `clarify.md`. Often the right number of questions is zero.

## Don'ts

- Don't suggest what to do next or reorder their priorities. That's the briefing's job, and only when asked.
- Don't ask why they need to do something. It doesn't change when it gets suggested.
- Don't turn an aside into a task. "Priya seemed stressed" is context for the journal, not "Check in on Priya" — unless they said they want to.
- Don't create a project for a one-off. A project is something that will still have items next month.

## Worked example

**User:** "quick one, I need to renew the car registration it expires end of the month and also I finished the migration runbook so that's off my plate"

**Store:** New #18 "Renew car registration" · Home / Admin · due 2026-09-30 (end of month resolved from today's date). #11 "Write migration runbook" moved to `done.md` dated today. Journal for today gets two lines.

**Skill:**

```text
Done: #11 Write migration runbook
Added: #18 Renew car registration (Home / Admin, due Sep 30)
```

No questions — nothing here would change how either item is suggested later.
