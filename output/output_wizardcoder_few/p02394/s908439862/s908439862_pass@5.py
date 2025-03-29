x,y,r = map(float, input().split())
if x > W-r and y < r or x<r or y>H-r:
    print("No")
else:
    print("Yes")