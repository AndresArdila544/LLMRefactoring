Here is a refactored version of the original program:

a,b,c=map(int,input().split())
s=sum([i for i in range(a,b+1) if i!=0 and c%i==0])
print(s)