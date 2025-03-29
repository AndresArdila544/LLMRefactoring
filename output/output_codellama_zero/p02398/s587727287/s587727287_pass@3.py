Here is the refactored Python program:
a, b, c = list(map(int, input().split()))
stack = sum(c % (a + i) == 0 for i in range(b - a + 1))
print(stack)