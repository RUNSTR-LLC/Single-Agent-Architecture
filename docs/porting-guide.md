# Porting Guide (Any Project)

## Objective
Adapt this framework to a new repository in under 30 minutes.

## Port steps
1. Fill `context/AGENT_CONTEXT.md`
2. Fill a copy of `context/PROJECT_PROFILE_TEMPLATE.md`
3. Replace project-specific commands in prompt inputs
4. Update PR safety constraints
5. Run one audit lane and one PR lane
6. Tune messaging for your human reviewer

## Common customization points
- language/toolchain-specific audit checks
- test strategy and required checks
- PR size/risk limits
- contributor etiquette per project

## Keep portable
Avoid hardcoding:
- product names
- private hostnames
- internal-only process names
