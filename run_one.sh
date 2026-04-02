#!/usr/bin/env bash
# ================================================================
# Run a single study
#
# Usage:
#   bash run_one.sh 3          # runs study 3 (belief-reality inversion)
#   bash run_one.sh 7          # runs study 7 (cross-cultural)
#   bash run_one.sh all        # runs all 10
#
# ================================================================

set -e
cd "$(dirname "$0")"

STUDIES=(
    "study_01_trial_testimony"
    "study_02_confession_linguistics"
    "study_03_belief_reality_inversion"
    "study_04_convergence"
    "study_05_four_pillars"
    "study_06_asd_compounding"
    "study_07_cross_cultural"
    "study_08_language_birthplace"
    "study_09_environmental_outcomes"
    "study_10_distillation_framework"
)

STUDY_NAMES=(
    "Trial Testimony Classifier"
    "Confession Linguistics"
    "Belief-Reality Inversion Matrix"
    "Convergent Validity"
    "Four Pillars Framework"
    "ASD Compounding Effect"
    "Cross-Cultural Deception Signals"
    "Language & Birthplace (Census N=1.8B)"
    "Environmental Determination of Outcomes"
    "Distillation Framework"
)

# Check setup
if [ ! -d ".venv" ]; then
    echo "Run setup.sh first:  bash setup.sh"
    exit 1
fi

BASE_DIR="$(cd "$(dirname "$0")" && pwd)"
PYTHON="$BASE_DIR/.venv/bin/python3"

run_study() {
    local num=$1
    local idx=$((num - 1))
    local dir="${STUDIES[$idx]}"
    local name="${STUDY_NAMES[$idx]}"

    if [ ! -d "$dir" ]; then
        echo "ERROR: $dir not found"
        return 1
    fi

    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "  Study $num: $name"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""

    cd "$dir"
    PYTHONPATH="$BASE_DIR/shared:$PYTHONPATH" "$PYTHON" src/run.py
    cd "$BASE_DIR"

    echo ""
    echo "  Results:  $dir/results/"
    echo "  Figures:  $dir/results/figures/"
    echo ""
}

if [ -z "$1" ]; then
    echo "Usage: bash run_one.sh <number>"
    echo ""
    echo "Available studies:"
    for i in "${!STUDIES[@]}"; do
        echo "  $((i+1)). ${STUDY_NAMES[$i]}"
    done
    echo ""
    echo "  all — run all 10 studies"
    exit 0
fi

if [ "$1" = "all" ]; then
    for i in $(seq 1 10); do
        run_study $i
    done
    echo "All 10 studies complete."
else
    NUM=$1
    if [ "$NUM" -lt 1 ] || [ "$NUM" -gt 10 ]; then
        echo "Study number must be 1-10"
        exit 1
    fi
    run_study "$NUM"
fi
