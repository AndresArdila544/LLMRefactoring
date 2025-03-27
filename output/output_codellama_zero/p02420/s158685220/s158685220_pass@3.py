Here's a more efficient solution:

import sys

for line in sys.stdin:
    line = line.strip('\n')
    if line == '-':
        break
    
    letters = line[int(line):] + line[:int(line)]
    
    m = int(line) - 1
    
    print(letters)