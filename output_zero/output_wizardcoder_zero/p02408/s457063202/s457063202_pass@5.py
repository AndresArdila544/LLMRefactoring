n = int(input())
s, h, c, d = [], [], []

def order_list(l):
    l[:] = sorted(l)  # sort list in-place and return it (no need for an extra variable)
    return l

def not_enough_cards(mark, cards):
    if len(cards) < 13:
        print(' '.join([mark + ' ' + str(x) for x in range(1, 14) if x not in cards]))

while True:
    try:
        line = input().split()
        line[1] = int(line[1])
        if line[0] == "S": s.append(line[1])
        elif line[0] == "H": h.append(line[1])
        elif line[0] == "C": c.append(line[1])
        elif line[0] == "D": d.append(line[1])
    except: break  # exit loop when no more input is available (assuming the input is a list of cards)

s = order_list(s)
h = order_list(h)
c = order_list(c)
d = order_list(d)

not_enough_cards("S", s)
not_enough_cards("H", h)
not_enough_cards("C", c)
not_enough_cards("D", d)