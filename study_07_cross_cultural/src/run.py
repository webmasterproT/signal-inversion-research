"""
Study 7: Cross-Cultural Variation in Truthful Speech Patterns
==============================================================
Signal Inversion Analysis — Constructed Guilt thesis, Appendix Section 6
Authors: Alex Applebee and L. N. Combe

Extends the core analysis to demonstrate that truthful speech patterns
vary significantly by cultural background — meaning any deception-detection
system calibrated on a dominant cultural baseline will systematically
misread minority speakers as deceptive.

Datasets used:
    1. Cross-Cultural Deception (Pérez-Rosas & Mihalcea, 2014)
       US, India, Mexico, Romania — essays on abortion, death penalty, best friend
       curl -L "https://web.eecs.umich.edu/~mihalcea/downloads/crossCulturalDeception.2014.tar.gz" -o crossCultural.tar.gz
       tar -xzf crossCultural.tar.gz -C data/crossCultural/

    2. Open-Domain Deception (Pérez-Rosas & Mihalcea, 2015)
       512 users, 7 lies + 7 truths each, with demographic data
       curl -L "https://web.eecs.umich.edu/~mihalcea/downloads/openDeception.2015.tar.gz" -o openDeception.tar.gz
       tar -xzf openDeception.tar.gz -C data/openDomain/

Thesis argument:
    Step 1 — Within truthful speech, cultural background predicts linguistic pattern.
             (If hedging/certainty/disfluency differ by culture among truth-tellers,
              a monocultural classifier misidentifies cultural difference as deception.)

    Step 2 — A classifier trained on one cultural group misidentifies truthful
             speakers from another group at a significantly higher rate.
             (The instrument is not broken — the design is the problem.)

Run:
    ./run.sh
    # or: python3 src/run.py
"""

import os
import re
import glob
import sys
import warnings
import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu, kruskal, f_oneway
from scipy.stats import pointbiserialr
from itertools import combinations
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import nltk

# Shared OMXUS figure style (optional — works without it)
try:
    import sys as _sys
    _sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'shared'))
    from style import apply_style, COLORS, save_figure
    apply_style()
    _HAS_STYLE = True
except ImportError:
    _HAS_STYLE = False

warnings.filterwarnings('ignore')

# Resolve project root (one level up from src/)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

for pkg in ['punkt', 'punkt_tab', 'stopwords', 'averaged_perceptron_tagger']:
    try:
        nltk.download(pkg, quiet=True)
    except Exception:
        pass

try:
    from nltk.tokenize import word_tokenize, sent_tokenize
except Exception:
    word_tokenize = lambda t: t.lower().split()
    sent_tokenize = lambda t: t.split('.')

# Create output directories relative to project root
os.makedirs(os.path.join(PROJECT_ROOT, "results", "figures"), exist_ok=True)
os.makedirs(os.path.join(PROJECT_ROOT, "results", "cultural"), exist_ok=True)


# ═════════════════════════════════════════════════════════════════════════
# FEATURE DEFINITIONS  (same as core pipeline for consistency)
# ═════════════════════════════════════════════════════════════════════════

HEDGING = [
    "i think", "i believe", "i'm not sure", "i'm not certain",
    "as far as i", "i guess", "i suppose", "maybe", "perhaps",
    "possibly", "probably", "it seems", "kind of", "sort of",
    "approximately", "around", "roughly", "about", "i thought",
    "i assumed", "if i recall", "if i remember", "to my knowledge",
    "i may be wrong", "i could be wrong", "not sure but",
    "i'm fairly certain", "i think i", "i believe i"
]

CERTAINTY = [
    "definitely", "absolutely", "certainly", "clearly", "obviously",
    "without doubt", "no doubt", "i know", "i knew", "i'm certain",
    "i'm sure", "i'm positive", "for sure", "100 percent", "100%",
    "without question", "undoubtedly", "i am sure", "there's no way",
    "i can tell you", "i guarantee", "trust me", "i swear",
    "i promise", "believe me"
]

