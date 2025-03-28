a,b,c = map(int,input().split())
x = 0
for n in range(1,b+1):
    if c % n == 0:
        x += 1
print(x)