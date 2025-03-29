n = int(input())
dices = [Dice([int(i) for i in input().split() for _ in range(n)]
if all(is_same(d1, d2) for d1, d2 in combinations(dices, 2)):
    print('Yes')
else:
    print('No')