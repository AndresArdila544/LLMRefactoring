cards = ""
for i in range(10):
    e = input()
    if e == "-":
        break
    else:
        cards = e
        len_cards = len(cards)
        m = int(input())
        for j in range(m):
            cards += cards
            h = int(input())
            cards = cards[h:h-len_cards]
        print(cards)
