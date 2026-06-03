# Benchmark Governance

這份文件定義 AI Search / GEO public benchmark 的維護原則，避免未來資料擴充時變成不可追溯的一次性表格。

## Benchmark Principles

- Public releases contain aggregate tables, methodology notes, figures, and evidence mapping.
- Raw responses, databases, client reports, private logs, credentials, and local execution traces are not public release artifacts.
- Every headline finding should map to a public aggregate table or Rosetta row.
- New benchmark dimensions should improve comparability across industry, intent, model interface, citation behavior, visibility, or rank volatility.

## Accepted Contribution Types

- Data corrections for existing public aggregate tables.
- Methodology clarifications.
- New metric proposals.
- Prompt set proposals that can be evaluated without exposing private data.
- Validator rules that improve release safety or reproducibility.
- Documentation improvements that make the benchmark easier to inspect.

## Review Criteria

Maintainers should review proposals against:

- Public evidence availability.
- Reproducibility from safe public or aggregate materials.
- Consistent terminology with `data/schema.md` and `docs/methodology.md`.
- Fit with the measurement layers in `docs/public_benchmark_schema.md`.
- No leakage of private execution materials.
- Clear value for researchers, website operators, or developers studying AI Search / GEO.

## Versioning

Public snapshots should use release tags such as `v0.1-public-research-snapshot`. Future data releases should update:

- `CHANGELOG.md`
- `docs/release_checklist.md`
- `data/rosetta/public_release_manifest.csv`
- Any affected schema, methodology, Rosetta, or figure-source files.
