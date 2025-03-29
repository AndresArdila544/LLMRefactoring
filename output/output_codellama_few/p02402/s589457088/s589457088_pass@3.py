n = int(input())
x = list(map(int, input().split()))
b,m,s = max(x),min(x),sum(x)
print(f"{m} {b} {s}")