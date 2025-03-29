lst1=[]
lst2=[]
for i in range(int(input())):
    lst1.append([int(x) for x in input().split()])
for j in range(int(input()):
    lst2.append(int(input())
print(sum(sum(a*b for a, b in zip(*lst1)) for i,j in enumerate(zip(lst1[i],lst2) if i%2==0 and j%2==0))/len(lst2))