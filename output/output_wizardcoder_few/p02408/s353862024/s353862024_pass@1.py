s = [False]*13
h = [False]*13
c = [False]*13
d = [False]*13

for _ in range(int(input())):
    m,a = input().split()
    if m == 'S': s[int(a)-1] = True
    elif m == 'H': h[int(a)-1] = True
    elif m == 'C': c[int(a)-1] = True
    else: d[int(a)-1] = True
    
print(*[f"{x} {i+1}" for i, x in enumerate([False, *s, False, *h, False, *c, False, *d]) if not x], sep="\n")