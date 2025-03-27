n = int(input())
cards = [input().split() for i in range(n)]

p_taro = 0
p_hanako = 0

#Pythonでは辞書で後ろの方にある方が大きい扱い
# "a" < "b" = True

for i in range(n):
    if cards[i][0] > cards[i][1]:   #太郎が花子に勝った時
        p_taro += 3
    elif cards[i][0] < cards[i][1]:
        p_hanako += 3
    else:
        p_taro += 1
        p_hanako += 1
print(p_taro, p_hanako)

