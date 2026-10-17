---
title: "The Hypervisor Under Your Lab: Why Proxmox Earns Its Place"
date: 2026-10-17
authors:
  - name: DevOps Professional Playbook
tags:
  - Proxmox
  - On-Prem
  - Kubernetes
  - Lab
  - Infrastructure as Code
summary: "Every on-prem lab on this site starts with 'you have three nodes.' This is how you get them — and why a hypervisor, not a second laptop, is what turns a tutorial into operable evidence."
---

Read the on-prem walkthroughs on this site and they all open the same way: *given three nodes running Ubuntu*. That first line
is where most home labs quietly fail. One machine means one operating system, one shot at `kubeadm init`, and a reinstall
every time an experiment goes sideways. You end up reading about node drains instead of doing them.

A hypervisor fixes that, and the fix is not subtle: it turns one or two physical boxes into a fleet you are allowed to
destroy. **Proxmox VE** is the version of that worth learning, because it is the one you can automate.
<!--more-->

## Why a Hypervisor, Not Another Laptop

This playbook judges competency by what you have *operated*. Look at what the
[Kubernetes competency](../../docs/competencies/kubernetes-container-platform) actually asks for: node pool rotation, kernel
patching, cluster version upgrades, replicated storage surviving a disk loss, a drain-and-replace on a node that is carrying
traffic. Each of those needs a cluster you can break on purpose — and a way back.

Three used mini-PCs give you that too, and plenty of people run exactly that. What they do not give you is a snapshot. The
difference shows up the first time an upgrade wedges etcd: on bare metal you reinstall and lose the afternoon; on a
hypervisor you roll back three VMs in about a minute and try the upgrade again with one variable changed. Learning happens in
that retry loop, and the retry loop is what a hypervisor is for.

Proxmox specifically, rather than VirtualBox, UTM, or whatever ships with your desktop:

- **It is Debian with KVM/QEMU and LXC**, so the host is a Linux box you already know how to operate — `apt`, systemd,
  `journalctl`, Linux bridges. Nothing about it is a toy.
- **Clustering and live migration are in the free tier.** Paid subscriptions buy the enterprise repository and support, not
  the features you need for a lab.
- **ZFS and Ceph are built in**, which means snapshots, send/receive, and a realistic path to practising storage failure
  rather than reading about it.
