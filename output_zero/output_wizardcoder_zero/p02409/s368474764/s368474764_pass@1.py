build = range(1,5)

floor = range(1,4)
for i in range(int(input())):
    b, f, p, q, r = map(int, input().split())
    if 0<=p<10 and 0<=q<10 and 0<=r<=10:
        dic[b-1][f-1] = [0]*10
        for i in range(len(dic[b-1][f-1]):
            if r!=0:
                dic[b-1][f-1][i]+=r
            if dic[b-1][f-1][i]>9:
                print('error')
print('\n'.join([' '.join(str(x) for x in row) for row in build])