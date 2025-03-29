cards = []
patterns = ['S', 'H', 'C', 'D']
n = int(input())
for p in patterns:
    for i in range(1, 13+1):
        cards.append(p + ' ' + str(i))
for _ in range(n):
    cards.remove(input())
for card in cards:
    print(card)