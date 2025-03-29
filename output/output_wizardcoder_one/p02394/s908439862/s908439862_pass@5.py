x1, y1, x2, y2 = map(float, input().split())
d = math.hypot((x1-x2),(y1-y2) if x1 != x2 or y1 > y2 else 0)
print("Yes" if d >= r else "No")