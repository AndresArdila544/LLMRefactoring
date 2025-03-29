matrix_size = [int(x) for x in input().split()]
vector_b = [int(input()) for _ in range(matrix_size[1])]
result = [[x*y for x, y in zip(row, vector_b)] for row in matrix]
for r in result:
    print(sum(r))