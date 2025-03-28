import sys
input = sys.stdin.readline
n=int(input())
for i in range(n):
    b,f,r,v=map(lambda x: int(x), input().split(" "))
    B, F, R =b-1, f-1, r-1
    new = rooms[B][F][R] + v
    rooms[B][F][R]=new if new>=0 else 0
for i in range(4):
    print("####################" if i>0 else "",end="")
    for j in range(3):
        print(" " + " ".join(map(lambda x: str(x), rooms[i][j])),end="")