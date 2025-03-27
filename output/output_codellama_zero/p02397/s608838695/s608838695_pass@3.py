Here is a more concise version of your code:

while True:
	x, y = map(int, input().split())
	if x == 0 and y == 0: break
	print(sorted([x, y]))