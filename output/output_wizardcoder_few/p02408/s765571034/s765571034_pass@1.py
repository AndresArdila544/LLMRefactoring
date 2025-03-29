```python
n = int(input())
suits = ['S', 'H', 'C', 'D']
for m in suits:
    for n in range(1, 13 + 1):
        if (m, n) not in [(card[0], card[1]) for card in [(input().split()) for _ in range(n)]]:
            print(m, n)
```