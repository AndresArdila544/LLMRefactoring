```python
import math

n = int(input())
point_t, point_h = 0, 0
for _ in range(n):
    card_t, card_h = map(int, input().split())
    if card_t > card_h:
        point_t += 3
    elif card_t < card_h:
        point_h += 3
    else:
        point_t += 1
        point_h += 1
print(point_t, point_h)
```