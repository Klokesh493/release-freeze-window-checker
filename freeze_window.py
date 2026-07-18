import csv
from datetime import datetime, time
import sys


def parse_time(value):
    return datetime.fromisoformat(value).time()


def is_blocked(row):
    deploy_time = parse_time(row["deploy_time"])
    freeze_start = parse_time(row["freeze_start"])
    freeze_end = parse_time(row["freeze_end"])
    tier = row["tier"].lower()
    risky_hour = deploy_time >= time(22, 0) or deploy_time < time(6, 0)
    in_freeze = freeze_start <= deploy_time <= freeze_end
    return in_freeze or (tier == "tier1" and risky_hour)


def evaluate(rows):
    return [{**row, "decision": "block" if is_blocked(row) else "allow"} for row in rows]


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        rows = evaluate(csv.DictReader(handle))
    writer = csv.DictWriter(sys.stdout, fieldnames=[*rows[0].keys()])
    writer.writeheader()
    writer.writerows(rows)


if __name__ == "__main__":
    main(sys.argv[1])
