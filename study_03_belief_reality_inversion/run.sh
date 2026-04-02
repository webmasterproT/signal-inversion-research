#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

echo "Study 3: Belief-Reality Inversion Matrix"
echo "========================================="

if ! command -v python3 &>/dev/null; then
    echo "ERROR: python3 not found"
    exit 1
fi

# Install deps if needed
if ! python3 -c "import pandas, scipy, matplotlib" 2>/dev/null; then
    echo "Installing dependencies..."
    pip3 install -q -r requirements.txt
fi

python3 src/run.py

echo ""
echo "Results:  results/study_3_results.txt"
echo "Figures:  results/figures/"
