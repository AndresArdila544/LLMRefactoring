```python
from itertools import combinations_with_replacement

class Dice:
    def __init__(self, nums):
        self.faces = sorted(nums)
        
    def is_same(self, other):
        return 'Yes' if self.faces == other.faces else 'No'

d1 = Dice([int(x) for x in input().split()])
d2 = Dice([int(x) for x in input().split()])
print(Dice.is_same(d1, d2))
```