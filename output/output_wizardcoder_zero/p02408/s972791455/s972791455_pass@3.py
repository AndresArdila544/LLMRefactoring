n = int(input())
suits = ["S", "H", "C", "D"]
card = list(range(1, 14))
for i in range(n):
    suit, value = input().split()
    card.remove(int(value)) if suit == suits[0] else None # Check for suit and remove corresponding card from Spades
    card.remove(int(value)) if suit == suits[1] else None # Check for suit and remove corresponding card from Hearts
    card.remove(int(value)) if suit == suits[2] else None # Check for suit and remove corresponding card from Clubs
    card.remove(int(value) if suit == suits[3] else None) # Check for suit and remove corresponding card from Diamonds
for value in card:
    print("S", value)
for value in card:
    print("H", value)
for value in card:
    print("C", value)
for value in card:
    print("D", value)