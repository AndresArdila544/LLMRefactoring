a,b,c = map(int,input().split())
x = 0
n = a
while True:
    if c % n == 0:
        x += 1
    n += 1
    if n > b:
        break
print(x)
