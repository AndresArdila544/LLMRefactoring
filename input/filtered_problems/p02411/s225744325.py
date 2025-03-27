
M = []
F = []
R = []
grade = []
m = 0; f = 0; r = 0
while 1:
    m, f, r = map(int, input().split())
    if m == -1 and f == -1 and r == -1:
        break
    M.append(m)
    F.append(f)
    R.append(r)


for i in range(len(M)):
    if M[i] == -1 or F[i] == -1 or M[i] + F[i] < 30:
        print('F')
    elif M[i] + F[i] >= 80:
        print('A')
    elif 65 <= M[i] + F[i] < 80:
        print('B')
    elif 50 <=  M[i] + F[i] < 65:
        print('C')
    elif 30 <= M[i] + F[i] < 50:
        if R[i] >= 50:
            print('C')
        else:
            print('D')



