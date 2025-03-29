r, c = map(int, input().split())
for i in range(r):
    row = list(map(int, input().split())) + [sum(list(map(int, input().split()))]
print(" ".join(map(str, row)))

total = []
for j in zip(*row):
    total.append(sum(j))
print(" ".join(map(str, total))