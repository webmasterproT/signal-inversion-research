"""
Deception Corpus Linguistic Analysis Pipeline
=============================================
Pérez-Rosas et al. (2016) Real-Life Trial Deception Dataset
University of Michigan

Usage:
    1. Download dataset:
       curl -L "https://web.eecs.umich.edu/~mihalcea/downloads/RealLifeDeceptionDetection.2016.zip" -o dataset.zip
       unzip dataset.zip -d data/

    2. Run analysis:
       python deception_analysis.py

    3. Output:
       - results/tables.txt     (all statistical results, SPSS-ready)
       - results/figures/       (publication-quality plots)
       - results/spss_ready.csv (raw coded data for SPSS import)

Thesis argument being tested:
    - If truthful statements hedge MORE than deceptive ones:
      => The system reads innocent linguistic behaviour as deception
    - If hedging REDUCES perceived credibility regardless of truth:
      => Conscientiousness is punished by the justice system's interpretive apparatus
"""

import os
import re
import csv
import json
import glob
import warnings
import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import mannwhitneyu, pointbiserialr, chi2_contingency
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import nltk
from collections import defaultdict

warnings.filterwarnings('ignore')

# ── download required NLTK data ───────────────────────────────────────────
for pkg in ['punkt', 'averaged_perceptron_tagger', 'stopwords', 'punkt_tab']:
    try:
        nltk.download(pkg, quiet=True)
    except Exception:
        pass

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag

# ── output dirs ───────────────────────────────────────────────────────────
os.makedirs("results/figures", exist_ok=True)

# ═════════════════════════════════════════════════════════════════════════
# LINGUISTIC FEATURE DEFINITIONS
# ═════════════════════════════════════════════════════════════════════════

# Hedging markers — epistemic qualification
# Truthful speakers qualify because reality IS uncertain
# Deceptive speakers rehearse clean, confident stories
HEDGING = [
    "i think", "i believe", "i'm not sure", "i'm not certain",
    "as far as i", "as far as i can remember", "i'm pretty sure",
    "i guess", "i suppose", "maybe", "perhaps", "possibly",
    "probably", "it seems", "it seemed", "kind of", "sort of",
    "approximately", "around", "roughly", "about", "i thought",
    "i assumed", "if i recall", "if i remember", "to my knowledge",
    "i may be wrong", "i could be wrong", "not sure but",
    "i'm fairly certain", "i think i", "i believe i"
]

# Certainty markers — confident assertion
# Deceptive speakers often use these to perform credibility
CERTAINTY = [
    "definitely", "absolutely", "certainly", "clearly", "obviously",
    "without doubt", "no doubt", "i know", "i knew", "i'm certain",
    "i'm sure", "i'm positive", "for sure", "100 percent", "100%",
    "without question", "undoubtedly", "unquestionably", "i am sure",
    "there's no way", "i can tell you", "i guarantee", "trust me",
    "i swear", "i promise", "believe me"
]

# Passive constructions — agency distancing
# Deceptive speakers may avoid first-person agency ("it happened"
# rather than "I did it") — or innocent speakers use passive because
# they genuinely weren't the agent
PASSIVE_INDICATORS = [
    " was ", " were ", " been ", " being ", " is ", " are ",
    "was done", "was taken", "was found", "was seen", "was hit",
    "was told", "was given", "was made", "were told", "were given",
    "it happened", "it occurred", "it was", "there was", "there were"
]

# Experiencer framing — first-person embodied detail
# Truthful accounts are grounded in sensory/experiential detail
# Deceptive accounts tend toward abstract narrative distance
EXPERIENCER = [
    "i felt", "i saw", "i heard", "i smelled", "i noticed",
    "i realized", "i remember", "i recalled", "i could see",
    "i could hear", "i could feel", "i was scared", "i was nervous",
    "i was afraid", "it felt", "it looked", "it sounded",
    "my heart", "my hands", "my face", "i started to", "i began to",
    "i could tell", "i could sense"
]

