def playCards():
    cards = ""
    while True:
        e = input()
        if e == "-": break
        cards += e
        m = int(input())
        for j in range(m):
            cards += cards[:10]
            h = int(input())
            cards = cards[h:]
    print(cards)