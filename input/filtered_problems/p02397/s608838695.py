while True:
	x, y = map(int, input().split())
	if x == 0 and y == 0:
		break
	[x1, y1] = sorted([x, y])
	print(x1, y1)