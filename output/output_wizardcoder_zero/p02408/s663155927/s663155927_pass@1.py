```python
cards = []
for p in ['S', 'H', 'C', 'D']:
    for i in range(1, 13+1):
        cards.append(p + str(i))

n = int(input())
for _ in range(n):
    cards.remove(input())
for card in cards:
    print(card)
```