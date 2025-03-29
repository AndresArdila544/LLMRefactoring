n, m = map(int, input().split())
A = list()
for i in range(n):
  A += [list(map(int, input().split())]
B = [int(input()) for i in range(m)]
res = []
for i in range(n):
    value = sum([A[i][j]*B[j] for j in range(m)]
print(*[value for i in res])