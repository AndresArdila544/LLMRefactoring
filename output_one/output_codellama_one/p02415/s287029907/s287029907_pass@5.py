Here is a refactoring of the Python program:

import sys
for c in sys.stdin:
    if 'a' <= c <= 'z':
        print(chr(ord(c) ^ 0x20), end='')
    elif 'A' <= c <= 'Z':
        print(chr(ord(c) | 0x20), end='')
    else:
        print(c, end='')
print()