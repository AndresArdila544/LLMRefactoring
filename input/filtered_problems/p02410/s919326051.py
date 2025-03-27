n, m = map(int, input().split())
A = list()

for i in range(n):
    A.append(list(map(int, input().split())))

B = list()
for i in range(m):
    B.append(int(input()))
res = []
for i in range(n):
  value = 0
  for j in range(m):
    value += A[i][j] * B[j]
  print(value)
