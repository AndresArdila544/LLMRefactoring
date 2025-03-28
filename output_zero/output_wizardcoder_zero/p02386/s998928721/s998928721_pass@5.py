from itertools import combinations
class Dice(object):
    def __init__(self, nums):
        self.nums = nums
        self.ifaces = [(1,2,3), (2,3,1), (3,1,2), (1,4,2), (4,2,1), (2,1,4), (1,5,4), (5,4,1), (4,1,5), (1,3,5), (3,5,1), (5,1,3), (2,6,3), (6,3,2), (3,2,6), (2,4,6), (4,6,2), (6,2,4), (4,5,6), (5,6,4), (6,4,5), (3,6,5), (6,5,3)]
    def index(self, num):
        return self.nums.index(num)
    def face(self, iface):
        return [self.nums[i-1] for i in iface]
    def all_face(self):
        yield from (self.face(iface) for iface in self.ifaces)
    
n = int(input())
dices = []
for _ in range(n):
    dices.append(Dice([int(i) for i in input().split()]))
same_found = False
for c in combinations(dices, 2):
    if all(any(is_same(c[0], d) for d in dices[:i]) and any(is_same(c[1], d) for d in dices[i+1:]) for i in range(n-1)):
        same_found = True
        break
print('Yes' if not same_found else 'No')