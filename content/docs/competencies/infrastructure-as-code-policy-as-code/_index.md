---
title: "Infrastructure as Code & Policy as Code"
linkTitle: "IaC & Policy as Code"
weight: 40
---

## Why This Matters in 2026

Writing infrastructure as code stopped being a differentiator years ago — every team with a Terraform file in a repo can claim it. What now separates a strong profile is **policy as code**: codifying security, cost, and compliance rules so violations are blocked at pull-request time, instead of being discovered in a cloud security audit or a 3 a.m. incident. By 2026, organizations are judged less on whether their infrastructure is codified and more on whether that code is *governed* — with guardrails that scale faster than the headcount reviewing changes.

{{< callout type="info" >}}
If your policy enforcement happens after a resource is already running in production, you don't have policy as code — you have a dashboard. The bar in 2026 is a check that fails the pull request, not an alert that fires after the fact.
{{< /callout >}}

## Core Skills & Tools

- Terraform/OpenTofu module design, versioning, and distribution through an internal module registry
- Helm chart and Kustomize overlay standardization across environments and teams
- Kubernetes admission policy with **OPA/Gatekeeper** and **Kyverno** (mutating and validating policies)
- Static policy scanning in CI with **Conftest**, **Checkov**, and **tfsec** against Rego or YAML policy bundles
- Designing PR-time policy gates that fail fast, with actionable error messages instead of opaque rejections
- Infrastructure drift detection at the cloud-resource level (distinct from GitOps application-state drift) using tools like `terraform plan` in CI, driftctl, or cloud-native config recorders
- Encoding tagging, naming, and resource-sizing conventions as enforceable policy rather than wiki documentation
- Versioning and testing policy bundles themselves (unit tests for Rego/Kyverno policies, not just for infrastructure code)

## What You Must Have Operated

- Built and published a reusable IaC module (or module set) that other teams actually consume from an internal registry, not just a copy-pasted example
- Implemented at least one PR-blocking policy check that caught and stopped a real violation before it reached production — not a theoretical rule that has never fired
- Migrated a category of manual or out-of-band infrastructure changes (console clicks, ad hoc scripts) into a fully codified, reviewed pipeline
- Run drift detection in production long enough to use it for an actual remediation, not just a one-time audit

## Evidence You Can Show

| Artifact | What it proves |
|---|---|
| IaC module registry or repository with consumption metrics | You design infrastructure code as a reusable product, not one-off scripts |
| OPA/Gatekeeper or Kyverno policy set (with tests) | You can encode organizational rules as enforceable, testable code |
| Screenshot or CI log of a PR check blocking a real violation | Your policy gates have actually prevented a problem, not just documented one |
| Provisioning-time before/after report | You can quantify the operational impact of codifying previously manual work |

## KPIs & Metrics

- **Infrastructure provisioning time** — time from request/PR merge to usable resource
- **% of manual/out-of-band changes** — share of infrastructure changes made outside the codified pipeline
- **Policy violation detection rate** — violations caught pre-merge vs. found post-deploy
- **Module reuse count** — number of teams/services consuming a shared IaC module
- Supporting metrics: policy check false-positive rate, mean time to remediate drift, PR rejection-to-merge turnaround for policy failures

## Maturity Levels

| Level | What you can demonstrate |
|---|---|
| **Associate** | Can write and apply a Terraform/OpenTofu resource using an existing internal module; understands the difference between IaC and policy as code |
| **Professional** | Has authored a reusable IaC module consumed by at least one other team and written a basic Conftest/Checkov policy enforced in CI |
| **Senior** | Has implemented a PR-blocking OPA/Gatekeeper or Kyverno policy set that prevented a real violation, and led a migration of manual infra changes into a codified pipeline |
| **Principal** | Has made policy as code a mandatory, org-wide merge gate, with module registries and policy bundles adopted as shared platform infrastructure across multiple teams |

## Proof Statements You Can Use

- "Cut average infrastructure provisioning time from 5 days to 45 minutes by replacing manual ticket-based requests with a self-service Terraform module registry."
- "Built an OPA/Gatekeeper policy set that blocked 34 non-compliant Kubernetes manifests at PR time in its first quarter, preventing them from reaching production."
- "Reduced manual/out-of-band infrastructure changes from 40% to under 5% by migrating networking and IAM provisioning into a fully codified pipeline."
- "Published an internal Terraform module library adopted by 9 teams, cutting duplicate module code by roughly 70% across the organization."
