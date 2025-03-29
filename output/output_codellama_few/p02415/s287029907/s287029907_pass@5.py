for c in input():
    print((c if 'a' <= c <= 'z' else chr(ord(c) | 0x20)) if c.isalpha() else c, end='')
print()