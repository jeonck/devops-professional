---
title: "DevSecOps & Software Supply Chain Security"
linkTitle: "DevSecOps & Supply Chain"
weight: 100
---

## Why This Matters in 2026

Software supply chain security has become one of the fastest-rising priorities in DevOps competency evaluation, driven by a steady stream of build-system compromises and dependency-poisoning incidents that no perimeter firewall could have stopped. The OpenSSF's [SLSA](https://slsa.dev) (Supply-chain Levels for Software Artifacts) framework has emerged as the common, progressive standard for build integrity, artifact trust, and provenance — giving organizations a shared vocabulary for "how trustworthy is this build" instead of ad-hoc checklists. The bar has moved well past "we run a vulnerability scanner": a strong profile now shows an end-to-end chain of SBOM generation, artifact signing, provenance attestation, and verified dependency trust, backed by disciplined secrets management across the pipeline.

{{< callout type="info" >}}
A vulnerability scanner that only produces a report nobody acts on is security theater. What separates a credible DevSecOps profile is enforcement: gates that actually block a build, signatures that are actually verified before deploy, and an SBOM that actually gets published — not just generated and forgotten in a build log.
{{< /callout >}}

## Core Skills & Tools

- SAST/DAST/SCA integration directly into CI/CD pipelines (e.g. Semgrep, CodeQL, Snyk, Trivy, OWASP ZAP) with results gating the build, not just informing a dashboard
- SBOM generation and management (e.g. Syft, CycloneDX, SPDX) as a build artifact published alongside every release
- Container image signing and verification with Sigstore/cosign, including keyless signing workflows tied to CI identity
- SLSA provenance generation and attestation, mapping a pipeline's actual build process to a target SLSA level
- Secrets management and rotation (e.g. HashiCorp Vault, AWS Secrets Manager, SOPS) eliminating long-lived credentials from pipelines and runtime
- Applying zero-trust network and identity design principles to CI/CD pipelines and runtime workloads (short-lived tokens, workload identity, least-privilege service accounts)
- Dependency trust policies: pinning, provenance verification, and blocking unvetted or unsigned third-party packages

## What You Must Have Operated

- Integrated security scanning (SAST/DAST/SCA) into a real CI/CD pipeline with an enforced, build-breaking gate — not an advisory-only report
- Generated and published SBOMs for a production artifact as a routine part of the release process
- Implemented container image signing and verification end-to-end, including a deploy-time check that blocks unsigned or unverified artifacts
- Operated a secrets rotation process for production credentials with a defined cadence and incident-driven revocation path

## Evidence You Can Show

| Artifact | What it proves |
|---|---|
| Pipeline security gate configuration | You enforce, rather than merely report, vulnerability and policy findings before code ships |
| Sample SBOM output (CycloneDX/SPDX) for a production artifact | You can produce machine-readable dependency transparency as a routine release step |
| Signed-artifact verification logs | You operate a working chain of trust from build to deploy, not just a signing step that nobody checks |
| Secrets rotation policy document | You manage credential lifecycle deliberately instead of relying on static, long-lived secrets |

## KPIs & Metrics

- **Residual vulnerability count/severity over time** — trend of critical/high findings left unresolved past SLA
- **Artifact signing rate** — percentage of production artifacts that are signed and have verifiable provenance
- **Unsigned/unapproved artifact block rate** — percentage of non-compliant artifacts actually stopped at the deploy gate
- **Secret rotation compliance rate** — percentage of credentials rotated within policy window
- Supporting metrics: mean time to remediate a critical CVE, SBOM coverage across production services, percentage of pipelines with enforced (not advisory) security gates

## Maturity Levels

| Level | What you can demonstrate |
|---|---|
| **Associate** | Can interpret a vulnerability scan report, understands severity ratings, and knows the basic SBOM and signing concepts |
| **Professional** | Has integrated SAST/DAST/SCA into a pipeline with an enforced gate and generates SBOMs for at least one production service |
| **Senior** | Has built an end-to-end signed-artifact chain (sign, attest, verify, block-if-unsigned) and runs a working secrets rotation program across multiple services |
| **Principal** | Has driven adoption of a zero-trust, SLSA-aligned supply chain security architecture as the mandatory org-wide standard across all production pipelines |

## Proof Statements You Can Use

- "Reduced critical/high vulnerabilities left unresolved past SLA from 47 to 6 by enforcing a build-breaking SCA gate across 15 services."
- "Achieved 100% artifact signing coverage for production container images, blocking 100% of unsigned deploy attempts at the cluster admission layer."
- "Rolled out SBOM generation for 30+ production services, cutting dependency-incident triage time from 2 days to under 4 hours."
- "Implemented automated secrets rotation across 12 production credentials, raising rotation compliance from 40% to 98% within one quarter."
