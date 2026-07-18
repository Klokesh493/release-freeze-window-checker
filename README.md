# Release Freeze Window Checker

Checks deployment windows against freeze periods and high-risk launch hours.

Focus: Consumer-scale SRE release safety.

Built as a small, runnable Python project with clear input, output, sample data, and tests.

## Run

```bash
python3 freeze_window.py sample_windows.csv
```

## Verify

```bash
python3 -m unittest discover . -v
```
