# Drop review — "you dropped these a while ago; still sure?"

Dropped items aren't deleted right away, because "forget about that" is often said in the moment and sometimes the thing comes back. But `dropped.md` shouldn't grow forever either. The drop review is the one interactive moment where old drops get deleted for good — with the user's say-so, never automatically.

## When to run it

- **At the end of a briefing**, after reactions have settled. Never at the top; the morning view shouldn't open with housekeeping.
- **When the user asks** ("clean up", "review dropped", "what have I dropped").
- **At most once per day.** If a review ran today (a `## Drop review` line in today's journal), skip.

A dropped item is a **candidate** when its `review` date is today or earlier. The review date is set when the item is dropped (drop date plus `drop_review_days` from `profile.md`, default 30) and pushed forward whenever the user defers.

If `profile.md` says `drop_review: auto`, skip the conversation and delete candidates silently, listing them in one line of the journal. Only the user sets that; the default is `ask`.

## How to present

One short block. Name each candidate by id and title, with how long ago it was dropped and the reason if one was recorded. Then a single question with the three outcomes in plain words.

- **"Let them go" / "yes" / "delete"** → remove the entries from `dropped.md` permanently. Note the count and ids in today's journal under `## Drop review`.
- **"Bring back #7"** → restore that one to `open.md` (fields intact, `touched` today, context notes "restored from dropped"). Delete or defer the rest as they said.
- **"Not sure" / "ask me later" / no clear answer** → push each candidate's `review` date forward by `drop_review_days`. Don't delete on a shrug.

If there are more than about eight candidates, show the oldest eight and say how many more there are; do the rest another day.

## Rules

- **Never delete without an explicit yes in this conversation.** Silence, a topic change, or a session ending all count as "later".
- **Don't editorialize.** No "you've been avoiding this" or "this seems important". They dropped it; you're asking whether that's still true.
- **Don't reopen the reason.** If they want to bring something back, they'll say so.

## Worked example

```text
Two things you dropped a while back — still want to let them go?
- #3 Call plumber · dropped 31 days ago · "will handle with bathroom remodel"
- #5 Set up the old laptop for the kids · dropped 45 days ago

Say "let them go", or name any to bring back.
```

**User:** "let them go, but bring the laptop one back actually"

**Skill:** deletes #3 from `dropped.md`, restores #5 to `open.md` under Home / Kids, notes both in today's journal.

```text
Deleted: #3 Call plumber
Restored: #5 Set up the old laptop for the kids (Home / Kids)
```
