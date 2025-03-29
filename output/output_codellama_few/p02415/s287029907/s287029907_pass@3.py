import sys

for c in sys.stdin.read():
    if 'a' <= ord(c) <= 'z':
        print(chr(ord(c) ^ 0x20), end='')
    elif 'A' <= ord(c) <= 'Z':
        print(chr(ord(c) | 0x20), end='')
    else:
        print(c, end='')
print()