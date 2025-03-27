Here is a refactored version of the code:

a = int(input())
print("%d:%02d:%02d" % (a // 3600, (a % 3600) // 60, a % 60))

The refactoring reduces the lines of code to 1 and improves readability by using the string formatting operator "%" instead of multiple calls to "print()" with format strings.