# Filler / disfluency markers — indicators of real-time cognitive effort
# Truthful speakers who are recalling genuine experience show MORE
# disfluency (um, uh, you know) because retrieval is effortful
# Deceptive speakers with rehearsed stories show LESS disfluency
FILLERS = [
    r'\bum\b', r'\buh\b', r'\bahh?\b', r'\buhh?\b', r'\bumm\b',
    r'\byou know\b', r'\bi mean\b', r'\blike\b', r'\bwell\b',
    r'\.\.\.', r'--'
]

# Negative emotion words (guilt, fear, shame) — the Pennebaker finding
# Liars use MORE negative emotion words to perform distress they don't feel
# (or: innocent people's language is dominated by confusion, not negative affect)
NEGATIVE_EMOTION = [
    "terrible", "awful", "horrible", "dreadful", "devastating",
    "tragic", "horrifying", "scared", "terrified", "frightened",
    "worried", "anxious", "guilty", "ashamed", "disgusted",
    "outraged", "shocked", "devastated", "heartbroken", "furious",
    "angry", "upset", "distressed", "traumatized", "nightmare"
]


# ═════════════════════════════════════════════════════════════════════════
# FEATURE EXTRACTION
# ═════════════════════════════════════════════════════════════════════════

def count_per_hundred_words(text, patterns, is_regex=False):
    """Count pattern occurrences per 100 words (normalised frequency)."""
    text_lower = text.lower()
    words = word_tokenize(text_lower)
    n_words = max(len(words), 1)

    count = 0
    if is_regex:
        for pat in patterns:
            count += len(re.findall(pat, text_lower))
    else:
        for phrase in patterns:
            count += text_lower.count(phrase)

    return (count / n_words) * 100


def extract_features(text):
    """
    Extract all linguistic features from a single transcript.
    Returns a dict of normalised feature values.
    """
    text_lower = text.lower()
    words = word_tokenize(text_lower)
    sentences = sent_tokenize(text)
    n_words = max(len(words), 1)
    n_sents = max(len(sentences), 1)

    features = {}

    # Core features
    features['hedging_rate']       = count_per_hundred_words(text, HEDGING)
    features['certainty_rate']     = count_per_hundred_words(text, CERTAINTY)
    features['passive_rate']       = count_per_hundred_words(text, PASSIVE_INDICATORS)
    features['experiencer_rate']   = count_per_hundred_words(text, EXPERIENCER)
    features['filler_rate']        = count_per_hundred_words(text, FILLERS, is_regex=True)
    features['neg_emotion_rate']   = count_per_hundred_words(text, NEGATIVE_EMOTION)

    # Hedge/certainty ratio — key compound measure
    # High value = more hedging relative to certainty = more truthful-pattern
    denom = features['certainty_rate'] + 0.001
    features['hedge_certainty_ratio'] = features['hedging_rate'] / denom

    # Lexical richness (type-token ratio)
    unique_words = set(words)
    features['ttr'] = len(unique_words) / n_words

    # Mean sentence length
    word_counts_per_sent = [len(word_tokenize(s)) for s in sentences]
    features['mean_sent_length'] = np.mean(word_counts_per_sent) if word_counts_per_sent else 0

    # Total word count (truthful statements tend to be longer — more detail)
    features['word_count'] = n_words

    # First-person pronoun rate
    first_person = ['i', 'me', 'my', 'mine', 'myself']
    fp_count = sum(1 for w in words if w in first_person)
    features['first_person_rate'] = (fp_count / n_words) * 100

    # Third-person rate (distancing)
    third_person = ['he', 'she', 'they', 'him', 'her', 'them', 'his', 'their']
    tp_count = sum(1 for w in words if w in third_person)
    features['third_person_rate'] = (tp_count / n_words) * 100

    return features


# ═════════════════════════════════════════════════════════════════════════
# DATA LOADING
# ═════════════════════════════════════════════════════════════════════════

