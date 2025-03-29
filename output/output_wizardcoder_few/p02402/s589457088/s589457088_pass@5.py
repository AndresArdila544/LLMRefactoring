n = int(input())
x = list(map(int, input().split()))
b = max(x)
m = min(x)
s = sum(x)
print(f"{m} {b} {s}")

Refactored version:

n = int(input())
x_list = list(map(int, input().split()))
print(*(min(x_list), max(x_list), sum(x_list))