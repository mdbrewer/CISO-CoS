# CISO CoS: Chief of Staff & Specialist Bench

A modular AI operating system for a world-class CISO. A **Chief of Staff** agent
is the single point of interaction; behind it sits an expandable bench of
**21 specialist sub-agents**, each an expert in a subset of the CISO role. The
Chief of Staff triages your requests, delegates to the right specialists,
synthesizes their work into one executive-ready answer, and creates or tunes
specialists as your needs evolve.

Built for a regulated biopharmaceutical context (patient data, clinical-trial
integrity, drug-discovery IP; HIPAA / GxP / 21 CFR Part 11 / GDPR), but the
patterns generalize to any industry.

## How it works

```
                        You (CISO)
                            |
                  ciso-chief-of-staff
        triage · delegate · synthesize · evolve the bench
                            |
   +----------+-------------+-------------+--------------+
   |          |             |             |              |
 Direction  Risk &        Defense      Build &        Communicate
            Compliance                 Protect         & Lead
```

You talk to the **Chief of Staff**. It decides which specialists to pull in,
runs them (in parallel when independent), and returns a single coherent answer,
not a pile of raw sub-agent output.

## The bench (21 specialists + orchestrator)

Specialists are grouped by function. Scopes are intentionally non-overlapping;
see each file's `description` for exact routing.

**Orchestrator**

| Agent | Role |
|---|---|
| `ciso-chief-of-staff` | Single front door: triage, delegate, synthesize, evolve the bench |

**Direction**

| Agent | Domain |
|---|---|
| `security-strategy` | Multi-year strategy, roadmap, operating model, maturity |
| `business-intelligence` | Threat landscape, peer benchmarking, metrics/KPIs |
| `budget-finance` | Budget, business cases, ROI, TCO, spend benchmarking |
| `ai-security-strategy` | AI-for-cyber strategy, market/vendor radar, latest capabilities |

**Risk & compliance**

| Agent | Domain |
|---|---|
| `grc-compliance` | Risk, frameworks, regulatory (HIPAA/GxP/GDPR/21 CFR 11) |
| `data-privacy` | Privacy program, GDPR/CCPA/HIPAA, DPIAs, subject rights |
| `third-party-risk` | Vendor & supply-chain risk, CRO/CDMO/SaaS, M&A diligence |
| `regulatory-affairs-liaison` | Security/GxP/FDA bridge, CSV/CSA, inspection readiness |

**Defense**

| Agent | Domain |
|---|---|
| `security-operations` | SOC, detection engineering, SIEM/SOAR/EDR, threat hunting |
| `threat-intelligence` | Adversary tracking, emerging threats, TTPs |
| `incident-response` | IR strategy, playbooks, crisis mgmt, breach decisions |
| `red-team-adversary` | Offensive testing, purple team, BAS, control validation |

**Build & protect**

| Agent | Domain |
|---|---|
| `security-architecture` | Reference architecture, zero trust, cloud, identity design |
| `identity-access` | IAM/IGA/PAM, MFA/passwordless, least privilege, non-human IDs |
| `cloud-security` | Cloud posture (CSPM/CNAPP), config, cloud IAM, SaaS (SSPM) |
| `application-security` | Secure SDLC/DevSecOps, SAST/DAST/SCA, API & product/SaMD |
| `ai-security` | AI/ML & GenAI security, model risk, AI governance |
| `ai-security-architecture` | Tactical AI-in-security architecture, best practices, diagrams |
| `ot-lab-security` | Lab instruments, OT/ICS (GMP), IoT/IoMT, cold-chain |

**Communicate & lead**

| Agent | Domain |
|---|---|
| `board-communications` | Board/exec reporting, translating security to business |
| `workforce-culture` | Awareness, human risk, org design, talent |

> **The AI trio.** `ai-security` secures the AI we build and use (governance,
> model risk). `ai-security-strategy` sets AI-for-cyber direction and watches
> the market. `ai-security-architecture` designs AI-in-security builds and
> produces diagrams.

All agents live in [`.claude/agents/`](.claude/agents/). Each is a Markdown
file with YAML frontmatter (`name`, `description`, `model`) plus a system prompt
defining its expertise.

