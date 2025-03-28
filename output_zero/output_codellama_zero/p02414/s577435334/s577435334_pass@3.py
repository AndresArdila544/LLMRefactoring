Here is the refactored version of the code:

N, M, L = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
B = [list(map(int, input().split())) for i in range(M)]
C = [[sum(a*b for a, b in zip(r1, r2)) for r2 in B] for r1 in A]
for line in C:
    print(*line)