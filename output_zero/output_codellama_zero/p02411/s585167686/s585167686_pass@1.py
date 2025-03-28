l=[]
while True:
    l_=[int(x) for x in input().split()]
    if l_==[-1,-1,-1]:
        break
    l.append(l_)
for i in l:
    if any(y<0 for y in i):
        print("F")
    elif sum(i[:2])>=80:
        print("A")
    elif sum(i[:2])<80 and sum(i[:2])>=65:
        print("B")
    elif sum(i[:2])<65 and sum(i[:2])>=50:
        print("C")
    elif sum(i[:2])<50 and sum(i[:2])>=30 and i[2]>=50:
        print("C")
    elif sum(i[:2])<50 and sum(i[:2])>=30 and i[2]<50:
        print("D")
    else:
        print("F")