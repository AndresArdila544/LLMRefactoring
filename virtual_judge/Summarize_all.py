import os
import csv

def summarize_summary_file(summary_file):
    model_name = summary_file.replace("results_", "").replace("_summary.csv", "")
    total = 0
    pass1 = 0
    pass3 = 0
    pass5 = 0
    failed = 0

    with open(summary_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += 1
            status = row["status"].strip().lower()

            if status == "pass@1":
                pass1 += 1
            elif status == "pass@3":
                pass3 += 1
            elif status == "pass@5":
                pass5 += 1
            else:
                failed += 1

    return {
        "model": model_name,
        "Pass@1": pass1 / total,
        "Pass@3": (pass1 + pass3) / total,
        "Pass@5": (pass1 + pass3 + pass5) / total,
        "failed": failed / total
    }

def process_all_summary_files(output_csv="overall_summary.csv"):
    summary_rows = []
    for file in os.listdir():
        if file.startswith("results_") and file.endswith("_summary.csv"):
            summary = summarize_summary_file(file)
            summary_rows.append(summary)

    # Write final summary table
    with open(output_csv, "w", newline='', encoding="utf-8") as f:
        fieldnames = ["model", "Pass@1", "Pass@3", "Pass@5", "failed"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in summary_rows:
            writer.writerow({
                "model": row["model"],
                "Pass@1": f"{row['Pass@1']:.2f}",
                "Pass@3": f"{row['Pass@3']:.2f}",
                "Pass@5": f"{row['Pass@5']:.2f}",
                "failed": f"{row['failed']:.2f}"
            })

    print(f"✅ Overall summary written to {output_csv}")


if __name__ == "__main__":
    process_all_summary_files()
