n = int(input())
var = input().split()
print(*reversed([var[i] for i in range(len(var)-1, -1, -1)]))