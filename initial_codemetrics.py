import os
import csv
from radon.metrics import mi_visit
from radon.complexity import cc_visit
from radon.raw import analyze
from radon.metrics import h_visit


INPUT_DIR = os.path.join("input", "filtered_problems")

def analyze_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        source = f.read()

    try:
        return analyze_source_metrics(source)
    except SyntaxError:
        # Try converting from Python 2 to 3
        converted = convert_python2_to_3(source)
        if not converted:
            raise SyntaxError("Could not convert Python 2 code.")
        return analyze_source_metrics(converted)

def analyze_source_metrics(source):
    raw_metrics = analyze(source)
    loc = raw_metrics.loc

    cc_scores = cc_visit(source)
    avg_cc = sum(block.complexity for block in cc_scores) / len(cc_scores) if cc_scores else 0

    halstead = h_visit(source)
    h_volume = halstead.total.volume if hasattr(halstead, 'total') else 0

    mi = mi_visit(source, True)

    return loc, avg_cc, h_volume, mi



def walk_and_analyze(input_dir):
    results = []
    for folder in os.listdir(input_dir):
        folder_path = os.path.join(input_dir, folder)
        if not os.path.isdir(folder_path):
            continue

        for file in os.listdir(folder_path):
            if file.endswith(".py"):
                file_path = os.path.join(folder_path, file)
                try:
                    loc, cc, halstead, mi = analyze_file(file_path)
                    results.append({
                        "filename": file,
                        "LOC": loc,
                        "Cyclomatic Complexity": round(cc, 2),
                        "Halstead Volume": round(halstead, 2),
                        "Maintainability Index": round(mi, 2)
                    })
                except Exception as e:
                    print(f"⚠️ Error analyzing {file_path}: {e}")
                    results.append({
                        "filename": file,
                        "LOC": "SKIPPED",
                        "Cyclomatic Complexity": "SKIPPED",
                        "Halstead Volume": "SKIPPED",
                        "Maintainability Index": "SKIPPED"
                    })
    return results


def write_results_to_csv(results, output_path="code_metrics.csv"):
    fieldnames = ["filename", "LOC", "Cyclomatic Complexity", "Halstead Volume", "Maintainability Index"]
    with open(output_path, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    print(f"✅ Metrics written to {output_path}")


from lib2to3.refactor import RefactoringTool, get_fixers_from_package

def convert_python2_to_3(source):
    fixers = get_fixers_from_package("lib2to3.fixes")
    tool = RefactoringTool(fixers)
    try:
        # Convert source in memory
        tree = tool.refactor_string(source, name="input.py")
        return str(tree)
    except Exception as e:
        print(f"❌ Failed to convert Python 2 code: {e}")
        return None

if __name__ == "__main__":
    results = walk_and_analyze(INPUT_DIR)
    write_results_to_csv(results)
