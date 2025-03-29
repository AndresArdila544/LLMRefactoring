# Refactored code (with fewer lines and improved readability)
r, c = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(r)]
for line in lines:
    line.append(sum(line))
total_row = sum([line[i] for line in lines for i in range(c + 1)])
lines.append(total_row)
for line in lines:
    print(*line)