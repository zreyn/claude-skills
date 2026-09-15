# Reactions — quick verbs for working the list

Load this whenever the user responds to items, during a briefing or on their own. Reactions are terse; the user shouldn't have to explain themselves. Apply the change, confirm it in one line with the id, and move on. Never argue with a reaction — it's their list.

## Vocabulary

| They say | Do | Write |
| --- | --- | --- |
| "did that", "done", "finished", "that's off my plate" | Close it. If it sounds partial ("did the first half"), update `next:` instead and don't ask. | Move to `done.md` with today's date; note in today's journal. |
| "forget about that", "drop it", "not doing that", "that's dead", "take it off" | Drop it. Don't ask why. If they volunteer a reason, keep it. | Move to `dropped.md` with today's date, reason if given, and a review date of today plus `drop_review_days` from `profile.md` (default 30). |
| "later", "someday", "not now", "someday maybe" | Park it. Hidden from daily briefings, kept forever. | `status: someday`. |
| "snooze until X", "next week", "after the trip", "push it a month" | Hide until a date. Resolve relative dates from today. If it's relative to an event with no known date, ask for the date (that meets the clarify bar). | `status: snoozed until YYYY-MM-DD`. |
| "waiting on Sam", "blocked on finance", "sent it, waiting to hear back" | Mark it waiting. | `status: waiting on <who> since YYYY-MM-DD`. |
| "that's actually home", "move that to the migration project", "call it X instead" | Edit fields. | Update the item; create the project if new. |
| "add …", "also I need to…", "oh and…" | Capture inline. | Follow `capture.md` and `clarify.md`. |
| "undo", "no, bring that back", "un-drop #7" | Reverse the last change, or restore the named item. | Move it back to `open.md`, restore fields, touch it today. Note "restored" in the item's context. |
| "show someday", "show dropped", "show what I did this week", "show done" | List. | Nothing. |

Every write updates the item's `touched` date. Anything that changes the shape of a project (new project, status line) also updates `projects.md`.

## Ambiguity

"Forget about that" after you showed one item: just do it. After you showed three: ask which — one short line naming them by id. Never guess on a drop; a wrong drop silently loses something.

"Did that" when two open items could match: same — name both, let them pick.

## Batching

The user will often fire several reactions in one message: "did 12 and 16, forget 3, snooze 9 to october." Apply all of them, then confirm in one compact list, one line per change with the id. Don't confirm each one separately and don't re-show the briefing.

## Worked example

**User:** "did the form, and forget about the plumber, I'll deal with it when we redo the bathroom"

**Skill:** #16 → `done.md` today. #3 → `dropped.md` today, reason "will handle with bathroom remodel", review 2026-10-15.

```text
Done: #16 Sign field trip form
Dropped: #3 Call plumber (bathroom remodel)
```
