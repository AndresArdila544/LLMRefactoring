<|start_of_text|><|/start_of_text|>

Below is a Python program that works as intended, but I need you to refactor the code to reduce its lines and complexity, while preserving its functionality. Make the code cleaner, more concise, and improve its readability.

Here is the original Python program:

a = list(map(int, input().split()))
for d in input():
    b = [a[1], a[5], a[2], a[3], a[0], a[4]]
    if d == "N":
        b = [a[1], a[5], a[2], a[3], a[0], a[4]]
    elif d == "E":
        b = [a[3], a[1], a[0], a[5], a[4], a[2]]
    elif d == "S":
        b = [a[4], a[0], a[2], a[3], a[5], a[1]]
    else:
        b = [a[2], a[1], a[5], a[0], a[4], a[3]]
    a = b
print(a[0])



Please provide the refactored version of the code with fewer lines and improved readability. 
DO NOT include any explanations, introductions, or concluding remarks. Just give me the Python code.