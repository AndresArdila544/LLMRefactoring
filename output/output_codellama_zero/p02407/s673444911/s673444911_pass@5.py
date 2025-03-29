Here is the refactored version of the Python program:

n = int(input())
A = list(input().strip().split())
print(*A[::-1], sep=' ')