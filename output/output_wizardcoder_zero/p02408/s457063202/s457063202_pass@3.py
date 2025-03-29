def order_list(lst):
    l = len(lst)
    for i in range(l-1):
        for j in range(i+1, l):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

for _ in range(int(raw_input())):
    card, value = raw_input().split()
    if card == "S":
        s.append(int(value))
    elif card == "H":
        h.append(int(value))
    elif card == "C":
        c.append(int(value)
    else:
        d.append(int(value)

for suit in [s, h, c, d]:
    print(" ".join([str(x) for x in order_list(suit) if x not in range(1, 14)]))
'''