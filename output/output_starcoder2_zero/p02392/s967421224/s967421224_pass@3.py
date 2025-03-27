Here is a refactored version of the code: 

n = input().split()
a , b , c = map(int, n)
print('Yes' if (a < b and b < c) else 'No')