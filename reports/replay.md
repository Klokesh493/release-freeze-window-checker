# Replay evidence

Captured stdout is compared with a checked-in baseline.

## Demo 1

Result: **PASS**

````text
service,tier,deploy_time,freeze_start,freeze_end,decision
storefront,tier1,2026-07-18T23:10:00,2026-07-18T18:00:00,2026-07-18T23:59:00,block
batch,tier3,2026-07-18T13:30:00,2026-07-18T18:00:00,2026-07-18T23:59:00,allow
````

## Last sample record in isolation

Result: **PASS**

````text
service,tier,deploy_time,freeze_start,freeze_end,decision
batch,tier3,2026-07-18T13:30:00,2026-07-18T18:00:00,2026-07-18T23:59:00,allow
````
