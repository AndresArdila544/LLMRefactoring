n = int(input())
l = list(map(int, input().split()))
m = sum(l) / n
print(f'{(sum((s-m)**2 for s in l) / n) ** 0.5:.5f}')