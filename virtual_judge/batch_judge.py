import csv
import json
import os
import subprocess

# CONFIGURATION
TEST_CASES_DIR = "test_cases"
FILTERED_DIR = r"A:\LLMProject\filtered_problems"
PROBLEM_MAP_CSV = "problem_id_name_map.csv"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_OUTPUT_DIR = os.path.join(SCRIPT_DIR, "..", "output")  # Your mapping file

def load_test_cases(problem_id):
    test_file = os.path.join(TEST_CASES_DIR, f"{problem_id}_test.json")
    if not os.path.exists(test_file):
        print(f"❌ Test case file not found: {test_file}")
        return []
    with open(test_file, "r", encoding="utf-8") as f:
        return json.load(f)

def detect_python_version(user_code_path):
    with open(user_code_path, "r", encoding="utf-8") as f:
        code = f.read()
    if "xrange(" in code or "print " in code:
        if os.path.exists("C:\\Python27\\python.exe"):
            return "C:\\Python27\\python.exe"
        else:
            print("⚠ Python 2 code detected but not found. Falling back to python3.")
            return "python3"
    return "python3"

import subprocess
import threading

def run_code(user_code_path, input_data, timeout=2):
    python_version = detect_python_version(user_code_path)

    try:
        proc = subprocess.Popen(
            [python_version, user_code_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        timer = threading.Timer(timeout, proc.kill)
        try:
            timer.start()
            stdout, stderr = proc.communicate(input=input_data)
            return stdout.strip(), stderr.strip()
        finally:
            timer.cancel()

    except Exception as e:
        return None, f"❌ Execution error: {str(e)}"


import math

def compare_outputs(expected, actual, abs_tol=1e-4, rel_tol=1e-9):
    """
    Compares all float tokens in the output, regardless of line breaks or spacing.
    Ignores formatting differences like newlines vs spaces.
    """
    expected_tokens = expected.strip().split()
    actual_tokens = actual.strip().split()

    if len(expected_tokens) != len(actual_tokens):
        return False

    for e, a in zip(expected_tokens, actual_tokens):
        try:
            e_val = float(e)
            a_val = float(a)
            if not math.isclose(e_val, a_val, abs_tol=abs_tol, rel_tol=rel_tol):
                return False
        except ValueError:
            if e.strip() != a.strip():
                return False

    return True




def evaluate(problem_id, user_code_path):
    test_cases = load_test_cases(problem_id)
    filename = os.path.basename(user_code_path)

    if not test_cases:
        print(f"⚠ Skipping: No test cases found for {problem_id}")
        return {"filename": filename, "problem_id": problem_id, "passed": 0, "total": 0, "status": "⚠ Skipped", "error_message": "No test cases"}

    print(f"\n🔍 Evaluating {filename} for problem {problem_id}...\n")

    passed = 0
    total = len(test_cases)
    error_message = ""
    all_passed = True

    for test in test_cases:
        serial = test["serial"]
        expected_output = test["out"].strip()
        user_output, error = run_code(user_code_path, test["in"])

        if error:
            print(f"❌ Test {serial} Failed - Error: {error}")
            error_message = error
            all_passed = False
        elif compare_outputs(expected_output, user_output):
            print(f"✅ Test {serial} Passed")
            passed += 1
        else:
            print(f"❌ Test {serial} Failed - Expected: {expected_output}, Got: {user_output}")
            all_passed = False

    print(f"\n📊 Final Score: {passed}/{total} tests passed.\n")

    return {
        "filename": filename,
        "problem_id": problem_id,
        "passed": passed,
        "total": total,
        "status": "Passed" if all_passed else "Failed",
        "error_message": error_message[:1000]  # Trim long stack traces
    }


def load_problem_folder_map(csv_path):
    mapping = {}
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=',')  # Use '\t' if tab-separated
        for row in reader:
            folder = row["folder"]
            problem_id = row["problem_id"]
            mapping[folder] = problem_id
    return mapping

def run_batch_evaluation_for_outputs(output_root_dir=DEFAULT_OUTPUT_DIR, mapping_file=PROBLEM_MAP_CSV):
    folder_to_problem = load_problem_folder_map(mapping_file)

    # Go through each model output folder
    for model_output_folder in os.listdir(output_root_dir):
        model_path = os.path.join(output_root_dir, model_output_folder)
        if not os.path.isdir(model_path) or not model_output_folder.startswith("output_"):
            continue

        print(f"\n🚀 Evaluating results for: {model_output_folder}")
        all_results = []

        for problem_folder in os.listdir(model_path):
            problem_path = os.path.join(model_path, problem_folder)
            if not os.path.isdir(problem_path):
                continue

            problem_id = folder_to_problem.get(problem_folder)
            if not problem_id:
                print(f"⚠ No problem ID mapped for folder {problem_folder}")
                continue

            for solution_folder in os.listdir(problem_path):
                solution_path = os.path.join(problem_path, solution_folder)
                if not os.path.isdir(solution_path):
                    continue

                for file in os.listdir(solution_path):
                    if file.endswith(".py"):
                        user_code_path = os.path.join(solution_path, file)
                        result = evaluate(problem_id, user_code_path)
                        all_results.append(result)

        # Write result CSV for this model output
        csv_name = f"results_{model_output_folder}.csv"
        write_results_to_csv(all_results, output_path=csv_name)




import csv

def write_results_to_csv(results, output_path="results.csv"):
    fieldnames = ["filename", "problem_id", "passed", "total", "status", "error_message"]
    with open(output_path, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    print(f"\n📁 Results written to {output_path}")




if __name__ == "__main__":
    run_batch_evaluation_for_outputs()

