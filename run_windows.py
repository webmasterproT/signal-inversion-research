"""
OMXUS Signal Inversion Research — Run Studies (Windows version)
===============================================================
Same as run_all.sh / run_one.sh but works on Windows without bash.

Usage:
    python3 run_windows.py          # run all 10 studies
    python3 run_windows.py 3        # run just study 3
    python3 run_windows.py 7        # run just study 7 (cross-cultural)
    python run_windows.py           # (same, if python3 doesn't work)
"""

import subprocess
import sys
import os
import glob

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

STUDIES = [
    ("study_01_trial_testimony", "Trial Testimony Classifier"),
    ("study_02_confession_linguistics", "Confession Linguistics"),
    ("study_03_belief_reality_inversion", "Belief-Reality Inversion Matrix"),
    ("study_04_convergence", "Convergent Validity"),
    ("study_05_four_pillars", "Four Pillars Framework"),
    ("study_06_asd_compounding", "ASD Compounding Effect"),
    ("study_07_cross_cultural", "Cross-Cultural Deception Signals"),
    ("study_08_language_birthplace", "Language & Birthplace (Census N=1.8B)"),
    ("study_09_environmental_outcomes", "Environmental Determination"),
    ("study_10_distillation_framework", "Distillation Framework"),
]

# Find Python in venv
venv_dir = os.path.join(HERE, ".venv")
if sys.platform == "win32":
    python_exe = os.path.join(venv_dir, "Scripts", "python.exe")
else:
    python_exe = os.path.join(venv_dir, "bin", "python3")

if not os.path.exists(python_exe):
    print("Run setup first:")
    print("  python3 setup_windows.py")
    sys.exit(1)

shared_dir = os.path.join(HERE, "shared")


def run_study(num):
    idx = num - 1
    dirname, name = STUDIES[idx]
    study_dir = os.path.join(HERE, dirname)
    run_py = os.path.join(study_dir, "src", "run.py")

    if not os.path.exists(run_py):
        print(f"  SKIPPED (no src/run.py)")
        return False

    print()
    print("=" * 55)
    print(f"  Study {num}: {name}")
    print("=" * 55)
    print()

    env = os.environ.copy()
    existing = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = shared_dir + os.pathsep + existing if existing else shared_dir

    result = subprocess.run(
        [python_exe, run_py],
        cwd=study_dir,
        env=env,
    )

    if result.returncode == 0:
        print(f"  PASSED")
        print(f"  Results:  {dirname}/results/")
        print(f"  Figures:  {dirname}/results/figures/")
        return True
    else:
        print(f"  FAILED")
        return False


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "--help" or arg == "-h":
            print("Usage:")
            print("  python3 run_windows.py        # run all 10")
            print("  python3 run_windows.py 3      # run study 3")
            print()
            print("Studies:")
            for i, (d, n) in enumerate(STUDIES, 1):
                print(f"  {i:2d}. {n}")
            sys.exit(0)

        try:
            num = int(arg)
        except ValueError:
            print(f"Unknown argument: {arg}")
            print("Use a number 1-10, or --help")
            sys.exit(1)

        if num < 1 or num > 10:
            print("Study number must be 1-10")
            sys.exit(1)

        run_study(num)
    else:
        # Run all
        passed = 0
        failed = 0
        failed_names = []

        print()
        print("Running all 10 studies...")
        print()

        for i in range(1, 11):
            if run_study(i):
                passed += 1
            else:
                failed += 1
                failed_names.append(STUDIES[i-1][0])

        print()
        print("=" * 55)
        print(f"  RESULTS: {passed} passed, {failed} failed")
        if failed_names:
            print(f"  Failed: {', '.join(failed_names)}")
        else:
            print("  All figures in each study's results/figures/ folder.")
        print("=" * 55)
