result=[]
while True:
    m,f,r=(int(x) for x in input().split())
    if m==f==r==-1:
        break
    score=m+f-2*r
    if score<0 or score>80:
        result.append("F")
    elif score>=80:
        result.append("A")
    elif score>=65:
        result.append("B")
    elif score>=50:
        result.append("C")
    else:
        if r<50:
            result.append("D")
        else:
            result.append("F")
for grade in result:
    print(grade)