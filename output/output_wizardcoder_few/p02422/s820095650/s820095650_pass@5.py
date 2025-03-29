```python
def process_input():
    s = str(input())
    q = int(input())
    
    for i in range(q):
        d = list(map(str, input().split()))
        if d[0] == 'print':
            print(s[int(d[1]): int(d[2])+1])
        elif d[0] == 'reverse':
            s = list(s)
            s[int(d[1]):int(d[2])+1] = reversed(s[int(d[1]):int(d[2])+1])
            s = ''.join(s)
        elif d[0] == 'replace':
            s = list(s)
            s[int(d[1]):int(d[2])+1] = list(d[3])
            s = ''.join(s)
        
    print(s)
```