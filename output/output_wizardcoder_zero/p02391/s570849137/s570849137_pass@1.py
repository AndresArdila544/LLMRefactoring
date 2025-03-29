x = list(map(int, input().split()))
print("a < b" if x[0] < x[1] else "a == b" if x[0] == x[1] else "a > b")