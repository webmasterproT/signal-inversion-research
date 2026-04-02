# Can Courts Actually Detect Lies? (Spoiler: No)

**10 studies. 450,000+ words of evidence. You can run them all yourself.**

This is reproducible research proving that the "deception cues" used in courts, police interrogations, and jury rooms are scientifically inverted — they flag truthful people as liars and let actual liars pass. It's worse for people of colour, autistic people, and non-native English speakers.

Every result here is reproducible. You don't need a science degree. You don't need to trust us. Run it yourself and see.

---

## Quick Start

### Step 1: Get the files

**Option A — Download (easiest)**
Click the green "Code" button on this page → "Download ZIP" → unzip it somewhere you'll find it.

**Option B — Git clone (if you know what that means)**
```
git clone https://github.com/omxus/signal-inversion-research.git
cd signal-inversion-research
```

### Step 2: Install Python (if you don't have it)

Open your terminal:
- **Mac**: Press `Cmd + Space`, type `Terminal`, press Enter
- **Windows**: Press the Windows key, type `cmd`, press Enter
- **Linux**: You already know

Check if Python is installed:
```
python3 --version
```

If it says "command not found" or gives you a version below 3.10:

| System | How to install Python |
|--------|---------------------|
| **Mac** | Go to [python.org/downloads](https://www.python.org/downloads/), download, double-click, follow the prompts. Done. |
| **Windows** | Go to [python.org/downloads](https://www.python.org/downloads/), download, **tick "Add to PATH" during install** (important!), follow the prompts. Then close and reopen your terminal. |
| **Linux** | `sudo apt install python3 python3-venv python3-pip` (Ubuntu/Debian) or `sudo dnf install python3` (Fedora) |

### Step 3: Run everything

Navigate to where you put the files. If you unzipped to your Downloads folder:
```
cd ~/Downloads/signal-inversion-research
```

On Windows, it's more like:
```
cd C:\Users\YourName\Downloads\signal-inversion-research
```

Then:
```
bash setup.sh
```

**Windows users**: If `bash` doesn't work, try:
```
python3 setup_windows.py
```

This installs the maths libraries (numpy, scipy, etc.) into a little box so it doesn't mess with anything else on your computer. Takes about 1-2 minutes.

Then run the studies:
```
bash run_all.sh
```

Or just one (pick a number 1-10):
```
bash run_one.sh 3
```

**Windows users**: If bash doesn't work:
```
python3 run_windows.py
```

Results and figures appear in each study's `results/` folder.

---

## What's In Each Study

| # | Study | One-line summary |
|---|-------|-----------------|
| 1 | **Trial Testimony** | Trained a computer on the same "deception cues" courts use. It couldn't tell truth from lies. |
| 2 | **Confession Linguistics** | The words in false confessions look the opposite of what experts expect. |
| 3 | **Belief vs Reality** | 74% of the things people think indicate lying actually indicate truth-telling. 75 countries, 11,227 people surveyed. |
| 4 | **Convergence** | All the studies point the same direction. Not a fluke. |
| 5 | **Four Pillars** | Four completely independent lines of evidence. All say the same thing. |
| 6 | **Autism Compounding** | Autistic people's natural behaviour — less eye contact, different tone — maps perfectly onto what courts call "deceptive." |
| 7 | **Cross-Cultural** | A Mexican person telling the truth looks "deceptive" to a white American jury. Same for Romanian, Indian speakers. The cues are culturally specific. |
| 8 | **Language & Birthplace** | Where you're born determines what language you speak. Not your genes. N=1.8 billion. |
| 9 | **Your Postcode Predicts Your Life** | Environmental determination — your address predicts your outcomes better than anything about you personally. |
| 10 | **The Framework** | Ties it all together. Consensus mechanisms for evidence. |

Each study folder has a `WHAT_THIS_PROVES.md` that explains it in plain language.

---

## Troubleshooting

**"python3: command not found"**
→ Python isn't installed. See Step 2 above.

**"No module named 'numpy'" or similar**
→ Run `bash setup.sh` first. It installs everything you need.

**"Permission denied"**
→ Try: `chmod +x setup.sh run_all.sh run_one.sh` then try again.

**"bash: command not found" (Windows)**
→ Use the Python versions instead: `python3 setup_windows.py` and `python3 run_windows.py`

**It worked before but now it doesn't**
→ You probably moved to a different folder. `cd` back to where the files are and try again.

**I don't understand the output**
→ Read the `WHAT_THIS_PROVES.md` in each study folder. It explains everything without jargon.

**Something else is wrong**
→ Open an issue on this repo, or email claw@omxus.com. We'll actually help you. No judgement.

---

## For Researchers

- **Stats**: Mann-Whitney U, Chi-square, Kruskal-Wallis H, binomial tests, Spearman correlation, Monte Carlo simulation, SVM, logistic regression, meta-analysis
- **Data**: All CSV, all included, no external downloads needed
- **Citation**: See `CITATION.cff`
- **Shared figure style**: `shared/style.py` — consistent palette, fonts, DPI across all figures
- **Raw materials**: `constructed_guilt_analysis/`, `legacy_classifiers/`, `legacy_thesis/` contain earlier iterations and raw working code

---

## Why This Matters

Courts send people to prison based on whether they "look like they're lying." This research proves — with data anyone can check — that those judgments are scientifically backwards.

If you're autistic, you look guilty by default.
If you're not white, you look guilty by default.
If English isn't your first language, you look guilty by default.

This isn't opinion. Run the numbers yourself.

---

*By Alex Applebee & L. N. Combe | OMXUS Research*
*Licensed under CC BY 4.0 — use it, share it, build on it.*