FILLERS = [
    r'\bum\b', r'\buh\b', r'\bahh?\b', r'\bumm\b',
    r'\byou know\b', r'\bi mean\b', r'\blike\b', r'\bwell\b',
    r'\.\.\.', r'--'
]

EXPERIENCER = [
    "i felt", "i saw", "i heard", "i noticed", "i realized",
    "i remember", "i could see", "i could feel", "i was scared",
    "it felt", "it looked", "my heart", "my hands", "i started to"
]


def extract_features(text):
    text_lower = text.lower()
    try:
        words = word_tokenize(text_lower)
    except Exception:
        words = text_lower.split()
    n_words = max(len(words), 1)

    def rate(patterns, is_regex=False):
        count = 0
        if is_regex:
            for pat in patterns:
                count += len(re.findall(pat, text_lower))
        else:
            for p in patterns:
                count += text_lower.count(p)
        return (count / n_words) * 100

    hedging    = rate(HEDGING)
    certainty  = rate(CERTAINTY)
    fillers    = rate(FILLERS, is_regex=True)
    experience = rate(EXPERIENCER)

    fp_words   = ['i', 'me', 'my', 'mine', 'myself']
    fp_rate    = (sum(1 for w in words if w in fp_words) / n_words) * 100
    hedge_cert = hedging / (certainty + 0.001)

    return {
        'hedging_rate':          hedging,
        'certainty_rate':        certainty,
        'filler_rate':           fillers,
        'experiencer_rate':      experience,
        'hedge_certainty_ratio': hedge_cert,
        'first_person_rate':     fp_rate,
        'word_count':            n_words,
    }


# ═════════════════════════════════════════════════════════════════════════
# DATASET 1: OPEN-DOMAIN DECEPTION
# ═════════════════════════════════════════════════════════════════════════

def load_open_domain(base_dir):
    """
    Expected layout after extraction:
        data/openDomain/
            deception_data.csv   OR
            lies/  + truths/     OR
            users/ with per-user files

    The dataset includes demographic columns: gender, age,
    country_of_origin / country, education_level / education
    """
    records = []

    # Try CSV first (most likely layout)
    csv_files = glob.glob(os.path.join(base_dir, "**", "*.csv"), recursive=True)
    for csv_path in csv_files:
        try:
            df = pd.read_csv(csv_path, encoding='utf-8', errors='ignore')

            # Identify relevant columns
            text_col    = next((c for c in df.columns if any(x in c.lower()
                           for x in ['text', 'statement', 'essay', 'content', 'lie', 'truth'])), None)
            label_col   = next((c for c in df.columns if any(x in c.lower()
                           for x in ['label', 'class', 'deceptive', 'truthful', 'truth', 'lie'])), None)
            country_col = next((c for c in df.columns if any(x in c.lower()
                           for x in ['country', 'origin', 'nationality', 'culture'])), None)
            gender_col  = next((c for c in df.columns if 'gender' in c.lower() or 'sex' in c.lower()), None)
            age_col     = next((c for c in df.columns if 'age' in c.lower()), None)
            edu_col     = next((c for c in df.columns if 'edu' in c.lower()), None)

            if not text_col:
                continue

            for _, row in df.iterrows():
                text = str(row[text_col]).strip()
                if len(text) < 10:
                    continue

                # Determine label
                label = None
                if label_col:
                    raw = str(row[label_col]).lower()
                    if any(x in raw for x in ['1', 'lie', 'deceptive', 'false', 'd']):
                        label = 1
                    elif any(x in raw for x in ['0', 'truth', 'true', 'honest', 't']):
                        label = 0

                feats = extract_features(text)
                feats['label']         = label
                feats['label_str']     = ('Deceptive' if label == 1
                                          else 'Truthful' if label == 0
                                          else 'Unknown')
                feats['country']       = str(row[country_col]).strip() if country_col else 'Unknown'
                feats['gender']        = str(row[gender_col]).strip()  if gender_col  else 'Unknown'
                feats['age']           = str(row[age_col]).strip()     if age_col     else 'Unknown'
                feats['education']     = str(row[edu_col]).strip()     if edu_col     else 'Unknown'
                feats['dataset']       = 'open_domain'
                feats['topic']         = 'open_domain'
                records.append(feats)

        except Exception as e:
            continue

    # Try txt files with folder-based labelling
    for label_name, label_val in [('lies', 1), ('truths', 0), ('lie', 1), ('truth', 0)]:
        folder = os.path.join(base_dir, label_name)
        for txt_path in glob.glob(os.path.join(folder, "*.txt")):
            try:
                text = open(txt_path, encoding='utf-8', errors='ignore').read().strip()
                if len(text) < 10:
                    continue
                feats = extract_features(text)
                feats['label']     = label_val
                feats['label_str'] = 'Deceptive' if label_val == 1 else 'Truthful'
                feats['country']   = 'Unknown'
                feats['gender']    = 'Unknown'
                feats['dataset']   = 'open_domain'
                feats['topic']     = 'open_domain'
                records.append(feats)
            except Exception:
                continue

    return pd.DataFrame(records) if records else pd.DataFrame()


