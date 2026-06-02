# Methodology

## Study Design

The study observes AI Search behavior across 10 industries, 3 intent types, 2 models, and 6 consecutive days.

The study sample is derived from an internal GEO tracking system. It is not a full-database export. The public research scope is selected by 10 industry targets, completed runs, and the observation window from 2026-04-27 to 2026-05-02. Each industry contains 9 keywords and 27 prompts. The designed sample contains 3,240 AI responses; after excluding missing or incomplete runs, the public analysis sample contains 3,237 responses.

Intent types:

- Recommendation prompts.
- Comparison prompts.
- Knowledge-oriented prompts.

Intent grouping uses the topic-cluster layer as the final classification source. Equivalent labels such as `推薦類型` are normalized to `推薦型`. Public intent summaries should therefore be read as topic-cluster intent groups, not as a direct copy of the prompt-level `intent_tag` field.

The public package uses aggregate outputs derived from the internal measurement system. Raw response text, run-level exports, API payloads, database files, and private execution metadata are not published.

The internal extraction chain uses topic clusters for industry targets and intent groups, keywords for query subjects, prompts for the actual AI Search questions, and runs for model responses, entity mentions, citations, and search keywords. Public files describe this chain at the aggregate level only.

## Measurement Layers

The research measures:

- Brand / product / platform entity mention count. Public tables may use "brand mention" as a readable shorthand.
- Citation count.
- Citation source category.
- Citation domain stability.
- Brand mention stability.
- Ordered entity-list consistency and rank volatility.
- Search keyword language profile.
- Model and intent differences.

Citation source categories are measured from citation domains, not from entity mentions in the response body. Domain categorization uses the project's domain-classification workflow and domain settings database. The categories include brand or official sites, ecommerce or platform sites, social media, news media, influencer or blogger sources, and other sources. When curated administrative categories are available, they are preferred for public aggregate reporting.

Ordered entity-list consistency is measured separately from entity-set stability. Entity-set stability uses adjacent-day set overlap for the same prompt and model. Ordered consistency keeps the order of entities in `mentions_json` as an approximation of response-order appearance, then compares adjacent days for exact ordered matches, exact unordered set matches, Top-1 matches, Top-3 overlap, and rank volatility. Public outputs aggregate these comparisons and do not publish prompt IDs, run IDs, raw responses, or client IDs.

## Public Reproducibility

Use `data/rosetta/key_findings_rosetta.csv` to trace claims to public evidence tables. Use `data/schema.md` to understand CSV fields. Use `scripts/validate_public_package.py` before publishing the folder.
