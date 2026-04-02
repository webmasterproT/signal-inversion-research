#!/bin/bash
# Study 4: Human vs Algorithmic Deception Detection — Convergence
# Standalone reproducible analysis
set -euo pipefail
cd "$(dirname "$0")"

echo "=== Study 4: Convergence Analysis ==="
echo "Creating virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

echo "Installing dependencies..."
pip install -q -r requirements.txt

echo "Running analysis..."
python3 src/run.py

echo ""
echo "=== Complete ==="
echo "Results:  results/study_4_convergence.txt"
echo "Figure:   results/figures/convergence_accuracy.png"
