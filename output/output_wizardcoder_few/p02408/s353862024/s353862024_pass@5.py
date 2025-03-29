n = int(input())
print("S ", end="")
for i in range(13):
    print("%d "%i if not any([bool(s[i]) for s in [False]*n] else "", end="")

print("\nH ", end="")
for i in range(13):
    print("%d "%i if not any([bool(h[i]) for h in [False]*n] else "", end="")

print("\nC ", end="")
for i in range(13):
    print("%d "%i if not any([bool(c[i]) for c in [False]*n] else "", end="")

print("\nD ", end="")
for i in range(13):
    print("%d "%i if not any([bool(d[i]) for d in [False]*n] else "", end="")