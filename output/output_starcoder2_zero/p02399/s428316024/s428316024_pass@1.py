Here is my attempt at a refactoring:

a,b = map(int, input().split())
print("{} {} {}".format(a//b, a%b, float(a/b)) )