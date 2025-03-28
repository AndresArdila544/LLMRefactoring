def roll(dice, d):
    return [dice[i] for i in dice.direction[d]]

class Dice:
    def __init__(self, t, f, l, r, b, u):
        self.a = [t, f, l, r, b, u]
        self.direction = {'S': (4, 0, 2, 3, 5), 'N': (1, 5, 2, 3, 0), 'E': (3, 1, 0, 5, 4), 'W': (2, 1, 5, 0, 4), 'Y': (0, 3, 1, 4, 2)}

    def move(self, d, n):
        self.a[n] = roll(self.a, d)
        
def main():
    n = int(input())
    dice = Dice(*map(int, input().split()))
    for _ in range(n-1):
        a = list(map(int, input().split()))
        dice.move('Y', 0)
        s='SSSWEE'
        w='YYYY'
        ans = 'Yes'
        for u in range(1, n):
            if dice.a == a:
                ans = 'No'
                break
            else:
                for r in w:
                    if dice.move(r, 0) == a or dice.move('Y', 0) == a[::-1]:
                        ans = 'Yes'
                        break
                    elif dice.move(s[u % 4], u):
                        ans = 'No'
                        break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        if ans == 'Yes':
            print('Yes')
            return
    print('No')