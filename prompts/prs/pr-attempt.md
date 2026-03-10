# PR Attempt Prompt

You are running one PR attempt lane.

## Inputs
- Ranked findings list
- Existing open PRs
- Safety constraints

## Task
1. Pick one non-overlapping, high-confidence fix.
2. Implement smallest safe change.
3. Open PR.
4. Output one outcome:
   - PR_CREATED
   - NO_PR
   - BLOCKED (execution failure only)

## Chat update format
[{{TIME_ET}}] PR opened. Bug: <plain english>. Fix: <plain english>. 2nd Brain updated.
