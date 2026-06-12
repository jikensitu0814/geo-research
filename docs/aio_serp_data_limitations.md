# AIO / SERP Data Limitations

## Public data boundary

This public module contains aggregate evidence only. It excludes raw DataForSEO payloads, raw AIO text, full URL inventories, private execution logs, customer names, and internal identifiers.

## Retrieval window

DataForSEO task retrieval is time-limited. The 2026-05-13 observations were available in the private task index but returned `Results Expired.` during retrieval, so they are counted in the requested scope but excluded from overlap calculations.

## SERP definition

The public overlap metrics use the normalized SERP rows produced from DataForSEO results. Top 3 and top 10 are based on the normalized rank order in the private analysis pipeline.

## Domain-level comparison

The public metrics compare hostnames, not full pages. A match means the same normalized hostname appears in both AIO citations and SERP results for the same observation. It does not prove that AIO cited the same page URL or passage.

## Sample interpretation

The sample is a commercial tracking sample rather than a general web query sample. It should be compared with external studies as directional evidence, not as a population-level estimate for all Google searches.
