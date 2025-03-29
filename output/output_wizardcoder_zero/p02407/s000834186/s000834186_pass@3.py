n = int(input())
a = list(map(int, input().strip().split()))
print(*reversed(a))