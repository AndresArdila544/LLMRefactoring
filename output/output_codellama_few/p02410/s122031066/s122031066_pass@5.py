Here is a refactoring of the original code:

lst1 = []
lst2 = []
n, m = map(int, input().split())
for s in range(n):
    lst1.append(list(map(int, input().split())))
for t in range(m):
    lst2.append(int(input()))
for u in range(n):
    lstA = lst1[u]
    for v in range(m):
        answer += lstA[v] * lst2[v]
        print(answer)