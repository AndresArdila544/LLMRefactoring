Here is the refactoring of the original Python program to reduce its complexity:
a,b = [int(n) for n in input().split()]
print("a == b" if a==b else "a > b" if a>b else "a < b")