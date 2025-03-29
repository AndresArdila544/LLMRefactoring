def dist(A_lst, B_lst, p):
    return math.hypot(*map(lambda a, b: abs(a - b) ** p, zip(A_lst, B_lst))) ** (1 / p)
 
N = int(input())
*A, = map(int, input().split())
*B, = map(int, input().split())
print("{:.6f}".format(dist(A, B, 1)))
print("{:.6f}".format(dist(A, B, 2)))
print("{:.6f}".format(dist(A, B, 3)))
chebyshev = max(abs(a - b) for a, b in zip(A, B))
print("{:.6f}".format(chebyshev))