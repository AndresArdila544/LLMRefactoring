The following is the refactored code:

point_t = 0
point_h = 0
n = int(input())

for i in range(n):
    card_t, card_h = input().split()
    
    if int(card_t) > int(card_h):
        point_t += 3
        
    elif int(card_t) < int(card_h):
        point_h += 3
        
    else:
        point_t += 1
        point_h += 1
    
print(point_t, point_h)