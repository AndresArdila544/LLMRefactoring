n = int(input())
Taro = Hanako = 0
for i in range(n):
    T, H = map(str, input().split())
    if (T > H): Taro += 3
    elif (T == H): Taro += 1; Hanako += 1
    else: Hanako += 3