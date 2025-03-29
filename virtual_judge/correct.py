import csv
import shutil
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.resolve()            # virtual_judge/
ROOT_DIR = SCRIPT_DIR.parent                            # root/
OUTPUT_DIR = ROOT_DIR / "output"
CORRECT_DIR = ROOT_DIR / "correct_refactorings"

SUMMARY_PREFIX = "results_output_"
SUMMARY_SUFFIX = "_summary.csv"

def read_passed_files(summary_file):
    passed_files = {}
    with open(summary_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            filename = row.get("filename")
            status = row.get("status", "").strip().lower()
            if filename and status.startswith("pass@"):
                passed_files[filename.strip()] = status
    return passed_files

def find_nested_path(model_dir, filename):
    """Search inside model_dir/*/filename"""
    for problem_folder in model_dir.iterdir():
        candidate = problem_folder / filename
        if candidate.exists():
            return problem_folder.name, candidate  # Return pXXXXX and full path
    return None, None

def copy_passed_files(modelname):
    summary_path = SCRIPT_DIR / f"{SUMMARY_PREFIX}{modelname}{SUMMARY_SUFFIX}"
    if not summary_path.exists():
        print(f"⚠️ Summary file not found: {summary_path}")
        return

    passed_files = read_passed_files(summary_path)
    model_dir = OUTPUT_DIR  / f"output_{modelname}"


    if not model_dir.exists():
        print(f"⚠️ Output folder not found for model {modelname}: {model_dir}")
        return

    for filename, status in passed_files.items():
        if not filename.startswith("s") or not filename[1:].isdigit():
            print(f"⚠️ Skipping invalid filename: {filename}")
            continue

        problem_folder_name, nested_path = find_nested_path(model_dir, filename)
        if not nested_path:
            print(f"⚠️ Could not find folder for {filename} in {model_dir}")
            continue

        expected_filename = f"{filename}_{status}.py"
        expected_file_path = nested_path / expected_filename
        if not expected_file_path.exists():
            print(f"⚠️ Refactored file not found: {expected_file_path}")
            continue

        destination_dir = CORRECT_DIR / modelname / problem_folder_name
        destination_dir.mkdir(parents=True, exist_ok=True)

        dest_path = destination_dir / expected_filename
        shutil.copy(expected_file_path, dest_path)
        print(f"✅ Copied: {expected_file_path.name} → {dest_path.relative_to(ROOT_DIR)}")


def main():
    found = False
    for file in SCRIPT_DIR.glob(f"{SUMMARY_PREFIX}*{SUMMARY_SUFFIX}"):
        found = True
        modelname = file.name.replace(SUMMARY_PREFIX, "").replace(SUMMARY_SUFFIX, "")
        print(f"📦 Processing model: {modelname}")
        copy_passed_files(modelname)

    if not found:
        print(f"❌ No summary files found in: {SCRIPT_DIR}")

if __name__ == "__main__":
    main()
