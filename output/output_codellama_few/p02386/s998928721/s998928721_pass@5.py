n = int(input())
dices = []
for _ in range(n):
    dices.append(Dice([int(i) for i in input().split()]))
if all(is_same(c[0], c[1]) for c in combinations(dices, 2)):
    print('Yes')
else:
    print('No')