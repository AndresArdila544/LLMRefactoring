```python
r, c = map(int, input().split())
a = [0]*(c+1)
for _ in range(r):
    v = list(map(int, input().split())) + [sum(v)]
print(*v for _ in range(len(a)) if a.append(v[i] for i in range(c)))
```