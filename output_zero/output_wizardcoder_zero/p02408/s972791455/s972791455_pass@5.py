n = int(input())
s_card, h_card, c_card, d_card = [], [], [], []
for i in range(4):
    for j in range(13):
        card = input().split()
        if card[0] == "S":
            s_card.append(int(card[1]))
        elif card[0] ==  "H":
            h_card.append(int(card[1]))
        elif card[0] ==  "C":
            c_card.append(int(card[1])
        else:
            d_card.append(int(card[1])

print("S", *s_card)
print("H", *h_card)
print("C", *c_card)
print("D", *d_card)