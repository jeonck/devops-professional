---
title: "Software Delivery Performance & DORA Metrics"
linkTitle: "Delivery Performance & DORA"
weight: 10
---

## Why This Matters in 2026

The starting point for proving DevOps competency is no longer "which tools have you used" — it's **can you explain your impact in numbers**. The [DORA](https://dora.dev) (DevOps Research and Assessment) program, now run by Google Cloud, remains the industry's reference model for measuring software delivery performance. Every other competency in this framework — CI/CD, GitOps, platform engineering, observability — ultimately has to show up as movement in these four metrics. A professional who can't tie their work to delivery performance numbers is describing activity, not impact.

{{< callout type="info" >}}
DORA metrics are the common language hiring managers, VPs of Engineering, and auditors already use to compare teams. Speaking in this language is the fastest way to make your experience legible to someone who has never seen your stack.
{{< /callout >}}

## Core Skills & Tools

- Defining and instrumenting the four key metrics: **Deployment Frequency**, **Lead Time for Changes**, **Change Failure Rate**, **Time to Restore Service (MTTR)**
- Building delivery dashboards from CI/CD, VCS, and incident data (e.g. Sleuth, LinearB, Apache DevLake, Faros AI, or homegrown pipelines on top of GitHub/GitLab APIs)
- Distinguishing **batch size** and **work-in-progress** as levers, not just outcomes
- Connecting delivery metrics to business outcomes (revenue impact of outages, cost of slow releases)
- Running blameless retrospectives that turn metric regressions into concrete process changes
- Understanding the 2023–2025 DORA findings on platform engineering and AI-assisted delivery as context for *why* an organization invests in the other competencies in this framework

## What You Must Have Operated

- A delivery pipeline instrumented well enough to calculate all four DORA metrics without manual log-digging
- At least one **before/after** transformation: a team or service whose deployment cadence, lead time, or failure rate you measurably changed
- A recurring reporting cadence (weekly/monthly) that kept delivery performance visible to engineering leadership

## Evidence You Can Show

| Artifact | What it proves |
|---|---|
| DORA metrics dashboard (screenshot + methodology doc) | You can instrument and interpret delivery performance, not just discuss it abstractly |
| Deployment lead-time trend report | You can quantify the effect of a specific intervention (e.g., trunk-based development, smaller PRs) |
| Post-incident analysis tied to MTTR improvement | You connect incident response work back to a delivery metric |
| Quarterly engineering performance review deck | You can communicate delivery health to non-engineering stakeholders |

## KPIs & Metrics

- **Deployment Frequency** — how often code ships to production (elite: on-demand, multiple times per day)
- **Lead Time for Changes** — commit to production time (elite: under one hour)
- **Change Failure Rate** — percentage of deployments causing a degradation or rollback (elite: 0–15%)
- **MTTR (Time to Restore Service)** — time to recover from a production incident (elite: under one hour)
- Supporting metrics: PR cycle time, batch size (lines/files per change), rollback rate, deploy approval wait time

## Maturity Levels

| Level | What you can demonstrate |
|---|---|
| **Associate** | Knows the four DORA metrics and can read them off an existing dashboard; understands why each one matters |
| **Professional** | Has instrumented DORA metrics for at least one team/service from raw pipeline and incident data |
| **Senior** | Has driven a measurable, sustained improvement in at least two of the four metrics across a team or org unit |
| **Principal** | Has established DORA-based reporting as an org-wide practice, tying it to investment decisions (platform engineering, tooling, headcount) |

## Proof Statements You Can Use

- "Moved a team from weekly manual releases to 10+ automated deploys/day by reducing batch size and adding progressive delivery gates."
- "Reduced average incident recovery time (MTTR) from 90 minutes to 18 minutes through improved alerting and automated rollback."
- "Cut change failure rate from 12% to 3% by introducing mandatory canary analysis before full rollout."
- "Built a DORA metrics dashboard adopted by 6 teams, used in quarterly engineering reviews to prioritize platform investment."
