```
while True:
    a = map(int, raw_input().split())
    if a == [0, 0]: break
    for x in sorted(a): print x,
    print()
```