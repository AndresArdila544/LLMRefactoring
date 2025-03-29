n, m, l = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split()) for _ in range(m))
C = [[sum(a*b for a, b in zip(row_a, col_b)) for col_b in zip(*B)] for row_a in A]
for line in C:
    print(*line)