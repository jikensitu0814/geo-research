# Release Notes: v0.1-public-research-snapshot

## Summary

This is the first public AI Search / GEO research snapshot for `geo-research`. It packages a Chinese research paper, aggregate CSV tables, figures, methodology notes, data limitations, reproducibility notes, and Rosetta evidence mapping.

## Included

- Public aggregate tables under `data/aggregated/`.
- Rosetta evidence mapping under `data/rosetta/`.
- Research papers and figures under `paper/`.
- Methodology, data limitation, reproducibility, benchmark governance, and release checklist docs.
- Public package validator under `scripts/`.
- GitHub issue and PR templates for community maintenance.

## Not Included

- Raw AI responses.
- SQLite databases.
- Client-facing reports.
- Full URL inventories.
- Runtime traces, local logs, or private execution records.
- Environment files or credentials.

## Validation

Before publishing the GitHub release, run:

```powershell
python scripts\validate_public_package.py
```

Expected output:

```text
public package validation passed
```

## Recommended Release Tag

`v0.1-public-research-snapshot`

