# Capture — recording what happened and what's new

Load this when the user is telling you about their day, about something that came up, or about a new thing to do. This is often a voice-dictated stream at the end of the day: run-on, unpunctuated, mid-thought corrections, misheard words. Treat it as speech, not as a form. Don't correct their grammar, don't quote it back, and don't make them repeat themselves.

The goal of capture is that **tomorrow's briefing is right** without the user having to do anything else tonight.

## What to extract

Read the whole input first, then sort it into five buckets:

1. **Done** — things they finished. Match each against `open.md` before creating anything. "Got the doc to Priya" closes #12 if #12 is the doc. If it sounds partial ("got most of the doc done"), don't close it — update its `next:` instead. If it could be one of two items, that's a question worth asking (see `clarify.md`).
2. **New** — things they'll need to do. Extract a short, verb-first title. Assign area and project from `projects.md`; if it's clearly a new project, create it and say so in the confirmation. Record `when` only if a date was stated or is clearly implied by a real event ("before the trip" is real if the trip has a date; "soon" is not a date). Record `next` if they said what the first step is or it's obvious; otherwise leave it blank rather than inventing one.
3. **Updates** — new facts about existing items or projects: blocked on someone, waiting since when, a decision that changes the plan, a date that moved. Apply these to the item's fields and to the project's status line in `projects.md`.
4. **Context** — things that aren't tasks but will matter later: who said what, decisions, dates on the horizon, how they're feeling about a project. This goes in today's `journal/` entry, and a one-line version goes in the relevant project's status if it changes what the project is about right now.
5. **Ideas** — something they'd like to explore, build, read, or try, with no commitment attached. "It'd be cool if the runbook generated itself", "I should learn Rust", "what if we did a family newsletter". These go in `ideas.md`, not `open.md`: an idea has no `next` and no date, and it never appears in a briefing. Keep the spark in their words, plus one line of why it seemed interesting if they said. If the idea clearly attaches to a project, note the project.

The line between a someday item and an idea: a someday item is something they intend to do eventually ("look into a standing desk at some point"); an idea is something they'd enjoy exploring and might never do. When it's unclear, it's an idea — ideas are cheaper to hold and easy to promote later.

## Write, then confirm

Write the store first — `open.md`, `done.md`, `projects.md`, `ideas.md` if any, and today's `journal/YYYY-MM-DD.md` — following `references/store-format.md`. Assign ids by taking the highest id across `open.md`, `done.md`, and `dropped.md` and adding one.

Then confirm in one compact block. Three labeled lines at most, ids included, one line each for Done / Added / Updated, omitting any that are empty. Flag anything you *inferred* (a project you created, an item you closed on a guess) with a short note so it's easy to correct. Don't restate the day back to them; the journal has it.

Then run the question pass from `clarify.md`. Often the right number of questions is zero.

## The ideas question

Once a day, at the end of an end-of-day capture, ask: **"Any cool ideas today — anything you'd want to explore later?"** This is a standing question, not a clarifying one, so it doesn't count against the `clarify.md` limit. The reason it exists: ideas are the things most likely to evaporate overnight, and the user asked to be prompted for them.

- Ask it **after** the confirmation block and any clarifying questions, as its own last line.
- Ask **once per day**. If today's journal already has an `## Ideas` section, don't ask again — even if this is a second capture.
- Skip it if the capture already contained an idea; just record that one.
- Skip it for quick one-item captures ("add: renew the registration") — it belongs to the recap, not to every add.
- "No" or "nothing" is a complete answer. Write `## Ideas` / `- none` to today's journal so the question doesn't come back, and say nothing more about it.
- If they answer, write each idea to `ideas.md` and echo them in today's journal under `## Ideas`. Confirm in one line. Don't turn an idea into a todo unless they say so.

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

No clarifying questions — nothing here would change how either item is suggested later. And no ideas question either: this is a quick add, not the end-of-day recap.

**Later, the end-of-day recap:** after its confirmation block, the skill ends with:

```text
Any cool ideas today — anything you'd want to explore later?
```

**User:** "yeah actually, it'd be neat if the runbook could generate itself from the terraform"

**Store:** `ideas.md` gets a dated line under Work / Platform migration: "Runbook that generates itself from the terraform." Journal gets `## Ideas` with the same line.

**Skill:**

```text
Saved: runbook that generates itself from the terraform (Platform migration)
```
