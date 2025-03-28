```python
r, c = map(int, input().split())
a = [[*map(int, input().split()), sum(input().split())] for _ in range(r)]
[print(*row) for row in zip(*reversed(a))]
print(sum([x[-1] for x in a])