def load_dataset(data_dir="Transcription"):
    """
    Load transcripts from the Pérez-Rosas (2016) dataset.
    Dataset structure: Clips/007/007.mp4, transcriptions in separate folder
    or .txt files alongside video clips.
    Handles multiple possible directory layouts.
    """
    records = []

    # Try multiple possible layouts
    # Layout 1: Transcription folder with label in filename
    txt_files = glob.glob(os.path.join(data_dir, "**", "*.txt"), recursive=True)

    # Layout 2: CSV label file
    label_files = glob.glob(os.path.join(data_dir, "**", "*.csv"), recursive=True)

    # Try to find the label/annotation file first
    labels = {}
    for lf in label_files:
        try:
            df = pd.read_csv(lf)
            # Common column names in the dataset
            for id_col in ['id', 'clip_id', 'filename', 'file']:
                for label_col in ['label', 'deceptive', 'truth', 'class', 'ground_truth']:
                    if id_col in df.columns and label_col in df.columns:
                        for _, row in df.iterrows():
                            labels[str(row[id_col])] = str(row[label_col])
        except Exception:
            pass

    for txt_path in txt_files:
        try:
            with open(txt_path, 'r', encoding='utf-8', errors='ignore') as f:
                text = f.read().strip()

            if len(text) < 10:
                continue

            filename = os.path.basename(txt_path).lower()
            clip_id  = os.path.splitext(os.path.basename(txt_path))[0]

            # Determine label
            label = None

            # Check label file
            if clip_id in labels:
                raw = labels[clip_id].lower()
                label = 1 if any(x in raw for x in ['d', 'lie', 'deceptive', 'false', '1']) else 0

            # Check directory name
            if label is None:
                parent = os.path.basename(os.path.dirname(txt_path)).lower()
                if 'decep' in parent or 'lie' in parent or 'false' in parent:
                    label = 1
                elif 'truth' in parent or 'true' in parent or 'honest' in parent:
                    label = 0

            # Check filename itself
            if label is None:
                if any(x in filename for x in ['decep', 'lie', 'false', '_d_', '_d.']):
                    label = 1
                elif any(x in filename for x in ['truth', 'true', 'honest', '_t_', '_t.']):
                    label = 0

            if label is None:
                continue

            feats = extract_features(text)
            feats['label']    = label
            feats['label_str'] = 'Deceptive' if label == 1 else 'Truthful'
            feats['clip_id']  = clip_id
            feats['text']     = text[:500]  # store excerpt
            records.append(feats)

        except Exception as e:
            continue

    if not records:
        print("\n⚠  No labelled transcripts found. Generating synthetic demo data.")
        print("   (Replace with real data from the Michigan dataset)\n")
        records = generate_demo_data()

    return pd.DataFrame(records)


def generate_demo_data():
    """
    Generate synthetic data with the expected real-world pattern
    (truthful = more hedging, deceptive = more certainty).
    Used for pipeline testing only — NOT for publication.
    """
    np.random.seed(42)
    n = 60  # 30 truthful, 30 deceptive (approximate dataset split)
    records = []

    # Truthful: higher hedging, lower certainty, more fillers, more words
    for i in range(30):
        records.append({
            'clip_id': f'truth_{i:03d}',
            'label': 0,
            'label_str': 'Truthful',
            'hedging_rate':       np.random.normal(4.2, 1.1),
            'certainty_rate':     np.random.normal(1.8, 0.7),
            'passive_rate':       np.random.normal(5.1, 1.4),
            'experiencer_rate':   np.random.normal(3.8, 1.0),
            'filler_rate':        np.random.normal(6.2, 1.8),
            'neg_emotion_rate':   np.random.normal(1.9, 0.8),
            'hedge_certainty_ratio': np.random.normal(2.4, 0.6),
            'ttr':                np.random.normal(0.72, 0.08),
            'mean_sent_length':   np.random.normal(14.2, 3.1),
            'word_count':         int(np.random.normal(148, 32)),
            'first_person_rate':  np.random.normal(8.1, 1.9),
            'third_person_rate':  np.random.normal(3.2, 1.1),
            'text': '[DEMO DATA — replace with real corpus]'
        })

    # Deceptive: lower hedging, higher certainty, fewer fillers, fewer words
    for i in range(31):
        records.append({
            'clip_id': f'decep_{i:03d}',
            'label': 1,
            'label_str': 'Deceptive',
            'hedging_rate':       np.random.normal(2.1, 0.9),
            'certainty_rate':     np.random.normal(3.4, 1.0),
            'passive_rate':       np.random.normal(6.8, 1.6),
            'experiencer_rate':   np.random.normal(2.4, 0.9),
            'filler_rate':        np.random.normal(3.8, 1.4),
            'neg_emotion_rate':   np.random.normal(3.1, 1.0),
            'hedge_certainty_ratio': np.random.normal(0.7, 0.3),
            'ttr':                np.random.normal(0.68, 0.09),
            'mean_sent_length':   np.random.normal(11.8, 2.8),
            'word_count':         int(np.random.normal(112, 28)),
            'first_person_rate':  np.random.normal(6.4, 1.7),
            'third_person_rate':  np.random.normal(4.8, 1.3),
            'text': '[DEMO DATA — replace with real corpus]'
        })

    return records


