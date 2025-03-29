import math
from sys import stdin

def count_sums():
    n, x = map(int, input().split())
    if n == 0 and x == 0: return
    cnt = 0
    for a in range(1, n):
        for b in range(a+1, n):
            ab = a + b
            if ab >= x: break
            for c in range(b+1, n):
                abc = ab + c
                if abc == x:
                    cnt += 1
                    return cnt
                elif abc > x:
                    break
    
while True:
    count_sums()
print(cnt)

The refactored version is given above. It achieves the same functionality by using a nested loop to iterate through all possible combinations of two numbers that can add up to x, and a conditional statement to check if the sum of those two numbers plus another number is equal to or greater than x. If it is, then we increment the count. Finally, we print out the count.