# CodeFlowLens Project Instructions

Use CodeFlowLens when the user asks to understand code execution flow, review AI-written code, inspect what calls what, visualize data movement, or create a browser-rendered HTML sequence diagram.

## CodeFlowLens Skill Source

Primary skill folder:

```text
skill/codeflowlens/
```

If this adapter is copied into another project, keep a local copy of the CodeFlowLens repository and reference:

```text
/path/to/codeflowlens/skill/codeflowlens/SKILL.md
```

Use the bundled scaffold for new diagrams:

```text
/path/to/codeflowlens/skill/codeflowlens/assets/strict-sequence-viewer-template.html
```

## Output Rules

- Produce a self-contained HTML file unless the user requests a different packaging format.
- Define ordered actors and render participants, lifelines, cards, and flows from explicit data.
- Align lifelines to participant centers and message endpoints to lifeline centers using measured DOM geometry.
- Keep card and participant hover/click relationships first-degree only.
- Highlight stores, caches, queues, files, audit logs, and result stores semantically.
- Validate the rendered HTML in a browser when possible.
- Report viewport sizes and maximum alignment deltas before claiming the artifact is ready.
