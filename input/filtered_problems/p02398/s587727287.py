a,b,c = list(map(int,input().split()))
stack = 0
for i in range(b-a+1):
    if c % (a+i) == 0:
        stack = stack + 1
print(stack)
