while True:
    N = list(map(int,input().split()))
    if not N[0]+N[1]: break #finish
    for i in range(N[0]):# H
        print("#"*(i==0 or i==N[0]-1)+(".#."*(N[1]-2))+"#")