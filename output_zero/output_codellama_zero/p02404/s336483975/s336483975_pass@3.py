while True:
    a,b=map(int,input().split())
    if a==0 and b==0: break
    for i in range(a):
        print(''.join(['#'*(i==0 or i==a-1)*2+'.'*(b-2)+'#']*b))
    print()