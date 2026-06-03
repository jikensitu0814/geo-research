# AGENTS.md

## 回應與編輯規範

- 對本 repository 的協作請以繁體中文回應。
- 讀寫文件時使用 UTF-8，避免中文內容產生亂碼。
- 修改前先確認公開資料邊界：本 repo 不收錄原始 AI 回應、SQLite 資料庫、客戶報告、私人執行紀錄或憑證。
- 規劃修改方案時，將流程與 checklist 記錄於 `docs/`。
- 進行修改時同步更新 checklist 狀態，避免只留下口頭紀錄。

## 安全與資料邊界

- `.env` 與 `.env.*` 必須留在 `.gitignore`，不得提交。
- 使用環境變數管理任何憑證或私有設定，不得硬編碼 secrets、tokens、passwords 或服務金鑰。
- 不提交 database、raw exports、runtime logs、完整 URL inventory、內部 ID、客戶可識別資訊或本機路徑。
- 發現敏感資料風險時，先描述風險類型，不要在 issue 或 PR 中貼出疑似敏感內容。

## 驗證

提交前至少執行：

```powershell
python scripts\validate_public_package.py
```

預期輸出：

```text
public package validation passed
```

若修改資料表、圖表或研究結論，需同步檢查 `data/schema.md`、`data/rosetta/key_findings_rosetta.csv`、`data/rosetta/figure_sources.csv`、`README.md`、`TAKEOUT.md` 與 `QUICK_REPORT.md`。

