import sys
print(*map(str.title, map(int, sys.stdin)), sep='\n')