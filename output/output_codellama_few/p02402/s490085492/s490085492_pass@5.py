import sys

n = list(map(int, sys.stdin.readline().split(" ")))
print(f"{min(n)} {max(n)} {sum(n)}")