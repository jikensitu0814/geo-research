# AIO / SERP Overlap Methodology

## Research question

This module measures how often Google AI Overviews cite domains that also appear in traditional Google SERP results for the same query observation.

The public release uses aggregate tables only. It does not include raw API responses, full result URLs, private execution traces, or customer-identifying fields.

## Study unit

The base unit is one keyword-day search observation with AIO triggered and a successfully retrieved DataForSEO result. The analyzable period is 2026-05-14 to 2026-06-12 because 2026-05-13 retrievals had expired.

## Domain normalization

All comparison metrics are domain-level metrics. Hostnames are lowercased and leading `www.` is removed before comparison. URL paths, page titles, snippets, and raw AIO text are not part of the public data package.

## Main overlap directions

### AIO to SERP

This answers: among domains cited by AIO, what share also appears in SERP top N for the same observation?

Formula:

```text
AIO to SERP top N overlap = count(AIO cited domains intersect SERP top N domains) / count(AIO cited domains)
```

This is the primary metric for comparing AIO citation sources with traditional search visibility.

### SERP to AIO

This answers: among SERP top N domains, what share is also cited by AIO for the same observation?

Formula:

```text
SERP top N to AIO overlap = count(SERP top N domains intersect AIO cited domains) / count(SERP top N domains)
```

This is the reverse direction and should not be mixed with the AIO-to-SERP metric.

## Weighting

The headline metrics are domain-instance weighted across all analyzable observations. A supplemental per-observation average is also retained in the research notes because AIO citation counts vary by query.

## Public evidence files

- `data/aggregated/public_aio_serp_overlap_overall.csv`
- `data/aggregated/public_aio_serp_overlap_by_date.csv`
- `data/aggregated/public_aio_serp_overlap_by_client_bucket.csv`
- `data/aggregated/public_aio_serp_top_domains.csv`
