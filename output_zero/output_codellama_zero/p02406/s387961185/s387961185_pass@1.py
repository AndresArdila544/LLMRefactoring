Here is the refactored version of your Python program:

a = int(input())
for x in range(1, a+1):
    if x % 3 == 0 or "3" in str(x):
        print(" {}".format(x), end="")