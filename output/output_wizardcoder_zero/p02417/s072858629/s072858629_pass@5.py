import sys
from string import ascii_lowercase

for line in sys.stdin:
    for c in line.lower():
        if c in ascii_lowercase:
            cnts = {c:cnts.get(c,0) + 1} if cnts else {c:1}

for i in range(ord('a'), ord('z')+1):
    print(chr(i), ':', cnts.get(chr(i), 0))