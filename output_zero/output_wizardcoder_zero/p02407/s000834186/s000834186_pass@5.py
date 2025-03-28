n = int(input())
print(*reversed(map(str, input().strip().split()[::-1]), sep=' ')