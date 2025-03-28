r, c = map(int, input().split())
lines = [list(map(int, input().split())) for i in range(r)] + [[sum([lines[i][j] for j in range(c+1)]) for i in range(len(lines)]]
for line in lines:
    print(*line)