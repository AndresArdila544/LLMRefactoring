n = int(input())
table = sorted(map(int, input().split()))
print(*table[0::-1] + [sum(table)])