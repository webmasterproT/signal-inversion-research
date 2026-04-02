#!/bin/bash
# ================================================================
# OMXUS Signal Inversion Research — Run All 10 Studies
# ================================================================
#
# Prerequisites: run setup.sh first
#
# What this does:
#   Runs all 10 studies in order. Each one analyses its data,
#   runs the statistics, generates figures, and saves results.
#
# Takes about 2-5 minutes depending on your machine.
#
# ================================================================

set -e
cd "$(dirname "$0")"

# Check setup
if [ ! -d ".venv" ]; then
    echo "Run setup.sh first:  bash setup.sh"
    exit 1
fi

BASE_DIR="$(cd "$(dirname "$0")" && pwd)"
PYTHON="$BASE_DIR/.venv/bin/python3"
PASS=0
FAIL=0
FAILED=""

echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║  Running all 10 studies                                  ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

for study_dir in study_*/; do
    study_name=$(basename "$study_dir")
    num=$(echo "$study_name" | grep -o '^study_[0-9]*' | grep -o '[0-9]*')

    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "  Study $num: $study_name"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    if [ -f "$study_dir/src/run.py" ]; then
        if (cd "$study_dir" && PYTHONPATH="$BASE_DIR/shared:$PYTHONPATH" "$PYTHON" src/run.py); then
            echo "  PASSED"
            PASS=$((PASS + 1))
        else
            echo "  FAILED"
            FAIL=$((FAIL + 1))
            FAILED="$FAILED $study_name"
        fi
    else
        echo "  SKIPPED (no src/run.py)"
    fi
    echo ""
done

echo "══════════════════════════════════════════════════════════"
echo ""
echo "  RESULTS: $PASS passed, $FAIL failed"
if [ $FAIL -gt 0 ]; then
    echo "  Failed:$FAILED"
    echo ""
    exit 1
fi
echo ""
echo "  All figures are in each study's results/figures/ folder."
echo ""
echo "══════════════════════════════════════════════════════════"
