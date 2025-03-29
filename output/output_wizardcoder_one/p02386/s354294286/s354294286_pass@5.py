class Dice:
    def __init__(self, t, f, r, l, b, u):
        self.a = [t, f, r, l, b, u]
        self.direction = {'S': (4, 0, 2, 3, 5, 1), 'N': (1, 5, 2, 3, 0, 4), 'E': (3, 1, 0, 5, 4, 2), 'W': (2, 1, 5, 0, 4, 3), 'Y': (0, 3, 1, 4, 2, 5)}
    
    def roll(self, d, n):
        self.a[n] = [self.a[i] for i in self.direction[d]]
        
def main():
    n=int(input())
    dice = Dice(*map(int, input().split()))
    
    for i in range(1, n):
        a = list(map(int, input().split()))
        if not any(a == dice.a[:4]):
            ans='No'
            continue
        
        dice_copy = Dice(*dice.a) # create a copy of the current dice state for each iteration
        for d in 'SSSWEE':
            for r in 'YYY':
                if dice_copy.a == dice_copy.roll(r, i):
                    ans='No'
                    break
            else:
                continue
            break
        else:
            continue
        break
    else:
        ans='Yes'
        
    print(ans)