lst1=[]
lst2=[]
answer=0
n,m=(int(x) for x in input().split())
for s in range(n):
    aij=input().split()
    lst1.append(aij)
for t in range(m):
    bi=int(input())
    lst2.append(bi)
for u in range(n):
    lstA=lst1[u]
    for v in range(m):
        number1=int(lstA[v])
        number2=lst2[v]
        answer+=number1*number2
    print(answer)
    answer=0
