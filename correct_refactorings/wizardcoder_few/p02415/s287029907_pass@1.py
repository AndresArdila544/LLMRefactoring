for c in input():
    print(chr(ord(c)^0x20) if 'a'<=c<='z' else chr(ord(c)|0x20), end='')
print()