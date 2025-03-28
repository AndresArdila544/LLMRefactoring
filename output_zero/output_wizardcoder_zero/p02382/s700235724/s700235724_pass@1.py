import math
n = int(input().strip())
x_coords = list(map(int, input().strip().split()))
y_coords = list(map(int, input().strip().split()))

dist_1 = sum(abs(a-b) for a, b in zip(x_coords, y_coords))

dist_2 = math.sqrt(sum(abs(a-b) ** 2 for a, b in zip(x_coords, y_coords))

dist_3 = sum(abs(a-b) ** 3 for a, b in zip(x_coords, y_coords)) ** (1/3)

dist_infinite = max(max(zip(x_coords, y_coords), key=lambda x: abs(x[0] - x[1]))
print("{:.5f}\n{:.5f}\n{:.5f}\n{:.5f}".format(dist_1, dist_2, dist_3, dist_infinite))