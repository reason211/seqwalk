# SeqWalk Gemini CLI Instructions

Use SeqWalk when the user asks to understand code execution flow, review AI-written code, inspect what calls what, visualize data movement, or create a browser-rendered HTML sequence diagram.

## Skill Source

Keep a local copy of the SeqWalk repository and reference:

```text
/path/to/seqwalk/skill/seqwalk/SKILL.md
```

Use this scaffold for new diagrams:

```text
/path/to/seqwalk/skill/seqwalk/assets/strict-sequence-viewer-template.html
```

## Output Rules

- Produce a self-contained HTML file unless the user requests a different packaging format.
- Define ordered actors and render participants, lifelines, cards, and flows from explicit data.
- Align lifelines to participant centers and message endpoints to lifeline centers using measured DOM geometry.
- Keep card and participant hover/click relationships first-degree only.
- Highlight stores, caches, queues, files, audit logs, and result stores semantically.
- Validate the rendered HTML in a browser when possible.
- Report viewport sizes and maximum alignment deltas before claiming the artifact is ready.
