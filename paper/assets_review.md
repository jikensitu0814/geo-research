# Paper Figure Review

Generated for `assets_preview.pdf`.

## Overall Judgment

The figure set is useful as a GitHub research snapshot, but not all figures are equally suitable for a formal paper or arXiv-style preprint. Figures based directly on data are strongest. Synthesis diagrams are useful for explanation, but some should be simplified or moved to appendix if the paper is submitted academically.

## Figure-Level Review

| Figure | File | Judgment | Recommendation |
| --- | --- | --- | --- |
| Fig. 1 | `08_geo_tracking_system_architecture.png` | Keep, but simplify for paper | Good method overview. For formal submission, reduce text density and use a cleaner pipeline diagram. |
| Fig. 2 | `09_measurement_layer_schema.png` | Keep in methods or appendix | Useful schema bridge. It is explanatory rather than empirical; acceptable in methods. |
| Fig. 3 | `10_sample_construction_funnel.png` | Keep | Strong figure. It clarifies the 4,127 / 4,019 / 3,240 / 3,237 sample-count distinction. |
| Fig. 4 | `11_analysis_matrix.png` | Optional | Good for readers, but more like a framework slide. Consider moving to appendix if space is limited. |
| Fig. 5 | `01_overall_model_comparison.png` | Keep | Empirical and central to the paper. Add exact source table in caption. |
| Fig. 6 | `04_citation_category_distribution.png` | Keep | Empirical and central. Consider adding exact percentages to improve standalone readability. |
| Fig. 7 | `02_industry_visibility_matrix.png` | Keep, but improve label collision | Important empirical figure. Some labels may be crowded; formal version should use larger canvas or facet by model. |
| Fig. 8 | `03_intent_pattern.png` | Keep | Strong empirical figure that supports intent differences. |
| Fig. 9 | `05_domain_stability_heatmap.png` | Keep | Important for cross-day stability claims. Good fit for paper. |
| Fig. 10 | `06_brand_stability_heatmap.png` | Keep | Important for stability claims. Good fit for paper. |
| Fig. 11 | `07_cross_industry_domains.png` | Keep | Useful empirical summary. Consider limiting labels or adding a table companion. |
| Fig. 12 | `12_model_strategy_matrix.png` | Move to discussion or appendix | This is a synthesized strategy diagram, not primary evidence. Good for GitHub report, weaker for formal paper. |
| Fig. 13 | `13_industry_geo_priority_matrix.png` | Use cautiously | This is partly interpretive. If submitted academically, explain scoring method or move to appendix. |
| Fig. 14 | `14_key_findings_evidence_table.png` | Convert to table | Better as a Markdown/LaTeX table than an image, especially for formal paper accessibility and citation. |
| Fig. 15 | `15_reproducibility_flow.png` | Keep in appendix | Useful reproducibility diagram. For formal submission, make it cleaner and less presentation-like. |

## Best Figures for Formal Paper Main Text

Use these in the main text first:

1. Fig. 3 Sample Construction and Cleaning Funnel
2. Fig. 5 ChatGPT vs Gemini Overall Difference
3. Fig. 6 Citation Category Distribution
4. Fig. 7 Industry Visibility Matrix
5. Fig. 8 Intent Pattern
6. Fig. 9 Domain Stability Heatmap
7. Fig. 10 Brand Stability Heatmap
8. Fig. 11 Cross-Industry Domains

## Figures Better Suited to Appendix

- Fig. 1 System Architecture
- Fig. 2 Measurement Layer
- Fig. 4 Analysis Matrix
- Fig. 12 Model Strategy Matrix
- Fig. 13 Industry GEO Priority Matrix
- Fig. 15 Reproducibility Flow

## Figure to Convert

- Fig. 14 should become a real table in the paper, not an image.

## Publication Readiness Notes

- Captions should be English if the paper is submitted internationally.
- Every empirical figure should state the exact source CSV in the caption.
- Avoid strategy diagrams unless clearly marked as discussion synthesis.
- Use vector PDF/SVG or high-resolution PNG for final submission.
- For LaTeX, prefer placing figures under `figures/` and referencing them via `\\includegraphics`.
