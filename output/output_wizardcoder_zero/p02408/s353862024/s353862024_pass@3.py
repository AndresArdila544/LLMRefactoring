def print_missing(n):
    s = [False]*13
    h = [False]*13
    c = [False]*13
    missing_cards = []
    
    for _ in range(n):
        card, suit = input().split()
        suit_map = {"S": s, "H": h, "C": c}
        if not suit_map[suit][int(card)-1]:
            missing_cards.append((card, suit))
    
    for card in range(13):
        if all(s) and all(h) and all(c):
            break
        else:
            if not s[card]:
                print("S %d"%(card+1))
            elif not h[card]:
                print("H %d"%(card+1)
            elif not c[card]:
                print("C %d"%(card+1)
    
    return missing_cards

n = int(input())
missing_cards = print_missing(n)