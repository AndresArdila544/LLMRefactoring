from itertools import combinations
import random

class Dice:
    def __init__(self, label):
        self.label = label
    
    def rotate_s(self):
        self.label = [self.getLabel(i) for i in (5, 1, 3, 4, 6, 2)]
        
    def rotate_n(self):
        self.label = [self.getLabel(i) for i in (2, 6, 3, 4, 1, 5)]
    
    def rotate_e(self):
        self.label = [self.getLabel(i) for i in (4, 2, 1, 5, 3)]
        
    def rotate_w(self):
        self.label = [self.getLabel(i) for i in (3, 2, 6, 1, 5, 4)]
    
    def spin_pos(self):
        self.label = [self.getLabel(i) for i in (1, 4, 2, 5, 3, 6) if i != 0]
        
    def spin_neg(self):
        self.label = [self.getLabel(i) for i in (1, 3, 5, 2, 4, 6) if i != 0]
    
    def rotate(self, rotates):
        for r in rotates:
            if r == 'S':
                self.rotate_s()
            elif r == 'N':
                self.rotate_n()
            elif r == 'E':
                self.rotate_e()
            elif r == 'W':
                self.rotate_w()
            elif r == 'T':
                self.spin_pos()
            elif r == 'B':
                self.spin_neg()
                
    def match_top_front(self, top, front):
        iTop = self.label.index(top) + 1
        topRot = {1: '', 2: 'N', 3: 'W', 4: 'E', 5: 'SS'}
        self.rotate(topRot[iTop])
        
        iFront = self.label.index(front) + 1
        frontRot = {2: '', 3: 'B', 4: 'T', 5: 'TT'}
        # top, front ????????????????¢????????????????´??????iFront???1???6????????
        try:
            self.rotate(frontRot[iFront])
            return True
        except KeyError:
            return False
        
    def copy(self):
        return Dice(self.label[:])
    
    def equal_without_overlap(self, other):
        if other.match_top_front(self.getLabel(1), self.getLabel(2)):
            return True if self.label == other.label else False
        else:
            return False
        
    def __eq__(self, other):
        # ??????????????????????
        if set(self.label) != set(other.label):
            return False
        # ?????????????????????
        elif len(self.label) == len(set(self.label):
            return self.equal_without_overlap(other)
        else:
            for rs in ('', 'S', 'N', 'E', 'W', 'SS'):
                tmp = self.copy()
                for r in rs:
                    tmp.rotate(r)
                # ??????????¢??????????§6??????????????°??????
                def side():
                    result, n = False, 3
                    while not result and n > 0:
                        if tmp.label[1:5] == other.label[1:5]:
                            result = True
                        else:
                            tmp.rotate('T')
                            n -= 1
                    return result
                if self.label[2:] == other.label[:4] and side():
                    return True
        else:
            return False
    
def main():
    faces = [random.sample(range(1,7),6) for _ in range(int(input()))
    all_pairs = combinations(faces, 2)
    any(Dice(f).match_top_front(*f2) and not Dice(f).equal_without_overlap(Dice(f2)) for f, f2 in all_pairs)
    
    print('Yes')

if __name__ == '__main__':
    main()