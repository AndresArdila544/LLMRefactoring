card_lst = []
for t in 'SHDC':
    for i in range(1, 14):
        card_lst += [f"{t} {i}" for i in range(1, 14)]
n = int(input())
[print(c) for c in card_lst if c not in f"{' '.join([input() for _ in range(n)])]"]