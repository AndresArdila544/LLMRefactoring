import csv
import os
from collections import defaultdict

def summarize_best_pass_attempt(results_csv_path, output_csv_path="summary.csv"):
    results_by_program = defaultdict(dict)

    with open(results_csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            full_filename = row["filename"]
            base_name = full_filename.split("_pass@")[0]
            status = row["status"].strip().lower()  # normalize

            if "pass@1" in full_filename:
                results_by_program[base_name]["pass@1"] = status
            elif "pass@3" in full_filename:
                results_by_program[base_name]["pass@3"] = status
            elif "pass@5" in full_filename:
                results_by_program[base_name]["pass@5"] = status

    # Now determine the final status per base file
    summary = []
    for base, passes in results_by_program.items():
        if passes.get("pass@1") == "passed":
            summary.append((base, "pass@1"))
        elif passes.get("pass@3") == "passed":
            summary.append((base, "pass@3"))
        elif passes.get("pass@5") == "passed":
            summary.append((base, "pass@5"))
        else:
            summary.append((base, "failed"))

    # Write summary to CSV
    with open(output_csv_path, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["filename", "status"])
        writer.writerows(summary)

    print(f"✅ Summary written to {output_csv_path}")


def process_all_results_csvs():
    for file in os.listdir():
        if file.startswith("results_") and file.endswith(".csv") and "_summary" not in file:
            summary_filename = file.replace(".csv", "_summary.csv")
            summarize_best_pass_attempt(file, summary_filename)


if __name__ == "__main__":
    process_all_results_csvs()
