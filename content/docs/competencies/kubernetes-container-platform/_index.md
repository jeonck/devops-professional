---
title: "Kubernetes & Container Platform Operations"
linkTitle: "Kubernetes & Containers"
weight: 60
---

## Why This Matters in 2026

Kubernetes has stopped being a differentiator and become table stakes — but operational *depth* with it remains one of the strongest signals of real distributed-systems competence. Anyone can deploy a workload to a managed cluster; far fewer people can design multi-cluster topologies, diagnose a control-plane degradation at 3 a.m., or safely roll a major version upgrade across hundreds of nodes without a customer noticing. By 2026, eBPF-based networking and security (Cilium, Tetragon) and service mesh have moved from cutting-edge experiments to mainstream production tooling, and interviewers now expect candidates to have an opinion on kernel-level observability and sidecar-vs-sidecar-less mesh architectures, not just "I've used Kubernetes."

{{< callout type="info" >}}
The interview question that separates real operators from tutorial-followers isn't "what is a StatefulSet" — it's "tell me about the last time a node pool upgrade or a CNI change went wrong, and how you found out." If you don't have an answer with a timeline and a root cause, you've used Kubernetes; you haven't operated it.
{{< /callout >}}

## Core Skills & Tools

- Multi-cluster architecture design: cluster sprawl vs. consolidation trade-offs, cross-cluster service discovery, and disaster-recovery topology
- Ingress and traffic management via **Ingress controllers** (NGINX, Traefik) and the newer **Gateway API** for protocol-aware, multi-team routing
- Service mesh operations with **Istio**, **Linkerd**, or **Cilium's eBPF-based service mesh**, including mTLS, traffic splitting, and mesh upgrade paths
- eBPF-based networking and security observability using **Cilium** and **Tetragon** for L3-L7 policy enforcement and runtime threat detection without sidecar overhead
- Autoscaling design: **Horizontal Pod Autoscaler (HPA)**, **Vertical Pod Autoscaler (VPA)**, and cluster autoscaling (Cluster Autoscaler, Karpenter) tuned for real workload elasticity, not just default thresholds
- Stateful workload operations: writing and operating **Kubernetes Operators**, managing **StatefulSets**, and selecting/tuning **StorageClasses** for databases, queues, and other stateful services
- Node lifecycle management: node pool rotation, kernel/OS patching, and **cluster version upgrade** strategies (blue/green node pools, surge upgrades, API deprecation handling)
- Multi-tenancy isolation strategies: namespace-based soft multi-tenancy, network policies, resource quotas, and hard isolation via separate clusters or virtual clusters (vcluster)

## What You Must Have Operated

- Production clusters of meaningful scale — dozens to hundreds of nodes and real multi-team workload mix, not a single-node minikube or sandbox demo
- At least one real cluster-level upgrade (Kubernetes minor/major version, CNI migration, or control-plane component change) or a major cluster-level incident you diagnosed and resolved
- A multi-cluster or multi-tenant separation strategy you designed — deciding where workload, team, or environment boundaries should be drawn and why
- Stateful workloads (databases, message queues, search clusters) running on Kubernetes under your operational ownership, including their backup/restore and failover behavior

## Evidence You Can Show

| Artifact | What it proves |
|---|---|
| Cluster architecture diagram (multi-cluster topology, network paths, trust boundaries) | You can design platform structure, not just consume someone else's cluster |
| Autoscaling configuration with a scaling-response-time report | You can tune elasticity to real traffic patterns and quantify the result |
| Stateful workload operations runbook (failover, backup/restore, upgrade steps) | You can run stateful systems on Kubernetes responsibly, not just stateless web apps |
| Multi-cluster / multi-tenant isolation design document | You can reason about blast radius, resource fairness, and security boundaries at the platform level |

## KPIs & Metrics

- **Resource utilization efficiency** — requested vs. actually consumed CPU/memory across the cluster (target: minimal slack without risking evictions)
- **Autoscaling reaction time** — time from load increase to additional capacity being ready and serving traffic
- **Cluster uptime / control-plane stability** — API server availability and scheduler responsiveness over a rolling window
- **Incident count per cluster** — frequency and severity of cluster-level incidents (node pressure, networking, control-plane) per quarter
- Supporting metrics: pod scheduling latency, node upgrade duration and rollback rate, mesh-induced latency overhead

## Maturity Levels

| Level | What you can demonstrate |
|---|---|
| **Associate** | Can deploy, debug, and roll back a workload on an existing cluster; understands core objects (Pods, Deployments, Services, ConfigMaps) and basic kubectl troubleshooting |
| **Professional** | Has configured HPA/VPA and Ingress/Gateway API routing for production services; can read and act on cluster-level metrics and events independently |
| **Senior** | Has led a cluster version upgrade or resolved a major cluster-level incident end-to-end; operates stateful workloads and service mesh policies in production |
| **Principal** | Has designed a multi-cluster or multi-tenant isolation model adopted as the org standard, balancing cost, blast radius, and team autonomy across the platform |

## Proof Statements You Can Use

- "Designed and rolled out a multi-cluster isolation model adopted by 12 product teams, cutting cross-team incident blast radius by 70%."
- "Led a zero-downtime Kubernetes major version upgrade across 8 production clusters, reducing total upgrade window from 3 days to 6 hours."
- "Tuned HPA and Karpenter-based cluster autoscaling to cut average scale-up reaction time from 4 minutes to 45 seconds during traffic spikes."
- "Migrated mesh traffic policy enforcement from sidecar-based Istio to Cilium's eBPF dataplane, reducing per-request latency overhead from 8ms to under 1ms."
