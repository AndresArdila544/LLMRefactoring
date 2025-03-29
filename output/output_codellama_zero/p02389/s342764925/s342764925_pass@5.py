This is the refactored version of the original program:

a, b = input().split()
if int(a) <= 100 and int(b) <= 100:
    print((int(a)*int(b), 2*(int(a)+int(b))))