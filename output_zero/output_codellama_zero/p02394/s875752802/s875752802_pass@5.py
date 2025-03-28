W,H,x,y,r = map(int,input().split())
if 0<=x<W and 0<=y<H and x+r <= W and y+r <= H:
    print("Yes")
else:
    print("No")