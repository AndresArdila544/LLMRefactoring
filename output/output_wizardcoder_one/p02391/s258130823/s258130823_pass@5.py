import math
s=input().rstrip().split(' ')
a,b = map(int, s)
if a > b:
    print("a > b")
elif a < b:
    print("a < b")
else:
    print("a == b")