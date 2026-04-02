#!/usr/bin/env bash
# ================================================================
# OMXUS Signal Inversion Research — One-Click Setup
# ================================================================
#
# This sets up everything you need to reproduce all 10 studies.
#
# WHAT YOU NEED:
#   - Python 3.10 or newer (check: python3 --version)
#   - That's it. Seriously.
#
# WHAT THIS DOES:
#   1. Creates a virtual environment (keeps your system clean)
#   2. Installs all the maths/stats libraries
#   3. Tells you what to do next
#
# HOW TO USE:
#   bash setup.sh          # set everything up
#   bash run_all.sh        # run all 10 studies
#   bash run_one.sh 3      # run just study 3
#
# If anything goes wrong, read the error. It's probably:
#   - Python not installed  → google "install python 3" for your system
#   - Permission denied     → try: chmod +x setup.sh && bash setup.sh
#
# ================================================================

set -e
cd "$(dirname "$0")"

echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║  OMXUS Signal Inversion Research — Setup                ║"
echo "║  10 studies proving credibility assessment is inverted   ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# Check Python
if ! command -v python3 &>/dev/null; then
    echo "ERROR: python3 not found."
    echo ""
    echo "Install Python 3.10+:"
    echo "  Mac:     brew install python3"
    echo "  Ubuntu:  sudo apt install python3 python3-venv python3-pip"
    echo "  Windows: https://www.python.org/downloads/"
    echo ""
    exit 1
fi

PY_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
echo "Found Python $PY_VERSION"

# Check version is 3.10+
PY_MAJOR=$(python3 -c "import sys; print(sys.version_info.major)")
PY_MINOR=$(python3 -c "import sys; print(sys.version_info.minor)")
if [ "$PY_MAJOR" -lt 3 ] || ([ "$PY_MAJOR" -eq 3 ] && [ "$PY_MINOR" -lt 10 ]); then
    echo "WARNING: Python 3.10+ recommended. You have $PY_VERSION."
    echo "Things might still work, but no promises."
    echo ""
fi

# Create venv
echo ""
echo "Creating virtual environment..."
python3 -m venv .venv

echo "Installing dependencies..."
.venv/bin/pip install --upgrade pip -q
.venv/bin/pip install -q \
    numpy \
    scipy \
    pandas \
    matplotlib \
    scikit-learn \
    seaborn \
    nltk

# Download NLTK data for study_07 (cross-cultural needs tokenizer)
echo "Downloading language data for cross-cultural study..."
.venv/bin/python3 -c "import nltk; nltk.download('punkt', quiet=True); nltk.download('punkt_tab', quiet=True); nltk.download('stopwords', quiet=True)" 2>/dev/null || true

echo ""
echo "══════════════════════════════════════════════════════════"
echo ""
echo "  SETUP COMPLETE"
echo ""
echo "  To run ALL 10 studies:"
echo "    bash run_all.sh"
echo ""
echo "  To run just one study (e.g. study 3):"
echo "    bash run_one.sh 3"
echo ""
echo "  To run one study manually:"
echo "    source .venv/bin/activate"
echo "    cd study_03_belief_reality_inversion"
echo "    python3 src/run.py"
echo ""
echo "  Results appear in each study's results/ folder."
echo "  Figures appear in each study's results/figures/ folder."
echo ""
echo "══════════════════════════════════════════════════════════"
