# Review — progress and the quarterly check-in

Two jobs share this file because they read the same data: the on-demand **progress review** ("how am I doing?") and the **quarterly check-in** that refreshes stats and capabilities. The skill reminds the user about the quarterly one; it never runs it uninvited.

## Progress review (on demand)

Read `profile.md` goals, `progress.md`, and `log.md` since the last review date. Answer the question they asked in a short block:

- **Per goal**, one or two lines: where they started, where they are, the trend. Numbers from the store only. If a goal has no measurable anchor, say so and propose one.
- **Consistency**: sessions per week over the period versus what the profile says they intended. Stated, not judged.
- **What's working and what to change**: one or two concrete adjustments to the programming, tied to the evidence. "Pressing has stalled for four weeks while pulling progressed — switch the press to a rep-range wave" beats "keep it up".

No charts, no grades, no motivational wrap-up.

## Quarterly check-in

**When to raise it.** `next_review` in `profile.md` is today or earlier. Mention it once per session, after a workout is accepted or at the end of a debrief — never at the top of a check-in. If they say "later", drop it for the session.

**What to refresh.** Walk through in two or three short exchanges, defaults from the current profile so "same" is an answer:

1. **Stats** — current weight (and height if they track it). Dated line in the weight history.
2. **Capabilities** — re-anchor the two or three numbers from onboarding, plus anything new they can do. Compare to the last anchor in one line each.
3. **Limitations** — anything cleared, anything new. Remove cleared ones (keep a dated "cleared" note in the history); add new ones with scope.
4. **Equipment and schedule** — anything changed? A new gym, a lost pull-up bar, a different number of days.
5. **Goals** — met, still on, or replaced. A met goal moves to a dated "achieved" line; a replaced one is noted as such, not deleted.

Then run the progress review above for the quarter just ended, record the check-in as a dated `## Review` block at the bottom of `profile.md`, and set `next_review` to today plus three months.

## Worked example

**User:** "how am I doing on the pull-ups?"

**Skill:**

```text
Pull-ups: 6 clean at onboarding (Jun 12) → 9 on Sep 10. Goal is 10 by October — on track.
You've pulled 2×/week for 11 of the last 13 weeks. The two misses were the vacation week.
One change: the last three sessions were all 3×max. Switch to 5×5 with a pause at the top for two weeks, then retest.
```
