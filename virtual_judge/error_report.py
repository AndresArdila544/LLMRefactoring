import os
import csv
import re
from collections import Counter, defaultdict

def extract_error_type(error_message):
    error_message = error_message.strip()

    # Empty error
    if not error_message:
        return "EmptyError"

    # Incomplete traceback
    if error_message.startswith("Traceback") and not re.search(r"[A-Za-z]+Error", error_message):
        return "IncompleteTraceback"

    # Markdown in code (e.g., ```python)
    if re.search(r"^```", error_message) or "```python" in error_message:
        return "MarkdownBlockError"

    # Natural language mixed with code
    if re.search(r"SyntaxError:.*Here is a refactored version|refactored version of the code", error_message):
        return "NaturalLanguageInCode"

    # LLM hallucinated tokens
    if re.search(r"<\|.*?\|>", error_message):
        return "LLMTokenArtifact"

    # Python 2 syntax patterns
    if re.search(r"SyntaxError:.*print [^(\n]", error_message):
        return "Python2PrintSyntax"
    if "raw_input" in error_message:
        return "Python2RawInput"
    
    # Missing import
    if re.search(r"name '.*' is not defined.*import", error_message) or "No module named" in error_message:
        return "MissingImport"

    # Input parsing issues
    if "EOFError" in error_message:
        return "EOFError"
    if "not enough values to unpack" in error_message:
        return "UnpackError"
    if "invalid literal for int()" in error_message or "ValueError" in error_message and "int" in error_message:
        return "InvalidIntCast"

    # Malformed expressions
    if re.search(r"was never closed|unterminated string literal|unexpected EOF while parsing", error_message):
        return "MalformedExpression"

    # Fallback to built-in errors
    match = re.search(r"([A-Za-z]+Error)\b", error_message)
    if match:
        return match.group(1)

    print("⚠️ Unmatched error:", repr(error_message[:200]))
    return "OtherError"


def process_results_file(file_path):
    error_counter = Counter()

    with open(file_path, "r", encoding="utf-8") as f:
        sample = f.read(2048)
        f.seek(0)
        try:
            dialect = csv.Sniffer().sniff(sample)
        except csv.Error:
            print(f"⚠️ Could not detect delimiter in {file_path}. Assuming comma.")
            dialect = csv.get_dialect("excel")

        reader = csv.DictReader(f, dialect=dialect)

        for row in reader:
            if not row:
                continue

            try:
                row = {k.strip().lower(): v for k, v in row.items() if k}
                status = row.get("status", "").strip().lower()
                if status != "passed":
                    error_type = extract_error_type(row.get("error_message", ""))
                    error_counter[error_type] += 1
            except Exception as e:
                print(f"⚠️ Skipping malformed row in {file_path}: {e}")
                continue

    return error_counter


def summarize_all_error_types():
    total_errors = defaultdict(Counter)

    for file in os.listdir():
        if file.startswith("results_output_") and file.endswith(".csv"):
            print(f"🔍 Processing {file}...")
            model_name = file.replace("results_output_", "").replace(".csv", "")
            errors = process_results_file(file)
            total_errors[model_name] = errors

    for model, error_counter in total_errors.items():
        output_file = f"errors_{model}.csv"
        with open(output_file, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Error Type", "Count"])
            for error_type, count in error_counter.most_common():
                writer.writerow([error_type, count])
        print(f"✅ Error summary written to: {output_file}")

if __name__ == "__main__":
    summarize_all_error_types()
