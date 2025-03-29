n, m = map(int, input().split())
matrix_a = [list(map(int, input().split())) for i in range(int(n))]
matrix_b = list(map(int, input().split()))
for row in matrix_a:
    print(sum([x*y for x, y in zip(matrix_b, row)]))