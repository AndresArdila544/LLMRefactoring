a, b, c = map(int, input().split())
if a < b: s= a; g=b
else: s=b; g=a
if c < s: print(str(c) + ' ' + str(s) + ' ' + str(g))
elif g < c: print(str(s) + ' ' + str(g) + ' ' + str(c))
else: print(str(s) + ' ' + str(c) + ' ' + str(g))