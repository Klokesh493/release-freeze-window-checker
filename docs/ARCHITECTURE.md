# Release Freeze Window Checker architecture

Checks deployment windows against freeze periods and high-risk launch hours.

```mermaid
flowchart LR
    N0["sample_windows.csv"]
    N1["freeze_window.py"]
    N2["parse time / is blocked / evaluate"]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
