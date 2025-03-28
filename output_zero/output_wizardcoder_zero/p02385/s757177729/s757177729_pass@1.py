```python
class Dice:
    TOP = 0
    FRONT = 1
    RIGHT = 2
    LEFT = 3
    BACK = 4
    BOTTOM = 5
    
    def __init__(self, face_val=None):
        self.f_keys = [self.TOP,  # 0
                     self.FRONT,  # 1
                     self.RIGHT,  # 2
                     self.LEFT,  # 3
                     self.BACK,  # 4
                     self.BOTTOM]  # 5
        
        if face_val is None or len(face_val) != 6:
            face_val = ['1', '2', '3', '4', '5', '6']
        
        self.f_key_to_val = {}
        self.f_val_to_key = {}
        for f_key, val in zip(self.f_keys, face_val):
            self.f_key_to_val[f_key] = val
            self.f_val_to_key[val] = f_key
    
    MOVE_SWAP_FACES = {
        'S': [(BACK, TOP), (TOP, FRONT), (FRONT, BOTTOM), (BOTTOM, BACK)],
        'W': [(RIGHT, TOP), (TOP, LEFT), (LEFT, BOTTOM), (BOTTOM, RIGHT)],  # rotate clockwise
        'E': [(LEFT, TOP), (TOP, RIGHT), (RIGHT, BOTTOM), (BOTTOM, LEFT)],  # rotate counter-clockwise
        'N': [(FRONT, TOP), (TOP, BACK), (BACK, BOTTOM), (BOTTOM, FRONT)]
    }
    
    def dice_move(self, direction):
        prev_faces = self.f_keys[:]
        for i in range(len(prev_faces)):
            prev_face, next_face = self.MOVE_SWAP_FACES[direction][i % 2]
            self.f_keys[next_face], self.f_keys[prev_face] = prev_faces[prev_face], prev_faces[next_face]
    
    def dice_fix(self, top, front):
        if type(top) == str:
            top = self.f_val_to_key[top]
            front = self.f_val_to_key[front]
        
        # 上面を指定された面にする
        if top != self.f_keys[self.TOP]:
            now_top = self.f_keys.index(top)
            move = ['N'] * (now_top % 3) + ['RCW', 'RCCW'] * ((now_top // 3) % 2)
            for direction in move:
                self.dice_move(direction)
        
        # 前面を指定された面にする、失敗したらidenticalではない
        for i in range(3):
            if front != self.f_keys[self.FRONT]:
                self.dice_move('W')
            if front == self.f_keys[self.FRONT]:
                break
        else:
            return False    # 3回転するうちに指定された面がfrontに来ないとおかしい
        
        for i in range(6):
            if self.get_value(i) != other.get_value(i):
                return False
        
        return True
    
    def get_value(self, face):
        return self.f_key_to_val[face]
    
    def is_identical(self, other) -> bool:
        # 含まれるvalueが同じであることをチェック
        if set(map(self.get_value, self.f_keys)) != set(map(other.get_value, other.f_keys):
            return False
    
        #selfのtopとfrontをotherに合わせる、失敗したらidenticalではない
        if not self.dice_fix(other.get_value(self.TOP), other.get_value(self.FRONT)):
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
    print(['No','Yes'][dice1.is_identical(dice2)])

main()