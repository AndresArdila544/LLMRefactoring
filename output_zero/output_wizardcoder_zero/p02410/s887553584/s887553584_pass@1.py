n, m = map(int, input().split())
A = [list(map(int, input().split()) for _ in range(n)]
b = list(map(int, input().split() for _ in range(m))
print(" ".join([str(sum(row*col for row, col in zip(A, b)))])