```python
while True:
    deck = input()
    if deck == '-':
        break
    m = int(input())
    h = [int(input()) for i in range(m)]
    deck = deck[h:] + deck[:h]
    print(deck)
```