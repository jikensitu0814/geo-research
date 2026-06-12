# Public Data Schema

This public release contains aggregate tables only. It does not include raw AI responses, SQLite databases, full URL inventories, or run-level exports.

## Core Public Tables

| File | Description |
| --- | --- |
| `public_industry_scope.csv` | Per-industry study period and sample counts |
| `public_model_metrics_by_industry.csv` | Brand / product / platform entity mentions and citation counts by industry and model |
| `public_model_intent_metrics_by_industry.csv` | Brand / product / platform entity mentions and citation counts by industry, model, and intent |
| `public_model_intent_metrics_overall.csv` | Overall model and intent summary |
| `public_citation_category_by_industry.csv` | Citation category distribution by industry |
| `public_citation_category_by_industry_model_intent.csv` | Citation category distribution by industry, model, and intent |
| `C_brand_mention_s1_category.csv` | Citation category mix split by whether an answer contains brand mentions |
| `public_domain_stability_by_industry_intent.csv` | Citation domain cross-day stability |
| `public_brand_stability_by_industry_intent.csv` | Brand mention cross-day stability |
| `public_search_keyword_language_by_industry.csv` | Search keyword language profile |
| `L1_ordered_consistency_by_model_intent.csv` | Ordered entity-list consistency by model and intent |
| `L2_ordered_consistency_by_industry_model_intent.csv` | Ordered entity-list consistency by industry, model, and intent |
| `L3_entity_visibility_rank_stability.csv` | Entity visibility, average position, first-position share, persistence, and rank volatility |

## Rosetta Tables

| File | Description |
| --- | --- |
| `dataset_scope.csv` | Study scope and public data boundaries |
| `key_findings_rosetta.csv` | Maps each major finding to evidence |
| `figure_sources.csv` | Maps retained figures to source data |
| `public_release_manifest.csv` | Included and excluded files |

## Common Fields

| Field | Meaning |
| --- | --- |
| `industry` | Industry group |
| `model_name` / `model` | ChatGPT or Gemini |
| `intent_type` / `intent` | Recommendation, comparison, or knowledge-oriented intent |
| `avg_mention_count` | Average detected brand / product / platform entity mentions per response; public reports may use brand mention as shorthand |
| `avg_citation_count` | Average citations per response |
| `category` | Citation source category, measured from citation domains rather than response-body mentions |
| `domain` | Citation source domain when published |
| `adjacent_day_overlap_pct` | Adjacent-day Jaccard overlap percentage |
| `citation_share_pct` | Citation category share |
| `adjacent_pair_count` | Number of adjacent-day prompt/model pairs compared |
| `exact_same_ordered_list_pct` | Percentage of adjacent-day pairs with the same entity list and the same order |
| `exact_same_unordered_set_pct` | Percentage of adjacent-day pairs with the same entity set regardless of order |
| `top1_same_pct` | Percentage of adjacent-day pairs where the first mentioned entity is the same |
| `avg_top3_overlap_pct` | Average overlap percentage between adjacent-day Top-3 entity sets |
| `avg_entity_set_jaccard_pct` | Average adjacent-day Jaccard overlap for entity sets |
| `avg_rank_volatility` / `rank_volatility` | Average absolute rank-position change for entities appearing in both adjacent-day lists |
| `visibility_pct` | Percentage of runs in which the entity is mentioned |
| `avg_pos` | Average zero-based mention position for the entity when present |
| `pct_first` | Percentage of entity mentions where the entity appears first |

## AIO / SERP Overlap Tables

| File | Description |
| --- | --- |
| `public_aio_serp_overlap_overall.csv` | Overall public AIO/SERP overlap metrics and study scope |
| `public_aio_serp_overlap_by_date.csv` | Daily anonymized AIO/SERP overlap metrics |
| `public_aio_serp_overlap_by_client_bucket.csv` | Anonymous customer-bucket overlap distribution |
| `public_aio_serp_top_domains.csv` | Top public hostnames appearing in AIO citations |

## AIO / SERP Fields

| Field | Meaning |
| --- | --- |
| `metric_group` | Metric family such as scope, retrieval, or overlap direction |
| `metric` | Machine-readable metric name |
| `value` | Public aggregate metric value |
| `unit` | Unit such as percent, tasks, hostnames, or keyword-day observations |
| `date` | Observation date for daily public aggregates |
| `client_bucket` | Anonymous stable customer bucket; does not identify a customer |
| `keyword_count` | Number of tracked keyword labels in an anonymous bucket |
| `analyzable_aio_tasks` | AIO-triggered observations successfully retrieved for overlap analysis |
| `tasks_with_aio_refs` | Analyzable observations with at least one AIO citation hostname |
| `aio_domain_instances` | AIO citation hostnames after per-observation hostname normalization |
| `serp_top3_domain_instances` | SERP top 3 hostnames after per-observation hostname normalization |
| `serp_top10_domain_instances` | SERP top 10 hostnames after per-observation hostname normalization |
| `top3_overlap_domain_instances` | AIO citation hostnames that also appear in SERP top 3 |
| `top10_overlap_domain_instances` | AIO citation hostnames that also appear in SERP top 10 |
| `aio_to_serp_top3_overlap_pct` | Share of AIO citation hostnames also appearing in SERP top 3 |
| `aio_to_serp_top10_overlap_pct` | Share of AIO citation hostnames also appearing in SERP top 10 |
| `serp_top3_to_aio_overlap_pct` | Share of SERP top 3 hostnames also cited by AIO |
| `serp_top10_to_aio_overlap_pct` | Share of SERP top 10 hostnames also cited by AIO |
| `hostname` | Public citation hostname, without URL path inventory |
