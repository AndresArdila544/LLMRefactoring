```python
import math

s = str(input())
q = int(input())

for i in range(q):
    d = list(map(str, input().split()))
    if d[0] == 'print':
        print( s[int(d[1])-1:int(d[2])] )
    elif d[0] == 'reverse':
        S = list(s)
        S[int(d[1]):int(d[2])+1] = reversed(S[int(d[1]):int(d[2]+1])
        s = "".join(S)
    elif d[0] == 'replace':
        S = list(s)
        S[int(d[1]):int(d[2])+1] = list(d[3])*len(d[4])
        s = "".join(S)
```