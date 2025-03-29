W, H, x, y, r = map(int, input().split())

flag = all((x-r) >= 0, (x+r) <= W, (y-r) >= 0, (y+r) <= H)

print("Yes" if flag else "No")