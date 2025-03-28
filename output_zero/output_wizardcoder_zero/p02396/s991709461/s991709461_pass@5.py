i = 0
while True:
    num = int(input())
    if num == 0:
        break
    print('Case {}: {}'.format(str(i+1).rjust(2, ' '), str(num))