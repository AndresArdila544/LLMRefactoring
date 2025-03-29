def scores(card1, card2):
    return (3,0) if card1 > card2 else (0, 3)

for i in range(int(input())):
    taro, hanako = 0, 0
    p1, p2 = input().split()
    taro += scores(*p1.split())[0]
    hanako += scores(*p2.split())[1]
print(taro, hanako)

# The refactored version of the code is given above. 
# It's a simple one-liner that checks for the score and increments it accordingly.