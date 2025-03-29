x, y = map(int, input().split())

while (x,y) != (0,0):
    if x >= y:
        print(y, x)
    else:
        print(x, y)