```python
from itertools import product

while True:
    try:
        if input() in [f'{x} {y}' for x, y in product('SHCD', range(1, 14))]:
            print(*filter(lambda i: i not in (f'{x} {y}' for x, y in product('SHCD', range(1, 14))), input().split()), sep='\n')
        else:
            break
    except EOFError:
        print(*filter(lambda i: i not in (f'{x} {y}' for x, y in product('SHCD', range(1, 14)), input().split()), sep='\n')
```