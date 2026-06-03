# Quick Report

## 這份公開包是什麼

這是 AI Search 品牌能見度研究的公開快照，觀察 ChatGPT 與 Gemini 在 10 個產業、3 種 prompt 意圖、6 天追蹤期間中如何提及品牌與引用來源。

## 快速閱讀路徑

1. 先讀 `TAKEOUT.md` 了解公開包包含什麼、如何驗證、哪些資料刻意排除。
2. 再讀 `paper/research_paper.md` 了解研究問題、方法與整體結論。
3. 再讀 `paper/ai_search_ranking_consistency_article.md` 了解 AI 推薦排序一致性。
4. 用 `data/rosetta/key_findings_rosetta.csv` 對照結論與證據表。
5. 用 `data/aggregated/` 檢查公開聚合統計。
6. 需要方法與限制時，閱讀 `docs/methodology.md` 與 `docs/data_limitations.md`。
7. 需要了解 benchmark schema、prompt contribution、release 或 Codex OSS 申請定位時，閱讀 `docs/public_benchmark_schema.md`、`docs/prompt_set_contribution.md`、`docs/release_checklist.md` 與 `docs/codex_for_open_source.md`。

## 核心數字

| 項目 | 數值 |
| --- | ---: |
| 研究期間 | 2026-04-27 至 2026-05-02 |
| 產業數 | 10 |
| 意圖類型 | 3 |
| 模型 | ChatGPT, Gemini |
| 研究設計量 | 3,240 筆 AI 回應 |
| 有效分析樣本 | 3,237 筆 AI 回應 |

## 重要限制

公開包保留品牌 / 產品 / 平台實體、domain 與聚合統計，但不包含客戶版產業報告、原始 AI 回應全文、SQLite 資料庫、完整 URL inventory、內部 run ID、API key 或環境變數。這是一份靜態研究快照，不代表目前即時 AI Search 結果。

## OSS 維護狀態

這份 snapshot 已補上 citation metadata、changelog、maintainer notes、security policy、support scope、GitHub issue templates、PR checklist 與 public package validator。建議第一個 release tag 為 `v0.1-public-research-snapshot`。
