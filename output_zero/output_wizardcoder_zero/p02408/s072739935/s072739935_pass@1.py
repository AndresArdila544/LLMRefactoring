S=['S 1','S 2','S 3','S 4','S 5','S 6','S 7','S 8','S 9','S 10','S 11','S 12','S 13']
H=['H 1','H 2','H 3','H 4','H 5','H 6','H 7','H 8','H 9','H 10','H 11','H 12','H 13']
C=['C 1','C 2','C 3','C 4','C 5','C 6','C 7','C 8','C 9','C 10','C 11','C 12','C 13']
cards=[S,H,C]
for i in range(len(cards)):
    for card in cards[i]:
        if card.split()[0]=='S':
            S.remove(card)
        elif card.split()[0]=='H':
            H.remove(card)
        else:
            C.remove(card)
for i in range(4):
    for j in cards[i]:
        print(j)