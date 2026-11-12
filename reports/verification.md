# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 freeze_window.py sample_windows.csv
service,tier,deploy_time,freeze_start,freeze_end,decision
storefront,tier1,2026-07-18T23:10:00,2026-07-18T18:00:00,2026-07-18T23:59:00,block
batch,tier3,2026-07-18T13:30:00,2026-07-18T18:00:00,2026-07-18T23:59:00,allow
test_blocks_tier1_late_deploy (test_freeze_window.FreezeWindowTest) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
````
