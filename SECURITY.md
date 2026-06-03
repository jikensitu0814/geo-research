# Security Policy

## Supported Scope

This repository is a public research package. Security review focuses on release safety and accidental disclosure prevention.

In scope:

- Credentials or environment files accidentally added to the repository.
- Raw responses, private reports, databases, runtime traces, local paths, or internal identifiers accidentally included in public files.
- Validator gaps that allow private artifacts to pass release checks.
- Public documentation that encourages unsafe handling of private data.

Out of scope:

- Requests for unpublished raw responses.
- Requests for client-specific analysis or private execution records.
- General SEO or GEO consulting requests unrelated to this public package.

## Reporting

Open an issue that describes the risk category without copying sensitive content into the issue body. If the risk requires sharing private evidence, contact the maintainer through https://jikensitu.com/ first and wait for a safe exchange path.

## Release Safety

Before each public release, run:

```powershell
python scripts\validate_public_package.py
```

The expected result is:

```text
public package validation passed
```

