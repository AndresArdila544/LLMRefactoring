<|start_of_text|>[3]
I need to refactor this Python program to reduce its lines and complexity while preserving its functionality:

Here is the original Python program:

s = ""
while True:
    try:
        s += input()
    except:
        break
s = s.lower()
for i in range(ord("a"),ord("z")+1):
    print(chr(i)+"  :",s.count(chr(i)))


Please provide the refactored version of the code with fewer lines and improved readability. DO NOT include any explanations, introductions, or concluding remarks. Just give me the Python code.