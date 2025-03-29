import statistics as stat
num = int(input())
xs = list(map(int, input().split()))
ys = list(map(int, input().split()))
print(round(stat.mean(abs(x-y) for x, y in zip(xs, ys)), 8))
print(round(stat.median(abs(x-y) for x, y in zip(xs, ys)), 8))
print(round(stat.pvariance(abs(x-y) for x, y in zip(xs, ys)), 8))
print(round(max(abs(x-y) for x, y in zip(xs, ys)), 8))