Below is the Python program that should work correctly:

import sys
s=sys.stdin.read().lower()
for c in map(chr, range(97,123)):
    print(c,':',s.count(c))