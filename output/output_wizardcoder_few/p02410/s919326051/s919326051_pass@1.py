n, m = map(int, input().split())
A = []
B = [0] * n
for i in range(n):
    A += list(map(int, input().split()))

for j in range(m):
  value = sum([x * B[j] for x in A])
print(value)