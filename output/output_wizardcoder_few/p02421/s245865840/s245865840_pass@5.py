n = int(input())
taro = hana = 0
for _ in range(n):
    taro_c, hana_c = map(int, input().split())
    if taro_c > hana_c:
        taro += 3
    elif taro_c == hana_c:
        taro += 1
        hana += 1
    else:
        hana += 3
print(taro, hana)