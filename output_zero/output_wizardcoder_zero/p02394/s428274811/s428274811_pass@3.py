x, y, W, H = map(int, input().split())
r = int(input())
print("Yes" if x+r <= W and x-r >= 0 and y+r <= H and y-r >= 0 else "No")