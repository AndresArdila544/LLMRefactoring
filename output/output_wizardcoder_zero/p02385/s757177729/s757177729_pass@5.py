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
        'S': [(__BACK, __TOP), (__TOP, __FRONT), (__FRONT, __BOTTOM), (__BOTTOM, __BACK)],
        'W': [(__RIGHT, __TOP), (__TOP, __LEFT), (__LEFT, __BOTTOM), (__BOTTOM, __RIGHT)],
        'E': [(__LEFT, __TOP), (__TOP, __RIGHT), (__RIGHT, __BOTTOM), (__BOTTOM, __LEFT)],
        'N': [(__FRONT, __TOP), (__TOP, __BACK), (__BACK, __BOTTOM), (__BOTTOM, __FRONT)],
        'RCW' : [(__LEFT, __FRONT), (__FRONT, __RIGHT), (__RIGHT, __BACK), (__BACK, __LEFT)],   # rotate clockwise
        'RCCW': [(__RIGHT, __FRONT), (__FRONT, __LEFT), (__LEFT, __BACK), (__BACK, __RIGHT)]    # rotate counter clockwise
        
    def dice_move(self, direction_list):
        for direction in direction_list:
            prev_faces = self.f_keys[:]
            
            if direction == 'RCW':
                for i in range(3):
                    self.dice_move(['N'])
                    
            elif direction == 'RCCW':
                for i in range(2):
                    self.dice_move(['N'])
                    
            else:
                prev_f, next_f = self.MOVE_SWAP_FACES[direction]
                self.f_keys[next_f], self.f_keys[prev_f] = prev_faces[prev_f], prev_faces[next_f]
                    
    def dice_fix(self, top=None, front=None):
        if top is not None:
            now_top = self.f_key_to_val[self.__TOP]
            target_top = self.f_key_to_val[top]
            
            while now_top != target_top:
                self.dice_move(['RCW'])
                
                if top not in self.f_keys:
                    return False
        
        if front is not None:
            for i in range(3):
                self.dice_move(['N'])
                
                if self.f_key_to_val[self.__FRONT] == front:
                    break
                    
            else:
                return False
            
        return True
        
    def get_value(self, face):
        return self.f_key_to_val[face]
        
    def is_identical(self, other) -> bool:
        # 含まれるvalueが同じであることをチェック
        if set(self.f_key_to_val.values()) != set(other.f_key_to_val.values()):
            return False
        
        # selfのtopとfrontをotherに合わせる、失敗したらidenticalではない
        other_top = other.get_value(self.__TOP)
        other_front = other.get_value(self.__FRONT)
        
        if not self.dice_fix(other_top, other_front):
            return False
            
        # 全面が同じであることをチェック、すべて通過したらTrue
        for i in range(6):
            if self.get_value(i) != other.get_value(i):
                return False
                
        return True
        
    def __repr__(self):
        return f'({",".join(map(str, self.f_keys))})'
    
def main():
    d1_faces = input().split()
    dice1 = Dice(d1_faces)
    d2_faces = input().split()
    dice2 = Dice(d2_faces)
    print(['No', 'Yes'][dice1.is_identical(dice2)])