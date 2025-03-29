```python
count = 0
W = input().lower()
for _ in range(int(input())):
    count += len([w for w in input().split() if w == W])
print(count)
```