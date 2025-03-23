import os
import random
import shutil

# Set paths
DATASET_DIR = r"A:\LLMProject\complete_dataset"
OUTPUT_DIR = r"A:\LLMProject\filtered_problems"
FILES_PER_PROBLEM = 10

def select_random_files(dataset_dir, output_dir, num_files=10):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for folder in os.listdir(dataset_dir):
        problem_path = os.path.join(dataset_dir, folder, "Python")

        # Check for valid problem folder
        if os.path.isdir(problem_path) and folder.startswith("p") and folder[1:].isdigit():
            all_py_files = [f for f in os.listdir(problem_path) if f.endswith(".py")]

            if len(all_py_files) < num_files:
                print(f"⚠️ Skipping {folder}: only {len(all_py_files)} .py files found.")
                continue

            selected_files = random.sample(all_py_files, num_files)

            dest_folder = os.path.join(output_dir, folder)
            os.makedirs(dest_folder, exist_ok=True)

            for filename in selected_files:
                src_file = os.path.join(problem_path, filename)
                dest_file = os.path.join(dest_folder, filename)
                shutil.copy(src_file, dest_file)

            print(f"✅ Copied 10 files to {dest_folder}")

if __name__ == "__main__":
    select_random_files(DATASET_DIR, OUTPUT_DIR, FILES_PER_PROBLEM)
    print("✅ Random file selection completed.")
