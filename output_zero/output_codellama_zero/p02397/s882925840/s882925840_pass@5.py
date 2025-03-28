Here is the refactored version of the code:

```
while True:
    a = list(map(int, input().split()))
    if not a: break
    min_a, max_a = sorted(a)
    print("{} {}".format(min_a,max_a))
```