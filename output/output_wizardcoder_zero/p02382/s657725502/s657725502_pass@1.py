n = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
s1 = 0
s2 = 0
s3 = 0
s4 = []
for i in range(n):
    s1 += abs(X[i] - Y[i])
    s2 += (abs(X[i] - Y[i]) ** 2)
    s3 += (abs(X[i] - Y[i]) ** 3)
    s4.append(abs(X[i] - Y[i]))
# print(s4)
s4max = max(s4)
print('{:.6f}'.format(s1))
print('{:.6f}'.format(math.sqrt(s2)))
print('{:.6f}'.format(math.pow(s3, 1/3)))
print('{:.6f}'.format(s4max))