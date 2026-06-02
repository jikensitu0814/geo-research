# Contributing

歡迎針對這份 AI Search / GEO 公開研究包提出 issue、修正文件、改善 validator，或協助設計後續 tracking and validation workflow。

## 可以貢獻什麼

- 修正文檔中的錯字、格式問題或不清楚的研究說明。
- 改善 `scripts/validate_public_package.py` 的公開包檢查規則。
- 補充資料 schema、Rosetta 對照或圖表來源說明。
- 提出 AI Search / GEO 指標建議，例如 visibility、citation stability、Top-3 overlap、rank volatility 等。
- 提出敏感資料掃描、release checklist 或資料安全流程改善建議。

## 不應提交什麼

請不要提交下列資料：

- API keys、tokens、passwords 或任何憑證。
- `.env`、`.db`、`.sqlite`、raw exports、runtime logs 或 private execution traces。
- 原始 AI 回應全文。
- 客戶版產業報告或任何客戶可識別資訊。
- 內部 run ID、prompt ID、client ID、target ID 或私有系統路徑。
- 未授權公開的第三方資料。

## Pull Request 建議

提交 PR 前，請先執行：

```powershell
python scripts\validate_public_package.py
```

預期結果：

```text
public package validation passed
```

如果 PR 修改資料表，請同步檢查：

- `data/schema.md` 是否需要更新。
- `data/rosetta/key_findings_rosetta.csv` 是否仍能對應主要結論。
- `data/rosetta/figure_sources.csv` 是否仍能對應圖表來源。
- README、TAKEOUT 或 QUICK_REPORT 是否需要更新。

## Security Notes

如果你發現可能的安全問題或敏感資料外洩風險，請先開 issue 描述風險類型，不要把疑似敏感內容直接貼在 issue 或 PR 中。這個專案後續會持續強化 sensitive data scanner 與 release validation workflow。
