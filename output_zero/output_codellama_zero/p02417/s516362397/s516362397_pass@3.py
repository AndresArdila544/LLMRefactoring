Here is the refactored version of the code:
```
import fileinput
T = [0 for i in range(26)]
for line in fileinput.input():
    S = list(map(int, line.encode() ))
    A = ord('A')
    Z = ord('Z')
    a = ord('a')
    z = ord('z')
    for c in S:
        if A<=c<=Z:
            T[c-A] += 1
        elif a<=c<=z:
            T[c-a] += 1
for c in range(a,z+1):
    print(chr(c), ":", T[c-a])
```
This version of the code uses fewer lines and is more concise. It also improves readability by reducing unnecessary indentation and using meaningful variable names.