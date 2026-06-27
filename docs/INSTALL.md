# Manual Installation

CodeFlowLens can be installed as a native skill where the tool supports skills, or as project instructions where the tool supports rule files.

## OpenAI Codex

Codex discovers user skills from `~/.agents/skills`.

```bash
cd codeflowlens
mkdir -p ~/.agents/skills
cp -R skill/codeflowlens ~/.agents/skills/codeflowlens
```

Restart Codex if `$codeflowlens` does not appear after copying.

For a repository-scoped install:

```bash
cd /path/to/your/project
mkdir -p .agents/skills
cp -R /path/to/codeflowlens/skill/codeflowlens .agents/skills/codeflowlens
```

Use it:

```text
Use $codeflowlens to create an interactive sequence diagram for this flow.
```

## Claude Code And Claude Custom Skills

For Claude environments that support local custom skills, copy the skill folder into the local skills directory:

```bash
mkdir -p ~/.claude/skills
cp -R skill/codeflowlens ~/.claude/skills/codeflowlens
```

If your Claude environment uses uploaded custom skills, zip the contents of `skill/codeflowlens` so the archive contains `SKILL.md` at the skill root:

```bash
cd skill/codeflowlens
zip -r ../../codeflowlens-skill.zip .
```

If your Claude Code setup does not auto-discover local skills, reference the skill directly in the prompt:

```text
Use the CodeFlowLens skill at /path/to/codeflowlens/skill/codeflowlens/SKILL.md.
Create a self-contained interactive HTML sequence diagram and use the bundled template asset.
```

## Cursor

Cursor uses project rules and `AGENTS.md` instructions. CodeFlowLens ships both adapters.

```bash
cd /path/to/your/project
mkdir -p .cursor/rules
cp /path/to/codeflowlens/adapters/cursor/.cursor/rules/codeflowlens.mdc .cursor/rules/codeflowlens.mdc
```

If the project has no `AGENTS.md`, copy the generic adapter:

```bash
test -f AGENTS.md \
  && echo "Merge /path/to/codeflowlens/adapters/agents/AGENTS.md into the existing AGENTS.md" \
  || cp /path/to/codeflowlens/adapters/agents/AGENTS.md AGENTS.md
```

If the project already has `AGENTS.md`, merge or append the CodeFlowLens section after reviewing both files.

Keep the CodeFlowLens repository available on disk, then ask Cursor:

```text
Use the CodeFlowLens rule to create an interactive HTML sequence diagram.
Use /path/to/codeflowlens/skill/codeflowlens/assets/strict-sequence-viewer-template.html as the scaffold.
```

## Gemini CLI

Gemini CLI loads project context from `GEMINI.md`.

```bash
cd /path/to/your/project
test -f GEMINI.md \
  && echo "Merge /path/to/codeflowlens/adapters/gemini/GEMINI.md into the existing GEMINI.md" \
  || cp /path/to/codeflowlens/adapters/gemini/GEMINI.md GEMINI.md
```

If the project already has `GEMINI.md`, merge or append the CodeFlowLens section after reviewing both files.

Then ask Gemini CLI:

```text
Use CodeFlowLens to create an interactive HTML sequence diagram.
Use /path/to/codeflowlens/skill/codeflowlens/assets/strict-sequence-viewer-template.html as the scaffold.
Validate it in a browser and report alignment deltas.
```

## Other Agents

For tools without native skill discovery, use the generic adapter:

```bash
cd /path/to/your/project
test -f AGENTS.md \
  && echo "Merge /path/to/codeflowlens/adapters/agents/AGENTS.md into the existing AGENTS.md" \
  || cp /path/to/codeflowlens/adapters/agents/AGENTS.md AGENTS.md
```

Then include the skill path in the prompt:

```text
Use CodeFlowLens from /path/to/codeflowlens/skill/codeflowlens/SKILL.md.
Build a self-contained interactive HTML sequence diagram.
Validate it in a browser and report alignment deltas.
```

## Verify Installation

Ask the agent for a smoke test:

```text
Use CodeFlowLens to create a tiny sequence diagram with Browser, API, and Postgres.
Save it as codeflowlens-smoke.html.
Validate at 1440x900 and 1280x800.
Report maxActorToLifelineDelta and maxMessageEndpointDelta.
```

Expected behavior:

- the agent reads `SKILL.md`;
- the agent uses `assets/strict-sequence-viewer-template.html`;
- the generated HTML is self-contained;
- browser validation reports max deltas at or below `1px`;
- hover and click highlights affect only first-degree related actors, cards, lifelines, and flows.
