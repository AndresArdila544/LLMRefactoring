import os
import csv
from collections import defaultdict

def load_error_counts(file_path):
    counts = {}
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            error_type = row["Error Type"]
            count = int(row["Count"])
            counts[error_type] = count
    return counts

def summarize_errors_across_models():
    error_summary = defaultdict(dict)
    all_error_types = set()
    model_variants = []

    for file in os.listdir():
        if file.startswith("errors_") and file.endswith(".csv") and "_summary" not in file:
            model = file.replace("errors_", "").replace(".csv", "")
            model_variants.append(model)

            error_counts = load_error_counts(file)
            for error_type, count in error_counts.items():
                error_summary[error_type][model] = count
                all_error_types.add(error_type)

    model_variants = sorted(model_variants)
    output_file = "error_summary_by_model.csv"

    with open(output_file, "w", newline='', encoding="utf-8") as f:
        fieldnames = ["Error Type"] + model_variants
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for error_type in sorted(all_error_types):
            row = {"Error Type": error_type}
            for model in model_variants:
                row[model] = error_summary[error_type].get(model, 0)
            writer.writerow(row)

    print(f"✅ Final error summary written to: {output_file}")

if __name__ == "__main__":
    summarize_errors_across_models()
