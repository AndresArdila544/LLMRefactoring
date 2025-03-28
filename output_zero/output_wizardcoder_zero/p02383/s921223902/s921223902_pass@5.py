```python
class Dice:
    def __init__(self): #クラス内で用いる変数の定義（クラス作成時に代入しなくてよい）
        self.number = [i for i in range(6)]
        self.work = [i for i in range(6)
    
    def setNumber(self, n0, n1, n2, n3, n4, n5): #サイコロの目の数を設定
        self.number[0] = n0
        self.number[1] = n1
        self.number[2] = n2
        self.number[3] = n3
        self.number[4] = n4
        self.number[5] = n5
    
    def roll(self, loc): #初期位置，サイコロを転がせ，それぞれのいちを追跡
        for i in range(6):
            self.work[i] = self.number[i]
        if loc == 'E':
            self.setNumber(self.work[3],self.work[1],self.work[0],self.work[5],self.work[4])
        elif loc == 'N':
            self.setNumber(self.work[1],self.work[5],self.work[2],self.work[3],self.work[0])
        elif loc == 'S':
            self.setNumber(self.work[4],self.work[0],self.work[2],self.work[3],self.work[5])
        else:
            self.setNumber(self.work[2],self.work[1],self.work[5],self.work[0],self.work[4])
    
    def get_Top(self): #最上位のいちを返す
        return self.number[0]
    
table = list(map(int, input().split()))
loc_array = str(input())
dice = Dice()
dice.setNumber(*table) #init
for tmp_loc in loc_array:
    dice.roll(tmp_loc)
print(dice.get_Top())
```