```python
for char in range(ord('a'), ord('z')+1):
    count = sum([int(char == ord(c.lower()) for c in input().lower()])
    print(f"{chr(char)}: {count}", end=' ')
```