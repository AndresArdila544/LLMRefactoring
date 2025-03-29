point_t = 0
point_h = 0
n = int(input())
for i in range(n):
    card_t, card_h = input().split()
    point_t += max(3, card_t - card_h)
    point_h += min(3, card_t - card_h)
print(point_t, point_h)