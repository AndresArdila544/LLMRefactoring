n = int(input())
taro_points = hana_points = 0
for _ in range(n):
    taro_c, hana_c = map(int, input().split())
    if taro_c > hana_c:
        taro_points += 3
    elif taro_c == hana_c:
        taro_points += 1
        hana_points += 1
    else:
        hana_points += 3
print(taro_points, hana_points)

# Refactored version with fewer lines and improved readability.