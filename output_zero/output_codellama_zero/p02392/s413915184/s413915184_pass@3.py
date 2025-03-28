Here is a refactored version of the code:
a, b, c = (int(i) for i in input().split())
print('Yes' if a < b < c else 'No')