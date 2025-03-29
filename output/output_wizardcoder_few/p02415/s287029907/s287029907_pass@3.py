```python
for c in input():
    print(chr((ord(c)+32) if 'A'<=c<='Z' else chr(ord(c)), end='')
print()
```