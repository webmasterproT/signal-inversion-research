#!/usr/bin/env python3
"""
Crop all images from trap/images_justice and save to 5-Figures
"""

from PIL import Image
from pathlib import Path

source_dir = Path('/Users/tiaastor/Koofr/BUILDING_THE_SYSTEM/content/novathesis-main/trap/images_justice')
dest_dir = Path('/Users/tiaastor/Koofr/BUILDING_THE_SYSTEM/content/templates/novathesis-main/5-Figures')

# Map source filenames to figure names
# Use the good ones primarily, alternatives as fallbacks
image_mapping = {
    # Primary (good quality)
    'checklist_deception.png': 'Figure-02-Signal-Inversion-Effect.png',
    'mammalian_justice.png': 'Figure-07-Mammalian-Justice-Comparison.png',
    'behaviour_loop.png': 'Figure-03-Behavioral-Adaptation-Loop.png',
    'CJS_pipeline.png': 'Figure-01-Criminal-Justice-Pipeline.png',
    'stress_response_justice.png': 'Figure-04-Pre-Interrogation-Timeline.png',
    'questions_rewrite_memory.png': 'Figure-05-Cross-Examination-Memory.png',
    'jury_confidence_changes_without_new_evidence.png': 'Figure-06-Jury-Polarization.png',
    'justice_defined_as_prevention_is_just.png': 'Figure-08-Prevention-Framework.png',

    # Alternatives (for missing figures)
    'prevention.png': 'Figure-10-Crime-Prevention-Mechanisms.png',
    'mamalso.png': 'Figure-09-Cost-Comparison.png',  # Using as placeholder for cost
}

dest_dir.mkdir(parents=True, exist_ok=True)

print("=" * 70)
print("CROPPING ALL IMAGES FROM trap/images_justice")
print("=" * 70)
print()

success = 0
for source_name, dest_name in image_mapping.items():
    source_path = source_dir / source_name
    dest_path = dest_dir / dest_name

    if not source_path.exists():
        print(f"✗ SKIP: {source_name} not found")
        continue

    try:
        img = Image.open(source_path)
        width, height = img.size

        # Crop top 12% and bottom 8%
        top = int(height * 0.12)
        bottom = int(height * 0.92)

        cropped = img.crop((0, top, width, bottom))
        cropped.save(dest_path, quality=95, optimize=False)

        print(f"✓ {source_name:45s} → {dest_name}")
        print(f"  {width}x{height} → {cropped.width}x{cropped.height}")
        success += 1

    except Exception as e:
        print(f"✗ ERROR: {source_name}: {e}")

print()
print("=" * 70)
print(f"DONE: Successfully cropped {success}/10 images")
print(f"Saved to: {dest_dir}")
print("=" * 70)
