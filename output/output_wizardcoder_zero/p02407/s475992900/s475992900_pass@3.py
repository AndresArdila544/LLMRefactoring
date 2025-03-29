numlist = list(map(int, input().split()))
print(' '.join(str(numlist[i-1]) for i in range(len(numlist), 0, -1)) + ' ' + str(numlist[0]))