<|start_of_text|>
a, b, c = map(int, input().split())
d = len([i for i in range(a, b + 1) if (c % i) == 0])
print(d)