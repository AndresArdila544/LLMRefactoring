```python
class Dice:
    __TOP = 0
    __FRONT = 1
    __RIGHT = 2
    __LEFT = 3
    __BACK = 4
    __BOTTOM = 5
    
    def __init__(self, face_val=None):
        self.f_keys = [self.__TOP, self.__FRONT, self.__RIGHT, self.__LEFT, self.__BACK]
        
        if face_val is None or len(face_val) != 6:
            face_val = ['1', '2', '3', '4', '5', '6']
            
        self.f_key_to_val = {}
        self.f_val_to_key = {}
        
        for f_key, val in zip(self.f_keys, face_val):
            self.f_key_to_val[f_key] = val
            self.f_val_to_key[val] = f_key
            
    MOVE_SWAP_FACES = {
        'S': [(__BACK, __TOP), (__TOP, __FRONT), (__FRONT, __BOTTOM), (__BOTTOM, __BACK)],  # Rotate the top face to the front face.
        'W': [(__RIGHT, __TOP), (__TOP, __LEFT), (__LEFT, __BOTTOM), (__BOTTOM, __RIGHT)],  # Rotate the dice counterclockwise.
        'E': [(__LEFT, __TOP), (__TOP, __RIGHT), (__RIGHT, __BOTTOM), (__BOTTOM, __LEFT)],  # Rotate the dice clockwise.
        'N': [(__FRONT, __TOP), (__TOP, __BACK), (__BACK, __BOTTOM), (__BOTTOM, __FRONT)],  # Rotate the front face to the top face.
        'RCW' : [(__LEFT, __FRONT), (__FRONT, __RIGHT), (__RIGHT, __BACK), (__BACK, __LEFT)],   # Rotate the dice clockwise.
        'RCCW': [(__RIGHT, __FRONT), (__FRONT, __LEFT), (__LEFT, __BACK), (__BACK, __RIGHT)]   # Rotate the dice counterclockwise.
    }
    
    def move_dice(self, direction):
        prev_faces = self.f_keys[:]
        
        for prev_face, next_face in self.MOVE_SWAP_FACES[direction]:
            self.f_keys[next_face] = prev_faces[prev_face]
            
    def get_value(self, face):
        return self.f_key_to_val[face]
    
    def is_identical(self, other):
        if set(self.f_keys) != set(other.f_keys):  # Check if the faces of two dices have the same values.
            return False
        
        # If the top face and front face are not as expected, rotate them to be at their correct positions.
        self.move_dice('N')
        ret = self.f_keys[self.__TOP] == other.f_keys[other.__TOP]  # Check if rotating the dice has been successful or not.
        
        if not ret:
            return False
            
        for i in range(6):
            a1 = self.get_value(i)
            a2 = other.get_value(i)
            
            if self.f_keys[i] != other.f_keys[i]:  # Check all the faces are identical or not.
                return False
                
        return True
    
    def __repr__(self):
        return str(self.f_keys)
        
def main():
    d1_faces = input().split()
    dice1 = Dice(d1_faces)
    d2_faces = input().split()
    dice2 = Dice(d2_faces)
    
    print(['No', 'Yes'][dice1.is_identical(dice2)] if len(dice1.f_keys) == 6 else 'Error')

main()
```