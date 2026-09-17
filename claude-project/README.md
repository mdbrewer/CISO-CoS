# CISO Chief of Staff: Claude.ai Project package

A ready-to-deploy packaging of the CISO Chief of Staff and its 19-specialist
bench as a **Claude.ai Project**, so you can use it on the standard Claude home
page (claude.ai) rather than only in Claude Code.

## Contents

| File | Purpose |
|---|---|
| `PROJECT_INSTRUCTIONS.md` | Paste into the Project's **Instructions** box (the Chief of Staff orchestrator, adapted for a single-assistant project). |
| `knowledge/01-operating-model.md` | Upload to **Project knowledge**: how the Chief of Staff works + the roster. |
| `knowledge/02-specialist-bench.md` | Upload to **Project knowledge**: the 21 specialist lenses (generated from `.claude/agents/`). |
| `SETUP.md` | Step-by-step deployment guide. |

## Quick start

See **`SETUP.md`**. In short: create a Project on claude.ai → paste
`PROJECT_INSTRUCTIONS.md` into the instructions box → upload both `knowledge/`
files → start chatting with your Chief of Staff.

## How this differs from the Claude Code version

In Claude Code, the specialists are **true parallel sub-agents**. A Claude.ai
Project is a **single assistant**, so here the Chief of Staff *consults*
specialist lenses (adopts their expertise from the knowledge file) and
synthesizes one answer. Same specialists, same honesty guardrails, two delivery
surfaces.

## Keeping in sync

`knowledge/02-specialist-bench.md` is generated from the source agents in
`.claude/agents/`. After changing an agent, regenerate and re-upload:

```
python3 scripts/build_project_bench.py
```
