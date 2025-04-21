import csv

REF_CSV = "correct_refactorings_metrics.csv"
ORIG_CSV = "code_metrics.csv"
OUT_CSV = "metric_comparison_summary.csv"

def load_original_metrics(filepath):
    data = {}
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = row['filename'].strip()
            data[key] = row
    return data

def compare_values(ref, orig):
    if ref == "SKIPPED" or orig == "SKIPPED":
        return "SKIPPED"
    if ref == orig:
        return "same"
    try:
        return "increase" if float(ref) > float(orig) else "decrease"
    except:
        return "n/a"

def main():
    orig_data = load_original_metrics(ORIG_CSV)

    with open(REF_CSV, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = []

        for row in reader:
            ref_filename = row['filename']
            student_id = ref_filename.split('_')[0] + ".py"
            original = orig_data.get(student_id)

            if not original:
                print(f"⚠️ No original match for {ref_filename}")
                continue

            # Skip if original metrics were skipped
            if any(original[m] == "SKIPPED" for m in ["LOC", "Cyclomatic Complexity", "Halstead Volume", "Maintainability Index"]):
                print(f"⏩ Skipping {student_id} due to incomplete original metrics")
                continue

            comparison = {
                "filename": ref_filename,
                "modelname": row["modelname"],
                "prompting": row["prompting"],
                "LOC_original": original["LOC"],
                "LOC_refactored": row["LOC"],
                "LOC_change": compare_values(row["LOC"], original["LOC"]),
                "CC_original": original["Cyclomatic Complexity"],
                "CC_refactored": row["Cyclomatic Complexity"],
                "CC_change": compare_values(row["Cyclomatic Complexity"], original["Cyclomatic Complexity"]),
                "Halstead_original": original["Halstead Volume"],
                "Halstead_refactored": row["Halstead Volume"],
                "Halstead_change": compare_values(row["Halstead Volume"], original["Halstead Volume"]),
                "MI_original": original["Maintainability Index"],
                "MI_refactored": row["Maintainability Index"],
                "MI_change": compare_values(row["Maintainability Index"], original["Maintainability Index"]),
                "Levenshtein_Distance": row["Levenshtein Distance"]
            }
            rows.append(comparison)

    fieldnames = [
        "filename", "modelname", "prompting",
        "LOC_original", "LOC_refactored", "LOC_change",
        "CC_original", "CC_refactored", "CC_change",
        "Halstead_original", "Halstead_refactored", "Halstead_change",
        "MI_original", "MI_refactored", "MI_change",
        "Levenshtein_Distance"
    ]

    with open(OUT_CSV, "w", newline='', encoding='utf-8') as out:
        writer = csv.DictWriter(out, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"✅ Comparison written to {OUT_CSV}")

if __name__ == "__main__":
    main()
