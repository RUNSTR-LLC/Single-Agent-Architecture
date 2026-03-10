# Job Manifests

These files define the canonical 24-hour lane map:
- `h00`–`h09`: audits
- `h10`–`h19`: PR attempts

## Usage
- Treat each file as a template input for your scheduler.
- Map each manifest to one OpenClaw cron job.
- Keep lane/job names human-readable.

## Outcome expectations
- Audit lanes: `AUDIT_DONE`
- PR lanes: `PR_CREATED` / `NO_PR` / `BLOCKED`
