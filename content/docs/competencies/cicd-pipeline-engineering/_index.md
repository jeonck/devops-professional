---
title: "CI/CD Pipeline Engineering & Automation"
linkTitle: "CI/CD Pipeline Engineering"
weight: 20
---

## Why This Matters in 2026

CI/CD has stopped being a differentiator on its own — every team has *a* pipeline. What separates a professional from a hobbyist in 2026 is whether that pipeline is reusable, supply-chain-aware, and increasingly AI-assisted: drafting pipeline YAML from a natural-language spec, auto-triaging a flaky test run, or summarizing why a build failed before a human opens the logs. Pipelines are now treated as a product with their own templates, versioning, and consumers, not a one-off script bolted onto a repo. (Deeper mechanics of GitOps reconciliation and SLSA-style supply-chain attestation are covered in their own competencies — this one is about the pipeline engineering itself.)

{{< callout type="info" >}}
The fastest way to spot a pipeline built by an amateur is to count how many times the same logic is copy-pasted across repos. The fastest way to spot a professional is a reusable template other teams adopted without being told to.
{{< /callout >}}

## Core Skills & Tools

- Pipeline design in GitHub Actions, GitLab CI, and Jenkins (declarative pipelines, matrix builds, multi-stage workflows)
- Reusable pipeline templates, composite actions, and shared workflow libraries consumed by multiple repos/teams
- Build caching strategies (dependency caching, layer caching, remote build caches) and test parallelization/sharding to cut pipeline wall-clock time
- Progressive delivery gates wired into CI (automated canary checks, blue-green cutover triggers, rollback-on-failure conditions)
- AI-assisted pipeline authoring (generating or refactoring pipeline YAML from a spec) and AI-assisted failure triage (summarizing failing test runs, flagging flaky vs. real failures)
- Artifact promotion across environments (build once, promote the same artifact through dev → staging → prod)
- Deployment approval workflows (manual gates, required reviewers, automated policy checks before promotion)

## What You Must Have Operated

- Designed and maintained CI/CD pipelines serving multiple services or teams, not just a single project's build script
- Built a reusable pipeline template or composite action that other teams adopted without you maintaining it for them
- Implemented an end-to-end release approval and promotion workflow spanning dev → staging → production, including who/what gates each stage

## Evidence You Can Show

| Artifact | What it proves |
|---|---|
| Pipeline YAML / reusable template repository | You can design pipeline logic that scales beyond a single team |
| Deployment approval flowchart | You can design and explain a multi-environment promotion and sign-off process |
| Release automation runbook | You've operationalized release steps so they're repeatable, not tribal knowledge |
| Before/after build-time report | You can quantify the impact of caching, parallelization, or pipeline redesign |

## KPIs & Metrics

- **Pipeline success rate** — percentage of pipeline runs that complete without manual rerun or intervention
- **Average build time** — wall-clock time from trigger to artifact/test completion, tracked before and after optimization
- **Release lead time / frequency** — time from merge to production-ready artifact, and how often releases ship
- **% of releases requiring manual intervention** — proportion of deployments needing a human to unblock, patch, or rerun the pipeline

## Maturity Levels

| Level | What you can demonstrate |
|---|---|
| **Associate** | Can read and modify an existing pipeline definition (add a step, fix a broken job) without breaking other stages |
| **Professional** | Has designed a pipeline from scratch for a real service, including caching and test parallelization to keep build times reasonable |
| **Senior** | Has built a reusable pipeline template or approval/promotion workflow adopted by multiple teams beyond their own |
| **Principal** | Has established the pipeline standard for an organization, shaping release policy (approval requirements, promotion gates) that other teams are required to follow |

## Proof Statements You Can Use

- "Cut average build time from 22 minutes to 7 minutes by introducing dependency caching and test parallelization across 40+ repos."
- "Built a reusable GitHub Actions workflow template adopted by 9 teams, eliminating duplicated pipeline logic and cutting new-service onboarding time from 2 days to 2 hours."
- "Designed a dev-to-prod promotion workflow with automated policy gates, reducing releases requiring manual intervention from 35% to 6%."
- "Raised pipeline success rate from 81% to 98% by replacing flaky integration tests with isolated, parallelized test suites and AI-assisted failure triage."

## Hands-On Labs

Step-by-step labs from [handson](https://handson.metacog.co.kr/#/notes) — install guides, runbooks and playbooks that were actually run, not just read:

- [GitLab CI to Argo CD on-prem — a FastAPI service from commit to running pod](https://handson.metacog.co.kr/#/note/01-install~gitlab-ci-argocd-fastapi-onprem)
- [GitLab CI to Argo CD FastAPI deployment — step-by-step procedure](https://handson.metacog.co.kr/#/note/02-runbook~gitlab-ci-argocd-fastapi-procedure)
- [Bruno — a git-friendly REST client, from a request to a CI gate](https://handson.metacog.co.kr/#/note/04-reference~bruno-api-client)
- [Nexus Repository — three repository types, and a login that lies about your password](https://handson.metacog.co.kr/#/note/01-install~nexus-repository-hosted-proxy-docker)
- [Gitea — where the repository actually lives, and what a deleted database row costs](https://handson.metacog.co.kr/#/note/01-install~gitea-selfhosted-git-server)
- [walgit — a git server whose disk you can delete, and two bugs between the README and the code](https://handson.metacog.co.kr/#/note/01-install~walgit-git-server-on-object-storage)

## Checklists

Run-before-you-ship lists from [IT Checklists](https://checklists.metacog.co.kr/docs/) — use them as the review gate behind the evidence above:

- [CI/CD Pipeline Review](https://checklists.metacog.co.kr/docs/devops/cicd-pipeline/)

## Reference Library

Background chapters, ready-to-fill documents and pipeline walkthroughs from the sibling sites — see the full [Reference Library](../../references) for everything else:

**Architecture Field Notes** — [Pipeline Design: Fast Feedback, Slow Gates](https://architectures.metacog.co.kr/docs/delivery/pipeline-design/) · [Build Reproducibility and Artifact Promotion](https://architectures.metacog.co.kr/docs/delivery/build-reproducibility/)

**Automation Playbook** — [Pipeline Design Principles](https://automations.metacog.co.kr/docs/cicd-pipelines/pipeline-design/) · [Automated Testing Strategy](https://automations.metacog.co.kr/docs/cicd-pipelines/testing-strategy/) · [Deployment Strategies](https://automations.metacog.co.kr/docs/cicd-pipelines/deployment-strategies/) · [Release Orchestration and Rollback](https://automations.metacog.co.kr/docs/cicd-pipelines/release-rollback/)

**Templates** — [Code Review Checklist](https://templates.metacog.co.kr/docs/development-release/code-review-checklist/) · [Coding Standards](https://templates.metacog.co.kr/docs/development-release/coding-standards/) · [Pull Request Template](https://templates.metacog.co.kr/docs/development-release/pull-request-template/) · [Test Plan](https://templates.metacog.co.kr/docs/testing-qa/test-plan/) · [Test Case Specification](https://templates.metacog.co.kr/docs/testing-qa/test-case-specification/) · [UAT Plan](https://templates.metacog.co.kr/docs/testing-qa/uat-plan/) · [Defect Report](https://templates.metacog.co.kr/docs/testing-qa/defect-report/) · [Test Summary Report](https://templates.metacog.co.kr/docs/testing-qa/test-summary-report/)

**Pipeline Field Guide** — [Your First Change](https://jeonck.github.io/pipelines/docs/your-first-change/) · [Pull Request to Production](https://jeonck.github.io/pipelines/docs/pull-request-to-production/)
