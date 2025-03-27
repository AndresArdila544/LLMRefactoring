Here is the refactoring version of the original code:
n = [int(i) for i in raw_input().split()]
print(" ".join([str(i) for i in reversed(n)]))