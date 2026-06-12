# Google AIO 引用來源與 SERP 重疊率研究筆記

## 摘要

本研究模組觀察 Google AI Overviews 的引用來源是否與傳統 SERP 前段排名重疊。公開資料只保留匿名聚合統計，不包含原始回應、完整 URL、客戶名稱或內部識別欄位。

## 核心結果

| 指標 | 數值 |
| --- | ---: |
| 關鍵字數量 | 490 |
| 搜尋觀測量 | 12,386 |
| AIO 觸發率 | 80.75% |
| 成功可分析 AIO 觀測量 | 9,693 |
| AIO 引用網域 vs SERP 前 3 | 25.38% |
| AIO 引用網域 vs SERP 前 10 | 62.26% |
| SERP 前 3 網域被 AIO 引用 | 66.22% |
| SERP 前 10 網域被 AIO 引用 | 50.16% |

## 解讀

AIO 引用來源與傳統搜尋結果有明顯關聯，但不是完全由傳統排名決定。AIO 引用網域中有 62.26% 也出現在同次觀測的 SERP 前 10；反向來看，SERP 前 10 網域中有 50.16% 被 AIO 引用。

這兩個方向回答不同問題。AIO-to-SERP 描述 AIO 引用來源有多依賴傳統搜尋結果；SERP-to-AIO 描述傳統排名靠前的網站有多常被 AIO 選為引用來源。

## 文獻對照

Xu et al. (2026) 在 arXiv 論文中回報，AIO reference domains 與 first-page top 10 的平均重疊率為 41.4%，與完整 first page 的重疊率為 70.2%。本研究的 SERP 前 10 重疊率為 62.26%，較高，但樣本來源不同：本研究是商業追蹤樣本，Xu et al. 使用 Google Trends trending queries。

## 公開資料

主要公開證據表位於：

- `data/aggregated/public_aio_serp_overlap_overall.csv`
- `data/aggregated/public_aio_serp_overlap_by_date.csv`
- `data/aggregated/public_aio_serp_overlap_by_client_bucket.csv`
- `data/aggregated/public_aio_serp_top_domains.csv`
