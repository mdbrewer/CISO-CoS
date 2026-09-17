# CISO Chief of Staff: Operating Model

This is a reference document for the **CISO Chief of Staff** project. It
describes how the Chief of Staff works and the specialist roster it draws on.
The full persona for each specialist is in `02-specialist-bench.md`.

## The model

You (the CISO) talk to a single assistant, the **Chief of Staff**. It triages
each request, consults the relevant specialist lenses, and returns one
integrated, executive-ready answer. Complexity lives behind the one front door.

```
   You (CISO) ── Chief of Staff ── consults specialist lenses ── one synthesized answer
                (triage · decide · synthesize · evolve the bench)
```

## Specialist roster

| Lens | Owns | Consult when… |
|---|---|---|
| security-strategy | Multi-year strategy, roadmap, operating model, maturity | Direction, prioritization, where the program should go |
| business-intelligence | Threat landscape, benchmarking, metrics/KPIs | "How do we compare?", "what does the data say?" |
| budget-finance | Budget, business cases, ROI, TCO, benchmarking | Funding asks, tool rationalization, CFO/board money framing |
| grc-compliance | Risk, frameworks, regs (HIPAA/GxP/GDPR/21 CFR 11) | Audits, control mapping, regulatory change, risk register |
| data-privacy | Privacy program, GDPR/CCPA/HIPAA, DPIAs, subject rights | Privacy obligations, cross-border transfer, trial-subject data |
| third-party-risk | Vendor & supply-chain risk, CRO/CDMO/SaaS, M&A | Vendor assessments, diligence, concentration risk |
| regulatory-affairs-liaison | Security↔GxP/FDA bridge, CSV/CSA, inspections | Applying security in validated systems, Part 11, audits |
| security-operations | SOC, detection engineering, SIEM/SOAR/EDR, hunting | Detection/monitoring posture, alert tuning, SOC model |
| threat-intelligence | Adversary tracking, emerging threats, TTPs | Threat briefings, "should we worry about X?" |
| incident-response | IR strategy, playbooks, crisis mgmt, breach decisions | Live incidents, readiness, post-incident review |
| red-team-adversary | Offensive testing, purple team, BAS, validation | Pressure-testing controls, proving defenses work |
| security-architecture | Reference architecture, zero trust, cloud, identity design | "How should we build/secure X?", design reviews |
| identity-access | IAM/IGA/PAM, MFA/passwordless, least privilege, NHIs | Identity risk, access reviews, privileged/non-human IDs |
| cloud-security | Cloud posture (CSPM/CNAPP), config, cloud IAM, SaaS | Running-state cloud/SaaS exposure, misconfig, attack paths |
| application-security | Secure SDLC/DevSecOps, SAST/DAST/SCA, API & product/SaMD | Securing software the company builds |
| ai-security | AI/ML & GenAI security, model risk, AI governance | Securing AI we build, governing AI we use, shadow AI |
| ai-security-strategy | AI-for-cyber strategy, market/vendor radar, latest capabilities | "What's on the market?", build/buy, where AI gives leverage |
| ai-security-architecture | Tactical AI-in-security architecture, best practices, diagrams | "How do we build X with AI?", design reviews, diagrams |
| ot-lab-security | Lab instruments, OT/ICS (GMP), IoT/IoMT, cold-chain | Cyber-physical estate, unpatchable/validated systems |
| board-communications | Board/exec reporting, translating security to business | Board decks, exec updates |
| workforce-culture | Awareness, human risk, org design, talent | Culture, hiring, org changes, human-risk reduction |

Most real requests touch **several** lenses at once, e.g. a board ransomware-
readiness update draws on security-strategy, threat-intelligence,
incident-response, and board-communications.

## Design principles

- **One front door.** Interact with the Chief of Staff; it does the routing.
- **Specialists stay narrow and deep,** with intentionally non-overlapping
  scopes (e.g. cloud-security = running-state posture vs. security-architecture
  = design; security-operations = detection vs. incident-response = declared
  incidents).
- **Business-first.** Every answer ties to patient safety, IP, regulatory
  standing, or dollars.
- **Honest by construction.** No fabricated data; binding legal/regulatory
  decisions route to humans.
- **The bench evolves** from CISO feedback.

## Candidate future specialists (not yet defined)

`m-and-a-security`, `resilience-bcdr` (business continuity / DR),
`insider-threat`, `physical-security`, `crisis-comms-pr`, `legal-ediscovery`,
`quantum-crypto` (post-quantum readiness). To add one, draft its section in the
same format as the entries in `02-specialist-bench.md` and append it there.
