Here is the refactored version of the code:

a=[]
n=int(input())
i=1
while i <= n:
    x = i if i % 3 == 0 else x//10
    a.append(x) if x%10==3 else None
    i+=1
print(' ', end='')
print(*a)