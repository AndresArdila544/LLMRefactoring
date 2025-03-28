N = int(input())
AP=BP=0
for i in range(N):
    A, B = input().split()
    X = max(len(A), len(B))
    A = A.ljust(X,'0')
    B = B.ljust(X,'0')
    for j in range(X):
        if A[j] > B[j]: AP+=3; break
        elif B[j] > A[j]: BP+=3; break
print(AP,BP)