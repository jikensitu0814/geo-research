# Prompt Set Contribution Guide

這份文件定義未來社群提案 AI Search / GEO prompt set 時的最低資訊要求。現階段 repository 不收 raw responses；prompt set contribution 以設計提案、方法論討論與 aggregate benchmark planning 為主。

## Proposal Requirements

每個 prompt set proposal 應說明：

- Target industry or topic area.
- Intent type, such as recommendation, comparison, or knowledge-oriented query.
- Intended AI search interface or model family.
- Expected public metric, such as visibility, citation source mix, Top-3 overlap, or rank volatility.
- Why the prompt set matters for researchers, site operators, or developers.
- How results can be published as aggregate tables without exposing private materials.

## Review Questions

Maintainers should ask:

- Is the proposed prompt set reusable and understandable without private context?
- Can its outputs be summarized as aggregate public metrics?
- Does it add a new industry, intent, language, source type, or stability measurement?
- Does it avoid collecting or publishing private, client-specific, or credential-bearing content?
- Does it fit the benchmark schema in `docs/public_benchmark_schema.md`?

## Non-Accepted Contributions

Do not submit:

- Raw model responses.
- Private customer prompts or reports.
- Credential-bearing request examples.
- Full private URL inventories.
- Local execution traces or database exports.

## Suggested Issue Template

Use `.github/ISSUE_TEMPLATE/benchmark-proposal.md` and include enough public context for maintainers to evaluate the benchmark value and release safety.

