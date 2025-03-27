Here is the refactored version of the original Python program:

a, b, c = map(int, input().split())
count = sum(i for i in range(a, b+1) if c % i == 0)