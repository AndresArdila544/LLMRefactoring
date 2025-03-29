n = int(input())
while True:
    x = input()
    if n == 0 and x == '0':
        break
    cnt = 0
    for a in range(1, n):
        if a >= x:
            break
        for b in range(a+1, n):
            ab = a + b
            if ab >= x:
                break
            for c in range(b+1, n):
                abc = ab + c
                if abc == x:
                    cnt += 1
                    break
                elif abc > x:
                    break
    print(cnt)
'''Refactored version of the code with fewer lines and improved readability:

n = int(input())
while n != '0':
    for a in range(1, n):
        if a >= input():
            for b in range(a+1, n):
                ab = a + b
                if ab >= input():
                    for c in range(b+1, n):
                        abc = ab + c
                        if abc == input():
                            print('1', end=' ')
                        elif abc > input():
                            break
            print()'''