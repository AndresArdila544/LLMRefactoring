x1,y1,x2,y2 = map(float, input().split())
print(round(math.hypot(x2-x1, y2-y1),8))