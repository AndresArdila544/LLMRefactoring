l=[]
while 1:
    l_=[int(x) for x in input().split()]
    if l_==[-1,-1,-1]:
        break
    l.append(l_)
for i in l:
    if i[0]==-1 or i[1]==-1:
        print("F")
    elif i[0]+i[1]>=80:
        print("A")
    elif i[0]+i[1]<80 and i[0]+i[1]>=65:
        print("B")
    elif i[0]+i[1]<65 and i[0]+i[1]>=50:
        print("C")
    elif i[0]+i[1]<50 and i[0]+i[1]>=30 and i[2]>=50:
        print("C")
    elif i[0]+i[1]<50 and i[0]+i[1]>=30 and i[2]<50:
        print("D")
    else:
        print("F")
