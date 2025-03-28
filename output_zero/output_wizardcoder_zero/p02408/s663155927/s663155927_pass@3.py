def remove_cards():
    cards = ['S ' + str(i) for i in range(1, 14)] + ['H ' + str(i) for i in range(1, 14)] + ['D ' + str(i) for i in range(1, 14)]
    n = int(input())
    for _ in range(n):
        cards.remove(input().strip()[0] + str(int(input()))
    for card in sorted(cards):
        print(card)