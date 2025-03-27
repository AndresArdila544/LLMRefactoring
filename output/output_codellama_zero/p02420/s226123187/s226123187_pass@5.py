```
while True:
    e = input()
    if e == "-":
        break
    cards += e * int(input())
    h = int(input())
    cards = cards[h:h-len(cards)]
print(cards)
```