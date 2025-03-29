n = int(input())
point_t = 0
point_h = 0
for i in range(n):
    card_t, card_h = input().split()
    if float(card_t) > float(card_h):
        point_t += 3.0
    elif float(card_t) < float(card_h):
        point_h += 3.0
    else:
        point_t += 1.0
        point_h += 1.0
print(point_t, point_h)