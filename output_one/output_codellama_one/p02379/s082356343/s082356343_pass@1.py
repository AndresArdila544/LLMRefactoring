def distance(x1, y1, x2, y2):
    return math.hypot(x1-x2, y1-y2)

print(distance(*map(float, input().split())))