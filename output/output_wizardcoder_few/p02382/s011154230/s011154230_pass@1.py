def dist(A_lst, B_lst, p):
    return sum([abs(a - b) ** p for a, b in zip(A_lst, B_lst)]).__pow__(1 / p)
    
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print("{:.6f}".format(dist(A, B, 1)))
print("{:.6f}".format(dist(A, B, 2))
print("{:.6f}".format(dist(A, B, 3)
chebyshev = max([abs(a - b) for a, b in zip(A, B)]
print("{:.6f}".format(chebyshev)

# Refactored version:
def dist(A_lst, B_lst):
    return sum((x-y)**2 for x, y in zip(A_lst, B_lst)) ** 0.5
    
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split())
print("{:.6f}".format(dist(A, B)
chebyshev = max([abs(a - b) for a, b in zip(A, B)]
print("{:.6f}".format(chebyshev)