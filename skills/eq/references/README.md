# Book references for `eq`

This folder holds short, action-oriented notes from books Zane has read. The main `SKILL.md` loads one of these only when:

- Zane names the framework explicitly, or
- The situation maps cleanly onto the book's frame, or
- The general guidance has stalled and a sharper frame would help.

## How to add a new reference

Create a new file named after the book (kebab-case, e.g. `nonviolent-communication.md`, `crucial-conversations.md`, `never-split-the-difference.md`). Keep each one tight — roughly under 150 lines. The point isn't to summarize the book; it's to give Claude the few moves from that book that actually change how a message gets drafted.

A good reference file has:

1. **One-paragraph posture** — what worldview the book brings (e.g. NVC: every action is an attempt to meet a universal human need).
2. **3–6 concrete moves** — the actual things to do differently. Phrasing patterns, question stems, sequence of steps.
3. **A worked example** — one short before/after showing the move in action on a realistic situation.
4. **When this frame is the wrong tool** — knowing the limits prevents over-application.

## Stub: how to ask Claude to help build a reference

When you want to add a book, tell Claude:

> "Add a reference file for [book] to the eq skill. I've read it; here are the moves I actually want to keep using: [list]. Here's a real situation where it would have helped: [story]. Write it in the format described in `skills/eq/references/README.md`."

Claude will draft the file. Review it, prune anything that doesn't match how you actually use the book, and commit.
