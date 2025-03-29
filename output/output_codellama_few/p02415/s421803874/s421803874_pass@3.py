Here is a refactored version of the program:

x = input()
print(''.join(v.lower() if v.isupper() else v.upper() for v in x))