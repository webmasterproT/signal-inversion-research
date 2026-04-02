#!/usr/bin/env python3
"""
Build a single ConstructedGuilt_SingleFile.tex from all thesis sources.
Run from: content/research/unjustjustice/latex/
"""
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
UNJUST = os.path.normpath(os.path.join(BASE, ".."))
PUBLISHABLE = os.path.join(UNJUST, "PUBLISHABLE")
THESIS_DIR = os.path.join(UNJUST, "thesis_proof_justice_is_unjust")
ANALYSIS = os.path.join(UNJUST, "analysis")

def escape_tex(s):
    if not s:
        return ""
    s = s.replace("\\", "\\textbackslash ")
    for c, r in [("{", "\\{"), ("}", "\\}"), ("&", "\\&"), ("%", "\\%"),
                  ("$", "\\$"), ("#", "\\#"), ("_", "\\_"), ("~", "\\tilde{}")]:
        s = s.replace(c, r)
    # Common Unicode
    s = s.replace("\u2014", "---").replace("\u2013", "--")
    s = s.replace("\u0141", "L").replace("\u0110", "-")  # Fisher ref
    return s

def paragraphs_to_tex(text):
    """Convert plain text paragraphs to LaTeX (escape + \\par)."""
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
    preamble = r"""% Constructed Guilt — Single-file Tufte thesis
% Build: python3 build_single_tex.py
% Then: pdflatex ConstructedGuilt_SingleFile (or use on Overleaf)

\documentclass[nohyper,nobib]{tufte-book}
\usepackage{nameref}
\usepackage{url}
\usepackage[utf8]{inputenc}
\usepackage{booktabs}
\usepackage{graphicx}
\setkeys{Gin}{width=\linewidth,totalheight=\textheight,keepaspectratio}
\graphicspath{{../PUBLISHABLE/neuroimaging_figures/}{../PUBLISHABLE/belief-reality-matrix/results/figures/}{../PUBLISHABLE/deception_analysis/}{./}}
\usepackage{array}
\usepackage{framed}
\usepackage{fancyvrb}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\fvset{fontsize=\normalsize}
\usepackage{xspace}
\usepackage{amsmath}

\title{Constructed Guilt\\\large Language, Power, and the Architecture of Criminal Justice}
\date{March 2026}
\author{Tia Astor}
\publisher{OMXUS Research}

\newcommand{\monthyear}{%
  \ifcase\month\or January\or February\or March\or April\or May\or June\or
  July\or August\or September\or October\or November\or
  December\fi\space\number\year
}

\makeatletter
\renewcommand{\maketitle}{%
  \begingroup
  \setlength{\parindent}{0pt}
  \fontsize{24}{24}\selectfont\textit{\@author}\par
  \vspace{1.75in}
  \fontsize{36}{54}\selectfont\@title\par
  \vspace{0.5in}
  \fontsize{14}{14}\selectfont\textsf{\smallcaps{\@date}}\par
  \vfill
  \fontsize{14}{14}\selectfont\textit{\@publisher}\par
  \thispagestyle{empty}
  \newpage
  \endgroup
}
\makeatother

\titlecontents{part}[0pt]{\addvspace{0.25\baselineskip}}{\allcaps{Part~\thecontentslabel}\allcaps}{\allcaps{Part~\thecontentslabel}\allcaps}{}[\vspace*{0.5\baselineskip}]
\titlecontents{chapter}[4em]{}{\contentslabel{2em}\textit}{\hspace{0em}\textit}{\qquad\thecontentspage}[\vspace*{0.5\baselineskip}]

\begin{document}
\frontmatter
\maketitle

\newpage
\begin{fullwidth}
~\vfill
\thispagestyle{empty}
\setlength{\parindent}{0pt}
\setlength{\parskip}{\baselineskip}
Copyright \copyright\ \the\year\ OMXUS.
\par\smallcaps{Published by OMXUS Research}
\par\smallcaps{omxus.com}
\par\textit{First printing, \monthyear}
\end{fullwidth}

\tableofcontents

\cleardoublepage
~\vfill
\begin{doublespace}
\noindent\fontsize{18}{22}\selectfont\itshape
Who decides who feels? The feeler or the feelee?
\end{doublespace}
\vfill\vfill

\cleardoublepage
\chapter*{Abstract}
\addcontentsline{toc}{chapter}{Abstract}
This thesis argues that guilt, as produced by the criminal justice system, is not an objective finding of fact but a performative linguistic construction---one that can be assembled from the behaviour of any individual, regardless of actual culpability. The system's methods for assessing credibility are not merely imperfect; they are inverted. The people who sound most guilty are most likely to be telling the truth. Drawing on semiotics, philosophy of language, critical legal theory, and empirical criminology, the analysis proceeds across pre-interrogation detention, police interrogation, courtroom proceedings, and media and jury processes. The architecture of criminal justice is designed to produce conviction, not truth.

\chapter*{Author's note}
\addcontentsline{toc}{chapter}{Author's note}
This thesis was not written as a personal story. It is an academic argument. It was not written ``for me.'' But it inadvertently describes what happened to me. The same system the thesis documents---the one that reads authenticity as deception, that punishes direct speech and neurodivergent presentation---is the system that processed me. So while the text speaks in general terms, it also works for my case.

\mainmatter
"""

    body_parts = []

    # Chapters 1-2
    ch12 = read(os.path.join(THESIS_DIR, "constructed_guilt_thesis_1_2.txt"))
    body_parts.append(r"\part{Part I: Foundations}")
    body_parts.append(r"\chapter{Introduction and Theoretical Framework}")
    body_parts.append(paragraphs_to_tex(ch12))

    # Chapters 3-4
    ch34 = read(os.path.join(THESIS_DIR, "constructed_guilt_chapters3_4.txt"))
    body_parts.append(r"\chapter{Pre-Interrogation Detention and the Reid Technique}")
    body_parts.append(paragraphs_to_tex(ch34))

    # Chapters 5-6
    ch56 = read(os.path.join(THESIS_DIR, "constructed_guilt_chapters5_6.txt"))
    body_parts.append(r"\chapter{Legislative Language and the Courtroom}")
    body_parts.append(paragraphs_to_tex(ch56))

    # Chapters 7-8-9
    ch789 = read(os.path.join(THESIS_DIR, "constructed_guilt_chapters7_8_9.txt"))
    body_parts.append(r"\chapter{Media, Jury, and Synthesis}")
    body_parts.append(paragraphs_to_tex(ch789))

    # Signal inversion
    sig = read(os.path.join(THESIS_DIR, "signal_inversion_effect.txt"))
    body_parts.append(r"\chapter{Signal Inversion Effect}")
    body_parts.append(paragraphs_to_tex(sig))

    # Statistical appendix
    app = read(os.path.join(THESIS_DIR, "constructed_guilt_statistical_appendix.txt"))
    body_parts.append(r"\chapter{Statistical Appendix}")
    body_parts.append(paragraphs_to_tex(app))

    # Phase 2 design
    phase2 = read(os.path.join(THESIS_DIR, "phase2_analysis_design.txt"))
    body_parts.append(r"\chapter{Phase 2 Analysis Design}")
    body_parts.append(paragraphs_to_tex(phase2))

    # Cultural analysis results
    cult = read(os.path.join(ANALYSIS, "results", "cultural", "cultural_analysis.txt"))
    body_parts.append(r"\chapter{Cultural Variation in Truthful Speech}")
    body_parts.append(paragraphs_to_tex(cult))

    # Executive summary (key numbers)
    exec_sum = read(os.path.join(PUBLISHABLE, "EXECUTIVE_SUMMARY.md"))
    body_parts.append(r"\chapter{Executive Summary: Key Findings}")
    body_parts.append(paragraphs_to_tex(exec_sum))

    # Neuroimaging supplement (abbreviated)
    neuro = read(os.path.join(PUBLISHABLE, "NEUROIMAGING_EVIDENCE_SUPPLEMENT.md"))
    body_parts.append(r"\chapter{Neuroimaging Evidence}")
    body_parts.append(paragraphs_to_tex(neuro[:6000]))  # First part

    # Supporting notes (caveat, deepdive, psych, summary)
    body_parts.append(r"\chapter{Supporting Notes and Context}")
    for name, fname in [
        ("Caveat (session context)", "2026-03-08-caveat-the-messages-below-were-generated-by-the-u.txt"),
        ("Deep dive", "deepdive.txt"),
        ("Psych", "psych.txt"),
        ("Summary", "summary.txt"),
    ]:
        path = os.path.join(UNJUST, fname)
        if os.path.exists(path):
            body_parts.append(r"\section{" + name + "}")
            body_parts.append(paragraphs_to_tex(read(path)[:15000]))  # Cap length

    back = r"""
\backmatter
\end{document}
"""

    out_path = os.path.join(BASE, "ConstructedGuilt_SingleFile.tex")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(preamble)
        f.write("\n\n".join(body_parts))
        f.write(back)
    print("Wrote", out_path)

if __name__ == "__main__":
    main()
