def f(a,b):
    k = b // 2
    if a % 2 == 0: #偶数
        print('#' * (k if b % 2 == 0 else k + 1))
    else: #奇数
        print('.#' * (k if b % 2 == 0 else k + 1))

L = []
while True:
    a,b = map(int,input().split())
    L.append([a,b])
    if a == 0 and b == 0 :
        break
for i in range(len(L)-1):
    f(*L[i])