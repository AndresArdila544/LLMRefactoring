import sys
n, m = map(int, sys.stdin.readline().split())
for j in range(1, n + 1):
    for i in range(1, m + 1):
        print("#", end="")
    print()
print()