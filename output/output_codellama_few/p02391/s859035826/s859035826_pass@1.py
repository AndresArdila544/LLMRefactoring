Here is the refactored version:

for a in map(int, input().split()):
    if a > 0:
        print('a > b')
    elif a < 0:
        print('a < b')
    else:
        print('a == b')