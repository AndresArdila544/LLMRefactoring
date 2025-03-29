cards = [list(map(int, input().split())) for _ in range(int(input()))]
p_taro, p_hanako = 0, 0
for card in cards:
    if card[0] > card[1]:   # 太郎が花子に勝った時
        p_taro += 3
    elif card[0] < card[1]:
        p_hanako += 3
    else:
        p_taro += 1
        p_hanako += 1
print(p_taro, p_hanako)