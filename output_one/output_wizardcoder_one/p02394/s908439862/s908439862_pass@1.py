W,H,x,y,r = map(float,input().split())

print("Yes" if x>0 and y>0 and 2*r<=min(W,H) else "No")