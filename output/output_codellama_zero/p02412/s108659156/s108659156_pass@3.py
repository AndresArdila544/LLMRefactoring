Here is the refactored version of the original Python program:

while True:
    n, x = map(int, input().split())
    if n == x == 0: break
    cnt = sum(i+j+k==x for i in range(1,n-1) for j in range(i+1,n) for k in range(j+1,n+1))
    print(cnt)