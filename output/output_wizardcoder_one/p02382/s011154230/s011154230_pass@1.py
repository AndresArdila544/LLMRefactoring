refactored_code = """
import math

for i in range(3):
    N = int(input())
    A_lst = list(map(int, input().split()))
    B_lst = list(map(int, input().split())
    
    if i == 0:
        print("{:.6f}".format(math.dist(A_lst, B_lst, p=1))
    elif i == 1:
        print("{:.6f}".format(math.dist(A_lst, B_lst, p=2)
    else:
        chebyshev = max(abs(a - b) for a, b in zip(A_lst, B_lst))
        print("{:.6f}".format(chebyshev))
"""

print(refactored_code)