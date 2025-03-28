N = int( input() )
AP = 0
BP = 0

for i in range(N):
    A,B = input().split()
    sa = 0
    if A == B:
        AP += 1
        BP += 1
    else:
        for j in range(max(len(A), len(B))):
            if ord(A[j]) > ord(B[j]):
                AP += 3
                break
            elif ord(B[j]) > ord(A[j]):
                BP += 3
                break
print(AP, BP, sep=' ')