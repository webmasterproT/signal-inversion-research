#!/usr/bin/env python3
"""
Build ONE .tex file and one folder for Overleaf (single directory, single file).
Run from master_thesis/:  python3 build_overleaf_single.py
Output: overleaf/Master_ConstructedGuilt.tex + 4 image files in same folder.
Upload the whole overleaf/ folder to Overleaf, set main doc to Master_ConstructedGuilt.tex.
"""
import os
import shutil

BASE = os.path.dirname(os.path.abspath(__file__))
UNJUST = os.path.normpath(os.path.join(BASE, ".."))
OUT_DIR = os.path.join(BASE, "overleaf")
BODY_PARTS_ORDER = [
    "EXECUTIVE_SUMMARY.tex",
    "CONSTRUCTED_GUILT_FULL_THESIS.tex",
    "INSTITUTIONAL_NEGLIGENCE_SUPPLEMENT.tex",
    "JUSTICE_PARADIGM_SHIFT_SUPPLEMENT.tex",
    "NEUROIMAGING_EVIDENCE_SUPPLEMENT.tex",
    "PERFECT_CASE_SYNTHESIS.tex",
    "cultural_section.tex",
]

# Images to copy (source path relative to BASE, dest filename in overleaf/)
IMAGES = [
    (os.path.join(UNJUST, "PUBLISHABLE", "neuroimaging_figures", "stress_pfc_figure.jpg"), "stress_pfc_figure.jpg"),
    (os.path.join(UNJUST, "PUBLISHABLE", "neuroimaging_figures", "threat_circuitry_figure1.jpg"), "threat_circuitry_figure1.jpg"),
    (os.path.join(UNJUST, "PUBLISHABLE", "neuroimaging_figures", "threat_circuitry_figure2.jpg"), "threat_circuitry_figure2.jpg"),
    (os.path.join(UNJUST, "final", "cross-cultural-falso-possitive.png"), "cross-cultural-falso-possitive.png"),
]

def main():
    # Ensure body_parts exist (run build_master.py if needed)
    body_parts_dir = os.path.join(BASE, "body_parts")
    if not os.path.isfile(os.path.join(body_parts_dir, "EXECUTIVE_SUMMARY.tex")):
        import subprocess
        subprocess.run([os.sys.executable, os.path.join(BASE, "build_master.py")], check=True, cwd=BASE)
    os.makedirs(OUT_DIR, exist_ok=True)

    # 1. Inline body: read each body_parts file
    body_parts_dir = os.path.join(BASE, "body_parts")
    body_content = []
    for name in BODY_PARTS_ORDER:
        path = os.path.join(body_parts_dir, name)
        if not os.path.isfile(path):
            print("Skip (not found):", path)
            continue
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            part = f.read()
        # Flatten image paths so they're just filename (same directory)
        part = part.replace("neuroimaging_figures/", "")
        body_content.append(part)

    inlined_body = "\n\n".join(body_content)

    # 2. Read master.tex and replace \input{body} with inlined body; fix graphicspath
    master_path = os.path.join(BASE, "master.tex")
    with open(master_path, "r", encoding="utf-8") as f:
        master = f.read()

    # Remove \input{body} and insert inlined body
    master = master.replace("\\input{body}\n\n", inlined_body + "\n\n", 1)

    # Replace \graphicspath block with same-dir so Overleaf uses current directory
    old_path = r"""% All image locations: PUBLISHABLE/ so that "neuroimaging_figures/foo" and "final/foo" resolve
\graphicspath{%
  {../PUBLISHABLE/}%
  {../PUBLISHABLE/neuroimaging_figures/}%
  {../final/}%
  {../constructed_guilt_cross_cultural_data_analysis/}%
  {../../../novathesis-main/images_justice/}%
  {../../../novathesis-main/}%
}"""
    master = master.replace(
        old_path,
        "% All images in same directory (Overleaf single-folder)\n\\graphicspath{{}}",
    )

    out_tex = os.path.join(OUT_DIR, "Master_ConstructedGuilt.tex")
    with open(out_tex, "w", encoding="utf-8") as f:
        f.write(master)
    print("Wrote:", out_tex)

    # 3. Copy images into overleaf/
    for src, dest_name in IMAGES:
        if os.path.isfile(src):
            shutil.copy2(src, os.path.join(OUT_DIR, dest_name))
            print("Copied:", dest_name)
        else:
            print("Skip image (not found):", src)

    print("Done. Upload folder:", OUT_DIR)
    print("  -> Overleaf: New Project > Upload Project > zip of overleaf/")
    print("  -> Set main document to: Master_ConstructedGuilt.tex")

if __name__ == "__main__":
    main()
