n, m = map(int, input().split())
A = [list(map(int, input().split())) for i in range(n)]
B = list(map(int, input().split()))
res = [[sum(a*b for a, b in zip(A[i], B)) for i in range(m)]]
for value in res:
  print(value)