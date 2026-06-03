# Maintainers

## Primary Maintainer

- 己見室 jikensitu
- Website: https://jikensitu.com/

## Maintainer Responsibilities

- Review public data, docs, scripts, and benchmark proposals.
- Keep the public release boundary clear: aggregated tables and evidence mapping are public; raw responses, databases, client-facing reports, runtime traces, and credentials are not.
- Run `python scripts\validate_public_package.py` before public releases.
- Keep `docs/release_checklist.md`, `CHANGELOG.md`, and release notes aligned with each public snapshot.
- Review methodology changes for reproducibility, claim-to-evidence mapping, and data-safety risk.

## Review Priorities

- Data safety issues take precedence over feature requests.
- Validator and release workflow fixes take precedence over new benchmark expansion.
- Methodology changes should be documented before related data tables are released.

