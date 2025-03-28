```python
cards = []
patterns = ['S', 'H', 'C', 'D']
for p in patterns:
    for i in range(1, 13+1):
        cards.append(p + str(i))
        
while len(cards) > n:
    cards.remove(input())
for card in cards:
    print(card)
```