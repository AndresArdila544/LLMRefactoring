def roll_dice(inputs):
    dice = [int(i) for i in inputs]
    
    class Dice:
        def __init__(self, a1, a2, a3, a4, a5, a6):
            self.face = [a1, a2, a3, a4, a5, a6]
        
        def top(self):
            return self.face[0]
        
        def north(self):
            newV = [self.face[1], self.face[2], self.face[3], self.face[0]]
            self.v, self.h = newV, newV
            
        def south(self):
            newV = [self.face[3], self.face[0], self.face[1], self.face[2] ]
            self.v, self.h = newV, newV
        
        def east(self):
            newH = [self.face[3], self.face[0], self.face[1], self.face[2]]
            self.v, self.h = self.h, newH
            
        def west(self):
            newH = [self.face[1], self.face[2], self.face[3], self.face[0] ]
            self.v, self.h = self.h, newH
        
        def searchFace(self, a):
            for i in range(6):
                if a == self.face[i]:
                    return i + 1
        
        def smallen(self, x): # a は 1 から 6 のどれか
            y = int(7 / 2 - abs(x - 7 / 2))
            if x != y:
                self.det *= -1
            return y
        
        def rightSide(self, top, front):
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
    
    dice1 = Dice(dice[0], dice[1], dice[2], dice[3], dice[4])
        
    questionAmount = int(input())
    for i in range(questionAmount):
        question = [int(j) for j in input().rstrip()]
        a, b = dice1.searchFace(question[0]), dice1.searchFace(question[1])
        top = dice1.smallen(a)
        front = dice1.smallen(b)
        
        if question[2] == 'N':
            dice1.north()
        elif question[2] == 'S':
            dice1.south()
        elif question[2] == 'E':
            dice1.east()
        else:
            dice1.west()
        
        position = dice1.rightSide(top, front)
        answer = dice1.face[position - 1]
        print(answer)