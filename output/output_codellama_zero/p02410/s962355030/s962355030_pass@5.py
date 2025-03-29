Here is the refactored Python program:
n, m = map(int, input().split())
matrix_a = [[int(i) for i in input().split()] for _ in range(n)]
matrix_b = [int(input()) for _ in range(m)]
for row in matrix_a:
    print(sum([x*y for x, y in zip(row, matrix_b)]))