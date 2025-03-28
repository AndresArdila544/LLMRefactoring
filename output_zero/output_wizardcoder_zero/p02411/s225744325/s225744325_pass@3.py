M = []
F = []
R = []
grade = []
m = f = r = 0
while True:
    m, f, r = map(int, input().split())
    if m == -1 and f == -1 and r == -1:
        break
    M.append(m)
    F.append(f)
    R.append(r)
for i in range(len(M)):
    if (M[i] == -1 or F[i] == -1) and not (M[i] + F[i] < 30):
        grade.append('F')
    elif M[i] + F[i] >= 80:
        grade.append('A')
    elif 65 <= M[i] + F[i] < 80:
        grade.append('B')
    elif 50 <= M[i] + F[i] < 65:
        if R[i] >= 50:
            grade.append('C')
        else:
            grade.append('D')
    else:
        if R[i] >= 50:
            grade.append('C')
        else:
            grade.append('D') 
for i in range(len(grade)):
    print(grade[i])