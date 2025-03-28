Here is the refactored version of the Python program:
```
n, m = map(int, input().split(' '))
a = [[0] * m for _ in range(n)]
b = [0] * m
c = [0] * n
for i in range(n):
    a[i] = list(map(int, input().split(' ')))
for j in range(m):
    b[j] = int(input())
for i in range(n):
    for j in range(m):
        c[i] += a[i][j] * b[j]
for j in range(n):
    print("%d" % c[j])
```