n = int(input())
taro_score = hana_score = 0
for i in range(n):
    taro_c, hana_c = map(int, input().split())
    if taro_c > hana_c:
        taro_score += 3
    elif taro_c == hana_c:
        taro_score += 1
        hana_score += 1
    else:
        hana_score += 3
print(taro_score, hana_score)