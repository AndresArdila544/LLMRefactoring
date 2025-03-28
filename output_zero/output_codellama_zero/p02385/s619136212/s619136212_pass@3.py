Here is a more concise and readable version of the original code:
```
class Dice:
    def __init__(self):
        self.eyes = [0, 1, 2, 3, 4, 5, 6]
        self.eyeIndex = 1
        self.eye_S = 2
        self.eye_E = 3
        self.eye_W = 4
        self.eye_N = 5
        self.eye_B = 6
    
    def shakeDice(self, in_command):
        if in_command == "E":
            self.eyeIndex = self.eyeIndex_W
            self.eyeIndex_E = 7 - self.eyeIndex_W
            self.eyeIndex_W = 7 - self.eyeIndex_N
        elif in_command == "W":
            self.eyeIndex = self.eyeIndex_E
            self.eyeIndex_W = 7 - self.eyeIndex_N
            self.eyeIndex_E = 7 - self.eyeIndex_S
        elif in_command == "N":
            self.eyeIndex = self.eyeIndex_S
            self.eyeIndex_N = 7 - self.eyeIndex_W
            self.eyeIndex_S = 7 - self.eyeIndex_E
        elif in_command == "S":
            self.eyeIndex = self.eyeIndex_N
            self.eyeIndex_S = 7 - self.eyeIndex_W
            self.eyeIndex_N = 7 - self.eyeIndex_E
        
    def rotateDice(self):
        pre_E = self.eyeIndex_E
        pre_S = self.eyeIndex_S
        pre_W = self.eyeIndex_W
        pre_N = self.eyeIndex_N
        self.eyeIndex_E = pre_S
        self.eyeIndex_S = pre_W
        self.eyeIndex_W = pre_N
        
dice_1 = Dice()
dice_2 = Dice()

shake_direction = "E"
judge = "def"

while dice_2.getEye() != dice_1.getEye() or dice_2.getEye_B() != dice_1.getEye_B():
    dice_2.shakeDice(shake_direction)
    
if shake_cnt >= 8:
    judge = "No"
else:
    while dice_1.getEye() != dice_2.getEye() or dice_1.getEye_E() != dice_2.getEye_E() or \
        dice_1.getEye_S() != dice_2.getEye_S() or dice_1.getEye_W() != dice_2.getEye_W() or \
        dice_1.getEye_N() != dice_2.getEye_N():
        
        dice_2.rotateDice()
    
if judge != "No":
    dice_1.shakeDice(shake_direction)
    dice_1.shakeDice(shake_direction)
    if dice_1.getEye() == dice_2.getEye():
        judge = "Yes"
    else:
        judge = "No"
    
print(judge)
```