n, m = map(int, input().split())
a = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    a[i]= list(map(int, input().split()))
b=list(map(int,input().split()))
print(*sum(map(lambda x,y:x*y,a,b)),sep='\n')