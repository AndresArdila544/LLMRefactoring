n = int(input())
x = list(map(int, input().split()))
print(*minmax(x), sum(x))