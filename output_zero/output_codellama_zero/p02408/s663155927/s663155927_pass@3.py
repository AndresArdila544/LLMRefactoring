Here is the refactored Python program:

cards = []
patterns = ['S', 'H', 'C', 'D']
n = int(input())
for p in patterns:
	cards += [p + " " + str(i) for i in range(1, 13+1)]
for _ in range(n):
    cards.remove(input())
for card in cards:
    print(card)