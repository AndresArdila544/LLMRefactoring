Here is a cleaned-up and shortened version of your original program:

dim = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(max([abs(x - y) for x, y in zip(a, b)]))
print(pow(sum([(x - y)**2 for x, y in zip(a, b)]), 1/2))
print(pow(sum([(abs(x - y))**3 for x, y in zip(a, b)]), 1/3))