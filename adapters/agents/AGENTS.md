# ExactSeq Project Instructions

Use ExactSeq when the user asks for an interactive sequence diagram, architecture flow walkthrough, swimlane timeline, process map, or browser-rendered HTML diagram.

## ExactSeq Skill Source

Primary skill folder:

```text
skill/exactseq/
```

If this adapter is copied into another project, keep a local copy of the ExactSeq repository and reference:

```text
/path/to/exactseq/skill/exactseq/SKILL.md
```

Use the bundled scaffold for new diagrams:

```text
/path/to/exactseq/skill/exactseq/assets/strict-sequence-viewer-template.html
```

## Output Rules

- Produce a self-contained HTML file unless the user requests a different packaging format.
- Define ordered actors and render participants, lifelines, cards, and flows from explicit data.
- Align lifelines to participant centers and message endpoints to lifeline centers using measured DOM geometry.
- Keep card and participant hover/click relationships first-degree only.
- Highlight stores, caches, queues, files, audit logs, and result stores semantically.
- Validate the rendered HTML in a browser when possible.
- Report viewport sizes and maximum alignment deltas before claiming the artifact is ready.
