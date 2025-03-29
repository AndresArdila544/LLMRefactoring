import math

while True:
    a, op, b = input().split()
    c = int(a)
    d = int(b)
    
    if op == '+': result = c + d
    elif op == '-': result = c - d
    elif op == '*': result = c * d
    elif op == '/': result = int(c / d)
    else: break

    print(result)