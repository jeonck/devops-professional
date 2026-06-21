---
title: "Incident Response, Resilience & Disaster Recovery"
linkTitle: "Incident Response & Resilience"
weight: 90
---

## Why This Matters in 2026

Real DevOps competency is rarely visible during steady-state operation — it is revealed the moment something breaks. Anyone can look capable when dashboards are green; the differentiator in 2026 is whether a person can drive a clean, repeatable recovery when they are not. Organizations have largely stopped accepting unverifiable claims of "zero downtime" and instead expect evidence of proactive resilience testing — chaos engineering, scheduled DR drills, fault injection — rather than purely reactive firefighting after the fact. The shift is from "we survived the incident" to "we already knew how the system would fail, because we tested it."

{{< callout type="info" >}}
A polished postmortem template means nothing without a trail of completed action items. The single strongest piece of evidence for this competency is a postmortem from six months ago whose fixes were actually shipped — not just written down.
{{< /callout >}}

## Core Skills & Tools

- On-call rotation design (scheduling, escalation policies, fatigue management) using tools like PagerDuty, Opsgenie, or Grafana OnCall
- Runbook authoring that is precise enough for someone outside the original team to execute under pressure
- Blameless postmortem facilitation: structuring a review around contributing factors and systemic fixes, not individual blame
- Disaster recovery scenario design and execution — region failover, data store restore, dependency-loss drills
- Chaos engineering and fault injection (e.g. Chaos Mesh, Gremlin, AWS Fault Injection Simulator, or custom latency/error injection harnesses)
- Designing automated recovery and self-healing systems (health-check-driven restarts, circuit breakers, automated failover)
- Defining RTO (Recovery Time Objective) and RPO (Recovery Point Objective) per service tier, and validating systems actually meet them

## What You Must Have Operated

- Served as on-call engineer or incident commander during a real production incident, not a tabletop simulation
- Authored postmortems whose findings led to concrete, tracked engineering fixes — and followed up to confirm they shipped
- Run at least one real disaster recovery drill or chaos engineering experiment against a production or production-like environment
- Maintained an on-call runbook set that was actually used — and revised — during live incidents, not written once and abandoned

## Evidence You Can Show

| Artifact | What it proves |
|---|---|
| Redacted postmortem document | You can diagnose root cause and contributing factors without assigning blame |
| DR drill report (scope, results, gaps found) | You can design and execute a recovery scenario, not just document a theoretical plan |
| Chaos experiment results and findings | You proactively probe for weaknesses instead of waiting for production to find them for you |
| On-call runbook set used in rotation | Your documentation survives contact with a real 3 a.m. incident |

## KPIs & Metrics

- **MTTR (Mean Time to Restore)** — average time from detection to service restoration
- **Recovery success rate** — percentage of DR drills or real failovers that met their target recovery criteria on the first attempt
- **RTO/RPO attainment rate** — percentage of services that actually meet their declared recovery objectives when tested
- **Postmortem action-item completion rate** — percentage of identified fixes closed within a defined window (e.g., 30/60/90 days)
- Supporting metrics: incident recurrence rate, time-to-detect, escalation accuracy, chaos experiments run per quarter

## Maturity Levels

| Level | What you can demonstrate |
|---|---|
| **Associate** | Can follow a runbook accurately during an incident and escalate appropriately when it doesn't cover the situation |
| **Professional** | Has acted as incident commander for a real production incident and authored a postmortem that led to at least one shipped fix |
| **Senior** | Has designed and run a disaster recovery drill or chaos experiment that uncovered a real gap, then closed it and re-validated |
| **Principal** | Owns an org-wide resilience strategy — DR tiers, RTO/RPO standards, and a recurring chaos engineering program — and continuously improves it based on drill and incident data |

## Proof Statements You Can Use

- "Served as incident commander for a Sev-1 outage, reducing MTTR from 65 minutes to 22 minutes by restructuring the escalation path."
- "Drove postmortem action items to a 95% completion rate within 60 days, eliminating 4 of the top 5 recurring incident causes."
- "Designed and executed a quarterly DR drill program that improved RTO attainment across 12 services from 58% to 91%."
- "Introduced a chaos engineering practice that surfaced a single point of failure in the payment pipeline before it caused a customer-facing outage."
