def manhattan_distance(x, y):
    return sum(abs(int(i) - int(j)) for i, j in zip(x, y))

def euclidian_distance(x, y):
    return math.sqrt(sum((int(i) - int(j)) ** 2 for i, j in zip(x, y)))

def max_abs_difference(x, y):
    return max(abs(int(i) - int(j)) for i, j in zip(x, y))

n = int(input())
x = input().split()
y = input().split()
print(manhattan_distance(x, y))
print(euclidian_distance(x, y))
print(max_abs_difference(x, y))