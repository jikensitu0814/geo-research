# Contributing

歡迎針對這份 AI Search / GEO 公開研究包提出 issue、修正文件、改善 validator，或協助設計後續 tracking and validation workflow。

Issues and pull requests are welcome for public data validation, methodology review, benchmark proposals, documentation fixes, and release-safety tooling.

## 可以貢獻什麼

- 修正文檔中的錯字、格式問題或不清楚的研究說明。
- 改善 `scripts/validate_public_package.py` 的公開包檢查規則。
- 補充資料 schema、Rosetta 對照或圖表來源說明。
- 提出 AI Search / GEO 指標建議，例如 visibility、citation stability、Top-3 overlap、rank volatility 等。
- 提出敏感資料掃描、release checklist 或資料安全流程改善建議。
- 提案新的 public benchmark schema、prompt set contribution workflow 或 reproducible analysis scripts。
- 回報 validator 誤判、漏判或錯誤訊息不清楚的情況。

## 不應提交什麼

請不要提交下列資料：

- API keys、tokens、passwords 或任何憑證。
- `.env`、`.db`、`.sqlite`、raw exports、runtime logs 或 private execution traces。
- 原始 AI 回應全文。
- 客戶版產業報告或任何客戶可識別資訊。
- 內部 run ID、prompt ID、client ID、target ID 或私有系統路徑。
- 未授權公開的第三方資料。

## Pull Request 建議

建議使用 `.github/pull_request_template.md` 內的 checklist。若是開 issue，請優先使用下列模板：

- Data error report：回報公開聚合資料、schema 或 Rosetta 對照問題。
- Methodology discussion：討論樣本設計、分類規則、研究限制或指標定義。
- Benchmark proposal：提出新的產業、prompt set、模型介面或 GEO 指標。
- Validator bug report：回報 public package validator 的誤判、漏判或執行問題。

若涉及敏感資料外洩風險，請先閱讀 `SECURITY.md`。不要在 issue 或 PR 中貼出疑似敏感內容。

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
