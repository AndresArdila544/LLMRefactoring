```python
r, c = map(int, input().split())
a = []
for i in range(r):
    a.append([sum(map(int, input().split()))] + list(map(int, input().split())))
print(*zip(*a[::-1])[0], sep=' ')
for i in zip(*a)[c]: print(i, end=' ')
print(sum(zip(*a)[c][-1], end='')
```