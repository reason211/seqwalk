# ExactSeq: Browser-Validated Sequence Diagrams for AI Coding Agents

ExactSeq is an Agent Skill and self-contained HTML template that helps Claude Code, OpenAI Codex, Cursor, Gemini CLI, and similar tools generate interactive sequence diagrams with measured lifelines, exact message endpoints, sticky participants, first-degree highlighting, store/cache emphasis, and browser validation.

AI agents are good at explaining systems, but their hand-written diagrams often drift: labels collide, lifelines miss their actors, hover states over-highlight, and the result looks plausible until somebody scrolls. ExactSeq turns that loose output into a constrained, testable artifact: one self-contained HTML file that behaves like a real interactive sequence viewer.

## Why ExactSeq

- **Exact alignment:** message lines are measured from real DOM lifeline centers, not guessed from grid spans.
- **Agent-ready instructions:** a focused `SKILL.md` tells coding agents how to create and validate the viewer.
- **Self-contained output:** the template runs as plain HTML, CSS, and JavaScript.
- **Readable interaction:** hover, focus, and click highlights stay first-degree so users can follow one path at a time.
- **Store-aware diagrams:** databases, queues, caches, files, result stores, and audit logs receive semantic emphasis.
- **Cross-tool adapters:** install as a native skill where supported, or use the Cursor and `AGENTS.md` adapters.

## Repository Layout

```text
exactseq/
  skill/exactseq/                       # Native skill bundle
    SKILL.md
    agents/openai.yaml
    assets/strict-sequence-viewer-template.html
  adapters/
    cursor/.cursor/rules/exactseq.mdc   # Cursor project rule adapter
    gemini/GEMINI.md                     # Gemini CLI context adapter
    agents/AGENTS.md                    # Generic agent instruction adapter
  docs/INSTALL.md                       # Detailed manual installation guide
  examples/prompt.md                    # Starter prompts
  scripts/validate_skill.py             # Zero-dependency validation helper
```

## Quick Install

From a local clone or downloaded copy of this repository, run commands from the repository root:

```bash
cd exactseq
```

Install for OpenAI Codex:

```bash
mkdir -p ~/.agents/skills
cp -R skill/exactseq ~/.agents/skills/exactseq
```

Install for a Codex project only:

```bash
mkdir -p /path/to/your/project/.agents/skills
cp -R skill/exactseq /path/to/your/project/.agents/skills/exactseq
```

Install for Claude Code or Claude environments that support local custom skills:

```bash
mkdir -p ~/.claude/skills
cp -R skill/exactseq ~/.claude/skills/exactseq
```

Install the Cursor adapter into a project:

```bash
mkdir -p /path/to/your/project/.cursor/rules
cp adapters/cursor/.cursor/rules/exactseq.mdc /path/to/your/project/.cursor/rules/exactseq.mdc
```

Merge `adapters/agents/AGENTS.md` into the target project's `AGENTS.md` when that project uses agent instruction files. Do not overwrite existing project instructions without reviewing them.

Install the Gemini CLI adapter into a project:

```bash
test -f /path/to/your/project/GEMINI.md \
  && echo "Merge adapters/gemini/GEMINI.md into the existing GEMINI.md" \
  || cp adapters/gemini/GEMINI.md /path/to/your/project/GEMINI.md
```

Merge the file instead of replacing it when the project already has a `GEMINI.md`.

See [docs/INSTALL.md](docs/INSTALL.md) for tool-specific details, verification steps, and fallback installs.

## Usage

Ask your agent:

```text
Use ExactSeq to create a self-contained interactive HTML sequence diagram for this architecture.
Actors: Browser, API Gateway, Auth Service, Postgres, Redis.
Show request flow, cache hit/miss behavior, DB fallback, and audit logging.
Validate alignment in a browser and report max deltas.
```

For tools with native skill support, invoke:

```text
Use $exactseq to build an interactive sequence diagram for ...
```

## What The Agent Should Produce

ExactSeq guides the agent toward an HTML artifact with:

- an ordered actor list;
- sticky participant rail;
- dashed lifelines aligned to actor centers;
- explicit `data-from` and `data-to` message lines;
- stable event card ids and actor mappings;
- scroll-aware active-step highlights;
- first-degree hover/focus/click locks;
- semantic store/cache highlighting;
- browser-side alignment validation.

## Support The Maintainer

ExactSeq is free MIT-licensed software built to solve a real developer annoyance: AI agents can explain architecture, but their generated diagrams often need hours of cleanup. If this project saves you that time, makes your documentation clearer, or helps your agent produce something you can actually share, optional tips help fund ongoing maintenance.

Direct support buys time for cross-browser testing, accessibility work, better adapters, and new diagram templates while keeping the project open. Tips do not buy priority support, future features, tokens, investment upside, or any guaranteed service.

<details>
<summary>Wallet addresses</summary>

**EVM-compatible chains**  
`0xF459A9D96cAC23fABb3F44E1F4508da7fe24c2f7`

**Solana**  
`8Q1dAVExNT62TcKowbrDL2DpnDyex77Xw1o9sJ9fAy6e`

**Tron**  
`TMqU8d1vh7mqjGSPLVMi7MXrCmHX4s6Gj2`

</details>

If ExactSeq helped you ship a clearer architecture doc, even a small tip is meaningful.

## GitHub Topics

Suggested repository topics:

```text
sequence-diagram
interactive-diagram
html-template
agent-skills
ai-coding-agents
claude-code
openai-codex
cursor
gemini-cli
developer-tools
architecture-diagrams
```

## License

MIT. See [LICENSE](LICENSE).
