refactored_code = '''
import math

while True:
    n, x = map(int, input().split())
    if not n+x:  # This condition checks for both n and x being equal to zero simultaneously
        break
    ans = 0
    for i in range(1,n):
        for j in range(i+1, n-i):   # We can start the second loop from i+1 instead of i+1, since we only need pairs of distinct numbers between 1 and n-i to calculate the number of combinations.
            if j<x-i:
                ans+=1
    print(ans)
'''