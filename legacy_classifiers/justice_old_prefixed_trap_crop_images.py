#!/usr/bin/env python3
"""
Crop images to remove top/bottom text
Assumes text is in top ~10% and bottom ~5% of image
"""

from PIL import Image
import os
from pathlib import Path

# Source and destination directories
source_dir = Path('/Users/tiaastor/Koofr/BUILDING_THE_SYSTEM/images_justice')
dest_dir = Path('/Users/tiaastor/Koofr/BUILDING_THE_SYSTEM/content/templates/novathesis-main/5-Figures')

# Ensure destination exists
dest_dir.mkdir(parents=True, exist_ok=True)

# Image mapping: source filename -> figure name
image_mapping = {
    'checklist_deception.png': 'Figure-02-Signal-Inversion-Effect.png',
    'mammalian_justice.png': 'Figure-07-Mammalian-Justice-Comparison.png',
    'behaviour_loop.png': 'Figure-03-Behavioral-Adaptation-Loop.png',
    'CJS_pipeline.png': 'Figure-01-Criminal-Justice-Pipeline.png',
    'stress_response_justice.png': 'Figure-04-Pre-Interrogation-Timeline.png',
    'questions_rewrite_memory.png': 'Figure-05-Cross-Examination-Memory.png',
    'jury_confidence_changes_without_new_evidence.png': 'Figure-06-Jury-Polarization.png',
    'justice_defined_as_prevention_is_just.png': 'Figure-08-Prevention-Framework.png',
    'au_vs_ch.png': 'Figure-11-Switzerland-vs-Australia.png',
}

def crop_image(input_path, output_path, top_crop_percent=12, bottom_crop_percent=8):
    """
    Crop image to remove top and bottom text

    Args:
        input_path: Path to input image
        output_path: Path to save cropped image
        top_crop_percent: Percentage of height to remove from top
        bottom_crop_percent: Percentage of height to remove from bottom
    """
    try:
        img = Image.open(input_path)
        width, height = img.size

        # Calculate crop box (left, top, right, bottom)
        top = int(height * top_crop_percent / 100)
        bottom = int(height * (100 - bottom_crop_percent) / 100)

        # Crop image
        cropped = img.crop((0, top, width, bottom))

        # Save with high quality
        cropped.save(output_path, quality=95, optimize=False)

        print(f"✓ Cropped: {input_path.name}")
        print(f"  Original: {width}x{height}")
        print(f"  Cropped:  {cropped.width}x{cropped.height}")
        print(f"  Saved to: {output_path.name}\n")

        return True
    except Exception as e:
        print(f"✗ Error processing {input_path.name}: {e}\n")
        return False

# Process all images
print("=" * 60)
print("CROPPING IMAGES - Removing Top/Bottom Text")
print("=" * 60)
print()

success_count = 0
for source_name, dest_name in image_mapping.items():
    source_path = source_dir / source_name
    dest_path = dest_dir / dest_name

    if source_path.exists():
        if crop_image(source_path, dest_path):
            success_count += 1
    else:
        print(f"✗ Not found: {source_name}\n")

print("=" * 60)
print(f"DONE: Successfully cropped {success_count}/{len(image_mapping)} images")
print(f"Saved to: {dest_dir}")
print("=" * 60)
