refactored_cards = ""
while True:
    e = input()
    if e == "-":
        break
    else:
        cards = e
        len_cards = len(cards)
        m = int(input())
        for j in range(m):
            h = int(input())
            cards += cards[:h]
print(cards)