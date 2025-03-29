n, m = map(int, input().split())
A = list()
for i in range(n): A += [list(map(int, input().split())]
B = list()
for i in range(m): B += [input()]
res = []
for i in range(n):
  value = sum([A[i][j] * B[j] for j in range(m)])
print(value)

# Refactored version of the code with fewer lines and improved readability.