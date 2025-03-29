Here is the original Python program:

for c in input():
    if 'a'<=c<='z':
        print(chr(ord(c)^0x20), end='')
    elif 'A'<=c<='Z':
        print(chr(ord(c)|0x20), end='')
    else:
        print(c, end='')
print()


Please provide the refactored version of the code with fewer lines and improved readability. 
DO NOT include any explanations, introductions, or concluding remarks. Just give me the Python code, no quotations. Just the code.