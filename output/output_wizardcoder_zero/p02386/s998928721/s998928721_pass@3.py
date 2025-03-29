def is_same(d1, d2):
    for f1 in d1.all_face():
        found = False
        for f2 in d2.all_face():
            if f1 == f2:
                found = True
                break
        if not found:
            return False
    return True

n = int(input())
dices = []
for _ in range(n):
    dices.append([int(i) for i in input().split()])
ans = all(is_same(d1, d2) for d1, d2 in combinations(dices, 2))
print('Yes' if ans else 'No')