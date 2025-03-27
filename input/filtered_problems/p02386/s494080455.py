transforms = []
for i, sides in enumerate(((3,1,2,4),(2,0,3,5),(4,0,1,5),(1,0,4,5),(3,0,2,5),(2,1,3,4))):
	for j in range(4):
		r = sides[j:] + sides[:j]
		transforms.append((i, r[1], r[2], r[0], r[3], 5-i))

possibilities = set()
for _ in range(int(input())):
	die = input().split()
	new_possibilities = {tuple(die[t] for t in transform) for transform in transforms}
	if new_possibilities.intersection(possibilities):
		print('No')
		break
	possibilities.update(new_possibilities)
else:
	print('Yes')

