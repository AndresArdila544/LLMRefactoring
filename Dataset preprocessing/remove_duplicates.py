import os
import hashlib

# Set your dataset root path
DATASET_DIR = r"A:\LLMProject\complete dataset"

def normalize_code(content):
    """
    Removes all whitespace characters to compare code structurally.
    """
    return ''.join(content.split())

def remove_duplicates_in_problem(problem_path):
    python_dir = os.path.join(problem_path, "Python")
    if not os.path.isdir(python_dir):
        return

    seen_hashes = {}
    for filename in os.listdir(python_dir):
        if not filename.endswith(".py"):
            continue

        file_path = os.path.join(python_dir, filename)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"⚠️ Could not read {file_path}: {e}")
            continue

        normalized = normalize_code(content)
        code_hash = hashlib.sha256(normalized.encode()).hexdigest()

        if code_hash in seen_hashes:
            # Duplicate detected
            print(f"🗑 Removing duplicate: {file_path}")
            os.remove(file_path)
        else:
            seen_hashes[code_hash] = file_path  # Keep first seen version

def remove_all_duplicates(dataset_dir):
    for folder in os.listdir(dataset_dir):
        problem_path = os.path.join(dataset_dir, folder)
        if os.path.isdir(problem_path) and folder.startswith("p") and folder[1:].isdigit():
            remove_duplicates_in_problem(problem_path)

if __name__ == "__main__":
    remove_all_duplicates(DATASET_DIR)
    print("✅ Duplicate removal completed.")