# ═════════════════════════════════════════════════════════════════════════
# STATISTICAL ANALYSIS
# ═════════════════════════════════════════════════════════════════════════

FEATURES_OF_INTEREST = [
    ('hedging_rate',         'Hedging Rate (per 100 words)'),
    ('certainty_rate',       'Certainty Markers (per 100 words)'),
    ('filler_rate',          'Disfluency / Filler Rate (per 100 words)'),
    ('experiencer_rate',     'Experiencer Framing (per 100 words)'),
    ('passive_rate',         'Passive Constructions (per 100 words)'),
    ('neg_emotion_rate',     'Negative Emotion Rate (per 100 words)'),
    ('hedge_certainty_ratio','Hedge:Certainty Ratio'),
    ('word_count',           'Total Word Count'),
    ('first_person_rate',    'First-Person Pronoun Rate'),
]


def cohens_d(group1, group2):
    """Compute Cohen's d effect size."""
    n1, n2   = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    pooled_sd = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2))
    return (np.mean(group1) - np.mean(group2)) / pooled_sd if pooled_sd > 0 else 0


def interpret_d(d):
    a = abs(d)
    if a < 0.2:  return "negligible"
    if a < 0.5:  return "small"
    if a < 0.8:  return "medium"
    return "large"


def run_group_comparisons(df):
    """Mann-Whitney U tests: truthful vs deceptive on all features."""
    truth  = df[df['label'] == 0]
    decep  = df[df['label'] == 1]
    results = []

    for feat, label in FEATURES_OF_INTEREST:
        t_vals = truth[feat].dropna().values
        d_vals = decep[feat].dropna().values

        if len(t_vals) < 3 or len(d_vals) < 3:
            continue

        stat, p = mannwhitneyu(t_vals, d_vals, alternative='two-sided')
        d       = cohens_d(t_vals, d_vals)
        r       = stat / (len(t_vals) * len(d_vals))  # rank-biserial r

        results.append({
            'Feature':           label,
            'Truthful Mean':     f"{np.mean(t_vals):.2f}",
            'Truthful SD':       f"{np.std(t_vals, ddof=1):.2f}",
            'Deceptive Mean':    f"{np.mean(d_vals):.2f}",
            'Deceptive SD':      f"{np.std(d_vals, ddof=1):.2f}",
            'U':                 f"{stat:.1f}",
            'p':                 f"{'<.001' if p < .001 else f'{p:.3f}'}",
            'Cohens d':          f"{d:.2f}",
            'Effect Size':       interpret_d(d),
            'Direction':         '↑ Truthful' if d > 0 else '↑ Deceptive',
        })

    return pd.DataFrame(results)


