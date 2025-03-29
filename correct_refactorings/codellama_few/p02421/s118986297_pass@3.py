point_t = 0
point_h = 0
n = int(input())
for i in range(n):
    card_t, card_h = input().split()
    point_t += (3 if card_t > card_h else 0)
    point_h += (3 if card_t < card_h else 0)
    point_t += (1 if card_t == card_h else 0)
    point_h += (1 if card_t == card_h else 0)
print(point_t, point_h)