# ═════════════════════════════════════════════════════════════════════════
# DATASET 2: CROSS-CULTURAL DECEPTION
# ═════════════════════════════════════════════════════════════════════════

KNOWN_CULTURES = ['us', 'usa', 'america', 'india', 'mexico', 'romania',
                  'mexican', 'indian', 'romanian', 'american']

def infer_culture_from_path(path):
    path_lower = path.lower()
    for c in ['india', 'mexico', 'romania', 'us', 'usa']:
        if c in path_lower:
            return c.upper() if c in ['us', 'usa'] else c.capitalize()
    return 'Unknown'


def load_cross_cultural(base_dir):
    """
    Expected layout:
        data/crossCultural/
            US/
                abortion/  lies/ truths/
                death_penalty/ ...
                best_friend/ ...
            India/ Mexico/ Romania/  (same structure)
    """
    records = []

    def process_one_text(text, path_lower, culture, label, topic):
        if len(text) < 10:
            return
        feats = extract_features(text)
        feats['label']     = label
        feats['label_str'] = 'Deceptive' if label == 1 else 'Truthful'
        feats['country']   = culture
        feats['topic']     = topic
        feats['dataset']   = 'cross_cultural'
        records.append(feats)

    # Walk all txt files
    for txt_path in glob.glob(os.path.join(base_dir, "**", "*.txt"), recursive=True):
        try:
            text = open(txt_path, encoding='utf-8', errors='ignore').read().strip()
            path_lower = txt_path.lower()
            culture    = infer_culture_from_path(txt_path)
            if any(x in path_lower for x in ['lie', 'decep', 'false']):
                label = 1
            elif any(x in path_lower for x in ['truth', 'true', 'honest']):
                label = 0
            else:
                continue
            topic = 'unknown'
            for t in ['abortion', 'death_penalty', 'death', 'best_friend', 'friend']:
                if t in path_lower:
                    topic = t
                    break
            process_one_text(text, path_lower, culture, label, topic)
        except Exception:
            continue

    # Extensionless .True / .False files (Pérez-Rosas 2014: id\tstatement per line)
    for fpath in glob.glob(os.path.join(base_dir, "**", "*"), recursive=True):
        if not os.path.isfile(fpath) or os.path.basename(fpath).startswith('.'):
            continue
        path_lower = fpath.lower()
        if '.true' not in path_lower and '.false' not in path_lower:
            continue
        if fpath.endswith('.txt') or fpath.endswith('.csv'):
            continue
        try:
            culture = infer_culture_from_path(fpath)
            label   = 0 if '.true' in path_lower else 1
            topic   = 'unknown'
            for t in ['abortion', 'death_penalty', 'death', 'best_friend', 'friend', 'ab', 'dp', 'bf']:
                if t in path_lower:
                    topic = t
                    break
            with open(fpath, encoding='utf-8', errors='ignore') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    # id\tstatement format
                    if '\t' in line:
                        text = line.split('\t', 1)[1].strip()
                    else:
                        text = line
                    process_one_text(text, path_lower, culture, label, topic)
        except Exception:
            continue

    # Also try CSV layout
    for csv_path in glob.glob(os.path.join(base_dir, "**", "*.csv"), recursive=True):
        try:
            df = pd.read_csv(csv_path, encoding='utf-8', errors='ignore')
            text_col    = next((c for c in df.columns if any(x in c.lower()
                           for x in ['text', 'essay', 'content', 'statement'])), None)
            label_col   = next((c for c in df.columns if any(x in c.lower()
                           for x in ['label', 'class', 'truth', 'lie'])), None)
            country_col = next((c for c in df.columns if any(x in c.lower()
                           for x in ['country', 'culture', 'origin'])), None)
            topic_col   = next((c for c in df.columns if 'topic' in c.lower()), None)

            if not text_col:
                continue

            for _, row in df.iterrows():
                text = str(row[text_col]).strip()
                if len(text) < 10:
                    continue
                label = None
                if label_col:
                    raw = str(row[label_col]).lower()
                    label = 1 if any(x in raw for x in ['1', 'lie', 'deceptive']) else 0

                feats = extract_features(text)
                feats['label']     = label
                feats['label_str'] = 'Deceptive' if label == 1 else 'Truthful'
                feats['country']   = str(row[country_col]) if country_col else infer_culture_from_path(csv_path)
                feats['topic']     = str(row[topic_col]) if topic_col else 'unknown'
                feats['dataset']   = 'cross_cultural'
                records.append(feats)
        except Exception:
            continue

    return pd.DataFrame(records) if records else pd.DataFrame()


