Here is the refactored version of the code:
W,H,x,y,r=map(float,input().split())
if x<r or x>(W-r) or y<r or y>(H-r):
     print("No")
     
else :
    print("Yes")