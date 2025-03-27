import sys
cnts = {}
for line in sys.stdin:
    for c in line.lower(): cnts[c] = cnts.get(c,0) + 1
  
print(*["{}:{}".format(chr(i),cnts.get(chr(i),0)) for i in range(ord('a'),ord('z')+1)],sep='\n')