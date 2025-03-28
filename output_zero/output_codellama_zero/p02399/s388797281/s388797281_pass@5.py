Here's the refactored Python program:

a, b = map(int, input().split())
d = a // b
r = a % b
f = f"{a / b:10.20f}"
print(d, r, f)