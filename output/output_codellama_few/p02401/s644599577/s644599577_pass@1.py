import math

# Read inputs
a, op, b = input().split()
a, b = int(a), int(b)

# Initialize variables
t = 0
ans = 0

# Evaluate expressions and print results
while op != "?":
    if op == "+":
        ans = a + b
    elif op == "-":
        ans = a - b
    elif op == "*":
        ans = a * b
    elif op == "/":
        ans = a // b
    print(f"{ans}")
    t += 1
    a, op, b = input().split()
    a, b = int(a), int(b)