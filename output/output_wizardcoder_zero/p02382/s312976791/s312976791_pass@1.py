dim = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

diffs = [abs(x - y) for x, y in zip(a, b)] 
print(sum(diffs))
print((sum([(x - y)**2 for x, y in zip(a, b)]) ** 0.5) if len(a) == len(b) else None)
print(sum([abs(x - y)**3 for x, y in zip(a, b)]) ** (1/3))
print(max(diffs) if len(a) == len(b) else None