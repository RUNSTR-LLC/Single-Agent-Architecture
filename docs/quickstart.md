# Quickstart

## Goal
Run a 24-hour single-agent contributor loop on your own codebase.

## Step 1: Configure context
- Edit `context/AGENT_CONTEXT.md`
- Copy `context/PROJECT_PROFILE_TEMPLATE.md` and fill values for your project

## Step 2: Confirm communication format
- Update `contracts/messaging-contract.md`
- Keep updates short, plain English, and human-readable

## Step 3: Choose lane scope
Default mode:
- H00-H09 audits
- H10-H19 PR attempts

Optional: add utility lanes only after core loop is stable.

## Step 4: Wire OpenClaw jobs
- Use `jobs/manifests/` as source templates
- Schedule each lane on hourly cadence in your OpenClaw cron setup
- Keep blocker alerts conservative (execution failures only)

## Step 5: Run and review
- Execute one day
- Inspect proofs/status artifacts
- Tune prompts and contracts
- Repeat

## Success checkpoint
After day 1 you should have:
- completed audit outputs
- PR attempt outcomes (`PR_CREATED` / `NO_PR` / `BLOCKED`)
- 2nd Brain entries that improve next-day behavior
