l=[]
while True:
    l_=[int(x) for x in input().split()]
    if l_==[-1,-1,-1]:
        break
    l.append(l_)
for i in l:
    if any(x<0 or x>100 for x in i):
        print("F")
    elif 80<=sum(i)<=89:
        print("A")
    elif 74<=sum(i)<80:
        print("B")
    elif 64<=sum(i)<75:
        print("C")
    elif 59<=sum(i)<64 and i[2]>=50:
        print("C")
    else:
        print("D")