# Codex for Open Source Application Notes

這份文件整理本 repository 申請 Codex for Open Source 時的專案敘事、維護負擔與 Codex 使用場景。

## Project Positioning

`geo-research` is a public AI Search / GEO research and benchmark package. It helps researchers, website operators, and developers inspect how AI search interfaces select citations, mention brands, construct recommendation lists, and vary ranking order across repeated runs.

The repository is not positioned as a popular software package. Its open source value is public research infrastructure for an emerging ecosystem: claim-to-evidence mapping, aggregate benchmark tables, release safety checks, and future validation tooling for AI Search / GEO studies.

## Ecosystem Importance

AI Search changes how users discover products, services, brands, and knowledge sources. Traditional single-rank SEO measurements do not fully describe citation selection, source mix, brand visibility, Top-3 overlap, or recommendation order volatility.

This project contributes:

- Public aggregate data for AI Search / GEO analysis.
- Reproducible evidence mapping through Rosetta tables.
- A release validator that checks public package completeness and private-data boundaries.
- A roadmap toward benchmark schemas, prompt contribution workflows, and tracking prototypes.
- Documentation that distinguishes public research outputs from non-published execution materials.

## Maintainer Workload

Expected maintainer work includes:

- Reviewing CSV schema changes and Rosetta mapping updates.
- Checking whether findings remain traceable to public aggregate tables.
- Reviewing methodology proposals and benchmark expansion requests.
- Strengthening sensitive-data checks before each release.
- Producing release notes, changelog entries, and reproducibility notes.
- Reviewing documentation and script pull requests.

## Codex Use Cases

Codex would be used to reduce repetitive maintainer work:

- Extend `scripts/validate_public_package.py` into a validator CLI.
- Review CSV headers, schema drift, and evidence mapping consistency.
- Identify release-safety risks in docs, data, and scripts.
- Draft changelog entries and release notes from diffs.
- Assist PR review for data, docs, benchmark proposals, and validation logic.
- Generate tests for validator behavior without exposing private materials.

## Current Gaps

- Public adoption signals are still early.
- The first GitHub release still needs to be created.
- The validator is currently a single script, not a packaged CLI.
- Benchmark schema and prompt contribution rules now have initial public docs, but still need examples based on future safe synthetic fixtures.

## Near-Term Improvements

- Publish `v0.1-public-research-snapshot`.
- Add validator test fixtures that contain only synthetic safe examples.
- Expand `docs/public_benchmark_schema.md` with examples after the next safe aggregate release.
- Expand `docs/prompt_set_contribution.md` with accepted proposal examples.
- Expand changelog discipline for future dataset snapshots.
