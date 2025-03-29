W,H,x,y,r=map(float,input().split())
print("Yes" if x>W-r and x<r and y<r and y>H-r else "No")