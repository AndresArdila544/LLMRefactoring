count = 1

while True:
    try:
        x = int(input())
    except ValueError:
        break
    if x != 0:
        print('Case {0}: {1}'.format(count, x))