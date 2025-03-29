```python
r, c = map(int, input().split())
lines = [list(map(int, input().split())) for i in range(r)] + [[sum(line) for line in lines] + [sum([line[i] for line in lines])] for i in range(c+1)]
for line in lines: print(*line)
```