# 2026-06-13 AIO / SERP Public Package Checklist

## Goal

Add a public, anonymized AIO / SERP overlap research module to this repository without exposing raw payloads, full URL inventories, customer-identifying fields, or private execution logs.

## Checklist

- [x] Confirmed repository public-data boundary in `AGENTS.md`.
- [x] Generated public aggregate AIO / SERP CSV tables.
- [x] Added rebuild script for public aggregate tables.
- [x] Added methodology, data limitations, and literature notes.
- [x] Added public research note.
- [x] Updated README, QUICK_REPORT, TAKEOUT, schema, Rosetta findings, release manifest, and changelog.
- [x] Verified no raw DataForSEO payloads or full URL inventories were added.
- [x] Ran `python scripts\validate_public_package.py` successfully.
- [x] Ran Python syntax check for `scripts\build_public_aio_serp_overlap.py`.

## Public outputs

- `data/aggregated/public_aio_serp_overlap_overall.csv`
- `data/aggregated/public_aio_serp_overlap_by_date.csv`
- `data/aggregated/public_aio_serp_overlap_by_client_bucket.csv`
- `data/aggregated/public_aio_serp_top_domains.csv`
- `docs/aio_serp_overlap_methodology.md`
- `docs/aio_serp_data_limitations.md`
- `docs/aio_serp_literature_notes.md`
- `paper/aio_serp_overlap_research_note.md`
- `scripts/build_public_aio_serp_overlap.py`
