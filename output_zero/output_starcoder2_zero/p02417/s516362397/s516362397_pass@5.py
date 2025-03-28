# Solution:

import fileinput
T = [0 for i in range(26)]
for line in fileinput.input():
    S = list(map(int, line.encode()))
    A = ord('A')
    Z = ord('Z')
    a = ord('a')
    z = ord('z')
    for c in S:
        if A <= c <= Z or a <= c <= z:
            T[c - (ord(chr(c)) if c > 97 else ord(chr(c)))] += 1
for c in range(a, z + 1):
    print(chr(c), ":", T[c - a])