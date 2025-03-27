Here is a refactored version of the code:

for c in input():
    if c.isalpha():
        print(c.swapcase(), end='')
    else:
        print(c, end='')