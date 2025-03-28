Here is the refactored version of your original Python program:

a,b,c = map(int,input().split())
ans = sum(i for i in range(a,b+1) if c%i == 0)
print(ans)