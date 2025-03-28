cnts = {}
for line in sys.stdin:
    for char in list(line.lower()):
        cnts[char] = cnts.get(char,0) + 1

for char in range(ord('a'), ord('z')+1): print(chr(char), ':', cnts.get(chr(char),0))