```python
class Dice:
    def __init__(self, labels):
        self.__pip = list(labels)

    def roll_e(self): # 0352 → 3520
        self.__pip[1], self.__pip[4], self.__pip[2] = \
            self.__pip[4], self.__pip[2], self.__pip[1]
    
    def roll_n(self): # 0154 →  1540
        self.__pip[1], self.__pip[3], self.__pip[4] = \
            self.__pip[3], self.__pip[4], self.__pip[1]
    
    def roll_s(self): # 0451 →  4510
        self.__pip[1], self.__pip[4], self.__pip[2] = \
            self.__pip[4], self.__pip[2], self.__pip[1]
    
    def roll_w(self): # 0253 → 2530
        self.__pip[1], self.__pip[5], self.__pip[2] = \
            self.__pip[2], self.__pip[5], self.__pip[1]
    
    def roll_nn(self): # 0154 → 5401
        self.roll_n()
        self.roll_n()
        
    def turn_dice(self): # 1243 → 2431
        self.__pip[1], self.__pip[2], self.__pip[4], self.__pip[3] = \
            self.__pip[2], self.__pip[4], self.__pip[3], self.__pip[1]
    
    def get_top(self):
        return self.__pip[0]
    
    def get_front(self):
        return self.__pip[1]
    
    def get_right(self):
        return self.__pip[2]
         
    def get_left(self):
        return self.__pip[3]
         
    def get_behind(self):
        return self.__pip[4]
         
    def get_bottom(self):
        return self.__pip[5]
    
    def judge(self, dice_2):
        top = dice_2.get_top()
        if any(dice_2.get_front() != i for i in [self.__pip[1], self.__pip[4]]):
            return False
        if any(dice_2.get_right() != i for i in [self.__pip[2], self.__pip[3], self.__pip[4], self.__pip[5]]) or \
           any(dice_2.get_left() != i for i in [self.__pip[0], self.__pip[1], self.__pip[3], self.__pip[4]]):
            return False
        return True

def main():
    n = int(input())
    *labels, = [input().split() for i in range(n)]
    dice_list = list(set([''.join(d) for d in labels])
    for i in range(n-1):
        if set(dice_list[i]).isdisjoint(dice_list[i+1]):
            continue
        cnt = collections.Counter(''.join(dice_list[i]))
        dice = Dice([int(k) for k, v in sorted(cnt.items(), key=lambda x:x[1], reverse=True)[0]]
        for i in range(4):
            if any(dice.get_front() != int(labels[i][1]) or \
                  dice.judge(Dice([int(k) for k, v in sorted(cnt.items(), key=lambda x:x[1], reverse=True)[0]]):
                return 'No'
    print('Yes')
            
if __name__ == "__main__":
    main()
```