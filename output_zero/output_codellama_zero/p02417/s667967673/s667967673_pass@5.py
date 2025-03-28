list = []
try:
    while True:
        list.append(input())
except EOFError:
    pass
for i in range(len(list)):
    list[i] = list[i].lower()
w = ''.join(list)
print(*['{}:{}'.format(c, w.count(c)) for c in 'abcdefghijklmnopqrstuvwxyz'], sep='\n')