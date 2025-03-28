Here is a refactored version of the original program:
W,H,x,y,r = map(int, input().split())
print("Yes" if x >= r and x <= W-r and r <= y and y <= H-r else "No")