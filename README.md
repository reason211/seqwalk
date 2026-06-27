# ExactSeq

**Understand AI-written code faster with interactive HTML sequence diagrams.**

Modern codebases are increasingly written or changed by AI agents. That makes code review harder: the code may work, but the execution flow is not always obvious. ExactSeq helps you ask an AI coding tool to turn code paths into an easy-to-read HTML sequence diagram, so you can quickly understand what runs, in what order, and where data moves.

ExactSeq works as an Agent Skill and template for Claude Code, OpenAI Codex, Cursor, Gemini CLI, and similar tools.

## What It Does

- Generates a self-contained HTML sequence diagram for a code flow.
- Shows services, functions, stores, queues, caches, and files as participants.
- Makes long flows easier to review with sticky participants and interactive highlights.
- Keeps message lines aligned and validates the result in a browser.
- Helps humans review, debug, and explain AI-generated code.

## Install

From a local clone or downloaded copy:

```bash
cd exactseq
```

Codex user install:

```bash
mkdir -p ~/.agents/skills
cp -R skill/exactseq ~/.agents/skills/exactseq
```

Codex project install:

```bash
mkdir -p /path/to/project/.agents/skills
cp -R skill/exactseq /path/to/project/.agents/skills/exactseq
```

Claude local skill install:

```bash
mkdir -p ~/.claude/skills
cp -R skill/exactseq ~/.claude/skills/exactseq
```

Cursor rule install:

```bash
mkdir -p /path/to/project/.cursor/rules
cp adapters/cursor/.cursor/rules/exactseq.mdc /path/to/project/.cursor/rules/exactseq.mdc
```

Gemini CLI adapter:

```bash
cp adapters/gemini/GEMINI.md /path/to/project/GEMINI.md
```

If the target project already has `AGENTS.md` or `GEMINI.md`, merge the ExactSeq instructions instead of replacing the file.

Detailed install notes: [docs/INSTALL.md](docs/INSTALL.md).

## Usage

Ask your agent:

```text
Use ExactSeq to inspect this code path and create an interactive HTML sequence diagram.
Focus on what calls what, where data is read or written, and what a reviewer should verify.
Validate the generated HTML in a browser and report alignment deltas.
```

For native skill tools:

```text
Use $exactseq to diagram this execution flow.
```

## Repository Layout

```text
skill/exactseq/                       # Native skill bundle
adapters/cursor/.cursor/rules/        # Cursor rule
adapters/gemini/GEMINI.md             # Gemini CLI context
adapters/agents/AGENTS.md             # Generic agent instructions
docs/INSTALL.md                       # Manual install guide
examples/prompt.md                    # Example prompts
scripts/validate_skill.py             # Validation helper
```

## Support

ExactSeq is free MIT-licensed software. If it saves you time reviewing AI-written code or helps you understand a messy execution path faster, optional tips help fund maintenance, browser testing, and new templates.

<details>
<summary>Wallet addresses</summary>

**EVM-compatible chains**  
`0xF459A9D96cAC23fABb3F44E1F4508da7fe24c2f7`

**Solana**  
`8Q1dAVExNT62TcKowbrDL2DpnDyex77Xw1o9sJ9fAy6e`

**Tron**  
`TMqU8d1vh7mqjGSPLVMi7MXrCmHX4s6Gj2`

</details>

## Suggested Topics

```text
sequence-diagram
html-template
code-review
ai-coding-agents
agent-skills
claude-code
openai-codex
cursor
gemini-cli
developer-tools
```

## License

MIT. See [LICENSE](LICENSE).
