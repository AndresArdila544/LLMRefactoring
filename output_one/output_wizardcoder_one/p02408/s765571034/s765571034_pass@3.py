for card in ['S','H', 'C', 'D']:
    for suit in range(1, 13+1):
        if (card,suit) not in [(m, int(n)) for m, n in [input().split() for i in range(int(input()))]:
            print(card, suit)