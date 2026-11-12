# Release Freeze Window Checker architecture

Checks deployment windows against freeze periods and high-risk launch hours.

```mermaid
flowchart LR
    A["Deploy time and freeze window"]
    B["Compare the time to the freeze and tier-specific policy"]
    C{"Policy blocks the time?"}
    D["Block recommendation"]
    E["Allow recommendation"]
    A --> B --> C
    C -->|Yes| D
    C -->|No| E
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
