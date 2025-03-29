n, m = map(int, input().split())
a = [[0]*m for i in range(n)]
b = [int(input()) for j in range(m)]
for row in a: print(sum(x*y for x, y in zip(row, b))