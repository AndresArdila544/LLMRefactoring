import itertools

class Dice:
    def __init__(self, face_val=None):
        self.faces = ['1', '2', '3', '4', '5', '6']
        if face_val is not None and len(face_val) == 6:
            self.faces = face_val
    
    def move(self, direction):
        for _ in range(len(direction)):
            next_f = direction[0]
            prev_f = direction[1]
            tmp = self.faces[next_f]
            self.faces[next_f] = self.faces[prev_f]
            self.faces[prev_f] = tmp
    
    def fix(self, top, front):
        if type(top) == str:
            top = self.faces.index(top)
            front = self.faces.index(front)
        
        now_top = top
        move = [i for i in range(3)]
        while now_top != 0:
            self.move(['RCW'])
            if now_top == 0:
                break
        
        if now_top != 0:
            return False
        
        for _ in range(4):
            self.move(['S','N'])
            if front == self.faces[self.__FRONT]:
                break
        else:
            return False
        return True
    
    def get_value(self, face):
        return self.faces[face]
    
    def is_identical(self, other) -> bool:
        self_values = [self.get_value(x) for x in self.faces]
        other_values = [other.get_value(x) for x in other.faces]
        if set(self_values) != set(other_values):
            return False
        
        other_top = other.get_value(self.__TOP)
        other_front = other.get_value(self.__FRONT)
        ret = self.fix(other_top, other_front)
        if not ret:
            return False
        
        for i in range(6):
            a1 = self.get_value(i)
            a2 = other.get_value(i)
            
            if self.get_value(i) != other.get_value(i):
                return False
            
        return True
    
    def __repr__(self):
        return f'({",".join(map(str, self.faces))})'


def main():
    d1_faces = input().split()
    dice1 = Dice(d1_faces)
    d2_faces = input().split()
    dice2 = Dice(d2_faces)
    print(['No','Yes'][dice1.is_identical(dice2)])

main()