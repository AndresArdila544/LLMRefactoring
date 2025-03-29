Here is a refactored version of the original code:

import sys
from collections import Counter

lines = sys.stdin.readlines()

for line in lines:
    for c in line.lower():
        if ord(c) >= 97 and ord(c) <= 123:
            dict[c] += 1

print(*dict.items(), sep='\n')