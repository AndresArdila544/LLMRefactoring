n = list(map(int, input().split()))
print('Yes' if min(n) < max(n[:2]) else 'No')