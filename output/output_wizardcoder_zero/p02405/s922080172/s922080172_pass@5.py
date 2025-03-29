```python
for line in map(int, open(0).read().split()):
    for i in range(line if line % 2 == 0 else None):
        print("#." * line + "\n" + ".#" * line)
```