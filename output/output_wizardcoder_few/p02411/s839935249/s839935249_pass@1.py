result=[]
while True:
    m, f, r = map(int, input().split())
    if all(x in (m,f,r)((-1,-1):
        break
    if any([m<0, f<0]):
        result.append("F")
    elif 80 >= m+f > 65:
        result.append("A")
    elif 65 >= m+f > 50:
        result.append("B")
    elif 50 >= m+f > 30 and r >= 50:
        result.append("C")
    else:
        result.append("D")
for grade in result:
    print(grade)