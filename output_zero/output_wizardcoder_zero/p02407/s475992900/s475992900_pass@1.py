```python
print(' '.join(map(str, reversed([int(num) for num in input().split()][1:])) + [input()])