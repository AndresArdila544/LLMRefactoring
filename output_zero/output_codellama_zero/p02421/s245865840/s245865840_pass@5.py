import sys

n = int(sys.stdin.readline())
taro, hana = 0, 0
for _ in range(n):
    taro_c, hana_c = input().split()
    taro += 3 if int(taro_c) > int(hana_c) else (1 if int(taro_c) == int(hana_c) else 0)
    hana += 3 if int(hana_c) > int(taro_c) else (1 if int(hana_c) == int(taro_c) else 0)
print(taro, hana)