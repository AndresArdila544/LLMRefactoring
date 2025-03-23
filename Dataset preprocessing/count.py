import os
import csv

# Use raw string to avoid backslash issues on Windows
DATASET_DIR = r"A:\LLMProject\complete dataset"
OUTPUT_CSV = "file_counts.csv"

def count_python_files(dataset_path):
    counts = []

    for folder in os.listdir(dataset_path):
        folder_path = os.path.join(dataset_path, folder)

        # Check for folders like pXXXXX
        if os.path.isdir(folder_path) and folder.startswith("p") and folder[1:].isdigit():
            python_subfolder = os.path.join(folder_path, "Python")

            if os.path.isdir(python_subfolder):
                py_files = [f for f in os.listdir(python_subfolder) if f.endswith(".py")]
                counts.append((folder, len(py_files)))
            else:
                counts.append((folder, 0))  # Folder exists but no "Python" subfolder

    return counts

def save_to_csv(data, output_path):
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Folder", "Python File Count"])
        writer.writerows(data)

if __name__ == "__main__":
    counts = count_python_files(DATASET_DIR)
    save_to_csv(counts, OUTPUT_CSV)
    print(f"✅ File counts saved to {OUTPUT_CSV}")
