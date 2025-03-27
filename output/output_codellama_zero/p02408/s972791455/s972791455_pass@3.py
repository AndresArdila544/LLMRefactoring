n=int(input())
card=[list(range(1,14)) for i in range(4)]
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
for i in card:
    for j in i:
        print(f"{a[i]}{j}")