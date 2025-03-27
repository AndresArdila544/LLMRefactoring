def PRINT(S,a,b):
    print(S[a:b+1])
def REPLACE(S,T,a,b):
    return S[:a] + T + S[b+1:]
def REVERSE(S,a,b):
    tmp = S[a:b+1]
    return S[:a] + tmp[::-1] + S[b+1:] 

S = input()
q = int(input())

for i in range(q):
    order = list(input().split())
    a = int(order[1])
    b = int(order[2])
    if order[0] == "replace":
        S = REPLACE(S,order[3],a,b)
    elif order[0] == "reverse":
        S = REVERSE(S,a,b)
    else:
        PRINT(S,a,b)
