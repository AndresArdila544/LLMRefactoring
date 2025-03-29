n, m = list(map(int, input().split()))
matrix_a = [list(map(int, input().split()) for i in range(n))
matrix_b = [int(input()) for i in range(m)]
for row_a in matrix_a:
    print(sum(x*y for x, y in zip(row_a, matrix_b))