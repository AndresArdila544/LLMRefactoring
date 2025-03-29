```python
class Dice:
    def __init__(self):
        self.directions = {'S': (4, 0, 2, 3, 5, 1), 'N': (1, 5, 2, 3, 0, 4), 'E': (3, 1, 0, 5, 4, 2), 'W': (2, 1, 5, 0, 4, 3), 'Y': (0, 3, 1, 4, 2, 5)}
    
    def roll(self, direction: str, n: int):
        self.a[n] = [self.a[n][i] for i in self.directions[direction]]

def main():
    n = int(input())
    dice = Dice()
    dice.a = [[int(x) for x in input().split()] for _ in range(n)]  # Initialize the list of dice positions.
    
    for i in range(1, n):
        for d, w in zip(['SSSWEEE', 'YYYY'], [['N', 'S']]:  # Iterate through directions and walls.
            for _ in range(n - 1):  # Check each possible path between positions.
                roll = False
                for r in w:  # Try rolling a direction to move from position i to the next one, if it's not blocked by any wall.
                    dice.roll(r, i)
                    if dice.a[i] == dice.a[i - 1]:
                        roll = True
                        break
                else:
                    continue
                if not roll:  # If we can't move from position i to the next one, it means there's a wall.
                    print('No')
                    return
            else:
                continue
            break
        else:
            continue
        break
    
    print('Yes')  # If we can move from all positions to the next one without rolling on any wall, it means there's no obstacle.

main()
```