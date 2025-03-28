N, M, L = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split()) for _ in range(M)]
for i in range(N):
    ans = sum(A[i][j]*B[j][L-1] for j in range(M))
    print(ans if L > 1 else ' '.join(map(str, [ans])) + ' ', end='')
print()