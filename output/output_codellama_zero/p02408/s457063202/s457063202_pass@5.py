n = int(raw_input())
s = []
h = []
c = []
d = []
i = 0
for _ in xrange(n):
    line = raw_input().split(" ")
    if line[0] == "S":
        s.append(int(line[1]))
    elif line[0] == "H":
        h.append(int(line[1]))
    elif line[0] == "C":
        c.append(int(line[1]))
    elif line[0] == "D":
        d.append(int(line[1]))
    
def order_list(list):
    return sorted(list)

def not_enough_cards(mark, list):
    for x in range(1, 14):
        if len(list) == i or x != list[i]:
            print mark + " " + str(x)
        else:
            i += 1
    
not_enough_cards("S", s)
not_enough_cards("H", h)
not_enough_cards("C", c)
not_enough_cards("D", d)