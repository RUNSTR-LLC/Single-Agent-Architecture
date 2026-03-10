#!/usr/bin/env python3
from pathlib import Path
import json, sys

if len(sys.argv) < 2:
    print("usage: generate_hourly_prompt.py H00")
    raise SystemExit(1)

hour = sys.argv[1].lower().replace('h','')
base = Path(__file__).resolve().parents[1]
manifest = base / 'jobs' / 'manifests' / f'h{int(hour):02d}-audit.json'
if not manifest.exists() and int(hour) >= 10:
    manifest = base / 'jobs' / 'manifests' / f'h{int(hour)}-pr-attempt-{int(hour)-9}.json'

print(json.dumps(json.loads(manifest.read_text()), indent=2))
