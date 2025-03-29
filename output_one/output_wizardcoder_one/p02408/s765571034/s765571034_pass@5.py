cards = set()
for i in range(int(input())):
    card = input().split()
    suit, value = card[0], int(card[1])
    if (suit, value) not in cards:
        print(f"{suit} {value}")