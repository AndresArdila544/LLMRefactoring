lst1 = []
lst2 = []
answer = 0
n, m = map(int, input().split())
for i in range(n):
    lst1.append([*map(int, input().split())] * 2)
for j in range(m):
    bi = int(input())
    lst2.append(bi)
for u in range(n):
    for v in range(m):
        answer += lst1[u][v] * lst2[v]
print(answer)