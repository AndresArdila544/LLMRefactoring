```
r, c = map(int, input().split())
lines = []
for i in range(r):
    lines.append([int(x) for x in input().split()])

for line in lines:
    sum_line = sum(line)
    line.append(sum_line)
    line.extend([sum_line for _ in range(c + 1)])

for line in lines:
    print(*line)
```