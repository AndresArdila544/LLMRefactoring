count = 0
while True:
    x = int(input())
    if x != 0:
        print('Case {}: {}'.format(count+1, x))
        count += 1
    else:
        break