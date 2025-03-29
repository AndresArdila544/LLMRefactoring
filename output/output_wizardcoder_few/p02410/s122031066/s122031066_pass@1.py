lst1 = []
lst2 = []
answer = 0
n, m = map(int, input().split())
for s in range(n):
    aij = list(map(int, input().split()))
    lst1.append(aij)
for t in range(m):
    bi = int(input())
    lst2.append(bi)
for u in range(n):
    for v in range(m):
        answer += lst1[u][v] * lst2[v]
    print(answer)