```python
def to_lowercase(char):
    return chr(ord(char) ^ 0x20)

for c in input():
    if 'a' <= c <= 'z':
        print(to_lowercase(c), end='')
    elif 'A' <= c <= 'Z':
        print(chr(ord(c) | 0x20), end='')
    else:
        print(c, end='')
print()
```