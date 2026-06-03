from __future__ import annotations

import re
import csv
import fnmatch
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    ".gitignore",
    ".github/ISSUE_TEMPLATE/benchmark-proposal.md",
    ".github/ISSUE_TEMPLATE/data-error-report.md",
    ".github/ISSUE_TEMPLATE/methodology-discussion.md",
    ".github/ISSUE_TEMPLATE/validator-bug-report.md",
    ".github/pull_request_template.md",
    "AGENTS.md",
    "CHANGELOG.md",
    "CITATION.cff",
    "README.md",
    "TAKEOUT.md",
    "ROADMAP.md",
    "CONTRIBUTING.md",
    "MAINTAINERS.md",
    "QUICK_REPORT.md",
    "SECURITY.md",
    "SUPPORT.md",
    "LICENSE.md",
    "LICENSE-CODE-MIT.md",
    "docs/benchmark_governance.md",
    "docs/codex_for_open_source.md",
    "docs/prompt_set_contribution.md",
    "docs/public_benchmark_schema.md",
    "docs/release_checklist.md",
    "docs/release_notes_v0.1.md",
    "paper/research_paper.md",
    "paper/ai_search_ranking_consistency_article.md",
    "data/schema.md",
    "data/rosetta/dataset_scope.csv",
    "data/rosetta/key_findings_rosetta.csv",
    "data/rosetta/figure_sources.csv",
    "data/rosetta/public_release_manifest.csv",
    "docs/methodology.md",
    "docs/data_limitations.md",
    "docs/reproducibility.md",
]

FORBIDDEN_DIRS = [
    "06_insdusty_paper",
    "07_integrated_report",
    "raw",
    "private",
]

FORBIDDEN_SUFFIXES = {
    ".db",
    ".sqlite",
    ".sqlite3",
}

FORBIDDEN_TERMS = [
    "client_id",
    "customer18",
    "geo_tracking_local.db",
    "geo_tracking.db",
    "C:\\Users\\",
    "api.openai.com/v1/responses",
    "generativelanguage.googleapis.com",
    "OPENAI_API_KEY",
    "GOOGLE_API_KEY",
    "GEMINI_API_KEY",
]

RELEASE_TAG = "v0.1-public-research-snapshot"

TEXT_SUFFIXES = {
    ".md",
    ".csv",
    ".txt",
    ".py",
}


def fail(message: str) -> None:
    raise SystemExit(f"public package validation failed: {message}")


def main() -> None:
    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            fail(f"missing required file: {rel}")

    license_text = (ROOT / "LICENSE.md").read_text(encoding="utf-8")
    for marker in ["SPDX-License-Identifier: CC-BY-4.0", "https://creativecommons.org/licenses/by/4.0/legalcode", "己見室 jikensitu"]:
        if marker not in license_text:
            fail(f"LICENSE.md missing marker: {marker}")

    cff_text = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    for marker in ['version: "0.1.0"', 'license: "CC-BY-4.0"', 'repository-code:']:
        if marker not in cff_text:
            fail(f"CITATION.cff missing marker: {marker}")

    release_checklist = (ROOT / "docs" / "release_checklist.md").read_text(encoding="utf-8")
    release_notes = (ROOT / "docs" / "release_notes_v0.1.md").read_text(encoding="utf-8")
    if RELEASE_TAG not in release_checklist or RELEASE_TAG not in release_notes:
        fail(f"release docs missing release tag: {RELEASE_TAG}")

    gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
    for pattern in [".env", ".env.*", "*.db", "*.sqlite", "*.sqlite3", "raw/", "private/"]:
        if pattern not in gitignore:
            fail(f".gitignore missing required pattern: {pattern}")

    manifest_path = ROOT / "data" / "rosetta" / "public_release_manifest.csv"
    with manifest_path.open("r", encoding="utf-8-sig", newline="") as f:
        manifest_rows = list(csv.DictReader(f))
    manifest_included = [
        (row.get("path") or "").strip()
        for row in manifest_rows
        if (row.get("status") or "").strip() == "included"
    ]
    for rel in REQUIRED:
        covered = rel in manifest_included or any(fnmatch.fnmatch(rel, pattern) for pattern in manifest_included)
        if not covered:
            fail(f"public_release_manifest.csv does not include required file: {rel}")

    for rel in FORBIDDEN_DIRS:
        if (ROOT / rel).exists():
            fail(f"forbidden directory present: {rel}")

    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() in FORBIDDEN_SUFFIXES:
            fail(f"database file present: {path.relative_to(ROOT)}")
        if path.name == ".env" or path.name.startswith(".env."):
            if path.name not in {".env.example"}:
                fail(f"environment file present: {path.relative_to(ROOT)}")
        if "__pycache__" in path.parts:
            fail(f"python cache present: {path.relative_to(ROOT)}")

    paper_files = sorted((ROOT / "paper").glob("*.md"))
    all_image_refs = []
    for paper in paper_files:
        text = paper.read_text(encoding="utf-8")
        image_refs = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text)
        all_image_refs.extend((paper, ref) for ref in image_refs)
        for ref in image_refs:
            if not (paper.parent / ref).exists():
                fail(f"missing paper image: {paper.relative_to(ROOT)} -> {ref}")
    if not all_image_refs:
        fail("paper markdown files have no image references")

    aggregated_count = len(list((ROOT / "data" / "aggregated").glob("*.csv")))
    if aggregated_count < 10:
        fail("expected at least 10 aggregated CSV files")

    aggregated_files = {path.name for path in (ROOT / "data" / "aggregated").glob("*.csv")}
    for rosetta_name in ["key_findings_rosetta.csv", "figure_sources.csv"]:
        rosetta_path = ROOT / "data" / "rosetta" / rosetta_name
        with rosetta_path.open("r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                source = (row.get("source_file") or "").strip()
                if source and source.endswith(".csv") and source not in aggregated_files:
                    fail(f"{rosetta_name} references missing source_file: {source}")

    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel == "scripts/validate_public_package.py":
            continue
        content = path.read_text(encoding="utf-8-sig", errors="ignore")
        for term in FORBIDDEN_TERMS:
            if term in content:
                fail(f"forbidden term {term!r} present in {rel}")

    print("public package validation passed")


if __name__ == "__main__":
    main()
