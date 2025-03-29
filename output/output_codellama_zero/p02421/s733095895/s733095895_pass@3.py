Here is the refactored version:
Taro = 0
Hanako = 0
n = int(input())
for i in range(n):
    T, H = map(str, input().split())
    if T > H:
        Taro += 3
    else:
        Hanako += 3
    if T == H:
        Taro += 1
        Hanako += 1
print(Taro, Hanako)