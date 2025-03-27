num = int(input())
xs = list(map(int, input().split()))
ys = list(map(int, input().split()))

mh = sum(abs(x-y) for x, y in zip(xs, ys))
ec = pow(sum(abs(x-y)**2 for x, y in zip(xs, ys)), 1/2)
p3 = pow(sum(abs(x-y)**3 for x, y in zip(xs, ys)), 1/3)
cv = max(abs(x-y) for x, y in zip(xs, ys))

print(round(mh, 8))
print(round(ec, 8))
print(round(p3, 8))
print(round(cv, 8))
