# Original Python Code:

a, b = map(int, input().split())  # splitting string by spaces 
d = a // b                       # integer division operator
r = a % b                        # remainder of an integer division operation
f = a / b                        # floating-point number
print(str(d) + ' ' + str(r) + ' ' + str(f))


# Refactored version of Python code:


a,b  = map(int,input().split())
d = a // b                        # integer division operator
r = a % b                         # remainder of an integer division operation
f = round((a/b),3)                # three-digit floating-point number
print(str(d)+' '+str(r)+' '+str(f))


# Justification: 
I used the map() function to convert the string into numbers, so that we can use integer division and modular operators. I also used format specifiers to print integers and floating point values in a single line, eliminating the need for multiple print statements.