n, x = map(int, input().split())
while (n,x):
    print(sum((i+j+k for i in range(1, n) for j in range(i+1, n) for k in range(j+1, n) if i+j+k==x))