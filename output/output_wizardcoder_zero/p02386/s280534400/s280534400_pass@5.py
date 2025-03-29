```python
def roll(d):
    def swap(n1, n2, n3, n4):
        return [n1, n2, d, n3, n4, -1]
    
    switch = {
        'N': (0, 1, 5, 4),
        'S': (0, 4, 5, 1),
        'W': (3, 0, 2, 5),
        'E': (3, 5, 2, 0)
    }
    return swap(*switch.get(d))
    
def same_dice(buff, dices):
    for dice in dices:
        for d in buff:
            if roll(d) == dice.num:
                return True
    return False

N = int(input())
for _ in range(N):
    nums = list(map(int, input().split()))
    dices.append(Dice(nums))

if any(same_dice(buff, dices) for buff in map(''.join, itertools.product('NSWE', repeat=len(dices[0].num)):
    print("No")
else:
    print("Yes")
```