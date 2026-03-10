# Test Plan Audit Prompt

You are running the **Test Plan Audit** lane.

## Inputs
- Target codebase path: {CODEBASE_PATH}
- Previous lane summary: {PREV_SUMMARY}
- Open loops: {OPEN_LOOPS}

## Task
1. Inspect relevant code for this audit domain.
2. Identify the highest-confidence issue.
3. Propose the safest fix candidate.
4. Output using `prompts/audits/_shared/audit-format.md`.

## Chat update format
[{TIME_ET}] Test Plan Audit complete. Bug found: <plain english>. Fix made: <none yet|summary>. 2nd Brain updated.
