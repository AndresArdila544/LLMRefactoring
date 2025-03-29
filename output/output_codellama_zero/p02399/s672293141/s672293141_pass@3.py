Here is the refactored version:

a, b = map(int, input().split())
d = a // b #integer division
r = a % b
f = float(a) / float(b)
print(d, r, "%10.8f"%f)

This code is significantly shorter and more concise than the original version, yet it performs the same operations while keeping readability high.