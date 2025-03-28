n = int(input())
card = [list(range(1, 14)) for i in range(4)]
for _ in range(n):
    suit, val = input().split()
    card[{"S":0,"H":1,"C":2,"D":3}[suit].remove(int(val))
for i, suit in enumerate(card):
    for j in suit:
        print("{} {}".format("SHCD"[i], j) if j else None)