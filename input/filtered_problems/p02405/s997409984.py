def f(a,b):
    for i in range(a):
        k = b // 2
        if i % 2 ==0:#偶数
            if b % 2 ==0:
                print("#."*k)
            else:
                print("#."*(k)+"#")
        else:#奇数
            if b % 2 ==0:
                print(".#"*k)
            else:
                print(".#"*(k)+".")
    print()

L = []
while True:
        a,b = map(int,input().split())
        k = [a,b]
        L.append(k)
        if a == 0 and b == 0 :
            break

for i in range(len(L)-1):
    f(L[i][0],L[i][1])

