Here is the refactored version of the program:

import sys
count = 1
while True:
    x = int(input())
    if x != 0:
        print('Case {0}: {1}'.format(count, x))
        count += 1
    else:
        break