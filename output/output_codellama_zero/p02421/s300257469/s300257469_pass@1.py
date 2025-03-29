n = int(input())
tp, hp = 0, 0
for i in range(n):
    tw,hw = input().split()
    if tw == hw:
        tp += 1
        hp += 1
    elif tw > hw:
        tp += 3
    elif tw < hw:
        hp += 3
print('%s %s' % (tp,hp))