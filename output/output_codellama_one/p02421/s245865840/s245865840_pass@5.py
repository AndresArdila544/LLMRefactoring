n = int(input())
taro = 0
hana = 0
for i in range(n) :
    taro_c, hana_c = input().split()
    if int(taro_c) > int(hana_c) :
        taro +=3
    elif int(taro_c) == int(hana_c) :
        taro+=1
        hana+=1
    else:
        hana+=3
print(taro, hana)