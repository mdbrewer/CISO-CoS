# Set up the CISO Chief of Staff as a Claude.ai Project

This folder is a **ready-to-deploy Claude.ai Project**. Follow these steps to
stand it up on the standard Claude home page (claude.ai). Takes ~5 minutes.

## What's in this folder

```
claude-project/
├── PROJECT_INSTRUCTIONS.md      # paste into the Project's Instructions box
├── knowledge/
│   ├── 01-operating-model.md    # upload to Project knowledge
│   └── 02-specialist-bench.md   # upload to Project knowledge (the 19 lenses)
└── SETUP.md                     # this file
```

## Steps

1. **Create the Project.** Go to [claude.ai](https://claude.ai) → **Projects**
   → **Create Project**. Name it e.g. **"CISO Chief of Staff"** and give it a
   short description ("My security-leadership chief of staff and specialist
   bench").

2. **Add the instructions.** Open the Project → **Instructions** (sometimes
   labeled "Set instructions" or found in Project settings). Open
   `PROJECT_INSTRUCTIONS.md`, copy everything **between the two PASTE markers**,
   and paste it into the instructions box. Save.

3. **Add the knowledge.** In the Project, find **Project knowledge** (the "Add
   content" / files area) and upload BOTH files from `knowledge/`:
   - `01-operating-model.md`
   - `02-specialist-bench.md`

   > Tip: upload them as-is. The instructions reference `02-specialist-bench.md`
   > by name, so keep the filenames.

4. **Test it.** Start a new chat inside the Project and try:
   - *"I have an audit-committee update in two weeks. Draft the security
     section focused on ransomware readiness and how we compare to peers."*
   - *"We just got a breach-notification email from a CRO. Triage it, what do
     we do in the first 24 hours and what clocks may have started?"*
   - *"Where should our security investment go next year? Give me a prioritized
     roadmap and the board narrative."*

   You should get a BLUF answer that clearly draws on several specialist lenses
   and ends with a recommendation, tradeoff, and next step.

## Using it day to day

- **Always start with the Chief of Staff** (just chat in the Project). It
  decides which specialist lenses to apply.
- **Give feedback** ("too technical for the board", "always add a regulatory
  angle"). It will apply the change in-conversation and, for durable changes,
  draft the revised persona text for you to paste into `02-specialist-bench.md`.
- **Grow the bench.** Ask for a new specialist (e.g. "add a business-continuity
  / DR specialist"). It drafts a persona section in the bench format; paste it
  into `02-specialist-bench.md` and re-upload to update the Project knowledge.

## Keeping it in sync with the Claude Code version

This Project is generated from the Claude Code agents in `.claude/agents/`.
If you evolve the source agents, regenerate the bench file:

```
python3 scripts/build_project_bench.py
```

Then re-upload `knowledge/02-specialist-bench.md` to the Project.

The same script also runs a **drift guard** on the hand-maintained "Email /
inbox triage" play, which lives in both `.claude/agents/ciso-chief-of-staff.md`
and `PROJECT_INSTRUCTIONS.md`. If you edit the play in one surface but not the
other, the script exits non-zero and names the file and the missing element,
so the two copies can't silently diverge. (The two are intentionally worded
differently, sub-agents vs. lenses, so the guard checks the load-bearing
substance, not an exact match.)

### Automated checks

Both checks (bench freshness + triage-play drift) run automatically:

- **CI (GitHub Actions):** `.github/workflows/sync-check.yml` runs on every
  push and pull request. It regenerates the bench, fails if the triage play has
  drifted, and fails if the committed bench is stale. No setup required.
- **Local pre-commit hook (opt-in):** enable once per clone with
  `git config core.hooksPath .githooks`. The hook (`.githooks/pre-commit`) runs
  the same checks before each commit and tells you exactly what to fix (e.g.
  `git add claude-project/knowledge/02-specialist-bench.md`) if something is out
  of sync.

## Claude.ai vs. Claude Code: what's different

| | Claude Code (`.claude/agents/`) | This Claude.ai Project |
|---|---|---|
| Where you use it | IDE / CLI | claude.ai home page |
| Sub-agents | True parallel sub-agents | One assistant adopting specialist lenses |
| Growing the bench | Claude edits agent files directly | Claude drafts persona text; you paste & re-upload |
| Best for | Deep, tool-driven, parallel work | Fast, always-available executive thinking partner |

Same specialists, same guardrails, two delivery surfaces.
