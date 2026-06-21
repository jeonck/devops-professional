---
title: "Coding & Scripting Proficiency"
linkTitle: "Coding & Scripting"
weight: 120
---

## Why This Matters in 2026

Platforms have absorbed more of the repetitive plumbing work, and AI coding assistants now draft a large share of the code that used to be written by hand — but the automation at the edges of every real system is still hand-written, and someone still has to own it. Python remains the lingua franca for automation, data plumbing, and internal tooling; Go remains the default for CLIs, Kubernetes controllers, and operators. What has changed is the leverage available to a single engineer: tools like Claude Code and GitHub Copilot can produce a working script or a first-draft controller in minutes. What hasn't changed — and has arguably gotten more important — is the engineering judgment to know whether that output is correct, maintainable, and safe to run against production. The bar for reviewing AI-generated infrastructure code is now higher than the bar for writing code used to be.

{{< callout type="info" >}}
The skill that separates a DevOps professional from someone who "can write a script" is not typing speed — it's the discipline to treat automation code with the same rigor as product code: version control, tests, and review, whether the first draft came from a human or an AI assistant.
{{< /callout >}}

## Core Skills & Tools

- **Python** for automation, data plumbing, glue scripts, and internal tooling (argparse/click/typer for CLIs, pytest for tests, type hints for maintainability)
- **Go** for building CLIs, Kubernetes controllers, and operators (client-go, controller-runtime, Cobra)
- Disciplined use of **AI coding assistants** (Claude Code, GitHub Copilot, and similar) as a force multiplier, not a replacement for review
- Writing tools that are **maintainable software**, not one-off throwaway scripts: clear interfaces, error handling, logging, and documentation
- Applying real software engineering practices — version control, automated tests, code review, semantic versioning — to operations and automation code, not just to application code
- Designing mandatory review/test gates specifically for AI-generated infrastructure and automation changes
- Refactoring and consolidating ad-hoc scripts into shared, owned tooling rather than letting them multiply unsupervised

## What You Must Have Operated

- Built and maintained an internal tool, CLI, or Kubernetes operator that is actually used by other engineers, with real users beyond yourself
- Used AI coding tools as part of a real engineering workflow with a documented review/test gate — not unreviewed AI output committed and shipped directly
- Refactored a "script graveyard" (a sprawl of undocumented, unversioned, single-author scripts) into properly tested, documented, and owned tooling
- Debugged a production incident caused by a defect in internal automation code, and fed that root cause back into the team's testing or review standards

## Evidence You Can Show

| Artifact | What it proves |
|---|---|
| Internal tool/CLI repository with tests, README, and CI pipeline | You build automation as real software, not disposable scripts |
| AI-assisted code review policy document | You've defined where and how AI-generated code is reviewed and gated before it touches production systems |
| Before/after report on automation maintenance burden or incident rate | You can quantify the cost of unmanaged scripts and the benefit of consolidating them |
| Kubernetes operator or controller source repository | You can extend the platform itself, not just consume it |

## KPIs & Metrics

- Number of internal users/adopters of a tool you built and maintain
- Defect rate in automation/tooling code (bugs per release or per 1,000 lines)
- Time saved per AI-assisted task (estimated hours before vs. after adoption)
- Percentage of automation/tooling code covered by automated tests
- Number of legacy ad-hoc scripts retired or consolidated into owned tooling
- Mean time to onboard a new contributor to an internal tool's codebase

## Maturity Levels

| Level | What you can demonstrate |
|---|---|
| **Associate** | Can write and debug scripts in Python or Go to automate a clearly defined task, with basic error handling |
| **Professional** | Has built a CLI or internal tool with tests and documentation that other engineers rely on; uses AI coding assistants productively with manual review of every change |
| **Senior** | Has built or substantially extended a Kubernetes controller/operator, or led the consolidation of a team's script graveyard into owned, tested tooling |
| **Principal** | Has established engineering standards for internal tooling and AI-assisted code review that are adopted org-wide, including required test coverage and gating for AI-generated infrastructure changes |

## Proof Statements You Can Use

- "Built and maintain a Python CLI used by 40+ engineers across 5 teams, cutting average environment setup time from 45 minutes to 6."
- "Refactored a 60-script automation graveyard into a single tested Go-based tool, reducing automation-related incidents by 70% over two quarters."
- "Designed the team's AI-assisted code review gate, requiring test coverage and human sign-off before any AI-generated infrastructure change merges, adopted by 8 squads."
- "Built a Kubernetes operator that automated a manual reconciliation process, saving an estimated 15 engineer-hours per week and eliminating a recurring class of config-drift incidents."
