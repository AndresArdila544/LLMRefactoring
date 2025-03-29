import numpy as np
def area(x):
    y=[]
    for i in x:
        y=y+ " "+x[i]
    return y
def kaijo(x):
    print "",
    for i in range(len(x)-1):
        print str(x[i]),
    print str(x[len(x)-1])
n=int(raw_input())
for l in range(n):
    list_mojiretsu=raw_input().split(" ")
    henka=map(int,list_mojiretsu)
    fldic[str(henka[0])+str(henka[1])][henka[2]-1]+=henka[3]

#----------------------------------#
floor_11=np.array([0, 0, 0]).astype('int')
floor_12=np.array([0, 0, 0]).astype('int')
floor_13=np.array([0, 0, 0]).astype('int')
floor_21=np.array([0, 0, 0]).astype('int')
floor_22=np.array([0, 0, 0]).astype('int')
floor_23=np.array([0, 0, 0]).astype('int')
floor_31=np.array([0, 0, 0]).astype('int')
floor_32=np.array([0, 0, 0]).astype('int')
floor_33=np.array([0, 0, 0]).astype('int')
floor_41=np.array([0, 0, 0]).astype('int')
floor_42=np.array([0, 0, 0]).astype('int')
floor_43=np.array([0, 0, 0]).astype('int')
fldic={"11":floor_11,"12":floor_12,"13":floor_13,"21":floor_21,"22":floor_22,"23":floor_23,"31":floor_31,"32":floor_32,"33":floor_33,"41":floor_41,"42":floor_42,"43":floor_43}
for l in range(n):
    list_mojiretsu=raw_input().split(" ")
    henka=map(int,list_mojiretsu)
    fldic[str(henka[0])+str(henka[1])][henka[2]-1]+=henka[3]
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