n, m = map(int, input().split())
matrix_a = [list(map(int, input().split())) for i in range(n)]
matrix_b = [int(input()) for i in range(m)]
print([sum(x*y for (x, y) in zip(matrix_b, matrix_a[i])) for i in range(n)])