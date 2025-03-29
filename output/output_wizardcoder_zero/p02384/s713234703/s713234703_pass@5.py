```python
class Dice:
    def __init__(self, lst):
        self.val = [lst[0], lst[1], lst[2], lst[3], lst[4], lst[5]]

    
    def rotate(self, dir):
        if dir == "N":
            self.val[:] = [self.val[1], self.val[0], self.val[5], self.val[4], self.val[2]]
        elif dir == "E":
            self.val[:] = [self.val[3], self.val[0], self.val[5], self.val[1], self.val[2]]
        elif dir == "S":
            self.val[:] = [self.val[4], self.val[0], self.val[1], self.val[5], self.val[3]]
        elif dir == "W":
            self.val[:] = [self.val[2], self.val[0], self.val[3], self.val[4], self.val[5]]
    
    def __str__(self):
        return ' '.join(map(str, self.val))
            
def int_to_dir(n):
    if n == 0:
        return "N"
    elif n == 1:
        return "E"
    elif n == 2:
        return "S"
    else:
        return "W"

def main():
    x = list(map(int, input().split()))
    q = int(input())
    dice = Dice(x)
    
    for _ in range(q):
        a, b = map(int, input().split())
        while True:
            dice.rotate(random.choice("NESW"))
            if dice[0] == a and dice[1] == b:
                print(dice[2])
                break
    
if __name__ == "__main__":
    main()
```