Here is a refactored version of the original Python program:
```python
num = int(input())
dice_ = [[int(i) for i in input().split()] for _ in range(num)]

def cross(a, b):
    return((a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]))

dice = {(n,) + dice_[n][i]: dice_[n][i] for n in range(num) for i in range(6)}

varif = min([1*dice[min_] + 10*dice[one] + 100*dice[tw] + 1000*dice[th] + 10000*dice[fo] + 100000*dice[opposing] for min_, one, tw, th, fo in [[(0,0,1), (0,-1,0), (1,0,0), (-1,0,0), (0,1,0), (0,0,-1)]], opposing = tuple([-i for i in min_])
    sides = list(set(dice.keys()) - set([opposing, min_]))
    if len(list(set(varif))) == num:
        print("Yes")
    else:
        print('No')
```