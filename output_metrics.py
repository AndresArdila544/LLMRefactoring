import os
import csv
from pathlib import Path
from radon.metrics import mi_visit
from radon.complexity import cc_visit
from radon.raw import analyze
from radon.metrics import h_visit
from difflib import SequenceMatcher

# === CONFIG ===
CORRECT_DIR = Path("correct_refactorings")
ORIGINAL_DIR = Path("input/filtered_problems")
OUTPUT_CSV = "correct_refactorings_metrics.csv"

def analyze_code(source):
    raw_metrics = analyze(source)
    loc = raw_metrics.loc

    cc_scores = cc_visit(source)
    avg_cc = sum(block.complexity for block in cc_scores) / len(cc_scores) if cc_scores else 0

    halstead = h_visit(source)
    h_volume = halstead.total.volume if hasattr(halstead, 'total') else 0

    mi = mi_visit(source, True)

    return loc, avg_cc, h_volume, mi

def load_file_content(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"⚠️ Failed to read file {path}: {e}")
        return None

def compute_levenshtein(a, b):
    return int((1 - SequenceMatcher(None, a, b).ratio()) * max(len(a), len(b)))

def collect_metrics():
    results = []

    for model_dir in CORRECT_DIR.iterdir():
        if not model_dir.is_dir():
            continue

        modelname, prompting = model_dir.name.rsplit("_", 1)

        for problem_folder in model_dir.iterdir():
            for file in problem_folder.glob("*.py"):
                refactored_code = load_file_content(file)
                if not refactored_code:
                    continue

                try:
                    loc, cc, h_volume, mi = analyze_code(refactored_code)
                except Exception as e:
                    print(f"⚠️ Error analyzing metrics for {file}: {e}")
                    continue

                # Match original
                student_id = file.stem.split("_")[0]  # sXXXXX
                original_path = ORIGINAL_DIR / problem_folder.name / f"{student_id}.py"
                original_code = load_file_content(original_path)

                if not original_code:
                    print(f"❌ Original file not found for {student_id} in {problem_folder.name}")
                    lev = "MISSING"
                else:
                    lev = compute_levenshtein(original_code, refactored_code)

                results.append({
                    "filename": file.name,
                    "modelname": modelname,
                    "prompting": prompting,
                    "LOC": loc,
                    "Cyclomatic Complexity": round(cc, 2),
                    "Halstead Volume": round(h_volume, 2),
                    "Maintainability Index": round(mi, 2),
                    "Levenshtein Distance": lev
                })

    return results

def write_to_csv(data, output_path=OUTPUT_CSV):
    with open(output_path, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"✅ Metrics written to {output_path}")

if __name__ == "__main__":
    metrics = collect_metrics()
    if metrics:
        write_to_csv(metrics)
    else:
        print("❌ No metrics collected.")
