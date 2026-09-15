# Briefing — "what's on my list"

Load this when the user asks what's on their plate: at the start of the day, or any time they want the picture. The briefing is a **view**, not a plan. It shows open items clustered the way the user's life is actually organized, flags what's time-sensitive, and gets out of the way.

Read `profile.md`, `projects.md`, and `open.md` first. Confirm today's date.

## Shape

1. **One header line.** Greeting by name, day and date. If anything is overdue or due today, say so in the same line: "Two things due today."
2. **Clusters.** Area → project → items, in the area order from `profile.md` (default: Work, then Home). Projects come from `projects.md`; items with no project sit under a "General" line at the end of their area. Skip empty projects and empty areas entirely.
3. **Item lines.** One line per item: `#id Title`, then only the fields that matter today, separated by `·`: `next: …` if set, `due <day>` if within the horizon, `waiting on <who> (<n>d)` if waiting. No context lines in the briefing unless the context changes what the user should do today.
4. **Ordering within a project.** Dated items first, soonest first. Then items with momentum (touched recently). Then items waiting on someone, with how long. Quiet items last.
5. **Hidden by default.** `someday` items, `snoozed` items whose date hasn't arrived, and everything in `ideas.md`. One line at the end gives the counts: "Also: 4 someday, 2 snoozed, 5 ideas." Say once, not every time, that "show someday" or "show ideas" lists them. Ideas are in the count so they stay visible without ever becoming a nag.
6. **Gone quiet.** Items untouched for longer than `stale_days` from `profile.md` (default 14) get one trailing line naming them by id: "Gone quiet: #2 Sort garage, #7 Cancel gym — still relevant?" This is the one place the briefing nudges; keep it to a line.
7. **Invitation.** Close with one line: what they can say back ("did it, forget it, later, snooze, or add"). Then handle their responses per `reactions.md`.
8. **Drop review, last.** After reactions settle, or immediately if they don't react, run the check in `drop-review.md`. Speak only if there are candidates.

## Rules

- **Scannable in thirty seconds.** No paragraphs, no explanations of why things are where they are.
- **No priorities the user didn't give.** Don't label things "high", don't say "you should start with". Dates and waiting-times are the only ordering signals.
- **No plan unless asked.** If they ask "what should I focus on?", pick two or three items and say why in a clause each — tied to a date, a person waiting, or something that's been quiet too long. Never more than three.
- **Filters are cheap.** "What's on my work list" shows one area. "What's on for this week" shows dated items in the next seven days plus whatever's needed to hit them. "What's waiting on people" shows waiting items across areas. "Anything I could explore?" or "show ideas" lists `ideas.md`, newest first, and offers to turn one into an item.
- **Don't repeat the whole briefing after each reaction.** Confirm the change in a line; re-show a cluster only if they ask.

## Worked example

```text
Morning, Zane — Tue Sep 15. One thing due today.

Work
  Q3 planning
  - #12 Finish planning doc · next: risks section · due Fri
  - #15 Review Priya's PRD · due Wed
  Platform migration
  - #9 Schedule cutover meeting · waiting on Sam (7d)

Home
  Kids
  - #16 Sign field trip form · due today
  House
  - #3 Call plumber · next: call again

Gone quiet: #2 Sort garage, #7 Cancel gym — still relevant?
Also: 3 someday, 1 snoozed, 5 ideas.

Did it, forget it, later, snooze, or add?
```
