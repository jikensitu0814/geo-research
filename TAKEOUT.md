# 公開研究包 Takeout

這份文件是給下載或 clone 此公開研究包的讀者使用的快速交付說明。

## 先讀哪些檔案

1. 先讀 `README.md`，了解 repository 概覽、研究範圍、排除資料與授權。
2. 再讀 `QUICK_REPORT.md`，快速掌握研究摘要與核心數字。
3. 讀 `paper/research_paper.md`，查看完整中文研究論文。
4. 讀 `paper/ai_search_ranking_consistency_article.md`，查看 AI 推薦排序穩定性的公開文章。
5. 用 `data/rosetta/key_findings_rosetta.csv` 將主要結論追溯到公開證據表。

## 這份公開包包含什麼

| 路徑 | 用途 |
| --- | --- |
| `paper/research_paper.md` | 主要中文研究論文 |
| `paper/ai_search_ranking_consistency_article.md` | 關於排名一致性的文章式寫法 |
| `paper/assets/` | 報告與文章使用的公開圖表 |
| `data/aggregated/` | 公開聚合 CSV 表格 |
| `data/rosetta/` | 結論證據、圖表來源、資料範圍與 manifest 對照表 |
| `data/schema.md` | 公開 CSV 欄位定義 |
| `docs/methodology.md` | 抽樣、測量與分類規則 |
| `docs/data_limitations.md` | 公開資料限制 |
| `docs/reproducibility.md` | 可重現性說明 |
| `scripts/validate_public_package.py` | 本地公開包驗證工具 |

## 研究快照

| 指標 | 數值 |
| --- | ---: |
| 研究期間 | 2026-04-27 至 2026-05-02 |
| 產業數 | 10 |
| 意圖類型 | 3 |
| 模型 | ChatGPT, Gemini |
| 研究設計量 | 3,240 筆 AI 回應 |
| 有效分析樣本 | 3,237 筆 AI 回應 |

## 核心 takeaways

1. AI Search visibility 應該被視為重複觀測系統，而不是單次排名結果。
2. Gemini 在本研究中通常使用比 ChatGPT 更寬的引用來源池。
3. 推薦型 prompt 會產生最強的品牌 / 產品 / 平台候選名單。
4. 引用來源類別會因產業與意圖而不同。
5. 實體名單穩定性與 citation domain 穩定性是兩個不同測量層。
6. 相鄰日推薦順序高度不穩定：加權後完全同序率為 4.10%，Top-1 穩定率為 24.10%。

## 如何驗證公開包

從 repository root 執行：

```powershell
cd research_paper\08_to_github
python scripts\validate_public_package.py
```

預期結果：

```text
public package validation passed
```

## 刻意排除哪些資料

- 客戶版產業報告。
- 原始 AI 回應全文。
- SQLite 資料庫。
- 完整 URL inventory。
- 內部 run ID、prompt ID、client ID 與私人執行紀錄。
- API payload、憑證、環境檔或本機 runtime artifacts。

## 如何引用或再利用

這份公開包中的論文、文章、圖表與聚合 CSV 表格可用於研究討論、公開寫作或二次分析。引用數字時，建議優先對照下列 Rosetta 檔案：

- `data/rosetta/key_findings_rosetta.csv`
- `data/rosetta/figure_sources.csv`
- `data/rosetta/dataset_scope.csv`

論文、圖表、文件與聚合資料除非另有標示，採 CC BY 4.0 授權。`scripts/` 內的程式碼採 MIT 授權。
