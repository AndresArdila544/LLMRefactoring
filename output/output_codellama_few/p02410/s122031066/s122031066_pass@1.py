n,m = map(int,input().split())
lst1 = []
lst2 = []
for s in range(n):
    aij = input().split()
    lst1.append(aij)
for t in range(m):
    bi = int(input())
    lst2.append(bi)
answer = 0
for u in range(n):
    lstA = lst1[u]
    for v in range(m):
        number1,number2 = map(int,lstA[v])
        answer+=number1*number2
print(answer)