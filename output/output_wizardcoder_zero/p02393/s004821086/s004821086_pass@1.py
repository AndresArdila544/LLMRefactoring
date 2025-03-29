a,b,c = map(int,input().split())
if a > b:
    a, b = b, a # swap values of a and b if a is greater than b
if b > c:
    b, c = c, b # swap values of b and c if b is greater than c
print(a,b,c)