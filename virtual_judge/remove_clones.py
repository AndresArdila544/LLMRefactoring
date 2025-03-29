import filecmp
import csv
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.resolve()
ROOT_DIR = SCRIPT_DIR.parent
INPUT_DIR = ROOT_DIR / "input" / "filtered_problems"
CORRECT_DIR = ROOT_DIR / "correct_refactorings"
REPORT_FILE = SCRIPT_DIR / "removed_duplicates.csv"
REMOVED_CSV = SCRIPT_DIR / "removed_clones.csv" 

def clean_code(file_path):
    cleaned_lines = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            # Remove inline comments
            if "#" in line:
                line = line.split("#", 1)[0].strip()
            cleaned_lines.append(line)
    return "\n".join(cleaned_lines)

def is_semantically_identical(file1, file2):
    return clean_code(file1) == clean_code(file2)

def remove_clones():
    removed = []

    for model_dir in CORRECT_DIR.iterdir():
        if not model_dir.is_dir():
            continue

        print(f"🔍 Scanning model: {model_dir.name}")

        for problem_dir in model_dir.iterdir():
            if not problem_dir.is_dir():
                continue

            problem_id = problem_dir.name  # pXXXXX
            input_file_candidates = list((INPUT_DIR / problem_id).glob("s*.py"))
            if not input_file_candidates:
                print(f"⚠️ No original file found for {problem_id}")
                continue

            original_file = input_file_candidates[0]  # Should only be one per folder

            for refactored_file in problem_dir.glob("*.py"):
                print(f"🔍 Checking {refactored_file.name}...")

                if is_semantically_identical(refactored_file, original_file):
                    print(f"🗑️ Removed identical clone: {refactored_file}")
                    removed.append((model_dir.name, problem_id, refactored_file.name))
                    refactored_file.unlink()

    if removed:
        with open(REMOVED_CSV, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Model", "Problem", "Filename"])
            writer.writerows(removed)
        print(f"\n✅ Removed {len(removed)} clone(s). Details saved to {REMOVED_CSV}")
    else:
        print("✅ No identical clones found.")

if __name__ == "__main__":
    remove_clones()