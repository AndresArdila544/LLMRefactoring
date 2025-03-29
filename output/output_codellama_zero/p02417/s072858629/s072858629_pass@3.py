import sys
cnts = {}
for line in sys.stdin:
    for c in line.lower():
        cnts[c] = cnts.get(c, 0) + 1
print(*[(chr(c), cnts.get(chr(c), 0)) for c in range(ord('a'), ord('z')+1)], sep='\n')