lst1 = []
lst2 = []
for s in range(int(input().split()[0])):
    aij = input().split()
    lst1.append(aij)
    lst2.append(int(input()))
    
answer = 0
for u in range(len(lst1)):
    for v in range(len(lst2)):
        answer += int(lst1[u][v])*lst2[v]
print(answer)