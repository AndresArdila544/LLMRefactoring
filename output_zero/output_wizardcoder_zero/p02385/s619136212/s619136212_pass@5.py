class Dice:
    def __init__(self):
        self.eyeIndex = 1 #center
        self.eyes = [0] * 8
        
    def setEyes(self, eyes):
        self.eyes = list(map(int, eyes.split(" ")))
    
    def getEye(self, index=None):
        if not index:
            return self.eyeIndex
        else:
            return self.eyes[index]
        
dice_1 = Dice()
dice_2 = Dice()

shake_direction = "E"
judge = "def"

while True:
    dice_1.setEyes(input().rstrip())
    dice_2.setEyes(input().rstrip())
    
    shake_cnt = 0
    while True:
        if dice_2.getEye() == dice_1.getEye():
            break
        
        dice_2.shakeDice(shake_direction)
        shake_cnt += 1
        
        if shake_cnt >= 8:
            judge = "No"
            break
            
    rotate_cnt = 0
    
    while True:
        if dice_1.getEye() == dice_2.getEye():
            for i in range(4):
                dice_2.shakeDice("S")
                dice_2.shakeDice("N")
                
            break
            
        elif rotate_cnt >= 5:
            judge = "No"
            break
        
    if judge != "No":
        for i in range(4):
            dice_1.shakeDice(shake_direction)
            dice_2.shakeDice(shake_direction)
            
    if dice_1.getEye() == dice_2.getEye():
        judge = "Yes"
        
print(judge