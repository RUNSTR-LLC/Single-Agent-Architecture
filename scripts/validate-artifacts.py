#!/usr/bin/env python3
from pathlib import Path
import json, sys

status = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('runtime/hourly/status.json')
if not status.exists():
    print('MISSING_STATUS')
    raise SystemExit(1)

obj = json.loads(status.read_text())
required = ['hour','action','outcome','blocked','updated_at']
missing = [k for k in required if k not in obj]
if missing:
    print('INVALID_STATUS', ','.join(missing))
    raise SystemExit(1)
print('STATUS_OK')
