class Dice:
    def __init__(self):
        self.eyeIndex = 1 #center
        self.eyeIndex_E = 3 #east
        self.eyeIndex_W = 4 #west
        self.eyeIndex_N = 5 #north
        self.eyeIndex_S = 2 #south
        
    def shakeDice(self, direction):
        pre_eyeIndex = self.eyeIndex
        if direction == "E":
            self.eyeIndex = self.eyeIndex_W
            self.eyeIndex_E = pre_eyeIndex 
            self.eyeIndex_W = 7 - self.eyeIndex_E
        elif direction == "W":
            self.eyeIndex = self.eyeIndex_E
            self.eyeIndex_W = pre_eyeIndex
            self.eyeIndex_E = 7 - self.eyeIndex_W
        elif direction == "N":
            self.eyeIndex = self.eyeIndex_S
            self.eyeIndex_N = pre_eyeIndex
            self.eyeIndex_S = 7 - self.eyeIndex_N
        elif direction == "S":
            self.eyeIndex = self.eyeIndex_N         
            self.eyeIndex_S = pre_eyeIndex
            self.eyeIndex_N = 7 - self.eyeIndex_S 
        
    def rotateDice(self):
        #rotate clockwise
        pre_E = self.eyeIndex_E
        pre_S = self.eyeIndex_S
        pre_W = self.eyeIndex_W
        pre_N = self.eyeIndex_N
        
        self.eyeIndex_E = pre_N
        self.eyeIndex_S = pre_E
        self.eyeIndex_W = pre_S
        self.eyeIndex_N = pre_W
    
    def setEyes(self, eyes):
        self.eyes = list(map(int, eyes.split(" ")))
        
dice1 = Dice()
dice2 = Dice()

shake_direction = input().rstrip()
judge = "def"
shake_cnt = 0
while True:
    if dice2.eyes[0] == dice1.eyes[0] and dice2.eyes[7-dice1.eyeIndex] == dice1.eyes[dice1.eyeIndex]:
        break
    
    dice2.shakeDice(shake_direction)
    shake_cnt += 1
    if shake_cnt >= 8:
        judge = "No"
        break
        
    if shake_cnt >= 4:
        shake_direction = "N"
    
rotate_cnt = 0
if judge != "No":
    while True:
        if dice1.eyes[0] == dice2.eyes[0] and dice1.eyes[dice1.eyeIndex_E] == dice2.eyes[dice1.eyeIndex_E] and \
            dice1.eyes[dice1.eyeIndex_S] == dice2.eyes[dice1.eyeIndex_S] and dice1.eyes[dice1.eyeIndex_W] == dice2.eyes[dice1.eyeIndex_W] and \
            dice1.eyes[7-dice1.eyeIndex] == dice2.eyes[7-dice2.eyeIndex]:
            break
        
        dice2.rotateDice()
        rotate_cnt += 1
        
        if rotate_cnt >= 5:
            judge = "No"
            break
            
    if shake_direction == "E":
        dice1.shakeDice("E")
        dice1.shakeDice("E")
        dice2.shakeDice(shake_direction)
        dice2.shakeDice(shake_direction)
    else:
        dice1.shakeDice(shake_direction)
        dice1.shakeDice(shake_direction)
        dice2.shakeDice("E")
        dice2.shakeDice("E")
        
    if dice1.eyes[0] == dice2.eyes[0]:
        judge = "Yes"
    else:
        judge = "No"

print(judge)