Here is my refactored Python program:

count = 1
while True:
    x = int(input())
    if x != 0:
        print('Case {}: {}'.format(count, x))
        count += 1

    else:
        break