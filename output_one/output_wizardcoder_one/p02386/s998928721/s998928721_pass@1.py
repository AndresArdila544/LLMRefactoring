```python
from itertools import combinations as combs
from math import hypot

class Dice(object):
    def __init__(self, nums):
        self.nums = list(set(nums))  # removes duplicates
        
    def index(self, num):
        return self.nums.index(num)
    
    def face(self, iface):
        return [sorted([self.nums[i-1] for i in iface])

class Roll:
    def __init__(self, nums):
        self.dice = Dice(list(set(map(int, input().split()))

    def same_as(self, other):
        for f1 in self.dice.all_face():
            if any(f2 == f1 for f2 in other.dice.all_face()):
                return True
        return False

n = int(input())
rolls = [Roll([int(i) for i in input().split()] for _ in range(n))
if all(r1.same_as(r2) or r2.same_as(r1) for r1, r2 in combs(rolls, 2)):
    print('Yes')
else:
    print('No')
```