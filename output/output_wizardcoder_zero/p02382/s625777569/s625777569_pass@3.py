def distance(x, y):
    return sum(abs(int(i) - int(j)) for i, j in zip(x, y))

n = int(input())
x = input().split()
y = input().split()
print(distance(x, y))
print(math.sqrt(distance(x, y)))
print(max(abs(int(i) - int(j) for i, j in zip(x, y)) ** 2)**0.5)
print(min(abs(int(i) - int(j) for i, j in zip(x, y)) ** 3)**(1/3))