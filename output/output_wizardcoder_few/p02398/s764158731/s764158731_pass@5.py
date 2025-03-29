Refactored Version:

n = int(input())
count = sum(i % 3 == 0 or '3' in str(i) for i in range(1, n+1))
print(count)