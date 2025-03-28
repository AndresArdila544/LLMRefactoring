```
n, m = map(int, input().split())
arrs = []
for _ in range(n):
    vector = list(map(int, input().split()))
    arrs.append(vector)
vector = list(map(int, input().split()))

for arr in arrs:
    c = 0
    for i in range(len(arr)):
        c += arr[i] * vector[i]
    print(c)
```