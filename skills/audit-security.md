# Skill: Security Audit

## Goal
Find real vulnerabilities with reproducible evidence and low false positives.

## Procedure
1. Map trust boundaries and input surfaces.
2. Trace auth/session/token flows.
3. Check injection, privilege escalation, insecure defaults.
4. Validate findings with a minimal reproduction path.
5. Propose smallest safe patch.

## Output
- `SECURITY_AUDIT_CREATED`
- Findings table:
  - severity
  - file/path
  - exploit scenario
  - confidence
  - fix plan
