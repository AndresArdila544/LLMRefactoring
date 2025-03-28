def roll_dice(inputs):
    dice = [int(i) for i in inputs]
    class Dice:
        def __init__(self, a1, a2, a3, a4, a5, a6):
            self.face = [a1, a2, a3, a4, a5, a6]  # サイコロを縦横にたどると書いてある数字(index1は真上、index3は真下の数字)
            self.v = [a5, a1, a2, a6] # 縦方向
            self.h = [a4, a1, a3, a6] # 横方向
            self.det = 1
        def top(self):
            return self.v[1]
        def north(self):
            newV = [self.v[1], self.v[2], self.v[3], self.v[0]]
            self.v = newV
            self.h[1] = self.v[1]
            self.h[3] = self.v[3]
        def south(self):
            newV = [self.v[3], self.v[0], self.v[1], self.v[2]]
            self.v = newV
            self.h[1] = self.v[1]
            self.h[3] = self.v[3]
        def east(self):
            newH = [self.h[3], self.h[0], self.h[1], self.h[2]]
            self.h = newH
            self.v[1] = self.h[1]
            self.v[3] = self.h[3]
        def west(self):
            newH = [self.h[1], self.h[2], self.h[3], self.h[0]]
            self.h = newH
            self.v[1] = self.h[1]
            self.v[3] = self.h[3]
        def search_face(self, a):
            b = 0
            for i in range(6):
                if a == self.face[i]:
                    # print('一致しました')
                    b = i + 1
            return b
        def smallen(self, x): # a は 1 から 6 のどれか
            y = int(7 / 2 - abs(x - 7 / 2))
            if x != y:
                self.det *= -1
            return y
        def right_side(self, top, front):
            r = 0
            if top == 1 and front == 2:
                r = 3
            elif top == 2 and front == 3:
                r = 1
            elif top == 3 and front == 1:
                r = 2
            elif top == 1 and front == 3:
                r = 5
            elif top == 3 and front == 2:
                r = 6
            elif top == 2 and front == 1:
                r = 4
            if self.det == -1:
                r = 7 - r
            return r
    dice_obj = Dice(dice[0], dice[1], dice[2], dice[3], dice[4])
    
    for _ in range(int(input())):
        command = input().split()
        if command[0] == 'N':
            dice_obj.north()
        elif command[0] == 'S':
            dice_obj.south()
        elif command[0] == 'E':
            dice_obj.east()
        elif command[0] == 'W':
            dice_obj.west()
        print(dice_obj.top())
            
    return