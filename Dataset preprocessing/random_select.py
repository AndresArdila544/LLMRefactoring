import os
import random
import shutil

SOURCE_ROOT = os.path.join("input", "filtered_problems")
DEST_ROOT = "sample_problems"
SAMPLES_PER_PROBLEM = 2

def select_random_samples():
    os.makedirs(DEST_ROOT, exist_ok=True)

    for problem_folder in os.listdir(SOURCE_ROOT):
        problem_path = os.path.join(SOURCE_ROOT, problem_folder)

        if not os.path.isdir(problem_path) or not problem_folder.startswith("p"):
            continue

        py_files = [f for f in os.listdir(problem_path) if f.endswith(".py")]
        if len(py_files) < SAMPLES_PER_PROBLEM:
            print(f"⚠️ Not enough files in {problem_folder}, skipping...")
            continue

        selected_files = random.sample(py_files, SAMPLES_PER_PROBLEM)

        dest_folder = os.path.join(DEST_ROOT, problem_folder)
        os.makedirs(dest_folder, exist_ok=True)

        for file_name in selected_files:
            src = os.path.join(problem_path, file_name)
            dst = os.path.join(dest_folder, file_name)
            shutil.copy2(src, dst)
            print(f"✅ Copied {file_name} → {problem_folder}")

    print(f"\n🎯 Sampling complete! Check the '{DEST_ROOT}' folder.")

if __name__ == "__main__":
    select_random_samples()
