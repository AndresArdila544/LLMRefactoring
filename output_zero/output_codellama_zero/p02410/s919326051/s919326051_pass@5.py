```
n, m = map(int, input().split())
A = list(map(list, input().split()))
B = list(map(int, input().split()))
res = [sum(i*j for i, j in zip(a, b)) for a in A for b in B]
for i in res:
  print(i)
```