# Single-Agent Architecture

A portable, open-source blueprint for building high-leverage AI workflows with **one agent + skills + memory**.

## Core Idea

Most teams add more agents to solve quality issues. This repo argues for a different default:

- Keep **one primary agent**
- Encode specialization in **skill prompts**
- Store institutional knowledge in a **memory vault**
- Keep tooling as replaceable plumbing

> "Ten markdown files and a folder of memories" is not a joke — it's the architecture.

## Why this exists

This repo supports a talk comparing:

- single-agent, skill-routed systems
- vs multi-agent orchestration-heavy systems

It includes practical templates for open-source contribution workflows (audit → fix → PR), memory loops (Obsidian-friendly), and reusable guardrails.

## Repository Map

- `context/` → canonical project context + guardrails
- `skills/` → modular specialist prompts (audit, PR, memory)
- `memory/` → schemas + examples for daily memory, audit logs, PR logs
- `workflows/` → end-to-end single-agent runbooks
- `audits/` → structured templates for security/perf/quality audits
- `pr/` → PR quality gates + merge choreography templates
- `docs/` → research notes, claim map, and speaking assets

## Design Principles

1. **Correctness > volume**
2. **Shared context beats fragmented context**
3. **Portable files beat framework lock-in**
4. **Conversation loop stays human-in-the-loop**
5. **Simple defaults first; parallelism only when truly independent**

## Quick Start

1. Copy this repo
2. Fill `context/AGENT_CONTEXT.md`
3. Customize skill prompts in `skills/`
4. Start logging runs in `memory/`
5. Execute `workflows/audit-to-pr.md`

## Safety + Redaction

Before publishing your own version:

- remove keys/tokens/secrets
- remove private customer/user data
- replace private repo names if needed
- use `docs/REDACTION_CHECKLIST.md`

## License

MIT (recommended). Replace if needed.
