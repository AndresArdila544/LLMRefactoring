```python
a, b = map(int, input().split())
bs = [list(map(int, input().split())) for i in range(a)]
for i in range(b+1):
    bs[i].append(sum([bs[j][i] for j in range(a)]))
print("\n".join(" ".join(str(x) for x in row)
              for row in zip(*[[*map(sum, zip(*row)] + [sum(row)] if i == b else row 
                               for i, row in enumerate(bs]))])
```