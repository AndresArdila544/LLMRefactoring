Here is a refactored version of your code with fewer lines:
```
r, c = map(int, input().split())
lines = []
for i in range(r):
    lines.append([int(x) for x in input().split()])

lines.append([sum([line[i] for line in lines]) for i in range(c + 1)])

for line in lines:
    print(*line)
```