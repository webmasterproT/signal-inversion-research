#!/usr/bin/env python3
"""
Build body.tex from THESIS_FULL_CONTENT/00-text and 02-research.
Run from: THESIS_FULL_CONTENT/latex/
Output: body.tex (included by main.tex)
"""
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(BASE, ".."))
TEXT = os.path.join(ROOT, "00-text")
RESEARCH = os.path.join(ROOT, "02-research")

# Figure list: filename (no path) -> short caption for thesis
FIGURES = [
    ("Figure-01-Criminal-Justice-Pipeline.png", "The Criminal Justice Pipeline: seven stages of guilt construction."),
    ("Figure-02-Signal-Inversion-Effect.png", "Signal inversion: authentic behaviours misread as deception."),
    ("Figure-03-Behavioral-Adaptation-Loop.png", "Behavioural adaptation feedback loop."),
    ("Figure-04-Pre-Interrogation-Timeline.png", "Pre-interrogation timeline and effects."),
    ("Figure-05-Cross-Examination-Memory.png", "Cross-examination and memory."),
    ("Figure-06-Jury-Polarization.png", "Jury polarization."),
    ("Figure-07-Mammalian-Justice-Comparison.png", "Mammalian justice comparison."),
    ("Figure-08-Prevention-Framework.png", "Prevention framework."),
    ("Figure-09-Cost-Comparison.png", "Cost comparison."),
    ("Figure-10-Crime-Prevention-Mechanisms.png", "Crime prevention mechanisms."),
    ("Figure-11-Interrogation-Arrest-Effects.png", "Interrogation and arrest effects."),
    ("Figure-12-Justice-Reform-Viability.png", "Justice reform viability."),
    ("Figure-13-Feedback-Loop-Dynamics.png", "Feedback loop dynamics."),
    ("Figure-14-System-Architecture-Pipeline.png", "System architecture pipeline."),
    ("Figure-15-Signal-Inversion-Deep-Dive.png", "Signal inversion: deep dive."),
    ("Figure-16-Suggestibility-Mechanisms.png", "Suggestibility mechanisms."),
    ("stress_pfc_figure.jpg", "Stress and PFC: alert vs stressed brain (Arnsten, PMC4816215)."),
    ("threat_circuitry_figure1.jpg", "Threat regulatory neurocircuitry (Fenster et al., PMC8617299)."),
    ("threat_circuitry_figure2.jpg", "Healthy vs PTSD threat circuits (Fenster et al.)."),
]

def escape_tex(s):
    if not s:
        return ""
    # Replace Unicode replacement character and other problematic chars before escaping
    s = s.replace("\uFFFD", "?")
    s = s.replace("\\", "\\textbackslash ")
    for c, r in [("{", "\\{"), ("}", "\\}"), ("&", "\\&"), ("%", "\\%"),
                  ("$", "\\$"), ("#", "\\#"), ("_", "\\_"), ("~", "\\textasciitilde{}")]:
        s = s.replace(c, r)
    s = s.replace("\u2014", "---").replace("\u2013", "--")
    s = s.replace("\u0141", "L").replace("\u0110", "-")
    return s

def paragraphs_to_tex(text):
    if not text or not text.strip():
        return ""
    blocks = re.split(r'\n\s*\n', text)
    out = []
    for b in blocks:
        b = b.strip().replace("\n", " ")
        if not b:
            continue
        out.append(escape_tex(b))
    return "\n\n".join(out)

def read(path):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    except Exception as e:
        return f"% Could not read {path}: {e}\n"

def main():
    parts = []

    # Part I: Introduction and theory
    parts.append(r"\part{Foundations}")
    parts.append(r"\chapter{Introduction and Theoretical Framework}")
    ch12 = read(os.path.join(TEXT, "constructed_guilt_thesis_1_2.txt"))
    parts.append(paragraphs_to_tex(ch12))
    parts.append(r"\begin{figure}[htbp]")
    parts.append(r"\centering")
    parts.append(r"\includegraphics[width=0.95\linewidth]{Figure-01-Criminal-Justice-Pipeline}")
    parts.append(r"\caption{The Criminal Justice Pipeline: seven stages of guilt construction.}")
    parts.append(r"\label{fig:pipeline}")
    parts.append(r"\end{figure}")

    # Chapters 3-4
    parts.append(r"\chapter{Pre-Interrogation Detention and the Reid Technique}")
    ch34 = read(os.path.join(TEXT, "constructed_guilt_chapters3_4.txt"))
    parts.append(paragraphs_to_tex(ch34))
    parts.append(r"\begin{figure}[htbp]")
    parts.append(r"\includegraphics[width=0.95\linewidth]{Figure-04-Pre-Interrogation-Timeline}")
    parts.append(r"\caption{Pre-interrogation timeline and effects.}")
    parts.append(r"\end{figure}")

    # Chapters 5-6
    parts.append(r"\chapter{Legislative Language and the Courtroom}")
    ch56 = read(os.path.join(TEXT, "constructed_guilt_chapters5_6.txt"))
    parts.append(paragraphs_to_tex(ch56))
    parts.append(r"\begin{figure}[htbp]")
    parts.append(r"\includegraphics[width=0.95\linewidth]{Figure-05-Cross-Examination-Memory}")
    parts.append(r"\caption{Cross-examination and memory.}")
    parts.append(r"\end{figure}")

    # Chapters 7-8-9
    parts.append(r"\chapter{Media, Jury, and Synthesis}")
    ch789 = read(os.path.join(TEXT, "constructed_guilt_chapters7_8_9.txt"))
    parts.append(paragraphs_to_tex(ch789))
    parts.append(r"\begin{figure}[htbp]")
    parts.append(r"\includegraphics[width=0.95\linewidth]{Figure-02-Signal-Inversion-Effect}")
    parts.append(r"\caption{Signal inversion effect.}")
    parts.append(r"\end{figure}")
    parts.append(r"\begin{figure}[htbp]")
    parts.append(r"\includegraphics[width=0.95\linewidth]{Figure-03-Behavioral-Adaptation-Loop}")
    parts.append(r"\caption{Behavioural adaptation feedback loop.}")
    parts.append(r"\end{figure}")

    # Signal inversion (research)
    sig = read(os.path.join(RESEARCH, "signal_inversion_effect.txt"))
    parts.append(r"\chapter{Signal Inversion Effect}")
    parts.append(paragraphs_to_tex(sig))

    # Statistical appendix
    parts.append(r"\chapter{Statistical Appendix}")
    app = read(os.path.join(TEXT, "constructed_guilt_statistical_appendix.txt"))
    parts.append(paragraphs_to_tex(app))

    # Phase 2 design
    phase2 = read(os.path.join(RESEARCH, "methods", "phase2_analysis_design.txt"))
    parts.append(r"\chapter{Phase 2 Analysis Design}")
    parts.append(paragraphs_to_tex(phase2))

    # Remaining figures (grouped)
    parts.append(r"\chapter{Figures}")
    for fname, cap in FIGURES:
        base, _ = os.path.splitext(fname)
        parts.append(r"\begin{figure}[htbp]")
        parts.append(r"\centering")
        parts.append(r"\includegraphics[width=0.85\linewidth]{" + base + "}")
        parts.append(r"\caption{" + escape_tex(cap) + "}")
        parts.append(r"\end{figure}")

    out_path = os.path.join(BASE, "body.tex")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(parts))
    print("Wrote", out_path)

if __name__ == "__main__":
    main()
