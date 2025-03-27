Below is a Python program that works as intended, but I need you to refactor the code to reduce its lines and complexity, while preserving its functionality. Make the code cleaner, more concise, and improve its readability.

Here is the original Python program:

n, m = map(int, input().split())
A = list()
b = list()
for i in range(n):
    A.append(list(map(int, input().split())))
for i in range(m):
    b.append(int(input()))
for i in range(n):
    _ = 0
    for j in range(m):
        _ += (A[i][j] * b[j])
    print(_)


Please provide the refactored version of the code with fewer lines and improved readability. 
DO NOT include any explanations, introductions, or concluding remarks. Just give me the Python code.