```python
s = str(input())
for i in range(int(input())):
    d = input().split()
    if d[0] == 'print':
        print( s[ int(d[1]) : int(d[2])+1 ] )
    elif d[0] == 'reverse':
        S = list(s)
        S[int(d[1]):int(d[2])+1] = reversed(S[int(d[1]):int(d[2])+1])
        s = "".join(S)  
    elif d[0] == 'replace':
        S = list(s)
        S[int(d[1]):int(d[2])+1] = [d[3]] * (len(d[2:]))
        s = "".join(S)  
```