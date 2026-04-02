#!/usr/bin/env bash
set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

echo "=== Study 2: Confession Linguistics ==="

# Create venv if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

echo "Installing dependencies..."
.venv/bin/pip install -q -r requirements.txt

echo "Running analysis..."
.venv/bin/python src/run.py

echo ""
echo "=== Complete ==="
echo "Results: results/study_2_results.txt"
echo "Figure:  results/figures/confession_word_ratios.png"
