n = int(input())
for i in range(n):
    card_t, card_h = map(int, input().split())
    point_t += 3 * (card_t > card_h)
    point_h += 3 * (card_t < card_h)
    point_t += 1 * (card_t == card_h)
    point_h += 1 * (card_t == card_h)
print(point_t, point_h)