def roll_dice(d, q):
	'''Rolls dice and returns result'''
	rolls = []
	while len(rolls) < q:
		a1, a2, a3, a4, a5, a6 = d
		com = random.choice(['E', 'W', 'S', 'N'])
		if com == 'E':
			d = [a4, a2, a1, a6, a5, a3]
		elif com == 'W':
			d = [a3, a2, a6, a1, a5, a4]
		elif com == 'S':
			d = [a5, a1, a3, a4, a6, a2]
		elif com == 'N':
			d = [a2, a6, a3, a4, a1, a5]
		rolls.append(d)
	return rolls[-1][2]

d = list(map(int, input().split()))
q = int(input())
print(roll_dice(d, q))