lst1 = []
lst2 = []
for s in range(n):
    aij = input().split()
    lst1.append(aij)
for t in range(m):
    bi = int(input())
    lst2.append(bi)
for u in range(n):
    answer = 0
    for v in range(m):
        number1 = int(lst1[u][v])
        number2 = lst2[v]
        answer += number1 * number2
        print(answer)