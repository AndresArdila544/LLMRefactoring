```python
s = str(input())
q = int(input())
for i in range(q):
    cmd, start, end, *args = input().split()
    if cmd == 'print':
        print(s[int(start):int(end)+1])
    elif cmd == 'reverse':
        s = list(s)
        s[int(start):int(end)+1] = reversed(s[int(start):int(end)+1])
        s2 = ''
        for i in s:
            s2 += i
        s = ''.join(s2)
    elif cmd == 'replace':
        S = list(s)
        S[int(start):int(end)+1] = args
        s2 = ''
        for i in S:
            s2 += i
        s = ''.join(s2)
```