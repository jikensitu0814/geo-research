# Public Benchmark Schema

這份文件定義本 repository 對 AI Search / GEO public benchmark 的最小公開 schema。它不是完整資料庫設計，而是 public release 中可以被引用、檢查與比較的欄位契約。

## Measurement Layers

| Layer | Purpose | Public artifact |
| --- | --- | --- |
| Scope | 研究期間、產業、模型、意圖與樣本數 | `data/rosetta/dataset_scope.csv`, `data/aggregated/public_industry_scope.csv` |
| Visibility | 品牌 / 產品 / 平台實體是否被提及 | `public_model_metrics_by_industry.csv`, `public_model_intent_metrics_by_industry.csv` |
| Citation | citation source mix 與 domain stability | `public_citation_category_by_industry*.csv`, `public_domain_stability_by_industry_intent.csv` |
| Rank stability | 推薦順序、Top-3 overlap 與 rank volatility | `L1_ordered_consistency_by_model_intent.csv`, `L2_ordered_consistency_by_industry_model_intent.csv`, `L3_entity_visibility_rank_stability.csv` |
| Evidence mapping | 結論與圖表可追溯性 | `key_findings_rosetta.csv`, `figure_sources.csv` |

## Required Public Dimensions

New benchmark tables should use these dimensions when applicable:

- `industry`
- `model` or `model_name`
- `intent` or `intent_type`
- study period or date bucket when public and safe
- metric-specific grouping such as `category`, `domain`, or entity label

## Required Metric Families

At least one metric should map to a documented family:

- Visibility: mention rate, mention count, persistence, first-position share.
- Citation: citation count, category share, domain overlap, source mix.
- Rank stability: exact ordered match, unordered set match, Top-1 stability, Top-3 overlap, rank volatility.
- Reproducibility: source file mapping, figure mapping, dataset scope, release manifest.

## Public Release Rules

- Publish aggregate tables only.
- Do not publish raw responses, databases, private reports, runtime traces, credentials, local paths, or full unpublished URL inventories.
- Document any new column in `data/schema.md`.
- Link headline findings to `data/rosetta/key_findings_rosetta.csv`.
- Link figures to `data/rosetta/figure_sources.csv`.
- Run `python scripts\validate_public_package.py` before release.

