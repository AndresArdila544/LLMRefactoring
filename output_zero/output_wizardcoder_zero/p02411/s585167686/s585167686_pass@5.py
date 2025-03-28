while True:
    marks = [int(x) for x in input().split()]
    if marks == [-1,-1,-1]:
        break
    l.append(marks)
for i in l:
    if any(j in i[:2] or j==-1 for j in (-1,)):
        print("F")
    elif sum(i[:2]) >= 80:
        print("A")
    elif sum(i[:2]) < 80 and sum(i[:2]) >= 65:
        print("B")
    elif sum(i[:2]) < 65 and sum(i[:2]) >= 50:
        print("C")
    elif sum(i[:2]) < 50 and all(j>=50 for j in i):
        print("C")
    else:
        print("F")