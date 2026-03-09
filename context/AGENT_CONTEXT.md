# AGENT_CONTEXT.md

## Mission
Contribute high-quality improvements to the codebase with minimal overhead and maximum correctness.

## Product Truths (edit for your project)
- Data store of record: `Supabase`
- Core architecture constraints:
  - Keep files under 500 lines unless justified
  - Reuse singleton clients (no duplicate NDK/client instances)
  - Preserve backward compatibility unless explicitly approved

## Non-Negotiables
- No external comms or merges without explicit human approval
- Never expose secrets, tokens, or private keys
- Prefer small, reviewable PRs
- Max 3 retry loops before escalating

## Quality Bar
- Every change must include:
  - clear problem statement
  - reproducible validation
  - test impact assessment
  - rollback plan if risky

## Preferred Workflow
1. Audit
2. Prioritize
3. Implement smallest viable fix
4. Validate locally
5. Open PR with evidence
6. Capture lessons in memory

## Human Preferences (fill this section)
- Communication style:
- Refactor tolerance:
- Risk tolerance:
- Preferred test strategy:
- Preferred PR size:
