def manhattan_distance(x1, y1, x2, y2):
    return sum(abs(int(a) - int(b)) for a, b in zip(x1, y1))

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt(sum((int(a) - int(b))**2 for a, b in zip(x1, y1)))

def max_absolute_difference(x1, y1, x2, y2):
    return max(abs(int(a) - int(b) for a, b in zip(x1, y1))

def manhattan_distance_3d(x1, y1, z1, x2, y2, z2):
    return sum(abs(int(a) - int(b) for a, b in zip(zip(x1, y1, z1)))

def euclidean_distance_3d(x1, y1, z1, x2, y2, z2):
    return math.sqrt(sum((int(a) - int(b))**2 for a, b in zip(zip(x1, y1, z1)))

def main():
    x = input().split()
    y = input().split()
    print(manhattan_distance(x, y))
    print(euclidean_distance(x, y))
    print(max_absolute_difference(x, y))
    x1, y1, z1 = map(float, input().split())
    x2, y2, z2 = map(float, input().split())
    print(manhattan_distance_3d(x1, y1, z1, x2, y2, z2))
    print(euclidean_distance_3d(x1, y1, z1, x2, y2, z2))

if __name__ == '__main__':
    main()