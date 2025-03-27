Here is a refactored version of the original program:
while True:
	x, y = map(int, input().split())
	if not x and not y:
		break
	[x1, y1] = sorted([x, y])
	print(x1, y1)