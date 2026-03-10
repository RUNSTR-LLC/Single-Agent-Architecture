# Single-Agent-Architecture

A portable framework for running an **OpenClaw-powered 24-hour single-agent contributor**.

This system is designed to work on **any software project**, not just one specific codebase.
The agent runs a full daily loop:
- H00–H09: audits
- H10–H19: PR attempts
- continuous memory updates in a **2nd Brain** (Obsidian-friendly)
- plain-English progress reporting for humans

## What this repo is

This is a reference architecture for teams that want one reliable agent to:
1. inspect code continuously,
2. open focused improvement PRs,
3. learn from outcomes over time,
4. stay human-supervised.

## Who this is for

- Maintainers of open-source projects
- Solo builders who want continuous contributor support
- Teams experimenting with agentic DevOps without multi-agent complexity

## OpenClaw focus

The repository is structured so OpenClaw agents can recreate this workflow with:
- prompt packs (`prompts/`)
- skill packs (`skills/`)
- contracts + schemas (`contracts/`, `schemas/`)
- cron/job manifests (`jobs/manifests/`)

## Project-agnostic by design

Everything is template-driven.
To adapt this framework to a new project, edit:
- `context/AGENT_CONTEXT.md`
- `context/PROJECT_PROFILE_TEMPLATE.md`
- `contracts/messaging-contract.md`
- prompt files in `prompts/`

No repository-specific assumptions are required.

## Repository layout

- `prompts/` prompt library (audits / PRs / 2nd brain / reporting / ops)
- `skills/` reusable skill modules (SKILL.md + optional references/scripts)
- `contracts/` behavior contracts (messaging, outcomes, blocker semantics)
- `schemas/` JSON schemas for status/proofs/memory entries
- `jobs/manifests/` H00–H19 lane manifests
- `docs/` architecture, quickstart, OpenClaw setup, portability guides
- `examples/` sample output artifacts
- `runtime/` local output area (gitignored by default in real deployments)

## Fast start

1. Read `docs/quickstart.md`
2. Read `docs/openclaw-setup.md`
3. Fill `context/AGENT_CONTEXT.md`
4. Load/adapt job manifests from `jobs/manifests/`
5. Run lanes and review results in your 2nd Brain

## License

MIT (replace if needed).
