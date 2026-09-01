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

## Field Cases

Real incident write-ups from [ICT Problem Notes](https://fieldcases.metacog.co.kr/problems/) that exercise this competency:

- [A revoked account kept working for four hours, and nothing anywhere recorded a problem](https://fieldcases.metacog.co.kr/problems/a-revoked-account-kept-working-for-four-hours)
- [TLS fails from every service, but the site loads fine in a browser](https://fieldcases.metacog.co.kr/problems/tls-fails-from-services-but-the-site-loads-fine-in-a-browser)

**The mechanisms behind them** — [Certificate chains and trust stores](https://fieldcases.metacog.co.kr/concepts/certificate-chains) · [Revocation latency](https://fieldcases.metacog.co.kr/concepts/revocation-latency) · [Image tags and digests](https://fieldcases.metacog.co.kr/concepts/image-tags-and-digests)

## Hands-On Labs

Step-by-step labs from [handson](https://handson.metacog.co.kr/#/notes) — install guides, runbooks and playbooks that were actually run, not just read:

- [Topic of the day — signing an image and attesting its SBOM with cosign v3 and syft](https://handson.metacog.co.kr/#/note/05-daily~2026-08-12-cosign-sbom-signing)
- [Vault — rotating a password without redeploying, and the two you rotated away that still work](https://handson.metacog.co.kr/#/note/01-install~vault-secrets-rotation)
- [Harbor on Apple Silicon — three fixable failures, then one that is not](https://handson.metacog.co.kr/#/note/03-troubleshoot~harbor-installer-on-podman-arm64)

## Checklists

Run-before-you-ship lists from [IT Checklists](https://checklists.metacog.co.kr/docs/) — use them as the review gate behind the evidence above:

- [Container Image Hardening](https://checklists.metacog.co.kr/docs/devops/container-image/)

## Staying Current

Vulnerability intake is part of this competency, not a side activity. [CuraSec](https://curasec.metacog.co.kr/)
publishes daily security verdicts cross-referenced against CISA KEV, EPSS scores, and public PoC availability,
split by audience (Engineers, SOC/IR, security leaders):

- [🔥 Act](https://curasec.metacog.co.kr/verdict/act/) — active exploitation, critical CVEs, supply-chain compromises
- [📌 Plan](https://curasec.metacog.co.kr/verdict/plan/) — important but schedulable this quarter
- [📚 Learn](https://curasec.metacog.co.kr/verdict/learn/) — research and trend awareness
- [Tags](https://curasec.metacog.co.kr/tags/) · [RSS](https://curasec.metacog.co.kr/index.xml)

For the DevOps-side equivalent — releases, EOL dates and deprecation deadlines — see
[CuraDevOps](https://curadevops.metacog.co.kr/) on the [Tools Landscape](../../tools) page.

## Reference Library

Background chapters, ready-to-fill documents and pipeline walkthroughs from the sibling sites — see the full [Reference Library](../../references) for everything else:

**Architecture Field Notes** — [Threat Modeling in One Hour](https://architectures.metacog.co.kr/docs/security/threat-modeling/) · [Identity, Authentication, Authorisation](https://architectures.metacog.co.kr/docs/security/identity-and-authorization/) · [Least Privilege and Auditability](https://architectures.metacog.co.kr/docs/security/least-privilege/) · [Secrets and Key Management](https://architectures.metacog.co.kr/docs/security/secrets-management/) · [Supply Chain: Dependencies, SBOM, Signing](https://architectures.metacog.co.kr/docs/security/supply-chain/)

**Automation Playbook** — [Shift-Left Security in the Pipeline](https://automations.metacog.co.kr/docs/security-compliance/shift-left-security/) · [Software Supply Chain Security](https://automations.metacog.co.kr/docs/security-compliance/supply-chain/) · [Secrets Management Automation](https://automations.metacog.co.kr/docs/security-compliance/secrets-management/) · [Compliance as Code](https://automations.metacog.co.kr/docs/security-compliance/compliance-as-code/)

**Templates** — [Information Security Policy](https://templates.metacog.co.kr/docs/security-compliance/information-security-policy/) · [Risk Register](https://templates.metacog.co.kr/docs/security-compliance/risk-register/) · [Access Review](https://templates.metacog.co.kr/docs/security-compliance/access-review/) · [Vendor Security Assessment](https://templates.metacog.co.kr/docs/security-compliance/vendor-security-assessment/) · [Data Protection Impact Assessment](https://templates.metacog.co.kr/docs/security-compliance/data-protection-impact-assessment/)
