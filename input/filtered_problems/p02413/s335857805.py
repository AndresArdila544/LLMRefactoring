r, c = map(int, input().split())
lines = []
for i in range(r):
    lines.append(list(map(int, input().split())))

for line in lines:
    line.append(sum(line))

lines.append([sum([line[i] for line in lines]) for i in range(c  + 1)])

for line in lines:
    print(*line)

