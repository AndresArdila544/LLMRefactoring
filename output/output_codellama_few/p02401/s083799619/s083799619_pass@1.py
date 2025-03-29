import sys
while True:
    a = sys.stdin.readline()
    if '?' in a:break
    print(int(eval(''.join(a.split()))))