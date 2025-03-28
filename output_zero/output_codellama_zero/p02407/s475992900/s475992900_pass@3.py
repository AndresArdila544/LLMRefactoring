Here's the refactored version:

numlist = list(map(int, input().split()))
print(*reversed(numlist), sep=' ')