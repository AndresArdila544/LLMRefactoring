n, m = map(int, input().split())
arrs = [[int(x) for x in input().split()] for _ in range(n)]
scalars = [int(input()) for _ in range(m)]
for arr in arrs:
    c = sum(arr[i]*scalars[i] for i in range(len(arr))
print(*c)