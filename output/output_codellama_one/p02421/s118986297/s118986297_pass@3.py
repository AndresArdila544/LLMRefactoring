point_t = 0
point_h = 0
n = int(input())
for i in range(n):
    card_t, card_h = input().split()
    if (card_t > card_h) or (card_t == card_h and point_t < 3):
        point_t += 3
    elif card_t < card_h:
        point_h += 3
print(point_t, point_h)