transforms = [(i, *[*sides[j:] + sides[:j], 5-i) for i, sides in enumerate((3,1,2,4),(2,0,3,5,(1,0,4,5),(3,0,2,5))]
possibilities = set()
for _ in range(int(input())):
	die = input().split()
	new_possibilities = {tuple(die[t] for t in transforms)
	if new_possibilities.intersection(possibilities):
		print('No')
		break
	possibilities.update(new_possibilities)
else:
	print('Yes')