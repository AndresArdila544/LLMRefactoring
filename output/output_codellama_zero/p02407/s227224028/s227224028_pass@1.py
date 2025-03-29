n = int(input())
var = input().split()
for i in range(len(var)-1, -1, -1):
    if i == 0:
        print(var[i])
        break