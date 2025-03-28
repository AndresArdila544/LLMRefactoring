Taro = 0
Hanako = 0
n = int(input())
for _ in range(n):
    T, H = map(int, input().split())
    if T > H:
        Taro += 3
    elif T == H:
        Taro += 1
        Hanako += 1
    else:
        Hanako += 3
print(Taro, Hanako)