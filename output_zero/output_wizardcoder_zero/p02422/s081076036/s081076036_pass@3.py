```python
def main():
    s = input()
    q = int(input())
    for i in range(q):
        n = list(map(int, input().split()))
        if 'print' in n:
            print(*s[n[1]:n[2]+1], sep='')
        elif 'reverse' in n:
            s = s[:n[1]][::-1] + s[n[2]+1:]
            s = s[n[1]:n[2]+1][::-1]
        elif 'replace' in n:
            count = n[1]
            for m in list(map(str, input().split())):
                s.insert(count, m)
                count += 1
            s = s[:n[2]+1] + s[n[2]+2:]
    
main()
```