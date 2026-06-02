# AI Search 品牌能見度研究

這個 repository 是一份 AI Search 公開研究快照，觀察生成式 AI 搜尋系統如何提及品牌 / 產品 / 平台實體、如何選擇引用來源，以及同一批 prompt 在多日重複執行時是否穩定。

公開包包含中文研究論文、聚合 CSV 表格、圖表、方法說明與 Rosetta 對照表，方便讀者把研究結論追溯到公開證據。這份公開包刻意排除客戶版產業報告、原始 AI 回應、SQLite 資料庫、內部 run ID、環境檔與私人執行紀錄。

## 先從這裡開始

| 入口 | 檔案 | 用途 |
| --- | --- | --- |
| 公開包 takeout | `TAKEOUT.md` | 給下載或 clone 這份資料的讀者使用的快速交付說明 |
| 主研究論文 | `paper/research_paper.md` | 中文研究論文草稿 |
| 排名一致性文章 | `paper/ai_search_ranking_consistency_article.md` | 關於 AI 推薦排序穩定性的公開文章 |
| 快速報告 | `QUICK_REPORT.md` | 最短閱讀路徑與核心數字 |
| 聚合資料 | `data/aggregated/` | 公開聚合 CSV 表格 |
| 結論對照表 | `data/rosetta/key_findings_rosetta.csv` | 將主要結論對應到公開證據表 |
| 研究方法 | `docs/methodology.md` | 樣本設計、測量層與分類規則 |
| 資料限制 | `docs/data_limitations.md` | 公開資料邊界與限制 |

## 研究快照

| 指標 | 數值 |
| --- | ---: |
| 研究期間 | 2026-04-27 至 2026-05-02 |
| 產業數 | 10 |
| 意圖類型 | 3 |
| 模型 | ChatGPT, Gemini |
| 研究設計量 | 3,240 筆 AI 回應 |
| 有效分析樣本 | 3,237 筆 AI 回應 |
| 公開原始回應全文 | 不包含 |
| 公開 SQLite 資料庫 | 不包含 |

## 主要發現

1. Gemini 在本研究中通常使用比 ChatGPT 更寬的引用來源池。
2. 推薦型 prompt 最容易觸發品牌 / 產品 / 平台候選名單。
3. 部落格、評測、媒體、社群、平台與官方來源在不同產業和意圖中扮演不同角色。
4. 實體名單穩定性與 citation domain 穩定性是兩個不同測量層。
5. ChatGPT 與 Gemini 經常使用不同來源池組裝回答。
6. AI 推薦順序在重複執行時高度不穩定；重複能見度、Top-3 overlap 與 rank volatility 比單次排名更適合追蹤 AI Search visibility。

## Repository 結構

```text
.
├─ paper/
│  ├─ research_paper.md
│  ├─ ai_search_ranking_consistency_article.md
│  └─ assets/
├─ data/
│  ├─ aggregated/
│  ├─ rosetta/
│  └─ schema.md
├─ docs/
├─ scripts/
├─ TAKEOUT.md
├─ QUICK_REPORT.md
├─ LICENSE.md
└─ README.md
```

## 不包含哪些資料

- SQLite 資料庫。
- 原始 AI 回應全文與 run-level exports。
- 客戶版產業報告。
- 完整 URL inventory。
- 環境檔、API key 或任何憑證。
- 內部 client ID、run ID 與私人執行紀錄。
- 簡報渲染快取或本機 office profile。

## License

論文、圖表、文件與聚合資料除非另有標示，採 CC BY 4.0 授權。`scripts/` 內的程式碼採 MIT 授權。
