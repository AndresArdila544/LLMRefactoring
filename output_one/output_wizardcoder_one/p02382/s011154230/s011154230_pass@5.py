import math
def dist(A_lst, B_lst):
    return [math.hypot(*(abs(a-b) for a, b in zip(A_lst, B_lst)), p=1), math.dist(*(abs(a-b) for a, b in zip(A_lst, B_lst), p=2), math.dist(*(abs(a-b) for a, b in zip(A_lst, B_lst), p=3)]

N = int(input())
*A, *B = map(int, input().split()), map(int, input().split())
print("{:.6f}".format(dist(A, B)))
chebyshev = max(abs(a - b) for a, b in zip(A, B))
print("{:.6f}".format(chebyshev))