# Single-Agent-Architecture

An open-source framework for running a **24-hour single-agent engineering system** with:
- hourly audits (H00-H09)
- hourly PR attempts (H10-H19)
- a persistent **2nd Brain** (Obsidian-friendly memory)
- human-readable status updates

## What this repo gives you

1. **Prompt system** for audits, PR attempts, reporting, and memory.
2. **Skill packs** so one agent can behave like a specialist without agent sprawl.
3. **Contracts + schemas** to keep output consistent and machine-checkable.
4. **Job manifests** for a full 24-hour lane map.
5. **Examples + scripts** for bootstrapping your own setup.

## Core architecture

- **One primary agent** runs the whole day.
- **Audits first** to discover and validate bugs.
- **PR attempts second** to ship focused fixes.
- **2nd Brain continuously updated** to avoid repeating mistakes.
- **Human-in-the-loop** keeps approval and merge decisions manual.

## Repository layout

- `prompts/` prompt library (audits / PRs / 2nd brain / reporting)
- `skills/` reusable skill modules (SKILL.md + references/scripts)
- `contracts/` behavior and messaging rules
- `schemas/` JSON schemas for status/proofs
- `jobs/manifests/` H00-H19 cron-ready manifests
- `scripts/` helper utilities
- `examples/` sample inputs/outputs
- `docs/` architecture docs and quickstart guides

## Fast start

1. Read `docs/quickstart.md`
2. Fill `context/AGENT_CONTEXT.md`
3. Customize `contracts/messaging-contract.md`
4. Customize prompt files under `prompts/`
5. Load job manifests from `jobs/manifests/`
6. Run and review outputs in your 2nd Brain

## License

MIT (replace if needed).
