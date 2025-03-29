lst1=[]
lst2=[]
answer=0
n,m=(int(x) for x in input().split())
for s in range(n):
    lst1.append(input().split())
for t in range(m):
    lst2.append(int(input()))
for u in range(n):
    lstA=lst1[u]
    for v in range(m):
        number1=int(lstA[v])
        number2=lst2[v]
        answer+=number1*number2
    print(answer)
    answer=0