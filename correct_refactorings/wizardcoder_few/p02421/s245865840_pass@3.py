n = int(input())
taro_count, hana_count = 0, 0
for _ in range(n):
    taro_c, hana_c = input().split()
    if taro_c > hana_c:
        taro_count += 3
    elif taro_c == hana_c:
        taro_count += 1
        hana_count += 1
    else:
        hana_count += 3
print(taro_count, hana_count)