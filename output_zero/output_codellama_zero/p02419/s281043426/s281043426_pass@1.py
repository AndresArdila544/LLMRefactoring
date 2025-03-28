Here is the refactored Python program:

import sys

W = input()

T = (sys.stdin.read()).split()
count = 0
for s in T:
    if s == "END_OF_TEXT":
        break
    
    target = s.lower()

    #print("count:%d,  target, W: %s, %s" % (count, target, W))
    if target == W:
        count += 1

print(count)