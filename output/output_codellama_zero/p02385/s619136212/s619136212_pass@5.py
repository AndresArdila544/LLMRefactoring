class Dice:
    def __init__(self):
        self.eyeIndex = 1
        self.eyes = [0, 0, 0, 0, 0, 0, 0, 7 - self.eyeIndex]
        self.convEyesIndexToEyes()
    
    def convEyesIndexToEyes(self):
        self.eye = self.eyes[self.eyeIndex]
        self.eye_S = self.eyes[self.eyeIndex_S]
        self.eye_E = self.eyes[self.eyeIndex_E]
        self.eye_N = self.eyes[self.eyeIndex_N]
        self.eye_W = self.eyes[self.eyeIndex_W]
        self.eye_B = 7 - self.eyeIndex
    
    def shakeDice(self, in_command):
        pre_eyeIndex = self.eyeIndex
        if in_command == "E":
            self.eyeIndex = self.eyeIndex_W
            self.eyeIndex_E = pre_eyeIndex
            self.eyeIndex_W = 7 - self.eyeIndex_E
            
        elif in_command == "W":
            self.eyeIndex = self.eyeIndex_E
            self.eyeIndex_W = pre_eyeIndex
            self.eyeIndex_E = 7 - self.eyeIndex_W
            
        elif in_command == "N":
            self.eyeIndex = self.eyeIndex_S
            self.eyeIndex_N = pre_eyeIndex
            self.eyeIndex_S = 7 - self.eyeIndex_N

        elif in_command == "S":
            self.eyeIndex = self.eyeIndex_N
            self.eyeIndex_S = pre_eyeIndex
            self.eyeIndex_N = 7 - self.eyeIndex_S
        
        self.convEyesIndexToEyes()
    
    def rotateDice(self):
        self.eyes[0] = self.eyes[-1]
        self.eyes[1] = self.eyes[-2]
        self.eyes[2] = self.eyes[-3]
        self.eyes[3] = self.eyes[-4]
        self.eyes[4] = self.eyes[-5]
        self.eyes[5] = self.eyes[-6]
        self.eyes[6] = 7 - self.eyeIndex
        self.convEyesIndexToEyes()
    
    def setEyes(self, eyes):
        self.eyes = [int(i) for i in eyes]
        self.convEyesIndexToEyes()
        
dice_1 = Dice()
dice_1.setEyes(input().rstrip())

dice_2 = Dice()
dice_2.setEyes(input().rstrip())


shake_direction = "E"
judge = "def"

shake_cnt = 0

while True:
    if dice_2.getEye() == dice_1.getEye() and dice_2.getEye_B() == dice_1.getEye_B():
        break
    
    dice_2.shakeDice(shake_direction)
    shake_cnt = shake_cnt + 1
    
    if shake_cnt >= 8:
        judge = "No"
        break
    if shake_cnt >= 4:
        shake_direction = "N"
        
rotate_cnt = 0
if judge != "No":
    while True:
        if dice_1.getEye() == dice_2.getEye() and dice_1.getEye_E() == dice_2.getEye_E() and \
            dice_1.getEye_S() == dice_2.getEye_S() and dice_1.getEye_W() == dice_2.getEye_W() and \
            dice_1.getEye_N() == dice_2.getEye_N():
            break
        
        dice_2.rotateDice()
        rotate_cnt = rotate_cnt + 1
        
        if rotate_cnt >= 5:
            judge = "No"
            break


if judge != "No":
    dice_1.shakeDice(shake_direction)
    dice_1.shakeDice(shake_direction)
    
    dice_2.shakeDice(shake_direction)
    dice_2.shakeDice(shake_direction)


if judge != "No":
    if dice_1.getEye() == dice_2.getEye():
        judge = "Yes"
    else:
        judge = "No"
        
print(judge)