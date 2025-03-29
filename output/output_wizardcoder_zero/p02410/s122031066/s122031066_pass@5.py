lst1 = []
lst2 = []
answer = 0
n, m = (int(x) for x in input().split())
for s in range(n):
    aij = list(map(int, input().split()))
    lst1.append(aij)
for t in range(m):
    bi = int(input())
    lst2.append(bi)
for u in range(n):
    lstA = lst1[u]
    for v in range(m):
        answer += sum(lstA[v] * i for i in lst2)
print(sum(answer))