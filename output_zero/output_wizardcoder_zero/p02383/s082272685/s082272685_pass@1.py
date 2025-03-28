```python
import sys
class Dice:
    def __init__(self, u, d, w, e, n):
        self.nums = {"u":u,"d":d,"w":w,"e":e,"n":n}
    
    def roll(self,direction):
        if direction == "S":
            self.nums = {"u":self.nums["u"],"n":self.nums["n"],"w":self.nums["d"],"e":self.nums["e"],"d":self.nums["w"]}
        elif direction == "W":
            self.nums = {"s":self.nums["s"],"n":self.nums["n"],"w":self.nums["u"],"e":self.nums["d"]}
        elif direction == "N":
            self.nums = {"w":self.nums["w"],"e":self.nums["e"],"u":self.nums["n"],"d":self.nums["d"]}
        else:
            self.nums = {"w":self.nums["w"],"e":self.nums["e"],"s":self.nums["s"],"d":self.nums["u"]}
    
def main():
    a = list(map(int,input().split()))
    s = input()
    dice = Dice(*a)
    for c in s:
        if c == "S":
            dice.roll("S")
        elif c == "W":
            dice.roll("W")
        elif c == "N":
            dice.roll("N")
        else:
            dice.roll("E")
    print(dice.nums["u"])

if __name__ == "__main__":
    main()
```