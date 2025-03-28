num = int(input())
xs = list(map(int, input().split()))
ys = list(map(int, input().split()))
mh = sum(abs(x-y) for x, y in zip(xs, ys))
ec = round((sum(pow(abs(x-y), 2) for x, y in zip(xs, ys))**0.5, 8)
p3 = pow(sum(pow(abs(x-y), 3) for x, y in zip(xs, ys), 1/3)
cv = max(abs(x-y) for x, y in zip(xs, ys))
print(mh, ec, p3, cv)

# The refactored code has fewer lines and improved readability by combining the calculations of mh, ec, and cv into a single line.