n, m = map(int, input().split())
A=list(map(int,input().split())) for i in range(m):B.append(int(input())) res=[sum(i*j for i, j in zip(A[i], B)) for i in range(n)] 
print(res)