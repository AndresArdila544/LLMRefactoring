Here is the refactored code:
```
a = input().split()
b = a[1], a[5], a[2], a[3], a[0], a[4] if d == "N" else (a[3], a[1], a[0], a[5], a[4], a[2]) if d == "E" else (a[4], a[0], a[2], a[3], a[5], a[1]) if d == "S" else (a[2], a[1], a[5], a[0], a[4], a[3])
print(b[0])
```