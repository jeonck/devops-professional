---
title: "Observability & SRE"
linkTitle: "Observability & SRE"
weight: 80
---

## Why This Matters in 2026

Observability stopped being a dashboard-installation task years ago, and by 2026 that distinction is what separates a junior monitoring setup from a real SRE practice. **OpenTelemetry** has become the vendor-neutral standard for instrumenting traces, metrics, and logs, which means the differentiator is no longer "which APM did you wire up" but how deliberately you designed signal coverage and SLOs before an incident ever happened. SLO and error-budget thinking is now the shared language teams use to define "what quality means here" in concrete, negotiable terms instead of vague uptime promises. At the same time, AIOps-assisted anomaly detection is increasingly used to cut through alert noise and shorten root-cause analysis, but it only works on top of well-structured signals — it doesn't replace the design work. The strongest SRE profiles design for reliability up front; they don't retrofit dashboards after the third 3 a.m. page.

{{< callout type="info" >}}
A pile of dashboards is not observability — it's an admission that nobody decided what "healthy" means. The professionals who stand out are the ones who can show an SLO that actually blocked a release, not just a Grafana board nobody acts on.
{{< /callout >}}

## Core Skills & Tools

- **OpenTelemetry** instrumentation spanning traces, metrics, and logs, with consistent semantic conventions across services
- Defining **SLIs/SLOs** and writing an error-budget policy that has real teeth (gates releases, triggers freezes, reallocates priorities)
- Dashboard and APM design with **Grafana**, **Prometheus**, **Datadog**, or **New Relic**, built around user-facing signals rather than infrastructure vanity metrics
- Alert design that separates actionable, page-worthy signals from informational noise (multi-window, multi-burn-rate alerting on SLOs)
- **AIOps**-assisted anomaly detection and cross-signal correlation (logs + metrics + traces) to accelerate root-cause analysis
- Building runbooks and dashboards that are actually used during an incident, not just referenced in a postmortem template

## What You Must Have Operated

- Defined and operated SLOs backed by an error-budget policy that was actually enforced — for example, it blocked or slowed a risky release rather than existing only on paper
- Led an alert-noise-reduction initiative with a measurable before/after, not just a one-time pruning of a few rules
- Built and used a cross-signal (logs + metrics + traces) debugging workflow during a real production incident, not a tabletop exercise
- Rolled out OpenTelemetry instrumentation across multiple services and made the resulting data the default source of truth for on-call engineers

## Evidence You Can Show

| Artifact | What it proves |
|---|---|
| SLO document plus enforced error-budget policy | You can translate reliability targets into a concrete operating rule, not just a target number |
| Alert-noise before/after report | You can quantify and reduce on-call fatigue, not just add more alerting rules |
| OpenTelemetry instrumentation architecture diagram | You can design observability coverage deliberately across services, not bolt on agents ad hoc |
| Incident timeline reconstructed from observability data | You can use traces, metrics, and logs together to explain what actually happened, fast |

## KPIs & Metrics

- **Mean Time to Detect (MTTD)** — how quickly a real degradation is identified after it starts
- **Alert noise reduction (%)** — drop in non-actionable alerts after a tuning or redesign effort
- **SLO attainment rate** — percentage of measurement windows where the SLO target was met
- **Instrumentation coverage (%)** — share of services/critical paths with OpenTelemetry traces, metrics, and logs wired in
- Supporting metrics: error-budget burn rate, time-to-correlate-signals during an incident, on-call pages per engineer per week

## Maturity Levels

| Level | What you can demonstrate |
|---|---|
| **Associate** | Can read existing dashboards, interpret SLO status, and understand why an alert fired |
| **Professional** | Has instrumented a service with OpenTelemetry end-to-end and defined SLIs/SLOs for it |
| **Senior** | Has enforced an error-budget policy that changed a real release decision, and led a measurable alert-noise reduction effort |
| **Principal** | Has made observability and SLO standards an org-wide practice, directly shaping release gates and reliability policy across teams |

## Proof Statements You Can Use

- "Reduced mean time to detect (MTTD) for critical service degradations from 22 minutes to 4 minutes by rolling out OpenTelemetry-based distributed tracing."
- "Cut non-actionable alert volume by 68% through multi-burn-rate SLO alerting, lowering on-call pages per engineer from 14/week to 4/week."
- "Defined and enforced an error-budget policy that blocked 3 risky releases in one quarter, holding SLO attainment above 99.5% for the core checkout path."
- "Drove OpenTelemetry instrumentation coverage from 35% to 92% of production services, making trace-based root-cause analysis the default incident workflow."

## Field Cases

Real incident write-ups from [ICT Problem Notes](https://sols.metacog.co.kr/problems/) that exercise this competency:

- [A 40-minute outage passed with no alert, and the error-rate panel showed a flat line](https://sols.metacog.co.kr/problems/a-40-minute-outage-passed-with-no-alert/)
- [All dashboards developed gaps and Prometheus restarted every twenty minutes](https://sols.metacog.co.kr/problems/all-dashboards-developed-gaps-and-prometheus-restarted-every-twenty-minutes/)
- [p99 latency spikes to 400ms while CPU utilisation sits at 30%](https://sols.metacog.co.kr/problems/p99-latency-spikes-while-cpu-utilisation-sits-at-30-percent/)
- [Every query got slower during business hours and recovered overnight, for three weeks](https://sols.metacog.co.kr/problems/every-query-got-slower-during-business-hours-and-recovered-overnight/)

## Hands-On Labs

Step-by-step labs from [handson](https://handson.metacog.co.kr/#/notes) — install guides, runbooks and playbooks that were actually run, not just read:

- [Prometheus — instrumenting a service, and three queries that lie if you read them wrong](https://handson.metacog.co.kr/#/note/01-install~prometheus-instrument-and-query)
- [Grafana — wiring metrics, logs and traces together so one ID walks between them](https://handson.metacog.co.kr/#/note/01-install~grafana-correlate-three-signals)
- [Loki — logs you can query, and the one label that multiplies your streams by 25](https://handson.metacog.co.kr/#/note/01-install~loki-logs-labels-and-cardinality)
- [OpenTelemetry tracing — one trace across two services, and where the 420ms actually went](https://handson.metacog.co.kr/#/note/01-install~opentelemetry-tracing-two-services)
- [OpenSearch — a single node, and the range query that quietly lies](https://handson.metacog.co.kr/#/note/01-install~opensearch-mappings-and-templates)
- [Topic of the day — Prometheus 3.13 LTS, a self-scrape lab and the new min_of()/max_of()](https://handson.metacog.co.kr/#/note/05-daily~2026-08-11-prometheus-3-13-lts)

## Case Studies

Industry patterns and incident write-ups from [IT Automation](https://automations.metacog.co.kr/docs/case-studies/) that show this competency at work across organizations:

- [Error Budgets and the SRE Model](https://automations.metacog.co.kr/docs/case-studies/error-budgets/)
- [The Alert That Never Fired](https://automations.metacog.co.kr/docs/case-studies/silent-alerts/)
