def dice_rotation(dice, command):
	# S:1->2,2->6,6->5,5->1
	if command == 'S':
		dice[0], dice[4], dice[5], dice[1] = dice[4], dice[5], dice[1], dice[0]
	# N:1->5,5->6,6->2,2->1
	elif command == 'N':
		dice[0], dice[1], dice[5], dice[4] = dice[1], dice[5], dice[4], dice[0]
	# W:1->4,4->6,6->3,3->1
	elif command == 'W':
		dice[0], dice[2], dice[5], dice[4] = dice[2], dice[5], dice[4], dice[0]
	# E:1->3,3->6,6->4,4->1
	elif command == 'E':
		dice[0], dice[3], dice[5], dice[2] = dice[3], dice[5], dice[2], dice[0]

def comparison_dices(Dice1, Dice2):
	return all(a == b for a, b in zip(Dice1, Dice2))

def full_validation_dices(Dice1, Dice2):
	for i in range(4):
		if comparison_dices(Dice1, Dice2) is True:
			return True
		else:
			dice_rotation(Dice2, 'S')
			dice_rotation(Dice2, 'N')
			dice_rotation(Dice2, 'W')
			dice_rotation(Dice2, 'E')
	return False

def test():
	n = int(input())
	Dices = []
	result = True
	for i in range(n):
		tmp_dice = list(map(int, input().split()))
		Dices.append(tmp_dice)
	for i in range(n-1):
		for j in range(i+1, n):
			if full_validation_dices(Dices[i], Dices[j]) is True:
				result = False
				break
		if result == False:
			break
	if result == True:
		print("Yes")
	else:
		print("No")

if __name__ == "__main__":
	test()