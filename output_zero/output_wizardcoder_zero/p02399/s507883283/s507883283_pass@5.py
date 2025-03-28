a, b = map(int, input().split())
print(*map(lambda x: int(x) if i % 2 == 0 else round(float(x), 8) for i, x in enumerate((a // b, a % b, f'{a / b:.08f}')))