```python
def process_commands():
    s = input()
    q = int(input())
    for _ in range(q):
        d = input().split()
        if d[0] == 'print':
            print(s[int(d[1])-1:int(d[2])])
        elif d[0] == 'reverse':
            s = list(s)
            s[int(d[1]):int(d[2])+1] = reversed(s[int(d[1]):int(d[2]+1)]);
            s = ''.join(s)
        elif d[0] == 'replace':
            s = list(s)
            for i in range(len(d)-1, int(d[2])+1):
                if i < len(s):
                    s.pop(int(d[1]))
            s.insert(int(d[1]), d[-1]);
            s = ''.join(s)
process_commands()
```