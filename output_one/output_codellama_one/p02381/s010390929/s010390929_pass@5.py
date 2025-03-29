Here is a refactored version of the code:

import math

while True:
    n = int(input())
    if n == 0:
        break
    
    b = list(map(int, input().split()))
    ave = sum(b) / n
    A.extend((ave - b[i]) ** 2 for i in range(n))
    p = math.sqrt(sum(A) / n)
    print("{:.8f}".format(p))
    A.clear()