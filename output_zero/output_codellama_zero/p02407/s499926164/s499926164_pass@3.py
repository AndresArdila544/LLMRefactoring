Here is a refactored version of your program:

n = raw_input().split()
x = map(int, raw_input().split())
print(" ".join([str(i) for i in reversed(x)]))