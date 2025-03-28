import math
W, H, x, y, r = map(float, input().split())
if r >= min(x, W - x, y, H - y): 
    print("Yes")
else:
    print("No")