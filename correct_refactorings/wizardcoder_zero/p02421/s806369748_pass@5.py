def scores(card1, card2):
    return (3,0) if card1>card2 else (0,3) if card1!=card2 else (1,1)

c = int(input())
taro, hanako = 0, 0
for i in range(c):
    t, h = scores(*input().split())
    taro += t
    hanako += h
print(taro,hanako)