n, m, l = map(int, input().split())
YEAH, FUCK = [], []
for i in range(n):
    YEAH.append([list(map(int, input().split())) for _ in range(i+1)] if i != 0 else [[]])
for j in range(m):
    FUCK.append([list(map(int, input().split()) for _ in range(l)])
for i in range(n):
    GOMI = sum((FUCK[k][j] * YEAH[i][k] for k in range(m))
    print(GOMI if j != l else (GOMI, end=" ")
print()