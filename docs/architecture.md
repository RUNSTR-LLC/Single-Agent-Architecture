# Architecture

## Control Loop
1. Load context + open loops + yesterday learnings
2. Run lane prompt for current hour
3. Produce artifacts + status JSON
4. Emit plain-English update
5. Save memory delta to 2nd Brain

## Layers
- Prompt layer (`prompts/`)
- Skill layer (`skills/`)
- Contract layer (`contracts/`)
- Proof layer (`schemas/` + runtime proofs)

## Reliability Rules
- `blocked=true` only for real execution failure
- unresolved backlog != blocked lane
- one lane, one outcome, one message
