"""

alp=input()
while alp!='-':
    m=int(input())
    for i in range(m):
        h=int(input())
        alp=alp[h:len(alp)]+alp[0:h]
    print(alp)
    alp = input()