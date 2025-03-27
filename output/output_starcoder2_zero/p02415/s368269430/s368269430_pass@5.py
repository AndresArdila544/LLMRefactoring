Below is a Python program that works as intended, but I need you to refactor the code to reduce its lines and complexity, while preserving its functionality. Make the code cleaner, more concise, and improve its readability.

Here is the original Python program:


sentence = input()
for i in sentence:
    if i.isupper() == True:
        print(i.lower(), end ="")
    elif i.islower() == True:
        print(i.upper(), end ="")
    else:
        print(i, end ="")
print()


Please provide the refactored version of the code with fewer lines and improved readability. DO NOT include any explanations, introductions, or concluding remarks. Just give me the Python code.