refactored_code = '''
import sys
for line in sys.stdin:
    for c in list(line.lower()):
        count[c] = count.get(c, 0) + 1
   
for i in range(ord('a'), ord('z')+1): print(chr(i), ':', count.get(chr(i), 0))
'''