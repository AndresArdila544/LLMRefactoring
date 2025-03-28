n = int(input())
table = sorted([int(x) for x in input().split()])
print(*table, sum(table))