```
a = sorted(list(map(int, input().split())))
for x in range(1, len(a)):
    print(" %d" % a[x], end='')
print(a[0],end='')
```