# CLAUDE.md: CISO Chief of Staff System

Guidance for Claude when working in this repository.

## User writing preferences (always apply)

- **Never use em dashes (the "—" character) in any material produced for the
  user.** This covers documents, slides, memos, emails, chat replies, and every
  other deliverable and format. Use commas, colons, parentheses, or reworded
  sentences instead. Applies to everything generated for Michael Brewer.

## What this project is

An AI operating system for a CISO, built as a **Chief of Staff orchestrator**
plus an expandable bench of **specialist sub-agents**. It targets a regulated
biopharmaceutical environment (patient data, clinical-trial integrity,
drug-discovery IP; HIPAA / GxP / 21 CFR Part 11 / GDPR). The agents are
decision-support: strategy, risk, compliance, threat intel, IR, architecture,
third-party risk, board comms, and workforce/culture.

## Repository layout

```
.claude/agents/
  ciso-chief-of-staff.md          # orchestrator & primary interface
  security-strategy.md            # specialists ↓
  business-intelligence.md
  grc-compliance.md
  threat-intelligence.md
  incident-response.md
  security-architecture.md
  third-party-risk.md
  board-communications.md
  workforce-culture.md
  security-operations.md
  identity-access.md
  cloud-security.md
  application-security.md
  data-privacy.md
  ai-security.md
  ai-security-strategy.md
  ai-security-architecture.md
  budget-finance.md
  ot-lab-security.md
  red-team-adversary.md
  regulatory-affairs-liaison.md
  _templates/specialist.md        # scaffold for new specialists
README.md                         # overview & usage
CLAUDE.md                         # this file
```

Specialists are grouped by function: **direction** (strategy, business-
intelligence, budget-finance, ai-security-strategy), **risk & compliance**
(grc-compliance, data-privacy, third-party-risk, regulatory-affairs-liaison),
**defense** (security-operations, threat-intelligence, incident-response,
red-team-adversary), **build & protect** (security-architecture,
identity-access, cloud-security, application-security, ai-security,
ai-security-architecture, ot-lab-security), and **communicate & lead**
(board-communications, workforce-culture). Scopes are intentionally
non-overlapping (see each file's `description`). Note the AI trio: `ai-security`
secures AI we build and use, `ai-security-strategy` sets AI-for-cyber direction
and market watch, and `ai-security-architecture` designs AI-in-security builds.

## Agent file contract

Each agent is Markdown with YAML frontmatter:

- `name`: unique kebab-case identifier
- `description`: WHEN to route to this agent (routing depends on it; keep it
  specific and non-overlapping with other agents)
- `model`: model tier (`opus` for these deep-reasoning roles)
- Body, the system prompt: role, core competencies, how it works, output
  standards.

## Conventions to preserve when editing

1. **The Chief of Staff is the single front door.** Users interact with it; it
   delegates to specialists and synthesizes. Don't collapse this into one mega-
   prompt.
2. **Specialists stay narrow and deep.** When adding one, ensure its scope does
   not overlap an existing specialist; if it does, tune the existing one
   instead.
3. **Keep the roster in sync.** Any new/removed specialist must be reflected in
   the roster table in `ciso-chief-of-staff.md` AND the table in `README.md`.
4. **Honesty guardrails are load-bearing.** Every specialist must keep its
   "never fabricate data / route legal & sign-off decisions to humans" rules.
   Preserve these when editing.
5. **Business-first framing.** Answers tie to patient safety, IP, regulatory
   standing, and dollars, not tooling for its own sake.
6. **BLUF everywhere.** Lead with the answer, then detail.

## Adding a specialist (the standard workflow)

1. Copy `.claude/agents/_templates/specialist.md` to `.claude/agents/<name>.md`.
2. Set a unique `name`, a precise routing `description`, and fill every
   `REPLACE`.
3. Register it in the roster table in `ciso-chief-of-staff.md` and `README.md`.
4. Note the addition so the bench has a running record.

## Tuning a specialist

Fold durable CISO feedback ("too technical for the board", "always include a
regulatory angle") into the relevant specialist's system prompt so the
improvement persists across sessions.

## Non-goals

- This is not a system of record. Do not treat agent output as authoritative
  data (that lives in the GRC platform, SIEM, etc.).
- Agents advise; they do not make binding legal/regulatory/notification
  decisions. Those route to Legal, Regulatory Affairs, and executives.
