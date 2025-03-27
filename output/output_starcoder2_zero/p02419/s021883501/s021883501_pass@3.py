Below is a Python program that works as intended, but I need you to refactor the code to reduce its lines and complexity, while preserving its functionality. Make the code cleaner, more concise, and improve its readability.

Here is the original Python program:
W = input().lower()
count = 0
line = []
while True:
    tmp_line = input()
    if tmp_line == "END_OF_TEXT":
        break
    line += tmp_line.lower().split()    
    
for word in line:
    if word == W:
        count += 1
    else:
        pass    
print(count)


Please provide the refactored version of the code with fewer lines and improved readability. 
DO NOT include any explanations, introductions, or concluding remarks. Just give me the Python code.