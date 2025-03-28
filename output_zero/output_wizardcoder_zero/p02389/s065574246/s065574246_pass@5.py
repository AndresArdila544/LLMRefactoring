x, y = map(int, input().split()) # refactored version
print("{} {}".format(x * y, 2 * x + 2 * y)) 

"""
The original program takes two integers as input separated by a space and prints their product followed by the sum of twice x plus twice y.

x, y = map(lambda x: int(x), input().split())
print("{} {}".format(x * y, 2 * x + 2 * y)) # can be simplified to:

print("{} {}".format(int(input().split()[0]) * int(input().split()[1], 2 * int(input().split()[0] + 2 * int(input().split()[1]))
""" 

# The first line splits the input by space and maps each element to integer, then assigns it to x and y respectively. 
# The second line prints the product of x and y in one variable and the sum of twice x plus twice y in another variable using string formatting.
# This version is more concise as it uses only one line of code instead of two and does not require a lambda function.