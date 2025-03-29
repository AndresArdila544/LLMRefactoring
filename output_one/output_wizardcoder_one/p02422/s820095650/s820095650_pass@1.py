```python
import math

s = str(input())
q = int(input())
for _ in range(q):
    d_list=[]
    s2 = ''
    d = list(map(str, input().split()))
    if d[0] == 'print':
        print(s[int(d[1]): int(d[2])+1 ])
    elif d[0] == 'reverse':
        S = list(s)
        S[int(d[1]):int(d[2])+1] = reversed(S[int(d[1]):int(d[2])+1])
        for i in S:
            s2 += i
        s = ''.join(s2)
    elif d[0] == 'replace':
        S = list(s)
        S[int(d[1]):int(d[2])+1] = [str(d[3])]*len(S[int(d[1]):int(d[2])+1])
        for i in S:
            s2 += i
        s = ''.join(s2)
```