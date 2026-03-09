# Redaction Checklist

Before publishing:

- [ ] Remove API keys, tokens, cookies, secrets
- [ ] Remove personal identifiers unless intentionally public
- [ ] Remove private hostnames and internal paths
- [ ] Remove confidential business metrics not approved for release
- [ ] Replace private repo links with placeholders
- [ ] Verify commit history does not contain leaked secrets
- [ ] Run secret scanning (gitleaks/trufflehog or equivalent)
