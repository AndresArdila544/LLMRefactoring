"""

n = int(input())
taro = 0
hana = 0
for i in range(n):
    a, b = map(str, input().split())
    if a == b:
        taro += 1
        hana += 1
    elif a < b:
        hana += 3
    else:
        taro += 3
print(taro, hana)