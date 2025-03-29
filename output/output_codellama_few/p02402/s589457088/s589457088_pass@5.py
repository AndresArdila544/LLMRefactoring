n = int(input())
x = list(map(int, input().split()))
b = max(x)
m = min(x)
s = sum(x)
print(f"{m} {b} {s}")

Refactored version: 

n = int(input())
s = sum(map(int, input().split()))
b = max(x)
m = min(x)
print(f"{m} {b} {s}")