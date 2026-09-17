#!/usr/bin/env python3
"""Generate the Claude.ai Project specialist-bench knowledge file from the
Claude Code agent definitions in .claude/agents/, and verify cross-surface
sync of the hand-maintained "Email / inbox triage" play.

This keeps the Claude.ai Project package in sync with the source-of-truth
agents. Run from the repo root:

    python3 scripts/build_project_bench.py

Then re-upload claude-project/knowledge/02-specialist-bench.md to the Project.

Exit code is non-zero if the triage-play drift check fails, so this can be used
in CI or a pre-commit hook.
"""
import os
import re
import sys
import pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
AGENTS_DIR = REPO / ".claude" / "agents"
OUT = REPO / "claude-project" / "knowledge" / "02-specialist-bench.md"

# --- Cross-surface drift guard for the "Email / inbox triage" play -----------
# The play lives, by hand, in two places that are intentionally NOT identical
# (Claude Code delegates to real sub-agents; the Project consults lenses):
COS_AGENT = AGENTS_DIR / "ciso-chief-of-staff.md"
PROJECT_INSTRUCTIONS = REPO / "claude-project" / "PROJECT_INSTRUCTIONS.md"
TRIAGE_HEADING = "## Play: Email / inbox triage"

# The load-bearing substance below MUST appear in both copies. Surface-specific
# wording (delegate to sub-agents vs. consult lenses) is deliberately excluded.
# If you change the play, update BOTH files and keep these invariants in sync.
TRIAGE_INVARIANTS = [
    "unread, last 7 days",
    "never",                        # never invent / never fabricate messages
    "invent messages",
    "security incident",
    "regulatory / legal",
    "notification clock",
    "board / executive",
    "third-party / vendor",
    "blocked on the ciso's decision",
    "read and draft only",
    "flag suspected phishing",
    "exfiltrate",
    "binding legal/regulatory",
    "draft reply in the ciso's voice",
]

# Functional ordering (excludes the orchestrator and the template).
ORDER = [
    # Direction
    "security-strategy", "business-intelligence", "budget-finance",
    "ai-security-strategy",
    # Risk & compliance
    "grc-compliance", "data-privacy", "third-party-risk",
    "regulatory-affairs-liaison",
    # Defense
    "security-operations", "threat-intelligence", "incident-response",
    "red-team-adversary",
    # Build & protect
    "security-architecture", "identity-access", "cloud-security",
    "application-security", "ai-security", "ai-security-architecture",
    "ot-lab-security",
    # Communicate & lead
    "board-communications", "workforce-culture",
]

HEADER = """# CISO Specialist Bench, Reference Personas

This document is the knowledge base for the **CISO Chief of Staff** project.
It defines the specialist lenses the Chief of Staff consults when answering.

In a Claude.ai Project there is a single assistant, not separate sub-agents, so
"consulting a specialist" means **adopting that specialist's expertise, method,
and output standards** from the relevant section below, usually several at once
and then synthesizing one integrated answer in the Chief of Staff's voice.

Each specialist below carries the same honesty guardrails: never fabricate
data, metrics, audit results, certifications, or legal certainty; state what is
unknown and what real input would sharpen the answer; and route binding legal,
regulatory, and notification decisions to the appropriate humans (Legal,
Privacy, Regulatory Affairs, executives).

---

"""


def parse(path):
    text = pathlib.Path(path).read_text()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise ValueError(f"No YAML frontmatter in {path}")
    fm, body = m.group(1), m.group(2).strip()
    desc = ""
    lines = fm.splitlines()
    i = 0
    while i < len(lines):
        if lines[i].startswith("description:"):
            i += 1
            buf = []
            while i < len(lines) and (lines[i].startswith("  ")
                                      or lines[i].strip() == ""):
                buf.append(lines[i].strip())
                i += 1
            desc = " ".join(b for b in buf if b)
            break
        i += 1
    return re.sub(r"\s+", " ", desc).strip(), body


def demote(body):
    """Demote ATX headings by two levels so specialist bodies nest under H2."""
    out = []
    for line in body.splitlines():
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            level = min(len(m.group(1)) + 2, 6)
            out.append("#" * level + " " + m.group(2))
        else:
            out.append(line)
    return "\n".join(out)


def main():
    sections = []
    for name in ORDER:
        path = AGENTS_DIR / f"{name}.md"
        desc, body = parse(path)
        title_m = re.search(r"^#\s+(.*)$", body, re.M)
        title = title_m.group(1).strip() if title_m else name
        body_wo = re.sub(r"^#\s+.*$", "", body, count=1, flags=re.M).strip()
        sections.append(
            f"## {title}\n\n*Agent id: `{name}`*\n\n"
            f"**Consult this lens when:** {desc}\n\n{demote(body_wo)}"
        )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(HEADER + "\n\n---\n\n".join(sections) + "\n")
    print(f"Wrote {OUT.relative_to(REPO)} ({len(sections)} specialists)")


def _extract_section(text, heading):
    """Return the body of the section starting at `heading`, up to the next
    top-level (## ) heading or the PASTE marker, or None if absent."""
    start = text.find(heading)
    if start == -1:
        return None
    rest = text[start + len(heading):]
    end = len(rest)
    for marker in (re.search(r"^## ", rest, re.M),):
        if marker:
            end = min(end, marker.start())
    paste = rest.find("PASTE ABOVE THIS LINE")
    if paste != -1:
        end = min(end, paste)
    return rest[:end]


def check_triage_sync():
    """Flag drift between the two hand-maintained triage-play sections.

    Returns a list of human-readable problem strings (empty == in sync).
    """
    problems = []
    files = {
        COS_AGENT.relative_to(REPO): COS_AGENT,
        PROJECT_INSTRUCTIONS.relative_to(REPO): PROJECT_INSTRUCTIONS,
    }
    for rel, path in files.items():
        if not path.exists():
            problems.append(f"{rel}: file not found")
            continue
        section = _extract_section(path.read_text(), TRIAGE_HEADING)
        if section is None:
            problems.append(f"{rel}: missing '{TRIAGE_HEADING}' section")
            continue
        norm = re.sub(r"\s+", " ", section.lower())
        missing = [inv for inv in TRIAGE_INVARIANTS if inv.lower() not in norm]
        if missing:
            problems.append(
                f"{rel}: triage play missing required element(s): "
                + ", ".join(f'"{m}"' for m in missing)
            )
    return problems


if __name__ == "__main__":
    main()
    drift = check_triage_sync()
    if drift:
        print("\nTRIAGE-PLAY DRIFT DETECTED:", file=sys.stderr)
        for p in drift:
            print(f"  - {p}", file=sys.stderr)
        print(
            "\nThe 'Email / inbox triage' play must stay in sync across both "
            "surfaces.\nUpdate both files (and TRIAGE_INVARIANTS if the play "
            "itself changed).",
            file=sys.stderr,
        )
        sys.exit(1)
    print("Triage-play sync check: OK (both surfaces in sync)")
