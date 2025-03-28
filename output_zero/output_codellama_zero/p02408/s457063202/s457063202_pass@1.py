n = int(raw_input())
i = 0
s = []
h = []
c = []
d = []

def order_list(list):
    l = len(list)
    for i in range(l):
        j = i + 1
        while j < l:
            if list[i] > list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
            j += 1
    return list
    
def not_enough_cards(mark, list):
    i = 0
    for x in range(1, 14):
        if i >= len(list):
            print mark + " " + str(x)
        elif x != list[i]:
            print mark + " " + str(x)
        else:
            i += 1
    
while i < n:
    line = raw_input().split(" ")
    line[1] = int(line[1])
    if line[0] == "S":
        s.append(line[1])
    elif line[0] == "H":
        h.append(line[1])
    elif line[0] == "C":
        c.append(line[1])
    elif line[0] == "D":
        d.append(line[1])
    i += 1

order_list(s)
order_list(h)
order_list(c)
order_list(d)
not_enough_cards("S", s)
not_enough_cards("H", h)
not_enough_cards("C", c)
not_enough_cards("D", d)