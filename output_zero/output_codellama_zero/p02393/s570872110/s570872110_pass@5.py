Here is a refactored version of the program:

num_sorted = list(map(int, input().split()))
print("{} {} {}".format(*sorted(num_sorted)))