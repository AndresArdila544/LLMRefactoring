Here is a refactored version of your code:
n = int(input())
A = list(map(int, input().split()))
print(*[min(A), max(A), sum(A)])