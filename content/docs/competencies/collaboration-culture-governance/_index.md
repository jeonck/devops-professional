---
title: "Collaboration, Culture & Governance"
linkTitle: "Collaboration & Governance"
weight: 130
---

## Why This Matters in 2026

This is the connective-tissue competency: it links development, security, operations, and finance into one operating system instead of four separate ones. Without it, the other twelve competencies in this framework are just local optimizations — a great CI/CD pipeline on one team, a clean observability stack on another, none of it transferring beyond the people who built it. By 2026, the organizations that scale DevOps practice are the ones that turned individual habits into shared mechanisms: a DORA-informed data culture that makes performance legible across teams, Architecture Decision Records (ADRs) that make technical reasoning durable and reusable, and a blameless postmortem culture that turns failure into organizational learning instead of individual blame. This is the competency that decides whether good engineering practice is a personality trait of one team or a property of the organization.

{{< callout type="info" >}}
A practice that only lives in your head or your team's Slack channel doesn't scale. If you can't point to a document, a model, or a metric that other teams adopted without you in the room, you haven't operated this competency yet — you've just been a good teammate.
{{< /callout >}}

## Core Skills & Tools

- Building a DORA-metrics-informed engineering culture that makes delivery and stability data part of normal team conversation, not just a leadership report
- Authoring and driving adoption of Architecture Decision Records (ADRs) using lightweight formats (e.g. Michael Nygard's template, MADR) stored alongside code
- Designing blameless postmortem culture: facilitation practices, incident review templates, and psychological-safety norms that produce honest root-cause analysis
- Defining RACI (Responsible/Accountable/Consulted/Informed) models for cross-team operational processes such as incident response, change approval, or on-call escalation
- Authoring engineering guidelines and standards documents (coding standards, service ownership requirements, security baselines) intended for org-wide use
- Creating training and enablement materials (runbooks, onboarding guides, internal workshops) that transfer tacit knowledge into reusable assets
- Preparing for and responding to internal and external audits (SOC 2, ISO 27001, internal compliance reviews) as a cross-functional coordination exercise

## What You Must Have Operated

- Authored an ADR, RFC, or engineering guideline that was adopted and followed by at least one team beyond your own, without you personally enforcing it
- Designed a RACI model or operating model for a cross-team process — for example, an incident response workflow spanning development, security, and operations — and had it formally adopted
- Measurably reduced handoff friction or wait time between two previously siloed teams (e.g. development and security) by changing the process or interface between them, not just the people
- Led or co-led a real audit response (security, compliance, or internal governance review) that required pulling evidence and context from multiple teams under a deadline

## Evidence You Can Show

| Artifact | What it proves |
|---|---|
| ADR repository with adoption history | You can document and propagate technical decisions in a way that outlives a single conversation |
| RACI matrix document for a cross-team process | You can design accountability structures that survive reorganizations and turnover |
| Engineering guideline/standards document | You can codify practice into something other teams can self-serve from |
| Training/enablement materials (runbooks, workshop decks) | You can transfer knowledge at scale instead of being a single point of failure |
| Audit response time report | You can coordinate evidence collection across teams under real deadline pressure |

## KPIs & Metrics

- **Handoff/wait time reduction** between teams on a defined process (e.g. security review turnaround, change approval lead time)
- **Standard/guideline adoption rate** — percentage of teams or services conforming to a published standard
- **Audit response time** — time from audit request to evidence package delivered
- **Postmortem action-item completion rate** — percentage of agreed follow-up actions closed within a set window
- Supporting metrics: ADR proposal-to-decision cycle time, onboarding time-to-productivity using enablement materials, recurring incident rate on processes covered by a RACI model

## Maturity Levels

| Level | What you can demonstrate |
|---|---|
| **Associate** | Follows existing ADRs and engineering standards correctly; participates constructively in blameless postmortems |
| **Professional** | Has authored at least one ADR or guideline adopted by their own team; runs postmortems using an established template |
| **Senior** | Has authored guidelines, RACI models, or training materials adopted by multiple teams beyond their own; has measurably reduced cross-team friction on a real process |
| **Principal** | Owns the operating model and governance standards at the org level, with adoption measured and tracked across teams, and is the escalation point for cross-functional audits |

## Proof Statements You Can Use

- "Authored an incident-response RACI model spanning development, security, and operations, cutting average incident triage handoff time from 45 minutes to 8 minutes."
- "Wrote and drove adoption of an ADR process now followed by 9 engineering teams, reducing repeated architectural debates by an estimated 70%."
- "Redesigned the security review workflow between development and security teams, cutting average review wait time from 6 business days to 1."
- "Led evidence coordination for a SOC 2 Type II audit across 5 teams, reducing total audit response time from 4 weeks to 9 business days."
