import numpy as np
#def area--------------------------#
ryouno syokiti
class ryou:
	def flinit(self):
		room=list()
		for i in range(10):
			room+=[0]
		return room

#def kaijo([a_1,a_2,a_3,a_4,a_5,a_6,a_7,a_8,a_9,a_10]):


def kaijo(x):
    print "",
    for i in range(len(x)-1):
        print str(x[i]),
    print str(x[len(x)-1])


#----------------------------------#
floor_11=ryou().flinit()
floor_12=ryou().flinit()
floor_13=ryou().flinit()
floor_21=ryou().flinit()
floor_22=ryou().flinit()
floor_23=ryou().flinit()
floor_31=ryou().flinit()
floor_32=ryou().flinit()
floor_33=ryou().flinit()
floor_41=ryou().flinit()
floor_42=ryou().flinit()
floor_43=ryou().flinit()


fldic={"11":floor_11,
       "12":floor_12,
       "13":floor_13,
       "21":floor_21,
       "22":floor_22,
       "23":floor_23,
       "31":floor_31,
       "32":floor_32,
       "33":floor_33,
       "41":floor_41,
       "42":floor_42,
       "43":floor_43
       }

#----------------------------------#
n=int(raw_input())

for l in range(n):
    list_mojiretsu=raw_input().split(" ")
    henka=map(int,list_mojiretsu)
    fldic[str(henka[0])+str(henka[1])][henka[2]-1]+=henka[3]
    
#----------------------------------#
print floor_11
print floor_12
print floor_13
print "####################"
print floor_21
print floor_22
print floor_23
print "####################"
print floor_31
print floor_32
print floor_33
print "####################"
print floor_41
print floor_42
print floor_43