# ═════════════════════════════════════════════════════════════════════════
# CORE ANALYSIS: TRUTHFUL SPEECH VARIES BY CULTURE
# ═════════════════════════════════════════════════════════════════════════

FEATURES = [
    ('hedging_rate',          'Hedging Rate'),
    ('certainty_rate',        'Certainty Rate'),
    ('filler_rate',           'Disfluency Rate'),
    ('hedge_certainty_ratio', 'Hedge:Certainty Ratio'),
    ('first_person_rate',     'First-Person Rate'),
    ('word_count',            'Word Count'),
]

COLOURS_CULTURE = {
    'US':      '#1f77b4',
    'India':   '#ff7f0e',
    'Mexico':  '#2ca02c',
    'Romania': '#d62728',
    'Unknown': '#9467bd',
}


def analyse_cultural_variation(df, dataset_name, out_prefix):
    """
    KEY ANALYSIS: Among truthful speakers only, do linguistic features
    differ significantly by cultural background?

    If YES: any monocultural detection system will produce structurally
    higher false-positive rates for minority culture truth-tellers.
    """
    results = []

    # Filter to truthful only
    truth_df = df[df['label'] == 0].copy()
    cultures = [c for c in truth_df['country'].unique()
                if c not in ('Unknown', 'nan', '') and len(truth_df[truth_df['country'] == c]) >= 5]

    if len(cultures) < 2:
        print(f"  ⚠  {dataset_name}: fewer than 2 cultures with enough data. Skipping cultural test.")
        return pd.DataFrame()

    print(f"\n  {dataset_name} — Cultures found: {cultures}")
    print(f"  Truthful N per culture:")
    for c in cultures:
        print(f"    {c}: n={len(truth_df[truth_df['country']==c])}")

    for feat, label in FEATURES:
        groups = [truth_df[truth_df['country'] == c][feat].dropna().values
                  for c in cultures]
        groups = [g for g in groups if len(g) >= 3]

        if len(groups) < 2:
            continue

        # Kruskal-Wallis (non-parametric ANOVA)
        try:
            stat, p = kruskal(*groups)
        except Exception:
            continue

        # Pairwise Mann-Whitney with Bonferroni correction
        pairwise = []
        n_pairs  = len(list(combinations(cultures, 2)))
        for c1, c2 in combinations(cultures, 2):
            g1 = truth_df[truth_df['country'] == c1][feat].dropna().values
            g2 = truth_df[truth_df['country'] == c2][feat].dropna().values
            if len(g1) < 3 or len(g2) < 3:
                continue
            u, p_pair = mannwhitneyu(g1, g2, alternative='two-sided')
            p_bonf    = min(p_pair * n_pairs, 1.0)
            d         = (np.mean(g1) - np.mean(g2)) / (
                np.sqrt((np.std(g1, ddof=1)**2 + np.std(g2, ddof=1)**2) / 2) + 0.001
            )
            pairwise.append(f"{c1} vs {c2}: d={d:.2f}, p={p_bonf:.3f}{'*' if p_bonf < .05 else ''}")

        results.append({
            'Feature':            label,
            'Kruskal-Wallis H':   f"{stat:.2f}",
            'p (cultures differ)': f"{'<.001' if p < .001 else f'{p:.3f}'}",
            'Significant':        'YES ✓' if p < .05 else 'no',
            'Pairwise':           ' | '.join(pairwise),
        })

    return pd.DataFrame(results)


