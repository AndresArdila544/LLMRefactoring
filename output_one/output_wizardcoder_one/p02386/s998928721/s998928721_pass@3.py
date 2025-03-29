```python
import itertools
from functools import reduce

class Dice(object):
    def __init__(self, nums):
        self.nums = nums
        self.ifaces = [(1,2,3), (2,3,1), (3,1,2),
                      (1,4,2), (4,2,1), (2,1,4),
                      (1,5,4), (5,4,1), (4,1,5),
                      (1,3,5), (3,5,1), (5,1,3),
                      (2,6,3), (6,3,2), (3,2,6),
                      (2,4,6), (4,6,2), (6,2,4),
                      (4,5,6), (5,6,4), (6,4,5),
                      (3,6,5), (6,5,3), (5,3,6)]
    
    def index(self, num):
        return self.nums.index(num)
    
    def face(self, iface):
        return [self.nums[i-1] for i in iface]
    
    def all_face(self):
        for iface in self.ifaces:
            yield self.face(iface)

def is_same(d1, d2):
    return any(reduce(lambda a, b: a & set(d1.all_face()), d2.all_face()) == d2.all_face()

n = int(input())

for _ in range(n):
    if not is_same(Dice([int(i) for i in input().split()]):
        print('No')
        break
else:
    print('Yes')
```