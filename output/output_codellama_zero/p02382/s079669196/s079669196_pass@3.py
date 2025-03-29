```
n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
tmp = [[0 for i in range(6)] for j in range(n+1)]
max = 0
for i in range(1, n+1):
    absDiff = abs(x[i]-y[i])
    tmp[i][0] = absDiff
    tmp[i][1] = absDiff ** 2
    tmp[i][2] = tmp[i][1] * absDiff
    tmp[i][3] = max(tmp[i-1][3], tmp[i][0])
    tmp[i][4] = max(tmp[i-1][4], tmp[i][1]) ** (1/2)
    tmp[i][5] = max(tmp[i-1][5], tmp[i][2]) ** (1/3)
    if absDiff > max:
        max = absDiff
print(tmp[n][3])
print(tmp[n][4])
print(tmp[n][5])
print(max)
```