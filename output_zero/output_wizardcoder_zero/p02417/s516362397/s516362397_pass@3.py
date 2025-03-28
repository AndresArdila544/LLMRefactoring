```python
with fileinput.input() as f:
    T = [0 for i in range(26)]
    for line in f:
        S = list(map(ord, line.encode()))
        A = ord('A')
        Z = ord('Z')
        a = ord('a')
        z = ord('z')
        for c in S:
            if A<=c<=Z: T[c-A] += 1
            elif a<=c<=z: T[c-a] += 1
    
    for c in range(a, z+1):
        print(chr(c),":",T[c-a])
```