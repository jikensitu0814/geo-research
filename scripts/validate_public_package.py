from __future__ import annotations

import re
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "TAKEOUT.md",
    "ROADMAP.md",
    "CONTRIBUTING.md",
    "QUICK_REPORT.md",
    "LICENSE.md",
    "LICENSE-CODE-MIT.md",
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
