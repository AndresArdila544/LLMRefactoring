Here is a refactored version of the original code:

import sys
for line in sys.stdin:
 if '0 0' in line: break
 sorted_ints = sorted(map(int, line.split()))
 print(*sorted_ints)