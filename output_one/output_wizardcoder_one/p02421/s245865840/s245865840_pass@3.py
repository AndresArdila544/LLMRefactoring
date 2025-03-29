refactored_code = """
n = int(input())
taro = hana = 0
for _ in range(n):
    taro_c, hana_c = map(int, input().split())
    if taro_c > hana_c:
        taro += 3
    elif taro_c == hana_c:
        taro += 1; hana += 1
    else: # taro_c < hana_c
        hana += 3
print(taro, hana)
"""

The code is already clean and concise. It can be reduced further to a single line using a list comprehension and the sum() function instead of a loop:

n = int(input())
taro_hana = [int(input().split()) for _ in range(n)]
print(sum((3 if t > h else 0, 1 if t == h else 3) for t, h in taro_hana))