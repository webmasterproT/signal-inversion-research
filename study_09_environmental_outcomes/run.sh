#!/bin/bash
set -e
cd "$(dirname "$0")"
python3 -m venv .venv 2>/dev/null || true
.venv/bin/pip install -r requirements.txt -q
.venv/bin/python src/run.py "$@"
echo "Done. Results in results/"
