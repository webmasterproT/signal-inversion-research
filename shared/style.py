"""
OMXUS Research — Shared Figure Style
=====================================
Import this at the top of any run.py to get consistent figures.

Usage:
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'shared'))
    from style import apply_style, COLORS, save_figure

Or just copy this file into your study's src/ directory.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# ──────────────────────────────────────────────────────────────
# COLOUR PALETTE
# Clean, accessible, works in print and on screen.
# Inspired by academic publishing (Lancet / Nature style).
# ──────────────────────────────────────────────────────────────

COLORS = {
    # Primary pair — inverted vs aligned / bad vs good
    "red": "#D64045",       # inverted / false positive / danger
    "green": "#2D936C",     # aligned / correct / safe

    # Secondary
    "blue": "#2D5F8A",      # neutral / primary data
    "orange": "#E88D3F",    # secondary data / highlight
    "purple": "#7B68A8",    # tertiary / supplementary
    "teal": "#45A5A5",      # alternative

    # Greys
    "dark": "#2C2C2C",      # text, axes
    "medium": "#666666",    # secondary text
    "light": "#CCCCCC",     # gridlines
    "bg": "#FAFAFA",        # background
    "white": "#FFFFFF",

    # Cultural palette (for study_07 cross-cultural)
    "us": "#2D5F8A",        # English US — blue
    "mexico": "#D64045",    # Spanish Mexico — red
    "romania": "#E88D3F",   # Romanian — orange
    "india": "#2D936C",     # English India — green
}

# Ordered list for bar charts / legends
PALETTE = [COLORS["blue"], COLORS["red"], COLORS["green"],
           COLORS["orange"], COLORS["purple"], COLORS["teal"]]

CULTURAL_PALETTE = {
    "EnglishUS": COLORS["us"],
    "SpanishMexico": COLORS["mexico"],
    "Romanian": COLORS["romania"],
    "EnglishIndia": COLORS["india"],
}


def apply_style():
    """
    Apply the OMXUS figure style globally.
    Call once at the top of your script.
    """
    plt.rcParams.update({
        # Figure
        "figure.facecolor": COLORS["white"],
        "figure.dpi": 200,
        "savefig.dpi": 200,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.15,

        # Font — use system sans-serif, falls back gracefully
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans"],
        "font.size": 11,

        # Axes
        "axes.facecolor": COLORS["bg"],
        "axes.edgecolor": COLORS["dark"],
        "axes.linewidth": 0.8,
        "axes.titlesize": 13,
        "axes.titleweight": "bold",
        "axes.titlepad": 12,
        "axes.labelsize": 11,
        "axes.labelcolor": COLORS["dark"],
        "axes.labelpad": 8,

        # Grid
        "axes.grid": True,
        "grid.color": COLORS["light"],
        "grid.linewidth": 0.5,
        "grid.alpha": 0.7,

        # Ticks
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "xtick.color": COLORS["medium"],
        "ytick.color": COLORS["medium"],
        "xtick.direction": "out",
        "ytick.direction": "out",

        # Legend
        "legend.fontsize": 10,
        "legend.frameon": True,
        "legend.framealpha": 0.9,
        "legend.edgecolor": COLORS["light"],
        "legend.fancybox": False,

        # Lines
        "lines.linewidth": 1.5,
        "lines.markersize": 6,

        # Patches (bars, boxes)
        "patch.edgecolor": COLORS["white"],
        "patch.linewidth": 0.5,
    })


def save_figure(fig, filepath, close=True):
    """Save a figure with consistent settings."""
    fig.savefig(filepath, dpi=200, bbox_inches="tight",
                facecolor="white", edgecolor="none")
    if close:
        plt.close(fig)
    print(f"  Figure saved: {filepath}")


def add_source_note(ax, text="Source: OMXUS Signal Inversion Research", y=-0.12):
    """Add a small source attribution below the plot."""
    ax.text(0.0, y, text, transform=ax.transAxes,
            fontsize=7, color=COLORS["medium"], style="italic")


# Auto-apply if imported
apply_style()
