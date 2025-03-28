Here is the refactored version:

n = int(input())
taro, hana = 0, 0
for a, b in (str for str in input().split()):
    if a == b:
        taro += 1
        hana += 1
    elif a < b:
        hana += 3
    else:
        taro += 3
print(taro, hana)