def calculate_stddev(n):
    l = list(map(int, input().split()))
    m = sum(l) / n
    return f'{(sum((s-m)**2 for s in l) / n) ** 0.5:.5f}' if n != 0 else None 

print(calculate_stddev(int(input()))