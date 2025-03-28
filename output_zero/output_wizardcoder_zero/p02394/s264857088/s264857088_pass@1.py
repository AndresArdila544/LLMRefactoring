x, y, W, H = map(int, input().split())
r = int(input())
print("Yes" if x-r >= 0 and x+r <= W and y-r >= 0 and y+r <= H else "No")