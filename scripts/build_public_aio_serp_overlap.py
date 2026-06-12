from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in fieldnames})


def pct(numerator: float, denominator: float) -> float:
    return round(numerator / denominator * 100, 2) if denominator else 0.0


def as_int(value: object) -> int:
    try:
        return int(float(str(value)))
    except (TypeError, ValueError):
        return 0


def as_float(value: object) -> float:
    try:
        return float(str(value))
    except (TypeError, ValueError):
        return 0.0


def build_public_tables(source_dir: Path, output_dir: Path) -> None:
    analysis_dir = source_dir / "analysis"
    summary = json.loads((analysis_dir / "overlap_summary.json").read_text(encoding="utf-8"))
    task_rows = read_csv(analysis_dir / "overlap_by_task.csv")
    client_rows = read_csv(analysis_dir / "overlap_by_client.csv")
    top_domain_rows = read_csv(analysis_dir / "top_aio_domains.csv")

    overall_rows = [
        {
            "metric_group": "scope",
            "metric": "client_count",
            "value": 19,
            "unit": "clients",
            "notes": "Distinct customers in the private source data; public release excludes client identifiers.",
        },
        {
            "metric_group": "scope",
            "metric": "client_keyword_count",
            "value": 490,
            "unit": "client_keywords",
            "notes": "Client x keyword count for 2026-05-13 to 2026-06-12.",
        },
        {
            "metric_group": "scope",
            "metric": "crawl_units_keyword_day",
            "value": 12386,
            "unit": "keyword_day_units",
            "notes": "Total keyword-day search records in the requested period.",
        },
        {
            "metric_group": "scope",
            "metric": "aio_triggered_units",
            "value": 10001,
            "unit": "keyword_day_units",
            "notes": "Keyword-day records with Google AIO triggered.",
        },
        {
            "metric_group": "scope",
            "metric": "aio_trigger_rate_pct",
            "value": 80.75,
            "unit": "percent",
            "notes": "AIO triggered units divided by total keyword-day search records.",
        },
        {
            "metric_group": "dataforseo_fetch",
            "metric": "task_total",
            "value": summary["status_unique_tasks"],
            "unit": "tasks",
            "notes": "AIO-triggered DataForSEO task ids requested for retrieval.",
        },
        {
            "metric_group": "dataforseo_fetch",
            "metric": "task_success_analyzable",
            "value": summary["success_tasks"],
            "unit": "tasks",
            "notes": "Tasks successfully retrieved and included in overlap analysis.",
        },
        {
            "metric_group": "dataforseo_fetch",
            "metric": "task_failed_expired",
            "value": summary["failed_tasks"],
            "unit": "tasks",
            "notes": "2026-05-13 tasks returned Results Expired and are excluded from overlap calculations.",
        },
        {
            "metric_group": "overlap_aio_to_serp",
            "metric": "aio_domain_overlap_serp_top3_pct",
            "value": summary["top3_domain_overlap_rate"],
            "unit": "percent",
            "notes": "AIO cited domains that also appear in SERP top 3, domain-instance weighted.",
        },
        {
            "metric_group": "overlap_aio_to_serp",
            "metric": "aio_domain_overlap_serp_top10_pct",
            "value": summary["top10_domain_overlap_rate"],
            "unit": "percent",
            "notes": "AIO cited domains that also appear in SERP top 10, domain-instance weighted.",
        },
        {
            "metric_group": "overlap_serp_to_aio",
            "metric": "serp_top3_domain_cited_by_aio_pct",
            "value": 66.22,
            "unit": "percent",
            "notes": "SERP top 3 domain instances that are also cited by AIO.",
        },
        {
            "metric_group": "overlap_serp_to_aio",
            "metric": "serp_top10_domain_cited_by_aio_pct",
            "value": 50.16,
            "unit": "percent",
            "notes": "SERP top 10 domain instances that are also cited by AIO.",
        },
        {
            "metric_group": "task_level_overlap",
            "metric": "task_with_top3_overlap_pct",
            "value": summary["top3_task_overlap_rate"],
            "unit": "percent",
            "notes": "Tasks with at least one AIO cited domain appearing in SERP top 3.",
        },
        {
            "metric_group": "task_level_overlap",
            "metric": "task_with_top10_overlap_pct",
            "value": summary["top10_task_overlap_rate"],
            "unit": "percent",
            "notes": "Tasks with at least one AIO cited domain appearing in SERP top 10.",
        },
    ]
    write_csv(
        output_dir / "data" / "aggregated" / "public_aio_serp_overlap_overall.csv",
        ["metric_group", "metric", "value", "unit", "notes"],
        overall_rows,
    )

    date_stats: dict[str, Counter] = defaultdict(Counter)
    for row in task_rows:
        date = row["check_date"]
        date_stats[date]["analyzable_aio_tasks"] += 1
        date_stats[date]["tasks_with_aio_refs"] += int(as_int(row["unique_aio_domains"]) > 0)
        date_stats[date]["aio_domain_instances"] += as_int(row["unique_aio_domains"])
        date_stats[date]["serp_top3_domain_instances"] += as_int(row["serp_top3_domains"])
        date_stats[date]["serp_top10_domain_instances"] += as_int(row["serp_top10_domains"])
        date_stats[date]["top3_overlap_domain_instances"] += as_int(row["top3_overlap_domains"])
        date_stats[date]["top10_overlap_domain_instances"] += as_int(row["top10_overlap_domains"])
        date_stats[date]["tasks_with_top3_overlap"] += as_int(row["has_top3_overlap"])
        date_stats[date]["tasks_with_top10_overlap"] += as_int(row["has_top10_overlap"])

    date_rows: list[dict[str, object]] = []
    for date in sorted(date_stats):
        stats = date_stats[date]
        date_rows.append(
            {
                "date": date,
                "analyzable_aio_tasks": stats["analyzable_aio_tasks"],
                "tasks_with_aio_refs": stats["tasks_with_aio_refs"],
                "aio_domain_instances": stats["aio_domain_instances"],
                "serp_top3_domain_instances": stats["serp_top3_domain_instances"],
                "serp_top10_domain_instances": stats["serp_top10_domain_instances"],
                "top3_overlap_domain_instances": stats["top3_overlap_domain_instances"],
                "top10_overlap_domain_instances": stats["top10_overlap_domain_instances"],
                "aio_to_serp_top3_overlap_pct": pct(stats["top3_overlap_domain_instances"], stats["aio_domain_instances"]),
                "aio_to_serp_top10_overlap_pct": pct(stats["top10_overlap_domain_instances"], stats["aio_domain_instances"]),
                "serp_top3_to_aio_overlap_pct": pct(stats["top3_overlap_domain_instances"], stats["serp_top3_domain_instances"]),
                "serp_top10_to_aio_overlap_pct": pct(stats["top10_overlap_domain_instances"], stats["serp_top10_domain_instances"]),
                "task_top3_overlap_pct": pct(stats["tasks_with_top3_overlap"], stats["tasks_with_aio_refs"]),
                "task_top10_overlap_pct": pct(stats["tasks_with_top10_overlap"], stats["tasks_with_aio_refs"]),
            }
        )
    write_csv(
        output_dir / "data" / "aggregated" / "public_aio_serp_overlap_by_date.csv",
        [
            "date",
            "analyzable_aio_tasks",
            "tasks_with_aio_refs",
            "aio_domain_instances",
            "serp_top3_domain_instances",
            "serp_top10_domain_instances",
            "top3_overlap_domain_instances",
            "top10_overlap_domain_instances",
            "aio_to_serp_top3_overlap_pct",
            "aio_to_serp_top10_overlap_pct",
            "serp_top3_to_aio_overlap_pct",
            "serp_top10_to_aio_overlap_pct",
            "task_top3_overlap_pct",
            "task_top10_overlap_pct",
        ],
        date_rows,
    )

    sorted_clients = sorted(client_rows, key=lambda r: (-as_int(r["aio_tasks_analyzed"]), r["client_name"]))
    public_client_rows: list[dict[str, object]] = []
    for index, row in enumerate(sorted_clients, start=1):
        public_client_rows.append(
            {
                "client_bucket": f"client_bucket_{index:02d}",
                "keyword_count": as_int(row["keywords"]),
                "analyzable_aio_tasks": as_int(row["aio_tasks_analyzed"]),
                "tasks_with_aio_refs": as_int(row["tasks_with_refs"]),
                "aio_to_serp_top3_task_overlap_pct": as_float(row["top3_task_overlap_rate"]),
                "aio_to_serp_top10_task_overlap_pct": as_float(row["top10_task_overlap_rate"]),
                "aio_to_serp_top3_domain_overlap_pct": as_float(row["top3_domain_overlap_rate"]),
                "aio_to_serp_top10_domain_overlap_pct": as_float(row["top10_domain_overlap_rate"]),
            }
        )
    write_csv(
        output_dir / "data" / "aggregated" / "public_aio_serp_overlap_by_client_bucket.csv",
        [
            "client_bucket",
            "keyword_count",
            "analyzable_aio_tasks",
            "tasks_with_aio_refs",
            "aio_to_serp_top3_task_overlap_pct",
            "aio_to_serp_top10_task_overlap_pct",
            "aio_to_serp_top3_domain_overlap_pct",
            "aio_to_serp_top10_domain_overlap_pct",
        ],
        public_client_rows,
    )

    public_domain_rows = [
        {
            "domain_rank": idx,
            "hostname": row["domain"],
            "aio_reference_rows": as_int(row["aio_reference_rows"]),
            "aio_tasks": as_int(row["aio_tasks"]),
            "serp_top20_rows": as_int(row["serp_top20_rows"]),
        }
        for idx, row in enumerate(top_domain_rows[:50], start=1)
    ]
    write_csv(
        output_dir / "data" / "aggregated" / "public_aio_serp_top_domains.csv",
        ["domain_rank", "hostname", "aio_reference_rows", "aio_tasks", "serp_top20_rows"],
        public_domain_rows,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Build public aggregate AIO/SERP overlap tables.")
    parser.add_argument(
        "--source-dir",
        required=True,
        help="Private source analysis directory. Do not commit this source data.",
    )
    parser.add_argument(
        "--output-dir",
        default=str(Path(__file__).resolve().parents[1]),
        help="Public geo-research repository root.",
    )
    args = parser.parse_args()
    build_public_tables(Path(args.source_dir), Path(args.output_dir))
    print("public AIO/SERP aggregate tables written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
