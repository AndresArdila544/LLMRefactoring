build = range(1, 5)
floor = range(1, 4)
dic = {b: {f: [0]*10 for f in floor} for b in build}
n = int(input())
for i in range(n):
    info = list(map(int, input().split()))
    dic[info[0]][info[1]][info[2] - 1] += info[3]
    if dic[info[0]][info[1]][info[2] - 1] > 9:
        print('error')
for b in build:
    for f in floor:
        print('{:>4}'.format(b), end=' ')
        print(' '.join(map(str, dic[b][f])).rjust(20))
    if b != 4:
        print('#' * 20)