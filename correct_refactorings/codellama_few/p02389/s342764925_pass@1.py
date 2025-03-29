import sys
a, b = sys.stdin.readline().split()
if 1 <= int(a) and int(b) <= 100:
    print(int(a)*int(b), 2*(int(a)+int(b)))