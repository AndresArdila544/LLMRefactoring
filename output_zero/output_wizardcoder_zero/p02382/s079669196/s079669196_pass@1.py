n = int(input())
x = [0] + list(map(int, input().split()))
y = [0] + list(map(int, input().split()))
tmp = [[0]*6 for _ in range(n+1)]
max_diff = 0
for i in range(1, n+1):
    diff = abs(x[i]-y[i])
    tmp[i][:3] = diff, diff**2, (tmp[i-1][3]+diff) if i > 1 else diff
    tmp[i][4:] = (tmp[i-1][4]+tmp[i][1]), (tmp[i-1][5]+tmp[i][2]) if i > 1 else tmp[i][1]
    max_diff = max(max_diff, diff)
print(*map(lambda x: round(x**0.5, 2), [tmp[n][3], tmp[n][4]]) + [max_diff])