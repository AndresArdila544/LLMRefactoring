import sys
input = sys.stdin.readline
a = map(int, input().split())
if a[0] < a[1]:
    print('a < b')
elif a[0] > a[1]:
    print('a > b')
else:
    print('a == b')