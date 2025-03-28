import math

dim = int(input().strip())
vec_x = list(map(int, input().strip().split(" ")))
vec_y = list(map(int, input().strip().split(" ")))

# Calculate the absolute difference between each coordinate in vec_x and vec_y
abs_xy = [abs(a - b) for a, b in zip(vec_x, vec_y)]

# Calculate the distance 1, 2, and 3
dist_1 = sum(abs_xy)
dist_2 = math.sqrt(sum([i**2 for i in abs_xy]))
dist_3 = (sum([i**3 for i in abs_xy]) ** (1/3))

# Calculate the maximum absolute value of vec_x and vec_y
max_abs = max(map(abs, zip(vec_x, vec_y)))

print("{:.5f}\n{:.5f}\n{:.5f}\n{:.5f}".format(dist_1, dist_2, dist_3, max_abs))