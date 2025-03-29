Here is the refactored version of the program with fewer lines:

# encoding:utf-8

while True:
    a,op,b = map(str, input().split())
    c,d = int(a),int(b)
    if op == '+': result = c + d
    elif op == '-': result = c - d
    elif op == '*': result = c * d
    elif op == '/': result = int(c / d)
    else: break
    print("{0}".format(result))