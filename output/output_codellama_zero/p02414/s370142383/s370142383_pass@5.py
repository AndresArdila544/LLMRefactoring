n, m, l = map(int, input().split())
A = [[int(s) for s in input().split()] for i in range(n)]
B = [[int(s) for s in input().split()] for i in range(m)]
print(*[str(sum(a*b for a, b in zip(row1, row2))) for row1, row2 in zip(A, B)], sep=' ')