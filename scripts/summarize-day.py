#!/usr/bin/env python3
from pathlib import Path
import json

runtime = Path('runtime/proofs')
count = len(list(runtime.glob('*.json'))) if runtime.exists() else 0
print(json.dumps({'proof_files': count}, indent=2))
