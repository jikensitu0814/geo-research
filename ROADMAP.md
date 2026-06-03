# Roadmap

這個 repository 目前是一份 AI Search / GEO 公開研究包。後續目標是把它逐步擴展成可重現、可檢查、可維護的 AI Search tracking and validation tool，協助社群理解 ChatGPT UI 搜尋、AI citation、品牌能見度與推薦排序如何變化。

This roadmap also clarifies the open source maintenance surface: public benchmark governance, validation tooling, sensitive-data safety, reproducible analysis scripts, and contribution workflows for prompt sets and measurement ideas.

## 近期目標

- 改善公開包 validator，檢查必要檔案、圖表引用、Rosetta 對照、資料 schema 與敏感資料風險。
- 強化 data release workflow，讓每次公開資料更新前都能執行一致性檢查。
- 建立公開 issue templates，方便回報資料錯誤、文件問題與研究方法疑問。
- 補充英文摘要與更完整的研究引用，方便國際讀者理解研究背景。
- 建立 `v0.1-public-research-snapshot` release，將目前公開研究包標記為第一個可引用 snapshot。
- Define the first public benchmark schema for visibility, citation source mix, Top-3 overlap, and rank volatility tables.
- Expand the validator into a CLI-style maintenance tool for release checks and contribution review.

## 中期目標

- 建立 AI Search / GEO tracking prototype，支援多產業、多 prompt、多模型與多日期追蹤。
- 加入 sensitive data scanner，降低提交 raw responses、API keys、internal IDs、client reports 或 private logs 的風險。
- 產出更標準化的 benchmark tables，讓不同研究者可以比較 visibility、citation source mix、Top-3 overlap 與 rank volatility。
- 改善 citation domain classification workflow，讓網站類別與語言分類更容易檢查與修正。
- 建立 prompt set contribution workflow，讓社群能提案產業、意圖類型、模型介面與評估指標。
- Add reproducible analysis scripts or notebooks that regenerate public aggregate tables from safe intermediate inputs.

## 長期目標

- 擴展到更多產業、更多 prompt 與更長觀測時間，建立可公開引用的 AI Search / GEO longitudinal dataset。
- 比較 ChatGPT、Gemini 與其他 AI Search interfaces 在 citation、brand mention、source selection 與 recommendation order 上的差異。
- 建立 public dashboards 或 notebook examples，協助研究者與網站經營者理解 AI Search visibility。
- 將研究包整理成 preprint-ready paper package，包含英文摘要、正式引用與可重現性說明。
- Publish stable benchmark versions with changelogs so downstream researchers can cite a fixed dataset snapshot.
- Maintain a public validator and sensitive-data checker as reusable tooling for similar AI Search / GEO research packages.

## Why This Matters

AI Search 正在改變使用者如何發現品牌、產品、服務與知識來源。傳統 SEO 的單次排名不足以描述 ChatGPT UI 搜尋與其他 AI Search 系統的行為。這個專案希望用公開資料、可檢查方法與持續維護的工具，幫助社群理解 AI visibility 的生態與邏輯。