def run_correlation_analysis(df):
    """
    Point-biserial correlations: each feature vs binary truth/deception label.
    Positive r = feature associated with truthfulness.
    Negative r = feature associated with deception.
    """
    results = []
    for feat, label in FEATURES_OF_INTEREST:
        vals = df[feat].dropna()
        lbls = df.loc[vals.index, 'label']
        if len(vals) < 5:
            continue
        # Flip label so 1 = truthful for interpretability
        truthful_binary = (lbls == 0).astype(int)
        r, p = pointbiserialr(truthful_binary, vals)
        results.append({
            'Feature': label,
            'r (truthful)': f"{r:.3f}",
            'p': f"{'<.001' if p < .001 else f'{p:.3f}'}",
            'Interpretation': (
                'Associated with truthful speech' if r > 0.1
                else 'Associated with deceptive speech' if r < -0.1
                else 'No reliable association'
            )
        })
    return pd.DataFrame(results)


# ═════════════════════════════════════════════════════════════════════════
# VISUALISATION
# ═════════════════════════════════════════════════════════════════════════

COLOURS = {'Truthful': '#2166ac', 'Deceptive': '#d6604d'}


def plot_feature_distributions(df, out_dir="results/figures"):
    """Box plots for key features split by truth/deception."""
    key_features = [
        ('hedging_rate',         'Hedging Rate'),
        ('certainty_rate',       'Certainty Rate'),
        ('filler_rate',          'Disfluency Rate'),
        ('hedge_certainty_ratio','Hedge:Certainty Ratio'),
    ]

    fig, axes = plt.subplots(2, 2, figsize=(12, 9))
    axes = axes.flatten()
    fig.suptitle(
        'Linguistic Feature Distributions: Truthful vs Deceptive Court Statements\n'
        'Pérez-Rosas et al. (2016) Real-Life Trial Dataset',
        fontsize=13, fontweight='bold', y=1.01
    )

    for ax, (feat, label) in zip(axes, key_features):
        data_t = df[df['label_str'] == 'Truthful'][feat].dropna()
        data_d = df[df['label_str'] == 'Deceptive'][feat].dropna()

        bp = ax.boxplot(
            [data_t, data_d],
            labels=['Truthful', 'Deceptive'],
            patch_artist=True,
            medianprops=dict(color='black', linewidth=2),
            notch=False,
            widths=0.5
        )
        for patch, colour in zip(bp['boxes'], [COLOURS['Truthful'], COLOURS['Deceptive']]):
            patch.set_facecolor(colour)
            patch.set_alpha(0.7)

        # Strip plot overlay
        for i, (data, lbl) in enumerate([(data_t, 'Truthful'), (data_d, 'Deceptive')], 1):
            jitter = np.random.uniform(-0.15, 0.15, len(data))
            ax.scatter(np.full(len(data), i) + jitter, data,
                       alpha=0.35, s=20, color=COLOURS[lbl], zorder=3)

        ax.set_ylabel(label, fontsize=10)
        ax.set_title(label, fontsize=11, fontweight='bold')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        # Mann-Whitney annotation
        stat, p = mannwhitneyu(data_t, data_d, alternative='two-sided')
        p_str = 'p < .001' if p < .001 else f'p = {p:.3f}'
        ax.text(0.98, 0.97, p_str, transform=ax.transAxes,
                ha='right', va='top', fontsize=9,
                color='darkgreen' if p < .05 else 'grey')

    plt.tight_layout()
    path = os.path.join(out_dir, "feature_distributions.png")
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {path}")


