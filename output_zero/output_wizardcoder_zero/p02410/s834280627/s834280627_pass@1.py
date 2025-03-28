matrix_size = list(map(int, input().split()))
vector_b = [int(input()) for i in range(matrix_size[1])]
result = [[x * y for x, y in zip(*zip(*r)] for r in ([list(map(int, input().split())] + [vector_b])][:matrix_size[0]])]
print(' '.join(str(sum(row)) for row in result)