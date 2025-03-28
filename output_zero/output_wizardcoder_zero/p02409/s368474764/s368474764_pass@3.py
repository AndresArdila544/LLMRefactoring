build = range(1, 5)
floor = range(1, 4)
dic = {b: [0] * 10 for b in build}
n = int(input())
for i in range(n):
    info = map(int, input().split())
    if info[2] > 0 and info[2] <= 10:
        dic[info[0]][info[1]-1] += info[3]
        print('error' if dic[info[0]][info[1]-1] > 9 else ' '.join(map(str, dic[info[0])), end=' ')
print('\n#'*20)
for f in floor:
    print(*dic[f], sep=' ', end='\n')