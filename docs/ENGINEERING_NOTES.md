# Skills and verification

## What this repository demonstrates

A release calendar check that compares deployment time against the inclusive freeze interval and applies a 22:00–06:00 restriction to Tier 1. It adds an allow or block decision to each CSV row.

## Reproduce the result

The sample blocks storefront at 23:10 and allows the lower-tier batch deployment in the afternoon. Reproduce the primary fixture with `python3 freeze_window.py sample_windows.csv`.

Run `make verify` locally. Ruff and Bandit medium/high checks passed for the checked Python code.

## Scope

The current rule compares clock times. Supply comparable local times and handle overnight freeze intervals or timezone normalization upstream.

Confirm all timestamps use the same timezone and review overnight intervals separately before using a freeze decision operationally.

[freeze_window.py](../freeze_window.py) · [examples/Demo 1.stdout.txt](../examples/Demo%201.stdout.txt) · [Architecture](../docs/ARCHITECTURE.md) · [Case study](../docs/CASE_STUDY.md) · [Runbook](../docs/RUNBOOK.md) · [CI template](../docs/github-actions/ci.yml)
