w, h, x, y, r = map(int,input().split())
print("Yes") if x >= r and x <= w-r and y >= r and y <= h-r else print("No")