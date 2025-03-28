n, m = map(int, input().split())
A, B = [], []
for _ in range(n): A += [list(map(int, input().split()))]
B = list(map(int, input().split()))
for i in range(n): res.append(sum(x * y for x, y in zip(A[i], B))
print(*res)