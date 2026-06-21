---
title: "GitOps & Declarative Deployment"
linkTitle: "GitOps & Declarative Deployment"
weight: 30
---

## Why This Matters in 2026

The question that matters in production is no longer "who changed something on the server" — it's **can the entire system state be reconstructed from Git alone**. GitOps has won the argument because it converts deployment into a reviewable, auditable, revertible Git history instead of a sequence of one-off operator actions. By 2026, progressive delivery patterns — canary, blue-green, rolling — are no longer a manual ritual run by a release engineer watching dashboards; they're expected to be codified, automated, and triggered by the same Git-driven control loop that manages everything else. A professional who can only describe "what we deployed" is behind; the bar is now "what does Git say, and does the cluster agree with it."

{{< callout type="info" >}}
The real test of GitOps maturity isn't whether you run Argo CD or Flux — it's what happens during a drift incident. If your answer to "the cluster doesn't match Git" is a manual `kubectl edit`, you've quietly reintroduced the exact problem GitOps was supposed to eliminate.
{{< /callout >}}

## Core Skills & Tools

- Operating **Argo CD** or **Flux** as the source of truth for cluster state in production, not just in a demo cluster
- Designing environment promotion through branching or **Kustomize overlays** (base + per-environment overlays) rather than templated copy-paste manifests
- Building **drift detection** and choosing the right **auto-sync policy** (auto-sync vs. manual sync, self-heal, prune) per environment risk profile
- Automating **progressive delivery** — canary, blue-green, and rolling rollouts — via Argo Rollouts, Flagger, or native Flux/Argo CD hooks, with automated analysis and rollback gates
- Handling secrets in a GitOps-safe way using **sealed-secrets**, **external-secrets**, or **SOPS**, so encrypted material can live in Git without leaking plaintext
- Designing **multi-cluster** and **multi-tenant** Argo CD/Flux topologies (hub-and-spoke control planes, per-team or per-namespace isolation)
- Structuring **app-of-apps** (or Flux Kustomization-of-Kustomizations) patterns to manage fleets of applications declaratively at scale

## What You Must Have Operated

- Run Argo CD or Flux in production across at least one genuinely multi-environment setup (e.g., dev/staging/prod), not just a single cluster
- Defined and enforced a drift policy, and personally handled a real drift incident where live cluster state diverged from Git
- Executed a production rollback purely through a **Git revert** — no manual server intervention, no out-of-band `kubectl` patch
- Designed or operated an app-of-apps or multi-tenant topology serving more than one team or application portfolio

## Evidence You Can Show

| Artifact | What it proves |
|---|---|
| Argo CD/Flux application manifests (repo excerpt) | You can structure declarative deployments, not just point a tool at a folder |
| Environment promotion diagram (dev → staging → prod via overlays/branches) | You understand controlled, auditable promotion rather than ad hoc environment drift |
| Drift incident write-up | You've handled the failure mode GitOps is supposed to prevent, and resolved it the GitOps way |
| Rollback time report (Git revert to stable state) | You can quantify how fast Git-driven recovery actually is under pressure |

## KPIs & Metrics

- **Deployment reproducibility** — percentage of live cluster state that can be explained, end-to-end, by what's committed in Git
- **Rollback time** — elapsed time from "revert merged" to "stable state restored" in production
- **Drift incident rate** — frequency of detected divergence between desired (Git) and live cluster state per month
- **Sync success rate** — percentage of sync operations that complete cleanly without manual intervention or hook failure
- Supporting metrics: time-to-promote across environments, percentage of secrets managed via GitOps-safe tooling, canary analysis pass rate

## Maturity Levels

| Level | What you can demonstrate |
|---|---|
| **Associate** | Can read Argo CD/Flux dashboards, understands sync state (Synced/OutOfSync, Healthy/Degraded), and can explain what GitOps changes about deployment |
| **Professional** | Has configured and operated Argo CD or Flux for a real application across multiple environments using overlays or branching, including basic drift detection |
| **Senior** | Has designed and enforced a drift/auto-sync policy, automated a progressive delivery pattern (canary/blue-green/rolling), and resolved a live drift incident without manual cluster edits |
| **Principal** | Has had their GitOps topology, drift policy, and rollback approach adopted as the org-wide standard across multiple teams, including multi-cluster or multi-tenant design |

## Proof Statements You Can Use

- "Migrated 14 services from manual `kubectl apply` deployments to Argo CD, cutting average rollback time from 45 minutes to under 3 minutes via Git revert."
- "Designed a Kustomize overlay structure across 3 environments that reduced environment-specific deployment errors by 80% over two quarters."
- "Resolved a production drift incident caused by an out-of-band hotfix by re-establishing Git as the single source of truth, then enforced self-heal sync policy across 9 namespaces to prevent recurrence."
- "Built an app-of-apps topology managing 40+ microservices across 5 clusters, achieving 99% sync success rate with zero manual interventions in 6 months."
