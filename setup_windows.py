"""
OMXUS Signal Inversion Research — Setup (Windows version)
=========================================================
Same as setup.sh but works on Windows without bash.

Usage:
    python3 setup_windows.py
    python setup_windows.py
"""

import subprocess
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

print()
print("=" * 58)
print("  OMXUS Signal Inversion Research — Setup")
print("  10 studies proving credibility assessment is inverted")
print("=" * 58)
print()

# Check Python version
v = sys.version_info
print(f"Found Python {v.major}.{v.minor}.{v.micro}")
if v.major < 3 or (v.major == 3 and v.minor < 10):
    print("WARNING: Python 3.10+ recommended. Things might still work.")
print()

# Create venv
venv_dir = os.path.join(HERE, ".venv")
if sys.platform == "win32":
    python_exe = os.path.join(venv_dir, "Scripts", "python.exe")
    pip_exe = os.path.join(venv_dir, "Scripts", "pip.exe")
else:
    python_exe = os.path.join(venv_dir, "bin", "python3")
    pip_exe = os.path.join(venv_dir, "bin", "pip")

print("Creating virtual environment...")
subprocess.run([sys.executable, "-m", "venv", venv_dir], check=True)

print("Installing dependencies...")
subprocess.run([pip_exe, "install", "--upgrade", "pip", "-q"], check=True)
subprocess.run([pip_exe, "install", "-q",
    "numpy", "scipy", "pandas", "matplotlib",
    "scikit-learn", "seaborn", "nltk"
], check=True)

# NLTK data
print("Downloading language data...")
subprocess.run([python_exe, "-c",
    "import nltk; nltk.download('punkt', quiet=True); "
    "nltk.download('punkt_tab', quiet=True); "
    "nltk.download('stopwords', quiet=True)"
], check=False)

print()
print("=" * 58)
print()
print("  SETUP COMPLETE")
print()
print("  To run all 10 studies:")
print("    python3 run_windows.py")
print()
print("  To run just one study (e.g. study 3):")
print("    python3 run_windows.py 3")
print()
print("=" * 58)
