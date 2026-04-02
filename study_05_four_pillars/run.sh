#!/bin/bash
# Study 5: Convergent Validity — The Four Empirical Pillars
# Standalone reproducible analysis
set -euo pipefail
cd "$(dirname "$0")"

echo "=== Study 5: Four Pillars Convergent Validity ==="
echo "Creating virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

echo "Installing dependencies..."
pip install -q -r requirements.txt

echo "Running analysis..."
python3 src/run.py

echo ""
echo "=== Complete ==="
echo "Results:  results/study_5_convergent_validity.txt"
echo "Figure:   results/figures/four_pillars_convergence.png"
