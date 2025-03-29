n = int(input())
taro_c, hana_c = map(int, input().split() * n)
taro, hana = 0, 0
for i in range(n):
    if taro_c[i] > hana_c[i]:
        taro += 3
    elif taro_c[i] == hana_c[i]:
        taro += 1
        hana += 1
    else:
        hana += 3
print(taro, hana)