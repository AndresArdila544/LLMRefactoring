n = int(input())
s, h, c, d = [], [], []
def order_cards(lst):
  l = len(lst)
  for i in range(l):
    j = i + 1
    while j < l:
      if lst[i] > lst[j]:
        lst[i], lst[j] = lst[j], lst[i]
      j += 1
  return lst

def print_missing_cards(mark, cards):
  ordered_cards = order_cards(sorted(cards))
  for x in range(1, 14):
    if len(ordered_cards) == 0 or x != ordered_cards[0]:
      print(f"{mark} {x}")
    else:
      del ordered_cards[0]

for _ in range(n):
  line = input().split()
  if line[0] == "S":
    s.append(int(line[1]))
  elif line[0] == "H":
    h.append(int(line[1]))
  elif line[0] == "C":
    c.append(int(line[1]))
print_missing_cards("S", s)
print_missing_cards("H", h)
print_missing_cards("C", c)
print_missing_cards("D", d)