# PR Quality Gate

A PR is "ready" only if all are true:

- Scope is minimal and focused
- Tests pass in baseline and changed area
- No secret leakage or unsafe defaults
- Rollback path is clear
- Human approval received

## Merge choreography (stacked PRs)
1. Merge in dependency order
2. Rebase dependents
3. Rerun baseline on `origin/main`
4. Mark release gate clear only after post-merge pass
