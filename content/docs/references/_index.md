---
title: "Reference Library"
linkTitle: "References"
weight: 18
sidebar:
  exclude: true
---

Everything this playbook links out to, in one place. Each competency page carries the handful of references
that belong to it; this page is the full index — including the material that is broader than any single
competency (architecture styles, cross-domain checklists, tool catalogues, and the daily feeds).

{{< callout type="info" >}}
Nothing here is a substitute for the [evidence](../competencies) each competency asks for. Use these to
close a gap or to prepare a review — then go operate the thing.
{{< /callout >}}

## The Sources

| Source | What it is | Best used for |
|---|---|---|
| [Architecture Field Notes](https://architectures.metacog.co.kr/) | Practitioner notes on architecture decisions, styles, and trade-offs | Deciding *before* you build — and writing down why |
| [IT Automation Playbook](https://automations.metacog.co.kr/docs/) | Automation practice by domain, plus real case studies | Choosing what to automate and how far to take it |
| [handson](https://handson.metacog.co.kr/#/notes) | Install guides, runbooks and playbooks that were actually run | Building the hands-on evidence a competency asks for |
| [ICT Problem Notes](https://sols.metacog.co.kr/problems/) | Real production failures with root cause and fix | Debugging patterns, interview war stories |
| [IT Checklists](https://checklists.metacog.co.kr/docs/) | Standardized review lists across IT domains | The gate you run before shipping or handing over |
| [IT Template Library](https://templates.metacog.co.kr/docs/) | Ready-to-fill documents for delivery, ops, and compliance | Producing the artifact instead of formatting one |
| [Pipeline Field Guide](https://jeonck.github.io/pipelines/) | End-to-end walkthroughs of how a change reaches production | Explaining delivery flow to a team or an interviewer |
| [Toolian](https://toolian.metacog.co.kr/) | Catalogue of practitioner tools by category | Finding the small tool that removes a daily papercut |
| [Framework Thinking](https://fw-thinking.metacog.co.kr/) | Governance, EA, quality and compliance frameworks | The management-side vocabulary DevOps work is judged in |
| [Release Board](https://rel-mgmt.metacog.co.kr/) | Nightly GO / HOLD / NO-GO verdicts on 99 products (releases, EOL, CVEs) | Upgrade and end-of-life decisions |
| [CuraDevOps](https://curadevops.metacog.co.kr/) · [CuraSec](https://curasec.metacog.co.kr/) · [OSS Insights](https://oss.metacog.co.kr/) | Daily Act / Plan / Learn verdicts on DevOps, security, and open-source signals | Keeping the landscape on this site current |

## Architecture Field Notes

Chapters that sit above any one competency — the ones tied to a specific competency are linked from its page.

- **Foundations** — [The Boring Baseline](https://architectures.metacog.co.kr/docs/foundations/boring-baseline/) · [Constraints First](https://architectures.metacog.co.kr/docs/foundations/constraints-first/) · [Coupling and Cohesion in Practice](https://architectures.metacog.co.kr/docs/foundations/coupling-and-cohesion/) · [Irreversible Decisions](https://architectures.metacog.co.kr/docs/foundations/irreversible-decisions/) · [Trade-off Sliders](https://architectures.metacog.co.kr/docs/foundations/trade-off-sliders/)
- **Styles** — [Monolith First, Split on Evidence](https://architectures.metacog.co.kr/docs/system-design/monolith-first/) · [Microservices: The Itemised Bill](https://architectures.metacog.co.kr/docs/styles/microservices/) · [Event-Driven](https://architectures.metacog.co.kr/docs/styles/event-driven/) · [Serverless and Managed Services](https://architectures.metacog.co.kr/docs/styles/serverless/) · [Layered (N-Tier)](https://architectures.metacog.co.kr/docs/styles/layered/) · [Ports and Adapters](https://architectures.metacog.co.kr/docs/styles/ports-and-adapters/) · [CQRS and Read Models](https://architectures.metacog.co.kr/docs/styles/cqrs-and-read-models/) · [Data Platform Styles](https://architectures.metacog.co.kr/docs/styles/data-platform/) · [Per-User Instances](https://architectures.metacog.co.kr/docs/styles/per-user-instances/)
- **System design** — [Service Boundaries That Survive Reorgs](https://architectures.metacog.co.kr/docs/system-design/service-boundaries/) · [Synchronous vs Asynchronous Integration](https://architectures.metacog.co.kr/docs/system-design/sync-vs-async/)
- **Data and state** — [Choosing a Datastore Without Regret](https://architectures.metacog.co.kr/docs/data-and-state/choosing-a-datastore/) · [Consistency Models You Actually Need](https://architectures.metacog.co.kr/docs/data-and-state/consistency-models/) · [Caching: The Four Questions](https://architectures.metacog.co.kr/docs/data-and-state/caching/) · [Event Sourcing and CDC](https://architectures.metacog.co.kr/docs/data-and-state/events-and-cdc/) · [Schema Migrations Without Downtime](https://architectures.metacog.co.kr/docs/data-and-state/zero-downtime-migrations/)

## Checklists Beyond DevOps and Operations

The [DevOps](https://checklists.metacog.co.kr/docs/devops/) and [Operations](https://checklists.metacog.co.kr/docs/operations/)
sections are linked from the competency pages. The rest of the library covers the domains a DevOps role
touches from the side:

[Cloud](https://checklists.metacog.co.kr/docs/cloud/) · [Security](https://checklists.metacog.co.kr/docs/security/) · [Networking](https://checklists.metacog.co.kr/docs/networking/) · [Data](https://checklists.metacog.co.kr/docs/data/) · [Development](https://checklists.metacog.co.kr/docs/development/) · [Compliance](https://checklists.metacog.co.kr/docs/compliance/) · [ITSM](https://checklists.metacog.co.kr/docs/itsm/)

## Templates

Delivery, operations, security and project templates are linked from the matching competency pages. The
design-document set sits here:

[Solution Architecture Document](https://templates.metacog.co.kr/docs/architecture-design/solution-architecture-document/) · [Technical Design Document](https://templates.metacog.co.kr/docs/architecture-design/technical-design-document/) · [API Specification](https://templates.metacog.co.kr/docs/architecture-design/api-specification/) · [Data Model Document](https://templates.metacog.co.kr/docs/architecture-design/data-model-document/)

Full library by category: [Architecture & Design](https://templates.metacog.co.kr/docs/architecture-design/) · [Development & Release](https://templates.metacog.co.kr/docs/development-release/) · [Operations & Incident](https://templates.metacog.co.kr/docs/operations-incident/) · [Testing & QA](https://templates.metacog.co.kr/docs/testing-qa/) · [Security & Compliance](https://templates.metacog.co.kr/docs/security-compliance/) · [Requirements](https://templates.metacog.co.kr/docs/requirements/) · [Project Management](https://templates.metacog.co.kr/docs/project-management/)

## Pipeline Field Guide

[Your First Change](https://jeonck.github.io/pipelines/docs/your-first-change/) · [Pull Request to Production](https://jeonck.github.io/pipelines/docs/pull-request-to-production/) · [Deploy Request](https://jeonck.github.io/pipelines/docs/deploy-request/) · [Feature Rollout](https://jeonck.github.io/pipelines/docs/feature-rollout/) · [Product Events](https://jeonck.github.io/pipelines/docs/product-events/) · [Delivery Platform](https://jeonck.github.io/pipelines/docs/delivery-platform/) · [Diagrams](https://jeonck.github.io/pipelines/diagrams/)

## Tool Catalogue

[Toolian](https://toolian.metacog.co.kr/) indexes practitioner tools by category — the DevOps-adjacent ones:

[DevOps](https://toolian.metacog.co.kr/docs/devops/) · [Observability](https://toolian.metacog.co.kr/docs/observability/) · [Security](https://toolian.metacog.co.kr/docs/security/) · [Automation](https://toolian.metacog.co.kr/docs/automation/) · [Git](https://toolian.metacog.co.kr/docs/git/) · [Network](https://toolian.metacog.co.kr/docs/network/) · [Terminal](https://toolian.metacog.co.kr/docs/terminal/) · [Files](https://toolian.metacog.co.kr/docs/files/) · [Editor](https://toolian.metacog.co.kr/docs/editor/) · [AI](https://toolian.metacog.co.kr/docs/ai/) · [AI Media](https://toolian.metacog.co.kr/docs/ai-media/) · [Vibe Infra](https://toolian.metacog.co.kr/docs/vibe-infra/) · [Linux Desktop](https://toolian.metacog.co.kr/docs/linux-desktop/) · [Writing](https://toolian.metacog.co.kr/docs/writing/) · [Getting Started](https://toolian.metacog.co.kr/docs/getting-started/)

For the opinionated, production-adoption view of the same space, see the [Tools Landscape](../tools).

## Governance & Framework Thinking

[Framework Thinking](https://fw-thinking.metacog.co.kr/) covers the management-side frameworks that DevOps
work gets audited and budgeted against — useful when a competency has to be defended outside engineering:

[IT Governance](https://fw-thinking.metacog.co.kr/docs/it-governance/) · [Enterprise Architecture](https://fw-thinking.metacog.co.kr/docs/enterprise-architecture/) · [Security Governance](https://fw-thinking.metacog.co.kr/docs/security-governance/) · [Data & AI Governance](https://fw-thinking.metacog.co.kr/docs/data-ai-governance/) · [Quality Management](https://fw-thinking.metacog.co.kr/docs/quality-management/) · [Software Engineering](https://fw-thinking.metacog.co.kr/docs/software-engineering/) · [Infrastructure & Operations](https://fw-thinking.metacog.co.kr/docs/infrastructure-operations/) · [Legal & Compliance](https://fw-thinking.metacog.co.kr/docs/legal-compliance/) · [Modern Organization](https://fw-thinking.metacog.co.kr/docs/modern-organization/) · [Economic Analysis](https://fw-thinking.metacog.co.kr/docs/economic-analysis/) · [Future Technology](https://fw-thinking.metacog.co.kr/docs/future-technology/)

## Daily Feeds

| Feed | Lanes |
|---|---|
| [Release Board](https://rel-mgmt.metacog.co.kr/) — nightly release, EOL and CVE sweep over 99 products | GO · HOLD · NO-GO per product |
| [CuraDevOps](https://curadevops.metacog.co.kr/) — DevOps and platform signals | [Act](https://curadevops.metacog.co.kr/verdict/act/) · [Plan](https://curadevops.metacog.co.kr/verdict/plan/) · [Learn](https://curadevops.metacog.co.kr/verdict/learn/) · [RSS](https://curadevops.metacog.co.kr/index.xml) |
| [CuraSec](https://curasec.metacog.co.kr/) — security signals against KEV, EPSS, public PoC | [Act](https://curasec.metacog.co.kr/verdict/act/) · [Plan](https://curasec.metacog.co.kr/verdict/plan/) · [Learn](https://curasec.metacog.co.kr/verdict/learn/) · [RSS](https://curasec.metacog.co.kr/index.xml) |
| [OSS Insights](https://oss.metacog.co.kr/) — open-source releases, projects and discussion worth acting on | [Insights](https://oss.metacog.co.kr/insights/) · [Verdicts](https://oss.metacog.co.kr/verdict/) · [RSS](https://oss.metacog.co.kr/index.xml) |
