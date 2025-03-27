W, H, x, y, r = map(int, input().split())

x1 = x-r
x2 = x+r
y1 = y-r
y2 = y+r

flag = 1

if x1 < 0:
    flag = 0

if x2 > W:
    flag = 0

if y1 < 0:
    flag = 0

if y2 > H:
    flag = 0

if flag < 1:
    print("No")

else:
    print("Yes")
    
