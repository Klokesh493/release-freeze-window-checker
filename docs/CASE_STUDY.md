# Release Freeze Window Checker walkthrough

## Business problem

Checks deployment windows against freeze periods and high-risk launch hours.

## Reproduce the workflow

Run `python3 freeze_window.py sample_windows.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
service,tier,deploy_time,freeze_start,freeze_end,decision
storefront,tier1,2026-07-18T23:10:00,2026-07-18T18:00:00,2026-07-18T23:59:00,block
batch,tier3,2026-07-18T13:30:00,2026-07-18T18:00:00,2026-07-18T23:59:00,allow
```

The sample supplies these fields. `service`, `tier`, `deploy_time`, `freeze_start`, `freeze_end`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
