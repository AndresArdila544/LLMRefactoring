s = int(input())
print(*[f"{x:02d}" for x in (s//3600, s%3600//60, s%60)], sep=':')