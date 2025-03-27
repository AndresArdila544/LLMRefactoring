import ollama
import os

# Function to load the Python file content
def load_python_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Unified refactoring prompt (without extra text)
def create_refactor_prompt(python_code):
    return f"""
You are an expert Python programmer. Below is a Python program that works as intended, but I need you to refactor the code to reduce its lines and complexity, while preserving its functionality. Make the code cleaner, more concise, and improve its readability.

Here is the original Python program:

{python_code}

Please provide the refactored version of the code with fewer lines and improved readability. 
DO NOT include any explanations, introductions, or concluding remarks. Just give me the Python code.
"""

def refactor_with_starcoder2(file_path):
    python_code = load_python_file(file_path)
    prompt = create_refactor_prompt(python_code)
    
    # Send prompt to StarCoder2
    response = ollama.chat(model="starcoder2", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"].strip()  # Strip any extra whitespace or lines

# Function to save the refactored code in the output directory
def save_refactored_code(file_name, refactored_code, output_dir, model_name):
    new_file_path = os.path.join(output_dir, f"{model_name}_{os.path.basename(file_name)}")
    
    with open(new_file_path, 'w') as file:
        file.write(refactored_code)
    print(f"Refactored code saved to {new_file_path}")

# Main function to process all Python files in a folder
def process_folder(input_dir):
    # Get the directory where the script is running
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "refactored_output")

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Process all .py files in the input directory
    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)
        
        if file_name.endswith('.py') and os.path.isfile(file_path):
            print(f"Processing file: {file_name}")
            
            # Refactor using Code Llama
            refactored_code_codellama = refactor_with_codellama(file_path)
            save_refactored_code(file_name, refactored_code_codellama, output_dir, "codellama")
            
            # Refactor using StarCoder2
            refactored_code_starcoder2 = refactor_with_starcoder2(file_path)
            save_refactored_code(file_name, refactored_code_starcoder2, output_dir, "starcoder2")

# Run the script
if __name__ == "__main__":
    input_folder = input("Enter the path to the input folder with Python files: ")
    
    process_folder(input_folder)
