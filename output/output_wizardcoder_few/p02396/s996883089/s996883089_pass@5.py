count = int(1)
while True:
    x = int(input())
    if x != 0:
        print('Case {}: {}'.format(count, x))
        count += 1
    else:
        break