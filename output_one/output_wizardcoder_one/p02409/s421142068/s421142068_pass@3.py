import numpy as np
class ryou:
    def flinit(self):
        room = list()
        for i in range(10):
            room += [0]
        return room
def kaijo([a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9, a_10]:
    y = []
    for i in range(len(x) - 1):
        y += " " + x[i]
    return y

fldic = {"11": floor_11, "12":floor_12, "13":floor_13, "21":floor_21, "22":floor_22, "23":floor_23, "31":floor_31, "32":floor_32, "33":floor_33, "41":floor_41, "42":floor_42, "43":floor_43}

n = int(raw_input())
for l in range(n):
    list_mojiretsu = raw_input().split(" ")
    henka = map(int, list_mojiretsu)
    fldic[str(henka[0]) + str(henka[1])][henka[2] - 1] += henka[3]

kaijo(floor_11)
kaijo(floor_12)
kaijo(floor_13)
print "####################"
kaijo(floor_21)
kaijo(floor_22)
kaijo(floor_23)
print "####################"
kaijo(floor_31)
kaijo(floor_32)
kaijo(floor_33)
print "####################"
kaijo(floor_41)
kaijo(floor_42)
kaijo(floor_43)