Here is a refactored version of the code:
```
a = []
n = int(input())
i = 1
while i <= n:
    x = i if i % 3 == 0 else i // 10
    a.append(x)
    i += 1
print(*a)
```