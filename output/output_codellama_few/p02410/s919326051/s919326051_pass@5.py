Here is a cleaner and more concise version of your original code:

n, m = map(int, input().split())
A = list()
for _ in range(n):
    A.append(list(map(int, input().split())))
B = list(map(int, input().split()))
res = []
for i in range(n):
  value = sum(A[i][j] * B[j] for j in range(m))
  res.append(value)
print(*res, sep=' ')