class Dice:
    def __init__(self, face_val=None):
        self.f_keys = ['1', '2', '3', '4', '5', '6']
        self.f_key_to_val = {0: '1', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6'}
        self.f_val_to_key = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5}
        if face_val is not None and len(face_val) == 6:
            self.f_keys = face_val[:]

    def dice_move(self, direction_list):
        for direction in direction_list:
            prev_faces = list(self.f_keys)
            for prev_f, next_f in [(__BACK, __TOP), (__TOP, __FRONT), (__FRONT, __BOTTOM), (__BOTTOM, __BACK)]:
                if prev_faces[prev_f] != self.f_keys[next_f]:
                    self.f_keys[next_f] = prev_faces[prev_f]
            #print(self.f_keys)

    def dice_fix(self, top, front):
        if type(top) == str:
            top = self.f_val_to_key[top]
            front = self.f_val_to_key[front]

        # 上面を指定された面にする
        if top != self.f_keys[self.__TOP]:
            now_top = self.f_keys.index(top)
            move = [self.MOVE_TO_TOP[now_top]]
            self.dice_move(move)

        if top != self.f_keys[self.__TOP]:
            return False    # 3回回転するうちに指定された面がfrontに来ないとおかしい
        return True

    def get_value(self, face):
        return self.f_key_to_val[self.f_keys[face]]

    def is_identical(self, other) -> bool:
        # 含まれるvalueが同じであることをチェック
        self_values = [self.get_value(x) for x in self.f_keys]
        other_values = [other.get_value(x) for x in other.f_keys]
        if set(self_values) != set(other_values):
            return False

        # 含まれる面が同じであることをチェック
        for i in range(6):
            a1 = self.get_value(i)
            a2 = other.get_value(i)

            if self.get_value(i) != other.get_value(i):
                return False

        return True

    def __repr__(self):
        return f'({",".join(map(str, self.f_keys))})'