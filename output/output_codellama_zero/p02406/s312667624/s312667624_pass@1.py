Here is the refactored version of the code with fewer lines and improved readability:

# Structured Programming
# if 入力: 30, output is " 3 6 9 12 13 15 18 21 23 24 27 30"

integer = int(input())
cout = []

for i in range(1, integer+1):
    x = i
    while x > 0:
        if x % 10 == 3 or x % 3 == 0:
            cout.append(i)
            x = 0
        else:
            x //= 10

for n in cout:
    print(' ' + str(n), end='')
print()