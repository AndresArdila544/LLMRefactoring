Here is a refactored version of the code:

import sys

p = 0
letters = ""
for line in sys.stdin:
    ls = line.strip('\n')
    if p == 0:
        if ls =='-': break
        letters = ls
        p = 1
    elif p == 1:
        m = int(ls)
        p =2
    elif p == 2:
        h = int(ls)
        print letters[h:] + letters[:h]
        if m > 1:
            m -= 1
            p = 2
        else:
            p = 0