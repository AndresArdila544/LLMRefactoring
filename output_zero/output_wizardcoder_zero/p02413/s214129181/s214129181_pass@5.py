a, b = map(int, input().split())
bs = [[int(i) for i in input().split()] for _ in range(a)]
for row in bs:
    row.append(sum(row))
print(*[sum([row[j] for j in range(b+1)]) for row in bs], sep=' ')