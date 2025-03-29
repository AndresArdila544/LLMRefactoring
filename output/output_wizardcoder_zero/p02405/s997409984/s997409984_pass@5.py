def f(a, b):
    k = b // 2
    print("#." * (k if a % 2 == 0 else -1) + "#" * max(-k, min(b - 2, 0)) if a > 0 else None
    
while True:
    try:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        f(a, b)
    except ValueError:
        break
        
print()