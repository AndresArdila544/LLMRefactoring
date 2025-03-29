class Dice:
    def __init__(self, default = [1, 2, 3, 4, 5, 6]):
        self._d = default
    
    def __str__(self):
        return str(self._d)
    
    def __repr__(self):
        return f"Dice({self._d})"
    
    def e(self):
        self._d[0], self._d[2], self._d[3], self._d[5] = self._d[3], self._d[0], self._d[5], self._d[2]
    
    def w(self):
        self._d[0], self._d[2], self._d[3], self._d[5] = self._d[2], self._d[5], self._d[0], self._d[3]
    
    def n(self):
        self._d[0], self._d[1], self._d[4], self._d[5] = self._d[1], self._d[5], self._d[0], self._d[4]
    
    def s(self):
        self._d[0], self._d[1], self._d[4], self._d[5] = self._d[4], self._d[0], self._d[5], self._d[1]
        
    def top(self):
        return self._d[0]

def main():
    dice = Dice([int(i) for i in input().split()])
    operations = {'E': 'e', 'W': 'w', 'S': 's', 'N': 'n'}
    
    for o in input():
        if o in operations:
            getattr(dice, operations[o])()
    
    print(dice.top())