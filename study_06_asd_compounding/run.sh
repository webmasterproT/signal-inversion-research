#!/bin/bash
# Study 6: The ASD Compounding Effect
# Standalone reproducible analysis
set -euo pipefail
cd "$(dirname "$0")"

echo "=== Study 6: ASD Compounding Effect ==="
echo "Creating virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

echo "Installing dependencies..."
pip install -q -r requirements.txt

echo "Running analysis..."
python3 src/run.py

echo ""
echo "=== Complete ==="
echo "Results:  results/study_6_asd_compounding.txt"
echo "Figure:   results/figures/asd_compounding.png"
