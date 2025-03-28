```python
n = int(input())
x = [0] + list(map(int, input().split()))
y = [0] + list(map(int, input().split()))
tmp = [[0]*6 for _ in range(n+1)]
max_diff = 0
for i in range(1, n+1):
    diff = abs(x[i]-y[i])
    tmp[i][:3] = [diff, diff**2, (tmp[i-1][5] if i>1 else 0) + diff**2]
    for j in range(4):
        tmp[i][j+3] += tmp[i][j]
    max_diff = max(max_diff, diff)
print(*tmp[n][:3])
print((tmp[n][4]**0.5))
print((tmp[n][5]**(1/3))
print(max_diff)
```