def plot_cultural_boxplots(df, dataset_name, out_prefix):
    """
    Box plots of hedging and certainty by culture, TRUTHFUL ONLY.
    This is the core visualisation of the thesis argument.
    """
    truth_df = df[df['label'] == 0].copy()
    cultures = [c for c in truth_df['country'].unique()
                if c not in ('Unknown', 'nan', '') and len(truth_df[truth_df['country']==c]) >= 5]

    if len(cultures) < 2:
        return

    fig, axes = plt.subplots(1, 3, figsize=(14, 6))
    fig.suptitle(
        f'Truthful Speech Patterns by Cultural Background\n{dataset_name}\n'
        'If these differ significantly: any monocultural detector will misidentify minority speakers',
        fontsize=11, fontweight='bold'
    )

    plot_feats = [
        ('hedging_rate',          'Hedging Rate (per 100 words)'),
        ('certainty_rate',        'Certainty Rate (per 100 words)'),
        ('hedge_certainty_ratio', 'Hedge:Certainty Ratio'),
    ]

    colour_list = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

    for ax, (feat, label) in zip(axes, plot_feats):
        data_by_culture = [truth_df[truth_df['country'] == c][feat].dropna().values
                           for c in cultures]

        bp = ax.boxplot(
            data_by_culture,
            labels=cultures,
            patch_artist=True,
            medianprops=dict(color='black', linewidth=2),
            widths=0.55
        )
        for patch, colour in zip(bp['boxes'], colour_list):
            patch.set_facecolor(colour)
            patch.set_alpha(0.7)

        for i, (data, c) in enumerate(zip(data_by_culture, cultures), 1):
            jitter = np.random.uniform(-0.15, 0.15, len(data))
            ax.scatter(np.full(len(data), i) + jitter, data,
                       alpha=0.3, s=18,
                       color=colour_list[i-1], zorder=3)

        ax.set_title(label, fontsize=10, fontweight='bold')
        ax.set_xlabel('Culture')
        ax.tick_params(axis='x', rotation=20)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        # Kruskal-Wallis annotation
        try:
            groups = [g for g in data_by_culture if len(g) >= 3]
            if len(groups) >= 2:
                stat, p = kruskal(*groups)
                p_str = 'p < .001' if p < .001 else f'p = {p:.3f}'
                colour = 'darkgreen' if p < .05 else 'grey'
                ax.text(0.98, 0.97, f'Kruskal-Wallis\n{p_str}',
                        transform=ax.transAxes, ha='right', va='top',
                        fontsize=8, color=colour)
        except Exception:
            pass

    plt.tight_layout()
    path = os.path.join(PROJECT_ROOT, "results", "figures", f"{out_prefix}_cultural_boxplots.png")
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {path}")


