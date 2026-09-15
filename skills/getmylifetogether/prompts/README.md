# Prompts for `getmylifetogether`

These files are the skill's behavior, one per mode. They're in git on purpose: as you use the skill and notice it asking too much, clustering wrong, or nagging, edit the file for that mode, commit, and run `/plugin marketplace update zane-skills` (then `/reload-plugins`).

| File | Governs |
| --- | --- |
| [`capture.md`](capture.md) | How a recap or a new todo gets parsed and written to the store, and the once-a-day "any cool ideas?" question. |
| [`clarify.md`](clarify.md) | When a clarifying question is worth asking, and how to ask it. |
| [`briefing.md`](briefing.md) | What "what's on my list" looks like: clustering, ordering, what's hidden. |
| [`reactions.md`](reactions.md) | The vocabulary of quick reactions ("did that", "forget about that", "later") and what each one writes. |
| [`drop-review.md`](drop-review.md) | When and how to ask about deleting long-dropped items. |

## Conventions

- **Each file is loaded fresh when its mode starts.** The model does not carry a copy between sessions, so an edit takes effect the next time the mode runs after the plugin is updated.
- **`SKILL.md` invariants win.** A prompt can change *how* something is asked or shown; it can't make the skill invent items, delete without a yes, or resurface dropped things. If you want to change one of those, change `SKILL.md`.
- **Say why, not just what.** The model generalizes from reasoning better than from rules. "Don't ask about priority — the user will reorder at the briefing anyway" is more robust than "never ask about priority."
- **Keep each file short.** Under ~80 lines. If it's growing past that, the mode is probably doing two jobs.
- **One worked example per file.** A short "user said / skill wrote / skill said" is worth more than a paragraph of policy.

## Editing from inside a session

If you tell the skill mid-session "from now on, do X," it will do X for the rest of that session and tell you which file to change, with a suggested line. If you're in this repo when you say it, it can make the edit for you. Personal thresholds (stale days, drop-review days, area order) don't need a prompt edit — they live in `profile.md` in the memory store.
