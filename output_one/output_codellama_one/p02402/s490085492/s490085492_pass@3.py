import sys
n = sys.stdin.readlines()
nstr = list(map(int, n[1].split(" ")))
print(f'{min(nstr)} {max(nstr)} {sum(nstr)}')