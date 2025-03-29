import ast

while True:
    a = input()
    if '?' in a:
        break
    print(ast.literal_eval(' '.join(a.split())))