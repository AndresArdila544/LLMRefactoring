Here is the refactored version of the code:
n,m = map(int, input().split())
matrix_a = [list(map(int,input().split())) for i in range(n)]
matrix_b = list(map(int, input().split()[1:]))
print(sum([x*y for (x, y) in zip(matrix_b, matrix_a[i])]))