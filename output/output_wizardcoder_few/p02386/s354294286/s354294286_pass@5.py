```python
class Dice:
    def __init__(self, t, f, r, l, b, u):
        self.a = [[t, f, r, l, b, u]]
        self.direction = {'S': (4, 0, 2, 3, 5, 1), 'N': (1, 5, 2, 3, 0, 4), 'E': (3, 1, 0, 5, 4, 2), 'W': (2, 1, 5, 0, 4, 3), 'Y': (0, 3, 1, 4, 2, 5)}
    def roll(self, d, n):
        self.a[n] = [self.a[n][i] for i in self.direction[d]]
        
def main():
    n = int(input())
    
    dice = Dice(*map(int, input().split()))
    s='SSSWEEE'
    w='YYYY'
    ans = 'Yes'
    
    for u in range(n-1):
        for t in range(u+1, n):
            for j in s:
                dice.roll(j,t)
                
                if dice.a == dice.a[u]:
                    ans = 'No'
                    break
            else:
                continue
            
        else:
            continue
        break
    
    print(ans)
        
if __name__ == "__main__":
    main() 
```