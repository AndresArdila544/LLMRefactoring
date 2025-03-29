num = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
s = [0 for i in range(4)]
for i in range(num):
    s[0] += abs(A[i] - B[i])
    s[1] += abs(A[i] - B[i])**2
    s[2] += abs(A[i] - B[i])**3
    s[3] = max(s[3], abs(A[i] - B[i]))
s[1] **= 0.5
s[2] **= 1/3
for i in range(4):
    print(f"{s[i]}")