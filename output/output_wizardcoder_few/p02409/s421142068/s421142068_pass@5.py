```python
import numpy as np

class ryou(object):
    def __init__(self):
        self.room = [0] * 10
    
def area():
    return ryou()

def input_array(n):
    return map(int, raw_input().split())

#def kaijo([a_1,a_2,a_3,a_4,a_5,a_6,a_7,a_8,a_9,a_10]):
def kaijo(x):
    return " ".join(str(y) for y in x[::-1]) + "\n"

#--------------------------
fldic = {
       '11': area(), '12': area(), '13': area(),
       '21': area(), '22': area(), '23': area(),
       '31': area(), '32': area(), '33': area(),
       '41': area(), '42': area(), '43': area()
}
#--------------------------

n = int(raw_input())
for _ in range(n):
    floor, room, value = input_array(7)
    fldic['{}{}'.format(floor, room)].room[value - 1] += 1
    
for i in range(1, 5):
    for j in range(3):
        print kaijo(fldic['{}1'.format(i)].room),
        print kaijo(fldic['{}{}'.format(i, 2)].room),
        print kaijo(fldic['{}{}'.format(i, 3)].room)
    if i != 4:
        print "####################"
```