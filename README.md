# Single-Agent Architecture

![Morpheus focus](assets/intro-morpheus.jpg)

A practical blueprint for running a **24-hour AI contributor loop** with one primary agent, clear guardrails, and memory that actually compounds.

This project exists for builders who want real output (audits, fixes, PRs, learning) without spinning up dedicated agents for specific tasks.

## System architecture

```mermaid
flowchart TD
    H[Human Owner<br/>Strategy + Approvals] --> C[Contracts + Prompts<br/>program.md / lane specs]
    C --> A[Single Primary Agent<br/>OpenClaw Runtime]

    A --> L1[Audit Lanes H00-H09<br/>security / perf / docs / health...]
    A --> L2[PR Lanes H10-H19<br/>one bounded fix attempt per run]
    A --> L3[Ops Lanes H20-H23<br/>content / memory / recovery / closeout]

    L1 --> Q[Priority Queue + Scoring]
    Q --> L2

    L2 --> G[GitHub Repo<br/>branch -> PR]
    G --> R[CI + Review Signals]
    R --> A

    A --> P[Run Proofs<br/>JSON outcome artifacts]
    A --> M[2nd Brain Memory<br/>Obsidian + daily logs]
    P --> M
    M --> C

    A --> S[Status Updates<br/>plain-English contract output]
    S --> H

    classDef core fill:#1f2937,color:#fff,stroke:#111827,stroke-width:1px;
    classDef data fill:#0f766e,color:#fff,stroke:#115e59,stroke-width:1px;
    classDef io fill:#1d4ed8,color:#fff,stroke:#1e3a8a,stroke-width:1px;
    class A,L1,L2,L3,Q core;
    class P,M data;
    class H,C,G,R,S io;
```

## Why we built this

Most teams trying agentic workflows hit the same wall: too many moving parts, not enough signal. We wanted a simpler system that still ships. So the default here is:

- one primary agent
- strong prompts + contracts
- strict outcomes
- memory-driven iteration
- human supervision where it matters

In short: fewer gears, more traction.

## What we borrowed from `karpathy/autoresearch`

`autoresearch` was a big inspiration for how to keep autonomous work disciplined. We adapted several core ideas:

1. **Constrain the writable surface**  
   Their loop limits where changes happen. We do the same by narrowing each run to one lane/task.

2. **Use fixed run budgets**  
   Their experiments run on a hard time budget. Our lanes do the same to avoid runaway sessions.

3. **Score outcomes, not effort**  
   Their keep/discard logic is metric-driven. We use explicit outcome contracts (`*_CREATED`, `*_BLOCKED`, `*_SKIPPED`) and quality gates.

4. **Keep a simple run ledger**  
   Their logging is lightweight and auditable. We mirror that with concise proof artifacts and memory entries.

5. **Treat instructions like code**  
   Their `program.md` model inspired our lane contracts and run-program files.

We’re not copying the ML training workflow itself — we’re applying the same operating philosophy to software delivery.

## What this repo is

This is a portable reference architecture for teams that want an agent to:

1. audit code continuously,
2. attempt focused improvements,
3. package reviewable PR outcomes,
4. learn from results over time,
5. stay aligned with human priorities.

## Who this is for

- Open-source maintainers
- Solo builders who want a reliable AI contributor loop
- Small teams testing agentic DevOps without multi-agent complexity

## Repo layout

- `prompts/` — lane prompts (audits, PR attempts, memory, reporting)
- `skills/` — reusable skill modules (`SKILL.md` + references/scripts)
- `contracts/` — behavior contracts (messaging, outcomes, blocker semantics)
- `schemas/` — JSON schemas for status/proof/memory artifacts
- `jobs/manifests/` — H00–H19 lane manifests
- `docs/` — quickstart, architecture notes, OpenClaw setup
- `examples/` — sample outputs
- `runtime/` — local generated outputs (typically gitignored)

## Fast start

1. Read `docs/quickstart.md`
2. Read `docs/openclaw-setup.md`
3. Fill `context/AGENT_CONTEXT.md`
4. Adapt manifests from `jobs/manifests/`
5. Run a day slice and review outputs in your memory vault / 2nd Brain

## Design stance

- correctness over volume
- clarity over cleverness
- one concern per run
- explicit outcomes over status noise
- humans approve what ships

## License

MIT (replace if needed)
