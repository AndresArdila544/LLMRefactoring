n=int(input())
cards=set()
for i in range(n):
    m,n=map(str,input().split())
    cards.add((m[0],int(n)))
print(*(i for i in [(x,y) for x in ['S','H','D','C'] for y in range(1,14) if (x,y) not in cards])