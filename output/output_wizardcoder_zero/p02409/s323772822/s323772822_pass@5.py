n=int(input())
a=[[0]*10 for _ in range(3)]
for i in range(n):
    b,f,v=map(int,input().split())
    a[(b-1)%4][(f-1)%3]+=v
for row in a:
    print(*row)
print('####################'*(3 if n>1 else '')