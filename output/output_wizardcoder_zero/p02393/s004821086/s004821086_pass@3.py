a,b,c = map(int, input().split())
if a > b:
    a, b = b, a if a>c else c, a if a<c else b # Swap values of a and c if necessary
print(*sorted([a,b,c]))