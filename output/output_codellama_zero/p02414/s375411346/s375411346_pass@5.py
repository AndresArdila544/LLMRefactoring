N,M,L = (int(i) for i in input().split())
A = [[int(i) for i in input().split()] for i in range(N)]
B = [[int(i)for i in input().split()] for i in range(M)]
C = [ans for i in range(N) for i2 in range(L) if i2 == L-1 else print(ans, end=" ")]
print(*C,sep='\n')