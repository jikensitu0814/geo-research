# Release Checklist

這份 checklist 用於維護 AI Search / GEO public research package，並記錄本次為 Codex for Open Source 申請所做的 repo 治理強化。

## v0.1-public-research-snapshot 準備

- [x] 確認公開包 validator 可執行。
- [x] 確認公開包不包含原始 AI 回應、SQLite、客戶報告、私人執行紀錄或憑證。
- [x] 修正 GitHub license 顯示問題，讓主授權更容易被辨識。
- [x] 補上 `.gitignore`，明確排除環境檔、database、raw exports、logs 與本機快取。
- [x] 補上 GitHub issue templates 與 PR template，強化社群維護訊號。
- [x] 補上 AGENTS.md，記錄 Codex 協作、UTF-8、secrets 與 validator 規範。
- [x] 更新 README 與 ROADMAP，清楚呈現 public benchmark、validator、sensitive-data checker 與 tracking prototype 方向。
- [x] 執行 `python scripts\validate_public_package.py` 並確認通過。
- [x] 補上 citation、maintainer、security、support、changelog 與 release notes，讓 repo 更接近可維護 OSS 研究專案。
- [x] 補上 Codex for Open Source 申請敘事與 benchmark governance 文件。
- [x] 補上 public benchmark schema 與 prompt set contribution guide 初版。
- [x] 將新增治理檔案納入 validator required files。
- [ ] 建立 GitHub Release：`v0.1-public-research-snapshot`。

## Release Gate

每次公開 release 前，維護者需確認：

- `data/aggregated/` 僅包含聚合 CSV。
- `data/rosetta/` 的 evidence mapping 可追溯公開資料來源。
- 文件、圖表與研究結論沒有引用未公開的客戶資料或 raw responses。
- `.gitignore` 仍排除 `.env`、database、logs、raw exports 與本機快取。
- validator 輸出為 `public package validation passed`。

## Codex for Open Source Notes

本 repo 的 Codex 使用重點是降低維護公開研究包的重複成本：

- 檢查 CSV schema 與 Rosetta mapping。
- 檢查敏感資料是否誤入公開包。
- 協助產生 release notes 與 changelog。
- 協助 review data / docs / scripts PR。
- 協助維護可重現分析與未來 validator CLI。