def plot_cross_classifier_error(df, out_prefix):
    """
    Simulate: train a 'cultural baseline' on US truthful patterns,
    classify other cultures' truthful speakers using that baseline.
    Show false-positive rate by culture.

    Method: Define 'Anglo baseline' as mean hedging/certainty among US truthful.
    Flag a speaker as 'deceptive' if their hedge:certainty ratio falls
    more than 1 SD below the US truthful mean (i.e. they look confident/rehearsed
    by US standards). Count false positives by culture.
    """
    truth_df = df[df['label'] == 0].copy()
    us_truth  = truth_df[truth_df['country'].str.upper().isin(['US', 'USA'])]

    if len(us_truth) < 5:
        print("  ⚠  Not enough US data for cross-classifier simulation.")
        return

    us_mean = us_truth['hedge_certainty_ratio'].mean()
    us_sd   = us_truth['hedge_certainty_ratio'].std(ddof=1)
    threshold = us_mean - us_sd  # 1 SD below US truthful mean

    cultures = [c for c in truth_df['country'].unique()
                if c not in ('Unknown', 'nan', '') and len(truth_df[truth_df['country']==c]) >= 5]

    fp_rates = {}
    for c in cultures:
        subset = truth_df[truth_df['country'] == c]['hedge_certainty_ratio'].dropna()
        if len(subset) == 0:
            continue
        # "False positive" = truthful speaker flagged as deceptive by US baseline
        fp_rate = (subset < threshold).mean() * 100
        fp_rates[c] = fp_rate

    if not fp_rates:
        return

    fig, ax = plt.subplots(figsize=(9, 5))
    cultures_sorted = sorted(fp_rates, key=fp_rates.get, reverse=True)
    colours = ['#d62728' if c.upper() in ['US', 'USA'] else '#1f77b4'
               for c in cultures_sorted]
    bars = ax.bar(cultures_sorted, [fp_rates[c] for c in cultures_sorted],
                  color=colours, alpha=0.8)

    ax.axhline(fp_rates.get('US', fp_rates.get('USA', 0)),
               color='grey', linestyle='--', linewidth=1, alpha=0.7,
               label='US baseline false-positive rate')

    ax.set_ylabel('False-Positive Rate (%) — truthful speakers flagged as deceptive', fontsize=10)
    ax.set_title(
        'Cross-Cultural False Positive Rate\n'
        'Truthful speakers from each culture classified by US linguistic norms\n'
        'Higher bar = more innocent people read as deceptive',
        fontsize=11, fontweight='bold'
    )
    ax.legend(fontsize=9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    for bar, c in zip(bars, cultures_sorted):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f"{fp_rates[c]:.1f}%", ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    path = os.path.join(PROJECT_ROOT, "results", "figures", f"{out_prefix}_cross_classifier_fp.png")
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {path}")


# ═════════════════════════════════════════════════════════════════════════
# DEMO DATA (run if real data not found)
# ═════════════════════════════════════════════════════════════════════════

def generate_demo_cultural():
    """Synthetic data with realistic cross-cultural hedging variation."""
    np.random.seed(99)
    records = []

    # Hedging patterns by culture — based on LIWC literature:
    # US:      moderate hedging (Anglo direct style)
    # India:   higher hedging (deference norms in English)
    # Mexico:  lower certainty, higher experiencer framing
    # Romania: lower hedging, more formal assertion
    culture_params = {
        'US':      {'h': 3.2, 'c': 2.1},
        'India':   {'h': 5.1, 'c': 1.4},
        'Mexico':  {'h': 2.8, 'c': 3.3},
        'Romania': {'h': 1.9, 'c': 2.8},
    }

    for culture, params in culture_params.items():
        for i in range(40):
            for label, lbl_str in [(0, 'Truthful'), (1, 'Deceptive')]:
                h = np.random.normal(params['h'] + (0.5 if label == 0 else -0.5), 1.0)
                c = np.random.normal(params['c'] + (-0.3 if label == 0 else 0.8), 0.9)
                records.append({
                    'label':              label,
                    'label_str':          lbl_str,
                    'country':            culture,
                    'topic':              np.random.choice(['abortion', 'death_penalty', 'best_friend']),
                    'dataset':            'cross_cultural',
                    'hedging_rate':       max(h, 0),
                    'certainty_rate':     max(c, 0),
                    'filler_rate':        np.random.normal(4.5 if label == 0 else 3.0, 1.2),
                    'experiencer_rate':   np.random.normal(3.0, 1.0),
                    'hedge_certainty_ratio': max(h, 0) / (max(c, 0) + 0.001),
                    'first_person_rate':  np.random.normal(7.5, 2.0),
                    'word_count':         int(np.random.normal(130, 30)),
                })

    return pd.DataFrame(records)


# ═════════════════════════════════════════════════════════════════════════
# MAIN
# ═════════════════════════════════════════════════════════════════════════

def main():
    print("\n" + "=" * 65)
    print("STUDY 7: CROSS-CULTURAL VARIATION IN TRUTHFUL SPEECH")
    print("Signal Inversion Analysis — Constructed Guilt Appendix")
    print("=" * 65)

    all_results = {}

    # ── Dataset 1: Open-Domain ────────────────────────────────────────
    print("\n── Dataset 1: Open-Domain Deception ────────────────────────")
    od_dir = os.path.join(PROJECT_ROOT, "data", "openDomain")
    od_df = load_open_domain(od_dir)
    if od_df.empty or 'label' not in od_df.columns:
        print("  ⚠  Open-Domain data not found. Download instructions:")
        print("     curl -L 'https://web.eecs.umich.edu/~mihalcea/downloads/openDeception.2015.tar.gz' -o openDeception.tar.gz")
        print("     tar -xzf openDeception.tar.gz -C data/openDomain/")
    else:
        print(f"  Loaded {len(od_df)} statements")
        results = analyse_cultural_variation(od_df, "Open-Domain Deception", "openDomain")
        if not results.empty:
            all_results['open_domain'] = results
            plot_cultural_boxplots(od_df, "Open-Domain Deception (Pérez-Rosas & Mihalcea, 2015)", "openDomain")
            plot_cross_classifier_error(od_df, "openDomain")

    # ── Dataset 2: Cross-Cultural ─────────────────────────────────────
    print("\n── Dataset 2: Cross-Cultural Deception ─────────────────────")
    cc_dir = os.path.join(PROJECT_ROOT, "data", "crossCultural")
    cc_df = load_cross_cultural(cc_dir)
    if cc_df.empty or 'label' not in cc_df.columns:
        print("  ⚠  Cross-Cultural data not found. Download instructions:")
        print("     curl -L 'https://web.eecs.umich.edu/~mihalcea/downloads/crossCulturalDeception.2014.tar.gz' -o crossCultural.tar.gz")
        print("     tar -xzf crossCultural.tar.gz -C data/crossCultural/")
        print("\n  Running on DEMO DATA for pipeline validation...")
        cc_df = generate_demo_cultural()
        print(f"  Demo: {len(cc_df)} synthetic statements")

    results = analyse_cultural_variation(cc_df, "Cross-Cultural Deception", "crossCultural")
    if not results.empty:
        all_results['cross_cultural'] = results
        plot_cultural_boxplots(cc_df, "Cross-Cultural Deception (Pérez-Rosas & Mihalcea, 2014)", "crossCultural")
        plot_cross_classifier_error(cc_df, "crossCultural")

    # ── Save results ──────────────────────────────────────────────────
    print("\n── Saving results ───────────────────────────────────────────")
    results_path = os.path.join(PROJECT_ROOT, "results", "cultural", "cultural_analysis.txt")
    with open(results_path, "w") as f:
        f.write("=" * 70 + "\n")
        f.write("STUDY 7: CROSS-CULTURAL VARIATION IN TRUTHFUL SPEECH — RESULTS\n")
        f.write("Signal Inversion Analysis — Constructed Guilt, Appendix Section 6\n")
        f.write("Authors: Alex Applebee and L. N. Combe\n")
        f.write("=" * 70 + "\n\n")
        f.write("THESIS ARGUMENT:\n")
        f.write("If truthful speech patterns differ significantly by cultural background,\n")
        f.write("then any deception-detection instrument calibrated on a dominant cultural\n")
        f.write("baseline will produce structurally higher false-positive rates for\n")
        f.write("minority speakers — not because they lie more, but because their truth\n")
        f.write("is linguistically illegible to the instrument.\n\n")
        f.write("Applied to Australia: An Aboriginal witness whose truthful speech follows\n")
        f.write("different hedging/disfluency norms than the Anglo baseline will be read\n")
        f.write("as deceptive. Guilt is being constructed from cultural identity.\n\n")

        for name, res in all_results.items():
            f.write(f"\n{'─'*70}\n")
            f.write(f"DATASET: {name.upper()}\n")
            f.write(f"{'─'*70}\n")
            f.write(res.to_string(index=False))
            f.write("\n")

        f.write("\n\n" + "=" * 70 + "\n")
        f.write("AUTISM / NEURODIVERGENCE — LITERATURE-BASED ARGUMENT\n")
        f.write("=" * 70 + "\n\n")
        f.write("No public dataset with neurodivergence flags exists — but published\n")
        f.write("experimental studies provide stronger evidence than corpus analysis:\n\n")
        f.write("KEY CITATIONS:\n")
        f.write("1. Lim, A., Young, R.L., & Brewer, N. (2021). Autistic Adults May Be\n")
        f.write("   Erroneously Perceived as Deceptive and Lacking Credibility.\n")
        f.write("   Journal of Autism and Developmental Disorders, 52(2), 490-507.\n")
        f.write("   N=1410 observers. FINDING: Autistic speakers rated as more deceptive\n")
        f.write("   and less credible than neurotypical speakers when TELLING THE TRUTH.\n\n")
        f.write("2. Autistica (2024). Autism, Deception and the Criminal Justice System.\n")
        f.write("   Survey of 394 police officers: only 37% had received autism training.\n")
        f.write("   1-2% prevalence in general population vs 2-18% in forensic populations.\n\n")
        f.write("3. Haworth, K. et al. (2023). Police suspect interviews with autistic\n")
        f.write("   adults. Frontiers in Psychology.\n")
        f.write("   FINDING: Autism-typical behaviours (gaze aversion, flat affect,\n")
        f.write("   repetitive movement) are diagnostically indistinguishable from the\n")
        f.write("   nonverbal cues trained investigators use to identify deception.\n\n")
        f.write("THE ARGUMENT:\n")
        f.write("The diagnostic criteria for autism overlap near-perfectly with the\n")
        f.write("behavioural deception cues used by trained investigators (Global\n")
        f.write("Deception Research Team, 2006): gaze aversion (#1 cue) and fidgeting\n")
        f.write("(#2 cue). An autistic person cannot present their truthful testimony\n")
        f.write("without involuntarily performing the exact behaviours the system reads\n")
        f.write("as deception. Their innocence is structurally illegible to the instrument.\n")

    print(f"  Saved: {results_path}")

    # Summary
    print("\n" + "=" * 65)
    print("SUMMARY")
    for name, res in all_results.items():
        sig = res[res['Significant'] == 'YES ✓']
        print(f"  {name}: {len(sig)}/{len(res)} features show significant cultural variation in truthful speech")
    print(f"\nOutputs:")
    print(f"  {os.path.join(PROJECT_ROOT, 'results', 'cultural', 'cultural_analysis.txt')}")
    print(f"  {os.path.join(PROJECT_ROOT, 'results', 'figures')}/*_cultural_boxplots.png")
    print(f"  {os.path.join(PROJECT_ROOT, 'results', 'figures')}/*_cross_classifier_fp.png")
    print("=" * 65 + "\n")


if __name__ == "__main__":
    main()
