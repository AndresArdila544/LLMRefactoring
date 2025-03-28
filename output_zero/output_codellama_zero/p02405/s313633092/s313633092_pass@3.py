while True:
    a,b=map(int, input().split())
    if a==0 and b==0:
        break
    else:
        pattern='#'*(b%2) + '.'*(b-1) % 2
        for i in range(a):
            print((pattern*i)%2*'#' + (pattern*i)%2*'.')