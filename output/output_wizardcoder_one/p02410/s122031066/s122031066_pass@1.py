lst1=[]
lst2=[0]*n
answer=0
for s in range(n):
    lst1.append([int(x) for x in input().split()])
for t in range(m):
    bi=int(input())
    lst2[t]=bi
    answer+=sum(num1*num2 for num1, num2 in zip(lst1, lst2))
print(answer