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

## Field Cases

Real incident write-ups from [ICT Problem Notes](https://fieldcases.metacog.co.kr/problems/) that exercise this competency:

- [A 40-second downstream blip became a 25-minute outage that continued after the downstream recovered](https://fieldcases.metacog.co.kr/problems/a-40-second-blip-became-a-25-minute-outage)
- [Writes keep failing with "read-only transaction" long after the failover finished](https://fieldcases.metacog.co.kr/problems/writes-keep-failing-with-read-only-transaction-after-failover)
- [The nightly reconciliation ran twice and both runs logged success](https://fieldcases.metacog.co.kr/problems/the-nightly-reconciliation-ran-twice-and-both-runs-logged-success)
- [Intermittent 503s that hit the quiet endpoints and never the busy ones](https://fieldcases.metacog.co.kr/problems/intermittent-503s-only-on-the-quiet-endpoints)

**The mechanisms behind them** — [Retry amplification](https://fieldcases.metacog.co.kr/concepts/retry-amplification) · [Idle timeout ordering](https://fieldcases.metacog.co.kr/concepts/idle-timeout-ordering) · [Wall-clock schedules and DST](https://fieldcases.metacog.co.kr/concepts/wall-clock-schedules)

## Hands-On Labs

Step-by-step labs from [handson](https://handson.metacog.co.kr/#/notes) — install guides, runbooks and playbooks that were actually run, not just read:

- [Diagnosing CrashLoopBackOff — from exit code to cause](https://handson.metacog.co.kr/#/note/03-troubleshoot~pod-crashloopbackoff)

## Automation Case Studies

Industry patterns and incident write-ups from [IT Automation](https://automations.metacog.co.kr/docs/case-studies/) that show this competency at work across organizations:

- [Chaos Engineering as a Reliability Practice](https://automations.metacog.co.kr/docs/case-studies/chaos-engineering/)
- [Two Stacks, One Notification Layer](https://automations.metacog.co.kr/docs/case-studies/two-stacks-one-notification-layer/)

## Checklists

Run-before-you-ship lists from [IT Checklists](https://checklists.metacog.co.kr/docs/) — use them as the review gate behind the evidence above:

- [Incident Management](https://checklists.metacog.co.kr/docs/operations/incident-management/)
- [On-Call Handover](https://checklists.metacog.co.kr/docs/operations/on-call-handover/)
- [Postmortem](https://checklists.metacog.co.kr/docs/operations/postmortem/)
- [Backup and Recovery](https://checklists.metacog.co.kr/docs/operations/backup-and-recovery/)

## Reference Library

Background chapters, ready-to-fill documents and pipeline walkthroughs from the sibling sites — see the full [Reference Library](../../references) for everything else:

**Architecture Field Notes** — [Failure Modes: Timeouts, Breakers, Bulkheads](https://architectures.metacog.co.kr/docs/reliability/failure-modes/) · [Incident Response and Blameless Postmortems](https://architectures.metacog.co.kr/docs/reliability/incident-response/)

**Automation Playbook** — [Runbook Automation](https://automations.metacog.co.kr/docs/observability-incident-response/runbook-automation/) · [Self-Healing and Auto-Remediation](https://automations.metacog.co.kr/docs/observability-incident-response/self-healing/)

**Templates** — [Incident Report](https://templates.metacog.co.kr/docs/operations-incident/incident-report/) · [Postmortem](https://templates.metacog.co.kr/docs/operations-incident/postmortem/) · [On-call Handover](https://templates.metacog.co.kr/docs/operations-incident/on-call-handover/) · [Operational Runbook](https://templates.metacog.co.kr/docs/operations-incident/operational-runbook/) · [Change Request](https://templates.metacog.co.kr/docs/operations-incident/change-request/)