def plot_effect_sizes(comp_df, out_dir="results/figures"):
    """Horizontal bar chart of Cohen's d values."""
    df = comp_df.copy()
    df['d'] = df['Cohens d'].astype(float)
    df = df.sort_values('d')

    fig, ax = plt.subplots(figsize=(10, 7))
    colours = ['#2166ac' if v > 0 else '#d6604d' for v in df['d']]
    bars = ax.barh(df['Feature'], df['d'], color=colours, alpha=0.8, height=0.6)

    ax.axvline(0, color='black', linewidth=0.8)
    ax.axvline(0.5,  color='grey', linewidth=0.6, linestyle='--', alpha=0.5)
    ax.axvline(-0.5, color='grey', linewidth=0.6, linestyle='--', alpha=0.5)
    ax.axvline(0.8,  color='grey', linewidth=0.6, linestyle=':',  alpha=0.5)
    ax.axvline(-0.8, color='grey', linewidth=0.6, linestyle=':',  alpha=0.5)

    ax.set_xlabel("Cohen's d  (positive = higher in truthful)", fontsize=11)
    ax.set_title(
        "Effect Sizes: Truthful vs Deceptive Court Statements\n"
        "Positive values = feature higher in truthful speech",
        fontsize=12, fontweight='bold'
    )

    truth_patch  = mpatches.Patch(color='#2166ac', alpha=0.8, label='Higher in Truthful')
    decep_patch  = mpatches.Patch(color='#d6604d', alpha=0.8, label='Higher in Deceptive')
    ax.legend(handles=[truth_patch, decep_patch], loc='lower right', fontsize=9)

    # Reference lines labels
    for x, txt in [(0.5, 'medium'), (0.8, 'large'), (-0.5, 'medium'), (-0.8, 'large')]:
        ax.text(x, -0.7, txt, ha='center', fontsize=7, color='grey', style='italic')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    path = os.path.join(out_dir, "effect_sizes.png")
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {path}")


def plot_hedge_certainty_scatter(df, out_dir="results/figures"):
    """
    Scatter plot: hedging rate vs certainty rate, coloured by truth/deception.
    Visualises the key theoretical argument directly.
    """
    fig, ax = plt.subplots(figsize=(9, 7))

    for lbl, colour in COLOURS.items():
        subset = df[df['label_str'] == lbl]
        ax.scatter(subset['certainty_rate'], subset['hedging_rate'],
                   c=colour, label=lbl, alpha=0.65, s=60, edgecolors='white', linewidths=0.5)

    ax.set_xlabel("Certainty Marker Rate (per 100 words)", fontsize=11)
    ax.set_ylabel("Hedging Rate (per 100 words)", fontsize=11)
    ax.set_title(
        "Hedging vs Certainty in Court Statements\n"
        "If truthful speakers hedge more and are certain less:\n"
        "the system reads the linguistic behaviour of innocence as deception",
        fontsize=11, fontweight='bold'
    )
    ax.legend(fontsize=10)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Quadrant labels
    xlim = ax.get_xlim(); ylim = ax.get_ylim()
    ax.text(xlim[1]*0.72, ylim[1]*0.88, 'High hedge\nHigh certainty\n(uncertain & emphatic)',
            fontsize=8, color='grey', ha='center', style='italic')
    ax.text(xlim[1]*0.72, ylim[0]+0.1,  'Low hedge\nHigh certainty\n(rehearsed / deceptive pattern)',
            fontsize=8, color='#d6604d', ha='center', style='italic')
    ax.text(xlim[0]+0.05, ylim[1]*0.88, 'High hedge\nLow certainty\n(truthful pattern)',
            fontsize=8, color='#2166ac', ha='center', style='italic')

    plt.tight_layout()
    path = os.path.join(out_dir, "hedge_certainty_scatter.png")
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {path}")


# ═════════════════════════════════════════════════════════════════════════
# EXPORT
# ═════════════════════════════════════════════════════════════════════════

def save_spss_csv(df, path="results/spss_ready.csv"):
    """Save numeric columns in SPSS-importable format."""
    cols = ['clip_id', 'label'] + [f for f, _ in FEATURES_OF_INTEREST]
    out  = df[[c for c in cols if c in df.columns]].copy()
    out.to_csv(path, index=False)
    print(f"  Saved SPSS-ready CSV: {path}")


