import sys
w = input().lower()
counter = sum(1 for i in sys.stdin.readline().split() if i.lower() == w)