## Repository layout

```
.claude/agents/            21 specialists + ciso-chief-of-staff + _templates/
claude-project/            ready-to-deploy Claude.ai Project package
  PROJECT_INSTRUCTIONS.md  paste into the Project's instructions box
  knowledge/               operating model + generated specialist bench
  SETUP.md                 step-by-step deployment guide
scripts/
  build_project_bench.py   regenerates the Project bench + runs the drift guard
.github/workflows/         sync-check CI
.githooks/                 opt-in pre-commit sync check
CLAUDE.md                  guidance & conventions for working in this repo
```

## Using it

1. **Start with the Chief of Staff.** Bring it any security-leadership ask:
   strategy, a board deck, an incident, a vendor review, "how do we compare?".
   It handles the routing.
2. **Give feedback.** "Too technical for the board", "always include a
   regulatory angle": the Chief of Staff tunes the relevant specialist so the
   improvement sticks.
3. **Grow the bench.** Ask for a new specialist and the Chief of Staff scaffolds
   it from the template and registers it in the roster.

### Built-in plays

- **Email / inbox triage.** Ask the Chief of Staff to triage your unread mail
  (requires a mail connector such as Microsoft 365 to be enabled in the
  session). It ranks by CISO-specific urgency, routes each item through the
  right specialist, and drafts replies. Defined in both the orchestrator and the
  Claude.ai Project instructions.

## Use it on claude.ai (Claude.ai Project package)

Prefer the standard Claude home page over the CLI? The
[`claude-project/`](claude-project/) folder packages the whole system as a
ready-to-deploy **Claude.ai Project**: paste the instructions, upload two
knowledge files, and chat with your Chief of Staff on claude.ai. See
[`claude-project/SETUP.md`](claude-project/SETUP.md).

Because a Claude.ai Project is a single assistant (not parallel sub-agents),
there the Chief of Staff *consults* specialist lenses from the knowledge file
and synthesizes one answer. Same specialists, same guardrails, two delivery
surfaces.

## Keeping the two surfaces in sync

The Project's specialist bench (`claude-project/knowledge/02-specialist-bench.md`)
is generated from the source agents in `.claude/agents/`:

```
python3 scripts/build_project_bench.py
```

The same script runs a **drift guard** on the hand-maintained email-triage play
(which lives in both the orchestrator and the Project instructions) and fails if
the two copies diverge. Both checks are automated:

- **CI:** `.github/workflows/sync-check.yml` runs on every push and pull request
  (regenerates the bench, fails on drift or a stale bench).
- **Local (opt-in):** enable the pre-commit hook with
  `git config core.hooksPath .githooks`.

## Extending the bench

1. Copy [`.claude/agents/_templates/specialist.md`](.claude/agents/_templates/specialist.md)
   to `.claude/agents/<name>.md`.
2. Fill in a unique `name`, a precise routing `description`, and the domain
   expertise. Keep scope non-overlapping with existing specialists.
3. Register it in the roster in `ciso-chief-of-staff.md`, this README, and the
   Project operating-model roster, then rerun `build_project_bench.py`.

Candidate future specialists (not yet built): `m-and-a-security`,
`resilience-bcdr`, `insider-threat`, `physical-security`, `crisis-comms-pr`,
`legal-ediscovery`, `quantum-crypto`.

## Design principles

- **One front door.** You interact with one agent; complexity lives behind it.
- **Specialists stay narrow and deep.** Non-overlapping scopes, real expertise.
- **Business-first.** Every answer ties to patient safety, IP, regulatory
  standing, or dollars.
- **Honest by construction.** Agents never fabricate metrics, audit results, or
  legal certainty; they say what they don't know and route decisions needing
  human sign-off (Legal, Regulatory Affairs, executives) accordingly.
- **The bench evolves.** The Chief of Staff continuously creates, tunes, and
  retires specialists based on your feedback.

> These agents are decision-support and thinking partners, not a system of
> record or a substitute for legal counsel. Ground-truth data (GRC platform,
> SIEM, audit results) and binding decisions stay with the humans and systems
> that own them.
