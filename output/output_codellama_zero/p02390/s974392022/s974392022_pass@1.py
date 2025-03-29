import math
x = int(input())
print(*math.floor([*divmod(x,3600),]*2)[:-1])