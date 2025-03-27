Here's the refactored version:

n = int(input())
card = [[1,2,3,4,5,6,7,8,9,10,11,12,13], [1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,7,8,9,10,11,12,13]]
for i in range(n):
    a,b=input().split()
    if a == "S":
        card[0].remove(int(b))
    elif a ==  "H":
        card[1].remove(int(b))
    elif a ==  "C":
        card[2].remove(int(b))
    elif a ==  "D":
        card[3].remove(int(b))

for i in range(4):
    for j in card[i]:
        print("S" if i==0 else ("H" if i==1 else ("C" if i==2 else "D")),j)