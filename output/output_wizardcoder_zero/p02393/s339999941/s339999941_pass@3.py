a,b,c = map(int, input().split())

if a > b and c: print(c,b,a) if a > c else (b,c,a)
elif b > a and c: print(c,a,b) if b > c else (a,c,b)
else: (b,a,c) or (a,b,c)