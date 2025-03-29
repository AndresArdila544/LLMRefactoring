i=int(input())
numlist = list(map(int, input().split()))
print(*reversed(numlist[1:]), sep=' ', end='\n')