def save_results_table(comp_df, corr_df, df, path="results/tables.txt"):
    """Write formatted results tables to text file."""
    n_truth = (df['label'] == 0).sum()
    n_decep = (df['label'] == 1).sum()
    is_demo = 'DEMO' in str(df['text'].iloc[0]) if 'text' in df.columns else False

    with open(path, 'w') as f:
        f.write("=" * 80 + "\n")
        f.write("DECEPTION CORPUS LINGUISTIC ANALYSIS — RESULTS\n")
        f.write("Pérez-Rosas et al. (2016) Real-Life Trial Dataset\n")
        if is_demo:
            f.write("*** DEMO MODE: synthetic data — replace with real corpus ***\n")
        f.write(f"N = {len(df)} clips  ({n_truth} truthful, {n_decep} deceptive)\n")
        f.write("=" * 80 + "\n\n")

        f.write("TABLE 1: Group Comparison (Mann-Whitney U)\n")
        f.write("-" * 80 + "\n")
        f.write(comp_df.to_string(index=False))
        f.write("\n\n")

        f.write("TABLE 2: Point-Biserial Correlations with Truthfulness\n")
        f.write("-" * 80 + "\n")
        f.write(corr_df.to_string(index=False))
        f.write("\n\n")

        f.write("THESIS ARGUMENT KEY:\n")
        f.write("-" * 80 + "\n")
        f.write("If hedging_rate is HIGHER in truthful speech:\n")
        f.write("  => Innocent speakers qualify their statements (because memory IS uncertain).\n")
        f.write("  => Investigators/juries who read hedging as deception are constructing guilt\n")
        f.write("     from the linguistic behaviour of innocence itself.\n\n")
        f.write("If certainty_rate is HIGHER in deceptive speech:\n")
        f.write("  => Liars perform confidence. Rehearsed stories are clean and unqualified.\n")
        f.write("  => The Reid Technique's emphasis on linguistic confidence as a truth signal\n")
        f.write("     is systematically inverted.\n\n")
        f.write("If filler_rate is HIGHER in truthful speech:\n")
        f.write("  => Genuine recall is effortful and produces disfluency.\n")
        f.write("  => Disfluency is used as a deception cue by trained investigators.\n")
        f.write("  => Innocent cognitive effort is read as guilty concealment.\n")

    print(f"  Saved results table: {path}")


# ═════════════════════════════════════════════════════════════════════════
# MAIN
# ═════════════════════════════════════════════════════════════════════════

def main():
    print("\n" + "=" * 60)
    print("DECEPTION CORPUS ANALYSIS PIPELINE")
    print("Constructed Guilt — Appendix Section 6")
    print("=" * 60 + "\n")

    print("Step 1: Loading dataset...")
    df = load_dataset("Transcription")
    print(f"  Loaded {len(df)} transcripts  "
          f"({(df['label']==0).sum()} truthful, {(df['label']==1).sum()} deceptive)\n")

    if 'DEMO' in str(df.get('text', pd.Series(['']))[0]):
        print("  ⚠  RUNNING ON DEMO DATA")
        print("  To use real data:")
        print("    curl -L 'https://web.eecs.umich.edu/~mihalcea/downloads/RealLifeDeceptionDetection.2016.zip' -o dataset.zip")
        print("    unzip dataset.zip -d data/\n")

    print("Step 2: Running statistical comparisons...")
    comp_df = run_group_comparisons(df)
    corr_df = run_correlation_analysis(df)
    print("  Done.\n")

    print("Step 3: Generating figures...")
    plot_feature_distributions(df)
    plot_effect_sizes(comp_df)
    plot_hedge_certainty_scatter(df)
    print()

    print("Step 4: Saving outputs...")
    save_spss_csv(df)
    save_results_table(comp_df, corr_df, df)
    print()

    print("Step 5: Key findings summary")
    print("-" * 60)
    for _, row in comp_df.iterrows():
        sig = "✓ sig" if row['p'] in ['<.001'] or (
            row['p'] != 'nan' and float(row['p']) < .05
        ) else "  n.s."
        print(f"  {sig}  {row['Feature'][:40]:<40}  d={row['Cohens d']}  {row['Direction']}")

    print("\n" + "=" * 60)
    print("OUTPUTS")
    print("  results/tables.txt          — full stats tables")
    print("  results/spss_ready.csv      — import directly into SPSS/R/Stata")
    print("  results/figures/            — publication-ready figures")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
