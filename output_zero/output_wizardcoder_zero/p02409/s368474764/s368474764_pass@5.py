build = range(1, 5)
floor = range(1, 4+1)
dic = {b: [0]*10 for b in build}
n = int(input())
for i in range(n):
    info = map(int, input().split())
    if info[2] <= 10 and info[2] >= 1:
        dic[info[0]][info[1]-1] += info[3]
        if dic[info[0][info[1]-1] > 9:
            print('error')
    elif info[2] <= 0 or info[2] >= 10:
        continue
for b in build:
    for f in floor:
        print(dic[b][f], end=' ')
    if b != 4:
        print("#"*20)
print() # add a final newline character to separate each output block.