- **It has a real REST API**, a CLI (`pvesh`, `qm`, `pct`), a
  Terraform/OpenTofu providers ([bpg](https://registry.terraform.io/providers/bpg/proxmox/latest/docs) and [Telmate](https://registry.terraform.io/providers/Telmate/proxmox/latest/docs) — both community-maintained, so pin a version) and
  [Packer](https://developer.hashicorp.com/packer/integrations/hashicorp/proxmox) support. This is the part that matters here:
  clickops in a web UI proves nothing, but a lab you can re-create from code is
  [IaC evidence](../../docs/competencies/infrastructure-as-code-policy-as-code).

Scaled past a lab, the same pieces — a Proxmox cluster, Ceph for shared storage, HA and live migration — are a small private cloud: API-driven VMs and containers without a public-cloud bill. That is the real-world version of the lab, and the reason the skill is worth having beyond a laptop. Ceph and HA both assume at least three nodes and a network that is not an afterthought.

The broader context is hard to miss if you work on-prem: the VMware licensing changes under Broadcom pushed a lot of
organizations into evaluating alternatives, and Proxmox became one of the common landing spots. Treat that as a reason the
skill is now marketable, not as a reason to migrate anything — a production hypervisor swap is a multi-quarter project with
storage, networking, and backup tooling attached to it.

## How It Actually Gets Used

### 1. A three-node cluster you can roll back

Build one VM template with cloud-init — Ubuntu, the kernel modules and sysctls `kubeadm` wants, your SSH key — then clone it
three times. Snapshot all three *before* the step you expect to get wrong (`kubeadm init`, the CNI install, the first
upgrade). The
[three-node kubeadm walkthrough](https://handson.metacog.co.kr/#/note/01-install~onprem-3node-kubeadm-ubuntu) assumes those
nodes exist; this is where they come from. [Talos](https://handson.metacog.co.kr/#/note/01-install~talos-kubernetes-local-cluster)
is an even better fit for VMs, since an immutable node with no shell is exactly what you want to clone.

### 2. Storage failure, on purpose

Give each node a second virtual disk and point [Longhorn](https://handson.metacog.co.kr/#/note/01-install~longhorn-storage-onprem)
at it. Then detach one — not gracefully — and watch what replication actually does. Do it again with the
[backup target](https://handson.metacog.co.kr/#/note/01-install~longhorn-backup-target-onprem) configured and you have run the
[Backup and Recovery checklist](https://checklists.metacog.co.kr/docs/operations/backup-and-recovery/) against a real
restore instead of a plan.

### 3. Networking that behaves like a site

A VLAN-aware Linux bridge on the host lets you hand the cluster its own segment, which is what makes
[MetalLB in L2 mode](https://handson.metacog.co.kr/#/note/01-install~metallb-l2-onprem) interesting: LoadBalancer IPs come
from a pool that is genuinely separate from your laptop's subnet, ARP behaves the way it does on site, and
[pinning a service IP](https://handson.metacog.co.kr/#/note/02-runbook~metallb-pin-loadbalancer-ip) stops being theoretical.

### 4. Node lifecycle drills

The [drain-and-replace runbook](https://handson.metacog.co.kr/#/note/02-runbook~k8s-node-drain-replace) is a different
exercise when the node is a VM: drain it, power it off mid-drain to see what that does to PodDisruptionBudgets, rebuild it
from the template, rejoin it. That is the loop you want muscle memory for before a real node goes bad.

### 5. The automation path

Once the lab works, delete it and build it again from code — Packer for the template, Terraform or OpenTofu for the VMs,
cloud-init for the node config. Now the lab is a repository, the rebuild takes minutes, and you can honestly say you have
provisioned infrastructure declaratively, including the
[state operations](https://handson.metacog.co.kr/#/note/02-runbook~terraform-state-operations) that go with it.

### 6. Ephemeral CI environments

Clone and snapshot are fast, which makes a VM or LXC container a disposable test bed: the pipeline clones a template,
runs the integration tests against a real OS and real networking, then destroys the clone or rolls it back to its clean
snapshot. A linked clone starts in seconds and costs almost no disk; use a full clone when the test needs to outlive its
template. It is the on-prem version of what the
[Zero-Touch Environment Provisioning](https://automations.metacog.co.kr/docs/case-studies/ephemeral-environments/) case study
describes, and it slots into the [CI/CD competency](../../docs/competencies/cicd-pipeline-engineering) as an environment you
create per run instead of one everybody shares and nobody trusts.

One boundary to respect: an LXC container shares the host kernel. For code you wrote and trust, that is a fine, cheap
sandbox; for untrusted pull requests, use a VM.

### 7. The team's own tooling, in LXC

Prometheus, Grafana, a Gitea or GitLab Runner, a registry, a log collector — the supporting cast of a DevOps team rarely
needs a full VM. LXC containers boot in seconds and cost a fraction of the memory, so the tooling stack fits next to the
cluster instead of competing with it. Use unprivileged containers by default, keep the data on its own volume so the
container stays disposable, and back them up with [Proxmox Backup Server](https://www.proxmox.com/en/products/proxmox-backup-server/overview).
The [Prometheus and Grafana labs](https://handson.metacog.co.kr/#/note/01-install~prometheus-instrument-and-query) are a
natural first set of tenants.

### 8. The cost question, answered honestly

Do the arithmetic before you argue it: node hours, power draw, and the capacity you actually need. A lab that runs a
three-node cluster plus a registry and an observability stack is cheap on owned hardware and conspicuously not cheap as
always-on cloud VMs — which is the
[FinOps](../../docs/competencies/cloud-infrastructure-finops) argument *for* a lab. The honest other half is that cloud wins
on burst, on managed control planes, and on anything you need for a week and then never again, and that
[sizing add-ons before you install them](https://handson.metacog.co.kr/#/note/02-runbook~schedulable-node-budget) matters
more on a two-node budget than it ever does with an autoscaler.

## What It Does Not Give You

The handson note [What a hypervisor under the lab would settle — and the four things it would not](https://handson.metacog.co.kr/#/note/04-reference~the-layer-under-the-three-node-lab) works through the same boundary from the evidence side — worth reading next to this list.

- **A lab's numbers do not transfer.** Overcommitted vCPUs are fine for control planes and useless for storage or latency
  benchmarks. Performance conclusions from a hypervisor on one box are not findings.
- **Nested virtualization has limits.** Running VMs inside your VMs works for some workloads and crawls or breaks for
  others, depending on CPU flags and what you expose to the guest.
- **HA is a cluster property, not a checkbox.** Proxmox HA needs three nodes for quorum and real fencing to be meaningful;
  two nodes and a shared disk is a split-brain generator.
- **A private cloud is an operations commitment.** Ceph health, upgrades, backups and capacity become your pager, not a vendor's. Do the staffing arithmetic next to the licensing one.
- **It is still a hypervisor.** It gives you nodes. Everything the
  [platform competencies](../../docs/competencies) ask for — golden paths, policy, observability, delivery — still has to be
  built on top.

## Where to Start

Install Proxmox VE on one machine with enough RAM to be boring (32GB is comfortable, 16GB works if you are careful), build
one cloud-init template, and clone it three times. Then pick the
[on-prem walkthrough](https://handson.metacog.co.kr/#/notes) you have been putting off because you did not have the nodes.

The hypervisor is not the skill. Having somewhere to break things repeatedly is what the skill grows out of.
