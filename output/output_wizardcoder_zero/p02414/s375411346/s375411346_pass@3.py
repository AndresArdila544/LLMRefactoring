```python
N, M, L = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [[int(input()) for _ in range(M)] for _ in range(L)]
for row in A:
    ans = sum(row[i]*B[i][j] for i in range(M) for j in range(L-1))
    print(ans, end=' ')
print(sum(A[i][k]*B[i][L-1] for i in range(N)))
```