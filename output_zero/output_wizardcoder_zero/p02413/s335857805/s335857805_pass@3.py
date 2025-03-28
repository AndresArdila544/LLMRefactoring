r, c = map(int, input().split())
lines = [[sum(line) for line in zip(*[map(int, input().split())]*2] + [c+1]) for _ in range(r)]
for line in lines: print(*line)