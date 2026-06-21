---
title: "AI/MLOps & AI-Augmented DevOps"
linkTitle: "AI/MLOps & AIOps"
weight: 110
---

## Why This Matters in 2026

AI/MLOps competency — operating LLM infrastructure, managing GPU capacity, and monitoring models in production — has moved from specialty niche to baseline expectation as organizations push AI workloads out of pilot projects and into production systems. Google Cloud's DORA research has reframed the conversation: AI adoption is no longer a question of *whether* a team uses AI tools, but a **systems and Value Stream Management (VSM)** question — *where* in the value stream AI is applied, and what happens to quality, speed, and rework as a result. The strongest profiles in 2026 don't claim "we use AI everywhere"; they can point precisely to where AI assistance helped, where it backfired, and what guardrails they put in place to keep it safe.

{{< callout type="info" >}}
This is the newest competency in the framework, and it is no longer optional. Teams that cannot operate, monitor, and govern AI-augmented workflows are now at a measurable disadvantage — DORA's own research shows AI adoption without guardrails *increases* rework and instability, while disciplined adoption improves both speed and quality.
{{< /callout >}}

## Core Skills & Tools

- LLM and GPU infrastructure operations: model serving (vLLM, Triton Inference Server, TGI, Ray Serve), GPU scheduling and utilization (Kubernetes device plugins, NVIDIA MIG, Slurm), and inference cost management (autoscaling, batching, spot/preemptible GPU strategies)
- Model monitoring in production: drift detection, output quality scoring, latency and throughput SLOs, token-level cost tracking
- AI-assisted DevOps workflows: AI-generated runbooks, IaC/pipeline code, and incident summaries — deployed with explicit guardrails such as mandatory human review and minimum test-coverage thresholds before merge
- Value Stream Management (VSM) tooling to identify exactly where AI assistance reduces cycle time versus where it introduces rework or hidden technical debt
- Prompt/agent observability — tracing AI-assisted changes back to their source so failures are attributable and reviewable
- Working knowledge of model lifecycle tooling (MLflow, Kubeflow, Vertex AI Pipelines, SageMaker) sufficient to operate, not just consume, AI infrastructure

## What You Must Have Operated

- GPU or model-serving infrastructure for at least one production AI workload, including capacity planning and cost ownership
- An AI-assisted automation deployed into a real operational workflow (e.g., AI-assisted incident triage, automated runbook generation, or AI-drafted pipeline changes) with measured before/after outcomes
- A guardrail policy for AI-generated changes that you personally defined and enforced — not just referenced from a vendor's documentation
- A value-stream analysis that identified at least one stage where AI assistance was net-negative, and a decision to scope or remove it there

## Evidence You Can Show

| Artifact | What it proves |
|---|---|
| Model-serving infrastructure architecture diagram | You can design and operate production LLM/GPU infrastructure, not just call a hosted API |
| GPU utilization and inference cost report | You manage AI infrastructure as a cost center with measurable efficiency, not an unmonitored blank check |
| AI-assisted workflow before/after metrics | You can prove AI assistance changed an outcome, with numbers, not anecdotes |
| AI usage guardrail policy document | You can govern AI-generated changes responsibly at the process level, not just the tool level |

## KPIs & Metrics

- **GPU utilization rate** — percentage of provisioned GPU capacity actively used (target: minimize idle spend without starving inference)
- **Inference cost per request** — fully loaded cost (compute + serving overhead) per model call, tracked over time
- **Rework rate on AI-assisted tasks** — percentage of AI-generated runbooks, code, or summaries that required significant human correction after the fact
- **Value-stream bottleneck reduction** — measurable cycle-time or lead-time improvement at the specific stage where AI assistance was deployed
- Supporting metrics: model drift rate, inference p95 latency, human-review override rate on AI-generated changes

## Maturity Levels

| Level | What you can demonstrate |
|---|---|
| **Associate** | Uses AI coding and ops assistants under supervision, with all output reviewed before it ships; understands why human review is mandatory |
| **Professional** | Has operated a production model-serving or GPU workload and instrumented basic cost and utilization tracking for it |
| **Senior** | Has deployed an AI-assisted automation into a live operational workflow, measured its before/after impact, and defined the guardrails (review gates, coverage thresholds) that made it safe to ship |
| **Principal** | Owns an org-wide AI-augmented delivery strategy — including guardrail policy, VSM-based placement of AI assistance, and a track record of measured impact across multiple teams |

## Proof Statements You Can Use

- "Reduced inference cost per request by 38% by introducing dynamic batching and right-sizing GPU instance types across a production LLM-serving cluster."
- "Deployed an AI-assisted incident-triage workflow that cut mean time to initial diagnosis from 22 minutes to 7 minutes across 4 on-call rotations."
- "Defined a mandatory-review guardrail policy for AI-generated pipeline changes that cut post-merge rework on AI-assisted PRs from 31% to 9%."
- "Used Value Stream Management analysis to identify and remove AI-assisted code review at a stage where it was adding 15% rework, while expanding it at two stages where it cut lead time by 24%."
