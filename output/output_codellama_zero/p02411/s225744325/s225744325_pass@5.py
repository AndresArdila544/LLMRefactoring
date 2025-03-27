M = []
F = []
R = []
grade = []
m = 0; f = 0; r = 0
while True:
    m, f, r = map(int, input().split())
    if m == -1 and f == -1 and r == -1:
        break
    M.append(m)
    F.append(f)
    R.append(r)
for i in range(len(M)):
   grade.append('F' if M[i]==-1 or F[i] == -1 or M[i]+F[i]<30 else 'A' if M[i]+F[i]>=80  else 'B' if 65<=M[i]+F[i]<80 else 'C' if 50 <=M[i]+F[i] < 65 else 'D')
print(grade)