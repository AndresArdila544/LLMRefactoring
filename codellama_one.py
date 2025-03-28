import ollama
import os

# Load file content
def load_python_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='latin-1') as file:
            return file.read()

# Refactoring prompt
def create_refactor_prompt(python_code):
    return f"""

This is an example of refactoring; reducing its lines and complexity, while preserving its functionality.
Example:

import math

x1, y1, x2, y2 = map(float, input().split())

dx = x1 - x2
dy = y1 - y2

d = math.hypot(dx, dy)

print(d)

Refactored version:

import math
x1, y1, x2, y2 = map(float, input().split())
d = math.hypot(x1-x2, y1-y2)
print(d)

Below is a Python program that works as intended, but I need you to refactor the code to reduce its lines and complexity, while preserving its functionality. Make the code cleaner, more concise, and improve its readability.

Here is the original Python program:

{python_code}

Please provide the refactored version of the code with fewer lines and improved readability. 
DO NOT include any explanations, introductions, or concluding remarks. Just give me the Python code, no quotations. Just the code.
"""

# Call the model
def refactor_with_model(code,model_name):
    prompt = create_refactor_prompt(code)
    try:
        response = ollama.chat(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a helpful and expert Python assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        result = response["message"]["content"].strip()
        if not result:
            print(f"⚠️ Empty response from {model_name}")
        return result
    except Exception as e:
        print(f"❌ Error with model {model_name}: {e}")
        return ""


# Save result
def save_output(output_dir, original_file_name, suffix, content):
    os.makedirs(output_dir, exist_ok=True)
    file_name = f"{os.path.splitext(original_file_name)[0]}{suffix}.py"
    output_path = os.path.join(output_dir, file_name)
    with open(output_path, 'w', encoding='utf-8') as f:  # <<< Fix here
        f.write(content)
    print(f"Saved: {output_path}")

# Process each problem file
def process_problem_folder(problem_path, output_root):
    model_name="codellama:7b"
    for file_name in os.listdir(problem_path):
        if file_name.endswith(".py"):
            file_path = os.path.join(problem_path, file_name)
            code = load_python_file(file_path)

            problem_id = os.path.basename(problem_path)
            base_name = os.path.splitext(file_name)[0]

            # Directory: output/output_MODELNAME_zero/pXXXXX/sXXXXXXXXX/
            file_output_dir = os.path.join(output_root, problem_id, base_name)
            # Skip if all 3 outputs already exist
            pass1_path = os.path.join(file_output_dir, f"{base_name}_pass@1.py")
            pass2_path = os.path.join(file_output_dir, f"{base_name}_pass@3.py")
            pass3_path = os.path.join(file_output_dir, f"{base_name}_pass@5.py")
            #print(pass1_path)
            #print(pass2_path)
            #print(pass3_path)
            #print(os.path.exists(pass1_path) )
            #print(os.path.exists(pass2_path))
            #print(os.path.exists(pass3_path))

            if os.path.exists(pass1_path) and os.path.exists(pass2_path) and os.path.exists(pass3_path):
                print(f"Skipping {file_name} (already processed)")
                continue

            print(f"Processing {file_name} in {problem_path}...")

            # Generate pass@1
            pass1 = refactor_with_model(code,model_name)
            save_output(file_output_dir, base_name, "_pass@1", pass1)

            # Generate pass@3
            pass2 = refactor_with_model(code,model_name)
            pass3 = refactor_with_model(code,model_name)
            save_output(file_output_dir, base_name, "_pass@3", pass3)

            # Generate pass@3
            pass4 = refactor_with_model(code,model_name)
            pass5 = refactor_with_model(code,model_name)
            save_output(file_output_dir, base_name, "_pass@5", pass5)


# Loop through all problems
def process_all(input_root):
    model_name = "codellama"
    output_root = os.path.join("output", f"output_{model_name}_one")
    os.makedirs(output_root, exist_ok=True)

    for problem_folder in os.listdir(input_root):
        problem_path = os.path.join(input_root, problem_folder)
        if os.path.isdir(problem_path):
            process_problem_folder(problem_path, output_root)

# Run
if __name__ == "__main__":
    base_input_dir = os.path.join("input", "sample_problems")
    process_all(base_input_dir)
