# Workflow: Audit → Fix → PR

## Input
- target scope (repo/module)
- selected skill (`audit-security` or `audit-performance`)

## Flow
1. Run audit skill
2. Prioritize one high-confidence issue
3. Implement minimal patch
4. Validate with tests/checks
5. Open PR with evidence
6. Log outcome in memory

## Success Criteria
- At least one merged or merge-ready PR
- Clear reproduction + validation evidence
- Memory entry updated

## Failure Contract
If blocked, emit `PR_BLOCKED` with:
- failing command
- failing artifact
- exact next step
