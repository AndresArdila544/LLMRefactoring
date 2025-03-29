n = int(input())
tp = 0
hp = 0
for i in range(n):
    tw, hw = input().split()
    if tw == hw:
        tp += 1
        hp += 1
    elif tw > hw:
        tp += 3
    else:
        hp += 3
print('%d %d' % (tp, hp))