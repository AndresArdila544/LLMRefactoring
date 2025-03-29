n, m = map(int, input().split())
A = [[int(x) for x in input().split()] for _ in range(n)]
B = [int(input()) for _ in range(m)]
for row in A:
    res = sum(x * y for x, y in zip(row, B))
    print(res)