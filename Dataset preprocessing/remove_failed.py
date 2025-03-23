import csv
import os

# CONFIGURATION
RESULTS_CSV = "results.csv"
SUBMISSION_ROOT = r"A:\LLMProject\filtered_problems"  # Base path

def delete_failed_files(csv_path, base_dir):
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        deleted = 0
        skipped = 0

        for row in reader:
            filename = row["filename"]
            status = row["status"].strip().lower()  # Normalize for safety

            # Delete if status is 'failed' or 'skipped'
            if status in ("failed", "skipped"):
                target_file_path = None

                for dir_name in os.listdir(base_dir):
                    file_path = os.path.join(base_dir, dir_name, filename)
                    if os.path.isfile(file_path):
                        target_file_path = file_path
                        break

                if target_file_path:
                    os.remove(target_file_path)
                    print(f"🗑️ Deleted: {target_file_path}")
                    deleted += 1
                else:
                    print(f"⚠️ File not found: {filename}")
                    skipped += 1

    print(f"\n✅ Deleted {deleted} failed/skipped files. Skipped {skipped} not found.")

if __name__ == "__main__":
    delete_failed_files(RESULTS_CSV, SUBMISSION_ROOT)
