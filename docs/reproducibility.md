# Reproducibility

## Public Verification

Run:

```bash
python scripts/validate_public_package.py
```

The validator checks required files, forbidden private artifacts, Markdown image references, Rosetta source references, and internal-term leakage.

## Evidence Mapping

- `data/rosetta/key_findings_rosetta.csv` maps findings to source CSV files.
- `data/rosetta/public_release_manifest.csv` lists included and excluded materials.
- `data/aggregated/` contains public aggregate tables.

## Non-Published Materials

The public release does not include the raw AI outputs, databases, or internal execution traces needed to reconstruct every individual response. The reproducibility target is claim-to-aggregate verification, not raw-response replay.
