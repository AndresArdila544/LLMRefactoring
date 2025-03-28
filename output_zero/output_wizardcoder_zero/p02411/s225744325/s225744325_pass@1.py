M = []
F = []
R = []
grade = []
m, f, r = 0, 0, 0
while m != -1 and f != -1 and r != -1:
    M.append(int(input()))
    F.append(int(input()))
    R.append(int(input()))
    m, f, r = map(int, input().split())
    
for i in range(len(M)):
    if M[i] == -1 or F[i] == -1 or M[i] + F[i] < 30:
        grade.append('F')
    elif M[i] + F[i] >= 80:
        grade.append('A')
    elif 65 <= M[i] + F[i] < 80:
        grade.append('B')
    elif 50 <= M[i] + F[i] < 65:
        grade.append('C')
    else:
        if R[i] >= 50:
            grade.append('C')
        else:
            grade.append('D')
print(*grade)