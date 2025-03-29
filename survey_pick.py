import random
import csv
from pathlib import Path
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter
from PIL import Image
import io
import uuid
# Constants
ROOT_DIR = Path(__file__).parent.resolve()
CORRECT_DIR = ROOT_DIR / "correct_refactorings"
INPUT_DIR = ROOT_DIR / "input" / "filtered_problems"
OUTPUT_DIR = ROOT_DIR / "Human_survey"
OUTPUT_DIR.mkdir(exist_ok=True)

CSV_INDEX_FILE = OUTPUT_DIR / "survey_index.csv"

import re

def remove_comments(code):
    """Remove full-line and inline Python comments from the code."""
    lines = code.splitlines()
    cleaned_lines = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#") or not stripped:
            continue
        # Remove inline comment unless it's in a string
        code_no_inline = re.sub(r'#(?![^"\']*["\'])[^#]*$', '', line)
        cleaned_lines.append(code_no_inline.rstrip())

    return "\n".join(cleaned_lines)


def collect_all_refactored_files():
    all_files = []
    for model_dir in CORRECT_DIR.iterdir():
        if model_dir.is_dir():
            for problem_dir in model_dir.iterdir():
                for file in problem_dir.glob("*.py"):
                    all_files.append((file, problem_dir.name, model_dir.name))  # (Path, pXXXXX, model)
    return all_files

def generate_image_from_code(code, output_path):
    formatter = ImageFormatter(font_name='Consolas', line_numbers=True, style='default')
    image_data = highlight(code, PythonLexer(), formatter)
    image = Image.open(io.BytesIO(image_data))
    image.save(output_path)

def process_and_save_image(source_path, dest_path):
    with open(source_path, "r", encoding="utf-8") as f:
        code = f.read()
    code = remove_comments(code)
    generate_image_from_code(code, dest_path)


def main():
    all_refactored = collect_all_refactored_files()
    if len(all_refactored) < 40:
        print("⚠️ Not enough files to sample 40.")
        return

    sampled = random.sample(all_refactored, 40)
    index_rows = []

    for refactored_path, problem_code, model in sampled:
        filename = refactored_path.stem  # s082356343_pass@5
        student_id = filename.split("_")[0]

        original_file = INPUT_DIR / problem_code / f"{student_id}.py"
        original_found = original_file.exists()

    # Generate UUIDs
        original_uuid = f"{uuid.uuid4()}.jpg"
        refactored_uuid = f"{uuid.uuid4()}.jpg"

    # Save original image
        if original_found:
            original_img_path = OUTPUT_DIR / original_uuid
            process_and_save_image(original_file, original_img_path)
        else:
            print(f"❌ Original file not found for {student_id} in {problem_code}")
            original_uuid = "NOT FOUND"

    # Save refactored image
        refactored_img_path = OUTPUT_DIR / refactored_uuid
        process_and_save_image(refactored_path, refactored_img_path)

        index_rows.append({
            "problem_code": problem_code,
            "student_id": student_id,
            "original_image": original_uuid,
            "refactored_image": refactored_uuid,
            "model": model
        })

    # Write CSV index
    with open(CSV_INDEX_FILE, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=index_rows[0].keys())
        writer.writeheader()
        writer.writerows(index_rows)

    print("✅ Image generation and CSV index complete.")


if __name__ == "__main__":
    main()
