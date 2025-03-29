n = int(input())
taro_count = 0
hana_count = 0
for i in range(n):
    a, b = map(str, input().split())
    if a == b:
        taro_count += 1
        hana_count += 1
    elif a < b:
        hana_count += 3
    else:
        taro_count += 3
print(taro_count, hana_count)